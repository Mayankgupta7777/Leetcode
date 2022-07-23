class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        d = 0
        if(len(s) == 0 or ord(s[0]) >= 65 or ord(s[0]) >= 97 or s[0] == '.'):
            return 0
        if(s[0] == '-'):
            d = -1
            s = s[1:]
        elif(s[0] == '+'):
            s = s[1:]
        else:
            s = s
            
            
        n = " "
        l_range = -(2**31)
        r_range = 2**31-1    
        for s in s:
            try:
                if(ord(s) == 32 or s == '.'  or ord(s) >= 65 or s == '-' or s == '+'):
                    break
                elif(int(s) >= 0 and int(s) <= 9):
                    n += s
            except:
                continue
        if(d < 0):
            try:
                n = -int(n)
            except:
                return 0
        else:
            try:
                n = int(n)
            except:
                return 0
            
            
        if(n < l_range):
            return l_range
        elif(n > r_range):
            return r_range
        else:
            return n
          
          
          #RESULT: 42ms
