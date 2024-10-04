class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        sumofchem=0
        n=len(skill)
        skill.sort()
        target=skill[0]+skill[-1]
        for i in range(n//2):
            if skill[i]+skill[-i-1]!=target:
                return -1
            sumofchem+=skill[i]* skill[-i-1]
        return sumofchem
            