def div42by(divideby):
    try:
        return 42 / divideby
    except:
        print('you tried to divide by zero.')
        
print(div42by(2))
print(div42by(21))
print(div42by(0))
