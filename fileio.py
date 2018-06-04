# write test

# text모드가 default : wt
f = open('text.txt', 'w', encoding='utf-8')
write_size = f.write('안녕하세요\n러리입니다.')
print(write_size)
f.close()

# binary mode : wb
f = open('text.txt', 'wb')
write_size = f.write(bytes('안녕하세요\n원휘입니다.', encoding='utf-8'))
print(write_size)
f.close()

# read test
f = open('text.txt', 'r', encoding='utf-8')
text = f.read()
print(text)
f.close()

# 이미지 하나 다운 받아서 폴더에 넣어놔야됨.
# copy binary file
f_src = open('python.jpg', 'rb')
data = f_src.read()
print(type(data))
f_src.close()

f_dest = open('python2.jpg', 'wb')
f_dest.write(data)
f_dest.close()
