# print("int data types ")
import math
import random


# 📖 Table of Content
# 00:00 - intro
# 00:25 - 3 Types of Numbers
# 04:22 - Number Functions Type
# 08:15 - Math Operators
# 12:17 - Rounding
# 22:14 - Random
# 24:42 - Validation
# 27:56 - Python Challenge


# convert data types easily string to fload to int 

# types
a=100
b=3.5
c=2+4j



print(type(a))

print(type(b))

print(type(c))


x=100
y=200 
print(complex(a+b))


monthly_savings=10;
num_months=4;
new_savings=(num_months*monthly_savings)
print(new_savings)

# math operators (+,-,*,%,/,//,%,**)

print(3+2)
print(3-2)
print(3*2)
print(3/2)
print(3//2)
print(3%2)
print(3**2)


# Rounding 

print(3-8)
print(abs(3-8))  # remove the minus value using abs

price=37.894523
print(round(price))   # round to 37

#floor()

price2=37.894523
print(math.floor(price2)) 


#ceil()
price2=37.894523
print(math.ceil(price2))  


#trunc

price2=37.894523
print(math.trunc(price2))   # truncate all after the full stop


price3=2
print(math.sqrt(price3))  


#Random
print(random.random())

print(random.randint(2,4)) 


#validation (is_integer and )

price4=3.2
print(price4.is_integer())  # becouse .2 is the values 

price5=3.0
print(price5.is_integer())  # becouse .0 is the no values its zero 









