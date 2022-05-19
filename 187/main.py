class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, result = set(), set()

        for i in range(len(s) - 9):
           current = s[i:i + 10]
           if current in seen:
                result.add(current)
           seen.add(current)
        return list(result)