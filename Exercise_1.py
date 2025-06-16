# S30 Problem #62 Rotting Oranges
#LeetCode #994 https://leetcode.com/problems/rotting-oranges/description/

# Author : Akaash Trivedi
# Time Complexity : O(m*n)
# Space Complexity : O(m*n)
# Did this code successfully run on Leetcode :  Yes #
# Any problem you faced while coding this : No

# dfs
# taking offset by 2 and updating the values so we dont visit the node that have less time again
# do dfs on node with rotten orange "2"

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        drcn = [[1,0],[0,-1],[-1,0],[0,1]]
        fresh = 0 # count number of fresh oranges
        time = 0 # result / min elapse 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    self.dfs(grid,i,j, 2, drcn)
        
        maxtime = 2
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: return -1
                maxtime = max(maxtime, grid[i][j])
        
        # take offset out and return
        return maxtime - 2

    def dfs(self, grid, r, c, time, drcn):
        #base
        if r < 0 or c < 0 or r == len(grid) or c == len(grid[0]): 
            return
        # if has smaller time then dont go
        # if 1 we should visit
        if grid[r][c] != 1 and grid[r][c] < time:
            return
        # logic
        grid[r][c] = time # if its smaller time
        for dr in drcn:
            nr = r + dr[0]
            nc = c + dr[1]
            self.dfs(grid, nr, nc, time+ 1, drcn)

# bfs 

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        drcn = [[1,0],[0,-1],[-1,0],[0,1]]
        queue = deque()
        fresh = 0 # count number of fresh oranges
        time = 0 # result / min elapse 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append([i,j])
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0: return 0
        while queue:
            size= len(queue) # taking size as we need to know when the level finishes
            for i in range(size):
                curr = queue.popleft()
                for dr in drcn:
                    nr = curr[0] + dr[0]
                    nc = curr[1] + dr[1]
                    if nr >= 0 and nc >= 0 and nr < m and nc < n and grid[nr][nc] == 1:
                        queue.append([nr,nc])
                        grid[nr][nc] = 2
                        fresh -= 1
            time += 1
        # if all are not rotten
        if fresh != 0: return -1
        # when last level is processed the time is increased, so -1
        return time - 1
