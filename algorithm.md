# 算法

## 最长子序列（匹配）

如 ： 给定两数列nums1,nums2于两平行线上，连接两数列相等元素，求最大连接数

这类问题符合最优子结构：即nums1[:i]与nums2[:j]之间的匹配如果是最优的，nums1[:i+1]和nums2[:j+1]之间的最有匹配只需考虑nums1[i+1]和nums[j+1]之间能否匹配


dp[i][j] 指 nums1[:i-1]与nums2[:j-1]之间的匹配数量，则

dp[i][j] = (dp[i-1][j-1] + 1) if nums1[i-1] == nums2[j-1] else max(dp[i-1][j],dp[i][j-1])


## 接雨水 42

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

### 双指针法

考虑在i处能接到的雨水数量为：

max(height[:i-1])和max(height[i+1:])之间的最小值

可构建leftMax与rightMax数组，leftMax[i] = max(height[:i-1])减少重复计算

或维护leftMax、rightMax、left和right变量：两对者从数列两端开始迭代

注意到：

leftMax较大时，right处必定能存rightMax量的水

rightMax较大时，left处必定能存leftMax量的水

二者相等时，left与right处各结算一次（注意left==right的可能性）

### 单调栈

维护一个下侧元素大于上侧元素的栈，将高度依次入栈；无法入栈时弹出之前的项，并根据即将入栈的值和要出栈的值计算储水量