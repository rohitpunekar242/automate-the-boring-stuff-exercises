import re

PhoneNumRegex = re.compile(r'(\+\d\d)-(\d\d\d\d\d\d\d\d\d\d)')
mo = PhoneNumRegex.search('Call me on +91-8799876654 tomorrow, and +91-9897887654 is my alternate number')
print(mo.group())
print(mo.group(1))
print(mo.group(2))
