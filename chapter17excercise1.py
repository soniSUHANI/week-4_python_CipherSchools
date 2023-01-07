# make a function 'divide'
# divide(a,b)
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        # print('you cannot divide a number by Zero')
        print(err)
    except TypeError as err:
        print("numbers must be int or floats")
    except :
        print("unexpected Error")

print(divide(10,'2'))

