import re

PhoneNumRegex = re.compile(r'\+\d\d-\d\d\d\d\d\d\d\d\d\d')
print(PhoneNumRegex.findall('Call me on +91-8799876654 tomorrow, and +91-9897887654 is my alternate number'))
