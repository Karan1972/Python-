# CUBE OF A NUMBER USING FUNCTIONS

# def cube(number):
#     return number**3


# num = int( input("Enter a number \n"))
# ans = cube(num)
# print(ans)

# MULTIPLICATION WITH POLYMORPHISM

# def mult( var1 , var2):
#     return var1*var2

# print( mult(3 , 2))
# print( mult(2, 'q'))
# print(mult('ww', 3))

# PLAY WITH RADIUS

# import math

# def circle( radius):
#     area = math.pi * radius**2
#     circum = 2 * math.pi * radius
#     return area , circum

# Area , Circumference = circle(5)

# print( " Area of circle is :" , Area )
# print(" Circumference of circle is : " , Circumference)

# FACTORIAL

def fact( num ):

    if( num == 0):
        return 1 
    else:
        return num * fact( num -1 )
    
print(fact(2)*fact(3))    