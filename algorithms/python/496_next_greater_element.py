class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        results = []
        for findNum in findNums:
            index = nums.index(findNum)
            result = index + 1
            for candidate in nums[index + 1:]:
                if candidate > findNum:
                    results.append(candidate)
                    break
                else:
                    result += 1

            if result >= len(nums):
                results.append(-1)

        return results


# Solution 2

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        result_hash = {}
        stack = []

        for num in nums:
            while stack and num > stack[-1]:
                result_hash[stack.pop()] = num
            stack.append(num)

        return [result_hash.get(x, -1) for x in findNums]
