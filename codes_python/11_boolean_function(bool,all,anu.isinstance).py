# # print('boolean expression')

print(bool(123))
print(type(True))
print(bool(0))
print(bool(""))
print(bool(None))

savings = 100
new_savings = 40


total_saving=savings+new_savings
print(total_saving)
print(type(total_saving))


# boolean functions 
#True and Faose

print(type(100))
print(type(0))
print(bool("100"))


# #Any with True and False

# # any will one value true  result true

a=''
b='98881289288'
c='' 
print(any([a,b,c])) # one true valee that is b


# # any will all false value true  result false

a=''
b=''
c='' 
print(any([a,b,c])) # all are false value

# # any will all True value true  result with True

a='abc'
b='98881289288'
c='def' 
print(any([a,b,c])) # All are true values 

# print('************************************************************')

# # all will one value true  result False

a=''
b='98881289288'
c='' 
print(all([a,b,c])) # one true valee that is b


# # all will all false value true  result False

a=''
b=''
c='' 
print(all([a,b,c])) # all are false value

# # all will all True value true result True

a='abc'
b='98881289288'
c='def' 
print(all([a,b,c])) # All are true values 

# #isinstance


print(isinstance(2,int))     #True
print(isinstance('gowda',int))    #False
print(isinstance('gowda',str))    #True



