#Exception handling
# try except else finally

while True:
    try:
        age = int(input('enter your age: ')) #seven
        break
    except ValueError:
        print('invalid input')


if age < 18:
    print('you can\'t play this game.')
else:
    print('you can play this game')