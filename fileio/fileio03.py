# 파일 읽기

file_editor = open(file="fileio/test.txt", mode="r", encoding="utf-8")
# mode r은 파일 읽기 (read)
# read()는 파일에 있는 모든 데이터를 가져온다.
my_text = file_editor.readline()
my_text1 = file_editor.readline()
my_text2 = file_editor.readline()
my_text3 = file_editor.readline()

# readline()은 파일에서 한줄씩 데이터를 가져온다.


file_editor.close()

print(my_text)
print(my_text1)
print(f"{my_text2=}")
print(f"{my_text3=}")
