class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        output = [""]

        for i in digits:
            tmp = []
            for j in dic[i]:
                for k in output:
                    tmp.append(k + j)
            output = tmp

        return output