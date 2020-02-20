class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        tokens = str.split()
        if (len(tokens) != len(pattern)):
            return False

        dictionary = {}
        for i, words in enumerate(tokens):
            if (words in dictionary.keys()):
                if (pattern[i] == dictionary[words]):
                    continue
                else:
                    return False
            else:
                if (pattern[i] in dictionary.values()):
                    return False
                dictionary[words] = pattern[i]

            return True