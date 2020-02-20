class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        dictionary = {}
        for i in range(len(s)):
            if s[i] in dictionary:
                if dictionary[s[i]] != t[i]:
                    return False
            else:
                if t[i] in dictionary.values():
                    return False
                else:
                    dictionary[s[i]] = t[i]
        return True
