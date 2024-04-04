#  REVERSE OF STRING

# string_name  = "Main tera Hero"

# rev_str =""

# for char in string_name:
#     rev_str = char + rev_str

# print(rev_str)    


# FACTORIAL OF A NUMBER

# num = int( input(" Enter a number"))

# ans = 1 

# for i in range(1 , num + 1):
#     ans = ans * i

# print( ans )    


# VALIDATE INPUT

# num = int( input( " Enter a number \n"))

# while( True ):
#     if(num >=1  and num <= 10):
#         print("Entered number is a valid input",num)
#         break
#     else:
#         num = int( input( " Enter a number \n"))

# CHECK PRIME

# num = int(input("Enter a number \n"))

# flag = 0 

# if(num <= 1):
#     flag = 1 
    
    

# for i in range(2 , num):
#     if( num % i == 0 ):
#         print("Not a prime number")
#         flag = 1 
#         break

# if( flag == 0 ):
#     print("Prime number") 


# DUPLICATE IN A LIST

# items =["banana" , "apple" , "orange" , "apple"]

# unique_set = set()

# for item in items:
#     if(item in unique_set):
#         print("Duplicate found :" , item)
#         break
#     unique_set.add(item)

# if len(unique_set) == len(items):
#         print("No duplicate found")


import time

attempts = 0
max_retries = 6
wait_time = 1

while( attempts < max_retries):
    print("Attempt" , attempts + 1 ,"- wait time" , wait_time)
    time.sleep(wait_time)
    wait_time *= 3
    attempts += 1 

