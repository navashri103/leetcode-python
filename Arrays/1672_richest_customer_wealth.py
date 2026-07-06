class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        m=len(accounts)
        max=0
        for i in range(m):
            n=len(accounts[i])
            num=0
            for j in range(n):
                num=num+accounts[i][j]
            if(num>max):
                max=num 
        return max 