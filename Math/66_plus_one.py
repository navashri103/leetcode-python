class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s=""
        for i in range(len(digits)):
            s=s+str(digits[i])
        m=int(s)
        y= m + 1
        z=str(y)
        n=[]
        for i in range (len(z)):
            n.append(int(z[i]))
        return n