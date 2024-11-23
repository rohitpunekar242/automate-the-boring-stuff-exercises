message = 'It is a very warm day and I was walking on the road surrounded by beautiful trees';
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character]+1

print(count)
    
