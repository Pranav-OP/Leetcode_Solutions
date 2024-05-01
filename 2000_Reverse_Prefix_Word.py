class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if word[i] == ch:
                prefix = word[:i+1]
                reversed_prefix = prefix[::-1]
                return reversed_prefix + word[i+1:]
        return word