class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        x=[]
        for i in range (len(s)):
            if(s[i] in "aeiouAEIOU"):
                x.append(s[i])
        x.reverse()
        y=[]
        j=0
        for i in range (len(s)):
            if(s[i] in "aeiouAEIOU"):
                y.append(x[j])
                j=j+1
            elif(True):
                y.append(s[i])
        return "".join(y)






        