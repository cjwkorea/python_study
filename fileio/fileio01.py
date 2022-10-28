# 파일 수정


file_editor = open(file="fileio/test.txt", mode="a", encoding="utf-8")
# mode a는 파일 수정 (append)

file_editor.write("\n반갑습니다.")

file_editor.close()
