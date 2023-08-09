import numpy as np



nums = np.array(list(map(int,input("enter elements").split())))
nums.sort()
key = int(input("enter the target"))

pivot = int(len(nums)/2)

def binaryS(pivot,key):
    
    if key == nums[pivot]:
        return pivot
        if key < nums[pivot]:
            return binaryS(pivot-1,key)
        if key > nums[pivot]:
            return binaryS(pivot+1,key)
    else:
        return -1


print(binaryS(pivot,key))
        





