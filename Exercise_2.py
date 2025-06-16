# S30 Problem #63 Employee Importance
#LeetCode #690 https://leetcode.com/problems/employee-importance/description/

# Author : Akaash Trivedi
# Time Complexity : O(n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode :  Yes #
# Any problem you faced while coding this : No

# Approach
# DFS
# to search the current id and its sub form the employee list we use hash map
# use DFS to traverse over suborsinates and add its importance to result

class Solution:
    # global variable to store result
    def __init__(self):
        self.imp = 0

    def getImportance(self, employees: List['Employee'], id: int) -> int:
        hashm = dict()
        # storing emp id to employee obj
        for emp in employees:
            hashm[emp.id] = emp
        self.dfs(hashm[id], hashm)

        return self.imp

    def dfs(self, root, hashm):
        # base
        # no base case as for loop take care of it

        #logic
        self.imp += root.importance
        for sub in root.subordinates:
            self.dfs(hashm[sub], hashm)



"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
# BFS
# to search the current id and its sub form the employee list we use hash map
# use BFS to go over all the subordinates and calculate their imps

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        hashm = dict()
        # storing emp id to employee obj
        for emp in employees:
            hashm[emp.id] = emp
        
        # queue for BFS
        queue = deque()
        queue.append(hashm[id])
        imp = 0 
        while queue:
            curr = queue.popleft()
            imp += curr.importance

            for sub in curr.subordinates:
                queue.append(hashm[sub])

        return imp