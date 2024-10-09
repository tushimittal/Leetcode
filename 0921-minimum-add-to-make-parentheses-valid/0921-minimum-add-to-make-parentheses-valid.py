class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        n=len(s)
        count1=0
        required=0
        for i in range(n):
            if(s[i]=="("):
                count1+=1
            else:
                if count1>0:
                    count1-=1
                else:
                    required +=1
        return required+count1