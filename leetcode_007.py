# #LeetCode_007-Reverse-Integer
# Given a number, reverse its digits.   If the reversed number is bigger than 32-bit integer range, return 0.  
# 7. Reverse Integer
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
# Example 1:
# Input: x = 123
# Output: 321
# Example 2:
# Input: x = -123
# Output: -321
# Example 3:
# Input: x = 120
# Output: 21
# Constraints:
# -231 <= x <= 231 - 1




class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        int_min = -2 ** 31
        int_max = 2 ** 31 - 1
        r = 0 

        sign = -1 if x < 0 else 1
        x = abs(x)  # 取絕對值
        
        while True:  # x 變成 0 就跳
            if x == 0:
                break

            digits = x % 10
            x = x // 10  # 整除

            if r > (int_max // 10):
                return 0
            
            r = r * 10 + digits

        return r * sign

        
