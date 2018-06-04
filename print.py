import sys

# print() 연습

print(1)
print('hello', 'world')

# 여러 인자(parameter)를 통한 출력
x = 0.2
s = "hello"

print(x)
print(s)

# sep(Seperator) 파라미터 값 대신에 + 연산하는 방법
# 단, + 연산은 앞의 객체(left)가 연산자 오버로딩이 되어 있어야한다.
print(x, s, sep=', ')
print(str(x) + ', ' + s)

# sep, end 키워드 파라미터 지정
print(x, s, sep=', ', end='')
# 기본적인 print() 호출은
# print(*args, sep=' ', end='\n') 이런 형태로 되어있을 것이다.
# file 파라미터 지정
print('Hello World', file=sys.stdout)
print('Error: Hello World', file=sys.stderr)

# file 출력
f = open('/hello.txt', 'w')
print('Hello World', file=f)

# cf.
sys.stdout.write('Hello World!!!')
