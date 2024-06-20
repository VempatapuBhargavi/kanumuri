print('hi')

ch = int(input('enter a num:'))
print(ch)
match(ch):
    case 2.0:
        print('one')
    case 2:
        print('two')
    case _ :
        print('none')