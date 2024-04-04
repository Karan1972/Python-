def maxSubarray(arr):

    length = len(arr)
    ans = arr[ 0 ]
    temp = arr[ 0 ]
    

    for i in range( 1 , length):

        temp += arr[ i ]

        if temp > arr[ i ]:
            if ans < temp:
                ans = temp

        else:
            temp = arr[ i ]
            ans = temp          

    return ans       

arr = [-2,1,-3,4,-1,2,1,-5,4]    
#arr = [5,4,-1,7,8] 

print( maxSubarray(arr))