# 파일 읽기

file_editor = open(file="fileio/test.txt", mode="r", encoding="utf-8")
# mode r은 파일 읽기 (read)
# read()는 파일에 있는 모든 데이터를 가져온다.
my_text = file_editor.read()

file_editor.close()

print(my_text)
