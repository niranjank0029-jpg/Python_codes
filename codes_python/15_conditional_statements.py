#conditional statements 

import sys
print(sys.version)


#IF statement 

# abc=int(input("enter the score:"))
# print("the score is :",abc)

# if abc==100:
#     print("Ok")



#IF-ELSE statements 

# abc=int(input("enter the score:"))
# print("the score is :",abc)

# if abc==100:
#     print("Ok")
# else:
#     print("not ok")


#IF-ELIF-ELSE


# >=90 A
# 80-89 b
# 70-79 c
# 60-69 d
# <60  e

# xyz=int(input('enter the marks: '))
# print('the marks is:',xyz)

# if xyz>=90:
#     print('A')
# elif 80<= xyz <=89:
#     print("B")
# elif 70<= xyz <=79:
#     print("C")
# elif 60<= xyz <=69:
#     print("D")
# else: 
#     print("E")

 #---Nested IF

# nn=int(input('enter the marks:'))
# print('the marks is:',nn)
# project_sub=False

# if nn>=90:
#      if project_sub:
#          print('A+')
#      else:
#          print('A')
# elif 80<= nn <=89:
#     print("B")
# elif 70<= nn <=79:
#     print("C")
# elif 60<= nn <=69:
#     print("D")
# else: 
#     print("E")




nn = int(input('Enter marks: '))
project = input("Project submitted? (yes/no): ")

project_sub = True if project == "yes" else False

if nn >= 90:
    if project_sub:
        print("A+")
    else:
        print("A")
elif nn >= 80:
    print("B")
elif nn >= 70:
    print("C")
elif nn >= 60:
    print("D")
else:
    print("E")






    



