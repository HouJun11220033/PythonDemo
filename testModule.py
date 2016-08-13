import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print("Hello World !")
    elif len(args) == 2:
        print("Hello,%s !" % args[1])
    else:
        print("Too many arguments !")


def _private_1(name):
    return 'Hello,%s' % name


def _private_2(name):
    return 'Hello,%s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

# 得有print语句啊！！！
fs = greeting('HouJun')

if __name__ == '__main__':
     test()

