class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        for i in range(n):
            if(i==0):
                new=[]
                new.append(nums[i])
            else:
                new.append(new[i-1]+nums[i])
        return new 
