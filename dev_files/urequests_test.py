
import urequests as requests

r = requests.get("http://ujyu.net")
print(r)
print(r.content)
print(r.text)
r.close()
print(r.status_code)
# print(r.json())

# It's mandatory to close response objects as soon as you finished
# working with them. On MicroPython platforms without full-fledged
# OS, not doing so may lead to resource leaks and malfunction.
r.close()
