class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            sign = -1
        
        num = x * sign
        reverse = int(str(num)[::-1])
        if reverse > 2**31:
            reverse = 0
            
        return reverse * sign
        
