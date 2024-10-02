class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        num={}
        sortedArr=sorted(arr)
        rank=1
        for i in range(len(sortedArr)):
            if i>0 and sortedArr[i] > sortedArr[i-1]:
                rank+=1
            num[sortedArr[i]]=rank
        for i in range(len(arr)):
            arr[i]=num[arr[i]]
        return arr