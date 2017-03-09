# Write a program that outpus the string representation of numbers from 1 to n
# But for multiples of 3 it should output "Fizz" instead of the number and for
# the multiples of 5 output "Buzz". For numbers which are multiples of both
# 3 and 5 output "FizzBuzz".

# example:

# n = 15
# return ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "15", "FizzBuzz"]


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        for i in range(1, n+1):
            if i % 5 == 0 and i % 3 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))

        return result
