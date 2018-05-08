import uxml

# request = {'x:Envelope': {'x:Body': {'soa:queryRQ': {'ns:transport': {'ns:header': {'ns:query': {'ns:key': {'$': {'id': 'http://j.kisarazu.ac.jp/PlantFactory/Daisen/West/Temperature', 'attrName': 'time', 'select': 'maximum'}}, '$': {'id': 'df5fe59b-0323-4d36-a0c9-59646e96b3a9', 'type': 'storage'}}}}}}, '$': {'xmlns:ns': 'http://gutp.jp/fiap/2009/11/', 'xmlns:soa': 'http://soap.fiap.org/', 'xmlns:x': 'http://schemas.xmlsoap.org/soap/envelope/'}}}

request = {'x:Envelope': {'x:Body': {'soa:queryRQ': {'ns:transport': {'ns:header': {'ns:query': {'ns:key': [{'$': {'id': 'http://j.kisarazu.ac.jp/PlantFactory/Daisen/West/Temperature', 'attrName': 'time', 'select': 'maximum'}}, {'$': {'id': 'http://j.kisarazu.ac.jp/PlantFactory/Daisen/West/Temperature', 'attrName': 'time', 'select': 'maximum'}}], '$': {'id': 'df5fe59b-0323-4d36-a0c9-59646e96b3a9', 'type': 'storage'}}}}}}, '$': {'xmlns:ns': 'http://gutp.jp/fiap/2009/11/', 'xmlns:soa': 'http://soap.fiap.org/', 'xmlns:x': 'http://schemas.xmlsoap.org/soap/envelope/'}}}

parser = uxml.Parser()
print(parser.parse(open("./request.xml")))
del parser

builder = uxml.Builder()
print(builder.build(request))
del builder
