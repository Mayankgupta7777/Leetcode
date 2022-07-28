#Simple O(n)--> Time complexity code:

class Solution:
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)
