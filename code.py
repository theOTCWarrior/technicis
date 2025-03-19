class Solution:
    def canJump(self, nums: List[int]) -> bool:
		n = len(nums)
		max = nums[0]  + 0
        dp = [False for _ in range(n+1)]
		dp[0] = True # always can reach the 0th index
		for i in range(1,n+1): # i-1
			if max < nums[i-1] + i-1 :
				max = nums[i-1] + i-1
			if i-1 <= max :
				dp[i] = True
		return dp[n]
# 55

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
		dp = [ None for _ in range(n)]
		dp[0] = 0
		for i in range(1,n)
			for j in range(i)
				if j + nums[j] >= i and dp[j] + 1 < dp[i] :
					dp[i] = dp[j] + 1
		return dp[n-1]
		
#45


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort().reverse()
		i = 0
		while i < len(citations) and citations[i] >= i :
			i += 1
		i -= 1
		return i

class Solution: # with extra space
    def hIndex(self, citations: List[int]) -> int:
		n = len(citations)
        buckets = [0 for _ in range(1002)]
		for cite in citations:
			buckets[cite] += 1
		
		h = len(buckets)
		count = 0
		while count < h:
			h -= 1
			count += buckets[h]
			
		return h
	
#274
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
		left = 1
		output = [1 for _ in range(n)]
		for i in range(n) :
			if i > 0:
				left *= nums[i-1]
			for j in range(i+1, n) :
				if output[i] != 0 and left != 0:
					output[i] *= nums[j]
			if output[i] != 0 and left != 0:
				output[i] *= left
		return output

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
		n = len(nums)
		left = [1 for _ in range(n)]
		right = [1 for _ in range(n)]
		output = [1 for _ in range(n)]
		for i in range(1,n) :
			left[i] = left[i-1] * nums[i]
		for i in range(n-2,-1,-1) :
			right[i] = right[i+1] * nums[i]
		for i in range(n) :
			output[i] = left[i] * right[i]
		return output
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
		n = len(nums)
		output = [1 for _ in range(n)]


#238

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(cost)
		max_reach = 0
		dp = [[] for _ in range(n)]
		
		
#134 greedy / dp


class Solution:
    def candy(self, ratings: List[int]) -> int:
		candies = [1 for _ in range(n)
        for i in range (1,n) :
			if ratings[i] > ratings[i-1] :
				candies[i] = candies[i-1] + 1
		for i in range(n-2, -1, -1) :
			if ratings[i] > ratings[i+1] :
				candies = candies[i+1] + 1
		sum = 0
		for i in range(n) :
			sum += candies[i]
		return sum

#135

class Solution:
    def trap(self, height: List[int]) -> int:
		n = len(height)
		sum = 0
        leftMax = [height[0] for _ in range(n)]
		rightMax = [height[n-1] for _ in range(n)]
		for i in range(1,n) :
			leftMax[i] = max(leftMax[i-1],height[i])
		for i in range(n-2,-1,-1) :
			rightMax[i] = max(rightMax[i+1],height[i])
		for i in range(n) :
			sum += min(leftMax[i],rightMax[i]) - height[i] if (min(leftMax[i],rightMax[i]) - height[i]) >= 0 else 0
		return sum

class Solution:
    def trap(self, height: List[int]) -> int:
		n = len(height)
		sum = 0
		left, leftMax, right, rightMax = 0, height[0], n-1, height[n-1]
		while left < right :
			if leftMax < rightMax :
				sum += leftMax - height[left] if (leftMax - height[left]) >= 0 else 0
				left += 1
				leftMax = max(leftMax,height[left]
			


#42