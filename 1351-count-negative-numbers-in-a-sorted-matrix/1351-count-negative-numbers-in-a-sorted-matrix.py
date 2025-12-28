class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        flat_list = [item for sublist in grid for item in sublist]
        count = 0
        for i in flat_list:
            if i < 0 :
                count+=1
        
        return count