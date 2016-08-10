# L=(x*x for x in range(11))
# L
# print(next(L))
# print(next(L))
# print(next(L))
# print(next(L))
# print(next(L))
# print(next(L))
# print(next(L))
# print(next(L))
# print(next(L))
# for n in L:
#     print(n)
# def fib(max):
#     #注意赋值方式！！！
#     n,a,b=0,0,1
#     while n < max:
#         # print(b)
#         yield(b)
#         a,b=b,a+b
#         n=n+1
#     return 'done'
# g=fib(6)

# while True:
#     try:
#         x=next(g)
#         print('g:',x)
#     except StopIteration as e:
#         print('Generator return value:',e.value)
#         break



# next(fib(6))
# next(fib(6))

# for n in fib(6):
#     print(n)

# generator函数的“调用”实际返回一个generator对象

# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield 3
#     print('step 3')
#     yield 5
# o=odd()
# next(o)
# next(o)
# next(o)
# next(o)









