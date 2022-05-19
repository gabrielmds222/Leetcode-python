class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        maxLen = 0
        result = 0

        for count in range(len(s)):
            while s[count] in charSet:
                charSet.remove(s[maxLen])
                maxLen += 1
            charSet.add(s[count])
            result = max(result, count - maxLen + 1)
        return result