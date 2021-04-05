def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
        print()


fib(100)


def default_param(s, a=10, b=3):
    print(s*a*b)


default_param(9, b=100, a=10)

"""
多行
注释
"""

# 打印注解
print(default_param.__annotations__)

