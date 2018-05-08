import xmltok

expected = [
('PI', 'xml'),
('ATTR', ('', 'version'), '1.0'),
('START_TAG', ('s', 'Envelope')),
('ATTR', ('xmlns', 's'), 'http://schemas.xmlsoap.org/soap/envelope/'),
('ATTR', ('s', 'encodingStyle'), 'http://schemas.xmlsoap.org/soap/encoding/'),
('START_TAG', ('s', 'Body')),
('START_TAG', ('u', 'GetConnectionTypeInfo')),
('ATTR', ('xmlns', 'u'), 'urn:schemas-upnp-org:service:WANIPConnection:1'),
('TEXT', 'foo bar\n  baz\n  \n'),
('END_TAG', ('u', 'GetConnectionTypeInfo')),
('END_TAG', ('s', 'Body')),
('END_TAG', ('s', 'Envelope')),
]

dom = {}
current_tag = dom
current_is_pi = False
outer_tags = []
pis = {}
current_pi = {}

tokens = xmltok.tokenize(open("./test.xml"))

def get_name_from_token(token):
    name = None
    if token[1][0] == '':
        name = token[1][1]
    else:
        name = ':'.join(token[1])
    return name

for token in tokens:
    if token[0] == 'PI':
        current_is_pi = True
        current_pi = {}
        pis[token[1]] = current_pi

    elif token[0] == 'START_TAG':
        current_is_pi = False
        tag_name = get_name_from_token(token)

        outer_tags.append(current_tag)
        current_tag[tag_name] = {}
        current_tag = current_tag[tag_name]

    elif token[0] == 'ATTR':
        attr_name = get_name_from_token(token)
        attr_value = token[2]

        if current_is_pi:
            current_pi.setdefault('$', {})
            current_pi['$'][attr_name] = attr_value
        else:
            current_tag.setdefault('$', {})
            current_tag['$'][attr_name] = attr_value

    elif token[0] == 'TEXT':
        current_tag['_'] = token[1]

    elif token[0] == 'END_TAG':
        current_tag = outer_tags.pop()

    else:
        # Error
        pass

print(dom)
print(pis)


# for token in tokens:
#     if i[0] == 'PI':
#         if i[1][0] == '':
#             tag_name = i[1][1]
#         else:
#             tag_name = ':'.join(i[1])
#
#         current_tag
#     elif i[0] == 'START_TAG':
#         if i[1][0] == '':
#             tag_name = i[1][1]
#         else:
#             tag_name = ':'.join(i[1])
#
#         print(tag_name)
#
#         outer_tags.append(current_tag)
#
#         current_tag[tag_name] = {}
#         current_tag = current_tag[tag_name]
#
#     elif i[0] == 'END_TAG':
#         current_tag = outer_tags.pop()
#
#     print(i)
#
# print(dom)
#
#
# def parse_pi(tokens):
#     pis = {}
#     pi_detected = False
#     pi = None
#     for i in tokens:
#         if pi_detected:
#             if i[0] == 'ATTR':
#                 attr_name = ''
#                 if i[1][0] == '':
#                     attr_name = i[1][1]
#                 else:
#                     attr_name = ':'.join(i[1])
#
#                 attr_value = i[2]
#                 pi[attr_name] = attr_value
#
#             else:
#                 pi_detect = False
#
#         else:
#             if i[0] == 'PI':
#                 pi_detect = True
#                 pi = {}
#                 pis[i[1]] = pi
#
#     return pis
