class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = str.strip()
        sign = 1
        answer = 0
        mydict = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
         
        for i in range(len(s)):
            if i == 0 and s[i] == '-':
                sign = -1
            elif i == 0 and s[i] == '+':
                sign = 1
            elif s[i] in mydict: 
                answer = answer * 10 + mydict[s[i]]
            else:
                break
        
        if sign == 1 and answer > (2**31 - 1):
            answer = 2**31 - 1
        if sign == -1 and answer > (2**31):
            answer = 2**31
        
        return sign * answer
        
