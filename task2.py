# Swap values of two variables and print before and after 

x = 10
y = 20

# first Method 

# temp = x # temp = 10
# x = y    # x = 20
# y = temp # y = 10


# print("X:-",x) 
# print("Y:-",y)

# Second Method

# x = x + y # 10 + 20 = 30
# y = x - y # 30 - 20 = 10
# x = x - y # 30 - 10 = 20 

# print("X",x)
# print("Y",y)

x,y = y,x
print("X",x)
print("Y",y)

