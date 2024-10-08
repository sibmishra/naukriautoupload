# Given an array A and an integer target, find the indices of the two numbers in the array whose sum is equal to the given target.
#
# Note: The problem has exactly one solution. Do not use the same element twice.
#
# Example
# A: [1, 3, 3, 4]
# target: 5
# Answer: [0, 3]

class Solution:
    def twoSum(self, A, target):
        # add your logic here
        for i in range(0, len(A) + 1):
            for j in range(i + 1, len(A)):
                sum = A[i] + A[j]
                if sum != target:
                    j += 1
                else:
                    print(i, j)
            i += 1
        return i, j


s = Solution()
list1 = [2, 1, 3, 3, 2, 4]
aaa = s.twoSum(list1, 5)
print(aaa)

#    browser.find_element(By.XPATH,'//a[@href="https://www.naukri.com/mnjuser/profile?id=&altresid"]').click()
