print('how many cats you have?')
catsNum = input()

try:
    if int(catsNum) >= 4:
          print('That is a lot of cats.')
    else:
          print('That is not that many cats.')
except ValueError:
    print('you did not entered a number.')
    
