
""" This file contains warm up exercises for Grocking the Coding interview"""


###      CONTAINS DUPLICATE (EASY)     ###


#  - Test Cases - #
test1 = [1,2,3,4]
test2 = [1,2,3,1]

class Solution:
    def containsDuplicate(self, nums):
      target_num = None

      for index,num in nums:
        

