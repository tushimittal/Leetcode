class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timeToMinutes = lambda time: int(time[:2]) * 60 + int(time[3:])
        
        minutes = sorted([timeToMinutes(time) for time in timePoints])
        
        min_diff = min(minutes[i] - minutes[i - 1] for i in range(1, len(minutes)))
        
        min_diff = min(min_diff, 1440 - minutes[-1] + minutes[0])
        
        return min_diff
