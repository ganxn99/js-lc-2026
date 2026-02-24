# Sliding window 
# reference: https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4502/ 


#  Q1 
# Example 1: Given an array of positive integers nums and an integer k, 
# find the length of the longest subarray whose sum is less than or equal to k. 

# Solution 
# param (int nums, int k) 
# return int longest  
# right - left + 1 

def find_length(nums, k):
    # initialize left/right pointer & answer  
    left = curr = ans = 0
    # iterate through the array 
    for right in range(len(nums)):
        # add the current right value to the current sum 
        curr += nums[right]
        # if the current sum is greater than k, we need to move the left pointer 
        while curr > k:
            # subtract the left value from the current sum 
            curr -= nums[left]
            # move the left pointer to the right 
            left += 1
        # update the answer with the maximum length of the subarray 
        ans = max(ans, right - left + 1)
    return ans
