class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Plan 1: Sliding window
        # TC: O(N)
        # SC: O:(N)

        l, total = 0, 0
        charSet = set()

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            total = max(total, r - l + 1)

        return total
