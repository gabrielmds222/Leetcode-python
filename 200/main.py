class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, column = len(grid), len(grid[0])
        islands = 0
        visit = set()

        def dfs(i, j):
            q = colections.deque()
            visit.add(i, j)
            q.append((i, j))

            while q:
                row, column = q.popleft()
                dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in dir:
                    i, j = row + dr, column + dc
                    if (i in range(row) and c in range(column) and grid[i][j] == "1" and (i, j) not in visit):
                        q.append(i, j)
                        visit.append(i, j)
        
        for i in range(row):
            for j in range(column):
                if grid[i][j] == "1" and (i, j) not in visit:
                    dfs(i, j)
                    islands += 1
        return islands