class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y=str(x)
        n=y[::-1]
        if(y==n):
            return True
        return False