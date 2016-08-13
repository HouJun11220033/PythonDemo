# f=int ('12345')
# print(f)

# e=int('12345',base=8)
# print(e)
#
# f=int('12345',16)
# print(f)

# def int2(x,base=2):
#     return int(x,base)
# print(int2('100000'))
import functools

# int2=functools.partial(int,base=2)
# print(int2('1000000'))
# kw={'base':2}
# print(int('10010',**kw))
max2 = functools.partial(max, 10)
print(max2(4, 2))
