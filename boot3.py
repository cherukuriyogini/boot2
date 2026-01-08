#Input:

#nums = [1, 2, 3, 1]


#Output:

#2

#Explanation:
#The element at index 2 is 3, which is greater than its neighbors (2 and 1), so it is a peak element.
def peakelement(nums):
    left=0 

    right=len(nums)

    while left<right:
        mid=(left+right)//2

        if num[mid] < nums[mid+1]:
            left=mid+1
        else:
            right=mid

    return left

