import string

string = "가나다라 마바사"
print(string)
#string[0] = '하' #배열에 0번자리(가) #불변이라서 변경 불가능

char_list = string.split(' ')

print(char_list)
change_string = string.replace('가','하')
print(id(string))
print(id(change_string))

list1 = [1,2,3]
list2 = [1,2,3]

print(id(list1))
print(id(list2))
