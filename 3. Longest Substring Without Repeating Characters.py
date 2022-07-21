class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        
        result = 1
        window_set = {s[0], }
        left = 0
        right = 1
        
        while right < len(s):
            if s[right] not in window_set:
                window_set.add(s[right])
                right += 1
            else:
                left += 1
                window_set.remove(s[left-1])
            result = max(result, len(window_set))        
        return result




#REMEMBER THIS CODE HAS BEEN DONE IN PYTHON 3.

#RESULT: 38ms
