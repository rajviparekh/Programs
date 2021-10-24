class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        maxRow = maxCol = n
        startRow, startCol = 0, 0
        currRow, currCol = 0,0
        dir = 'R'
        valueCounter = 1
        result = [[False] * n for _ in range(n)]
        while currRow < n and currCol< n and valueCounter < n*n +1: #spiralling across all values in matrix
            if dir == 'R':
                for currCol in range(startCol, maxCol):
                    if not result[currRow][currCol]:
                        result[currRow][currCol] = valueCounter
                        valueCounter += 1
                    
                startRow += 1
                dir = 'D'
            if dir == 'D':
                for currRow in range(startRow, maxRow):
                    if not result[currRow][currCol]:
                        result[currRow][currCol] = valueCounter
                        valueCounter += 1
                maxCol -= 1
                dir = 'L'
            if dir == 'U':
                for currRow in range(maxRow, startRow-1, -1):
                    if not result[currRow][currCol] :
                        result[currRow][currCol] = valueCounter
                        valueCounter += 1
                    
                startCol += 1
                dir = 'R'
            if dir == 'L':
                for currCol in range(maxCol, startCol-1, -1):
                    if not result[currRow][currCol]:
                        result[currRow][currCol] = valueCounter
                        valueCounter += 1
                    
                maxRow -= 1
                dir = 'U'
        return result