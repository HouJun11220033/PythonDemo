from collections import Iterable
a=isinstance([],Iterable)
print(a)
# isinstance({},Iterable)
# isinstance('abc',Iterable)
# isinstance((x for x in range(100)),Iterable)
# isinstance(100,Iterable)
from collections import Iterator
print(isinstance((x for x in range(10)),Iterator))
print(isinstance(iter({}),Iterator))
print(isinstance({},Iterator))

# 凡是可作用于for循环的对象都是Iterable类型
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列