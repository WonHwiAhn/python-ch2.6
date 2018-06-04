# 다양한 파일 입출력 함수

f = open('text.txt', 'r', encoding='utf-8')
text = f.read()
print(text)
text = f.read()
print('--- text ' + text)

# position단위는 byte다.
# file pointer
pos = f.tell()
print(pos)

f.seek(16)
text = f.read()
print(text)

#
line_num = 0

f2 = open('fileio2.py', 'r', encoding='utf-8')
while True:
    line = f2.readline()
    if line == '':
        f2.close()
        break

    line_num += 1

    print(str(line_num) + " : " + line, end='')

print()

f3 = open('fileio2.py', 'r', encoding='utf-8')
lines = f3.readlines()
print(lines, type(lines))

for line_num, line in enumerate(f3.readlines()):
    print('{0}: {1}'.format(line_num, line))

with open('fileio2.py', 'r', encoding='utf-8') as f4:
    for line_num, line in enumerate(f3.readlines()):
        print('{0}: {1}'.format(line_num, line))

print(f4.closed)