import re

SpiderRegex = re.compile(r'spider(man|world|iron)')
mo = SpiderRegex.search('spideriron got knocked out from the world war')
print(mo.group())
