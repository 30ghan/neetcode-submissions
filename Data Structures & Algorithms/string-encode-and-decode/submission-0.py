class Solution:

    def encode(self, strs: List[str]) -> str:
        results = ''
        for s in strs:
            results += str(len(s)) + "#" + s
        return results

    def decode(self, s: str) -> List[str]:
        results = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            word = s[j + 1: j + 1 + length]
            results.append(word)

            i = j + 1 + length

        return results
