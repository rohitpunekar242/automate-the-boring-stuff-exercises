#copy module example

import copy

spam = ['A','B','C','D']
cheese = copy.deepcopy(spam)
cheese[1] = 'Hello'

print(spam)
print(cheese)
