class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        ch=0
        for i in range(len(word)):
            if word[i].isupper():
                ch+=1
        if(ch == len(word)):
            return True
        elif(ch==0):
            return True
        elif(ch==1 and word[0].isupper()):
            return True
        else:
            return False

        