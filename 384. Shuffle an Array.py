import random

class Solution(object):

    def __init__(self, nums):
        self.nums = nums
        

    def reset(self):
        return self.nums
        

    def shuffle(self):
        answer = self.nums[:]
        start = 0
        for i in range(len(answer)):
            index = random.randint(start, len(answer) - 1)
            temp = answer[i]
            answer[i] = answer[index]
            answer[index] = temp
            start += 1
        
        return answer
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
