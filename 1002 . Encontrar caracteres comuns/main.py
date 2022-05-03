class Solution:
    def commonChars(self, palavra: List[str]) -> List[str]:
        palavra = palavra[0]
        for i in range(1, len(palavra)):
            palavra = [x for x in palavra if x in palavra[i]]
        return palavra
            