class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        A=s.split()
        w=A[-1]
        return len(w)
        