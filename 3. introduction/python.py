print(1-1)
print(1+1)
print(5 ** 3)

print(len("abc"))

print("s" * 2) # 重复字符串
print('un' + 'ium') # 重复字符串 必须是python3才支持
print('Py' 'thon' 'Py' 'thon')

word = (
    'Python'
    'Python'
    'Python'
    'Python'
    'Python'
)

print(len(word))
print(word[0])
print(word[-1])
print(word[-2])

print([1, 4, 9, 16, 25][-1])

print([1] + [2])

# java str[str.length - 1]

a, b = 0, 1
while a < 1000:
    print(a, end='-')
    a, b = b, a+b
