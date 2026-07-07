class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq={}
        count=0
        for i in nums:
            if i in freq:
                count+=freq[i]
                freq[i]+=1
            else:
                freq[i]=1
        return count

    