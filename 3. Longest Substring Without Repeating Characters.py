class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub = ""
        length = 0
        
        for i in s:
            if i not in sub:
                sub += i
                length = max(len(sub), length)
            else:
                sub = sub[sub.index(i) + 1:]
                sub += i
        
        return length
