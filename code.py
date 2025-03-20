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
        for i in range(1,n) :
            output[i] = output[i-1] * nums[i-1]
            output[n-1-i] = output[n-i] * nums[n-i]
        return output
        
        
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 1
        right = 1
        output = [1 for _ in range(n)]
        for i in range(1,n) :
            left *= nums[i-1]
            right *= nums[n-i]
            output[i] *= left
            output[n-i] *= right
        return output
    
        
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
        if n == 0:
            return 0
        left, right = 0, n - 1
        left_max, right_max = height[left], height[right]
        total_water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                total_water += max(0, left_max - height[left])
            else:
                right -= 1
                right_max = max(right_max, height[right])
                total_water += max(0, right_max - height[right])

        return total_water

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        left, right = 0, n - 1
        left_max, right_max = height[left], height[right]
        total_water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                total_water += max(0, left_max - height[left])
            else:
                right -= 1
                right_max = max(right_max, height[right])
                total_water += max(0, right_max - height[right])

        return total_water



#42


class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        n = len(s)
        word_count, letter_count, index_left, index_right = 0, 0, 0, 0
        while index_left < n and index_right < n :
            # print("before left move",index_left,index_right)
            while index_left < n and s[index_left] == ' ' :
                index_left += 1
            # now s[index_left] is a letter
            index_right = index_left
            if index_left < n :
                word_count += 1
            
            while index_right < n and s[index_right] != ' ' :
                index_right += 1
                letter_count += 1
            # now s[index_right] is a space and s[index_right] is a letter
            # print("after right move",index_left,index_right)
            for i in range((index_right-index_left)//2) :
                s[index_left+i],s[index_right-i-1] = s[index_right-i-1],s[index_left+i]

            index_left = index_right
            
        index_set, index_pick = 0, 0
        while index_pick < n : ## delete surplus spaces
            while index_pick < n and s[index_pick] == ' ' :
                index_pick += 1
            while index_pick < n and s[index_pick] != ' ' :
                s[index_set] = s[index_pick]
                index_pick += 1
                index_set += 1
            if index_set < n :
                s[index_set] = ' '
                index_set += 1
        str_length = letter_count + word_count - 1
        
        for i in range(str_length // 2) :
            s[i], s[str_length-1-i] = s[str_length-1-i], s[i]
        
        return ''.join(s[:str_length])
        
# 151

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        strs = [[] for _ in range(numRows)]
        n = len(s)
        position = list(range(numRows)) + list(range(numRows-2,0,-1))
        pn = len(position)
        for i in range(n) :
            strs[position[i%pn]].append(s[i])
        return ''.join([''.join(row) for row in strs])

# 6



class Solution:
    def strStr(self,haystack: str, needle: str) -> int:
        nh = len(haystack)
        nn = len(needle)
        next_array = [0 for _ in range(nn)]
        # next[i] 表示 needle[:i+1]的最长公共前后缀的长度。
        j = 0 ## dual pointer i and j
        for i in range(1,nn) :
            while j > 0 and needle[j] != needle[i] :
                j = next_array[j-1]
            if needle[j] == needle[i] :
                j += 1
            next_array[i] = j
# 当needle匹配成功了j-1个然后发现不匹配时，例如匹配到了sadsad中的第二个sa,此时j要回退到d的位置避免重复匹配 j = 5
# next_array[j] = 2， 意味着 needle[0:2]和needle[j-next_array[j]:j]相同 回退是基于最长公共前后缀的
        i = 0  # haystack pointer
        j = 0  # needle pointer
        while i < nh:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j != 0:
                    j = next_array[j - 1]
                else:
                    i += 1
            if j == nn:
                return i - nn
        return -1



# 28 kmp