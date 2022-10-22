# import string
# name = 'jaybon'
# age = 10

#은 주석처리,줄 중간이나 끝에서 ctrl+/는 그줄 전체 주석
# print("내 이름은 " + name + " 내 나이는 " + str(age))
#f= 포맷(재설정)
# print(f"내 이름은 {name} 내 나이는 {age}")
# print(f"{name=} {age=}")
# print("내 이름은 %s 내 나이는 %d"% (name,age))
# print("내 이름은 {0} 내 나이는 {1}".format(name,age))
# print("내 이름은 {n} 내 나이는 {a}".format(n=name, a=age))

# my_list = [1,2,3,4] # 스네이크 표기법 _을 사용하고 파이썬에서 자주 사용함

# my_list[0] = 9 #리스트는 가변이라서 변경 가능

# print(my_list)

# for element in my_list:
#     print(element)  
    

# myList 카멜 표기법 스크립트에서 자주 쓰임
# MyList 파스칼 표기법

# string = "가나다라 마바사"

# string[0] = '하' #배열에 0번자리(가) #불변이라서 변경 불가능

# print(string)

# char_list = string.split(' ')

# print(char_list)

# change_string = string.replace('가','하')
# print(id(string))
# print(id(change_string))

# list1 = [1,2,3]
# list2 = [1,2,3]

# print(id(list1))
# print(id(list2))

# x = 1
# while x < 10:
#     x = x + 1
#     print("가나다")

    
# for item in [1,2,3,4]:
#     print(item)

# def sum_two_num(n1, n2):
#     return n1 + n2
    

    
# sum_num = sum_two_num(1, 2)
# sum_num = 3
    
# print(sum_num)




# def check_data():
#     data = int(input())

#     if data == 1:
#         print("1이다")
#     elif data == 2:
#         print("2다")
#     elif data == 3:
#         print("3다")
#     elif data == 4:
#         print("4다")
#     else:
#         print("모르겠다")

# while True:
#     check_data()

# print(True or True)
# print(True or False)
# print(True and True)
# print(True and False)
# print(not True)
# print(not False)
# print(1 == 1)
# print(1 <= 1)
# print(1 < 1)
# print(1 != 2)# != 다르다는 뜻이다
# result = not (1 != 2)
# print(result)

# my_set = {1,2,3,4,1,1,1,1}
# my_set = set([1,2,3,4,1,1,1,1])
# print(my_set)
# for item in my_set:
#     print(item)

# my_dict = {"name" : "jaybon", "age" : 12}
# for key, value in my_dict.items():
#     print(f"{key} 은/는 {value}")

# my_tuple = (1 ,1,    2 ,3, 4)
# my_tuple = [1,2,3]
# print(my_tuple)
# for item in my_tuple:
#     print(item)
