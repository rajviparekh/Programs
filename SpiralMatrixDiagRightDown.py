class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if not matrix: 
            return result
        maxRow,maxCol = len(matrix)-1,len(matrix[0])-1
        currRow, currCol = 0,0
        
        dir = 'DU' #DU is diagonal up, DD is diagonal down
        
        while currRow in range(maxRow+1) and currCol in range(maxCol+1):
            if dir == 'DU':
                
                result.append(matrix[currRow][currCol])
                # can move up only till 1st row or last col
                while currRow > 0  and currCol < maxCol:
                    currRow -= 1
                    currCol += 1
                    
                    result.append(matrix[currRow][currCol])
                    
                # end of upward diagonal ; determine next direction down or right
                if currCol == maxCol:
                    # can move only down and not right
                    dir  = 'D'
                else:
                    dir = 'R'
            if dir == 'DD':
                
                result.append(matrix[currRow][currCol])
                # can move down only till last row or first col
                while currRow < maxRow and currCol > 0:
                    currRow += 1
                    currCol -= 1
                    
                    result.append(matrix[currRow][currCol])
                # end of downward diagonal ; determine next direction down or right
                if currRow == maxRow:
                    # cannot go down
                    dir = 'R'
                else:
                    dir = 'D'
                    
            if dir == 'D':
                currRow += 1
                if currCol == maxCol:
                    dir = 'DD'
                else:
                    dir = 'DU'
            
            if dir == 'R':
                currCol += 1
                if currRow == maxRow:
                    dir = 'DU'
                else:
                    dir = 'DD'
            
        return result