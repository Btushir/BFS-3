"""
Start by exhaustive approach such as: remove one parenthesis and then check if the substring formed is valid or not.
This could be done using BFS and DFS.
For BFS: once at a given level, we found the valid parentheses no need to proceed further.
DFS is the exhaustive approach. Since it will explore the all babies of all the levels.
BFS is better here.
TC: O(2^n)*n, SC: O(n)
"""

from collections import deque

class Solution_bfs_with_size:
    def isValid(self, s):
        count = 0
        for c in s:
            if count < 0:
                return False
            if c == "(":
                count += 1
            elif c == ")":
                count -= 1

        if count != 0:
            return False
        return True

    def bfs(self, s, validStr):
        q = deque()
        q.append(s)
        # it is possible after removing the parentheses
        # same string is prodcued to avoid visiting the same path
        # use hset
        hset = set()
        hset.add(s)
        flag = False
        while q:
            size = len(q)
            # process one level fully
            for _ in range(size):
                curr = q.popleft()
                if self.isValid(curr):
                    print(curr)
                    flag = True
                    validStr.append(curr)

                # the given index should not be part of the
                # new string
                for i in range(len(curr)):
                    new_str = curr[:i] + curr[i + 1:]
                    if new_str not in hset:
                        q.append(new_str)
                        hset.add(new_str)
            if flag:
                return

    def removeInvalidParentheses(self, s: str) -> List[str]:
        validStr = []
        self.bfs(s, validStr)
        return validStr




class Solution_without_size:
    def isValid(self, s):
        count = 0
        for c in s:
            if count < 0:
                return False
            if c == "(":
                count += 1
            elif c == ")":
                count -= 1

        if count != 0:
            return False
        return True

    def bfs(self, s, validStr):
        # no need for size variable: why? once valid string is found,
        # the next level will have all strings are invalid since the length
        # would be odd.
        q = deque()
        q.append(s)
        # it is possible after removing the parentheses
        # same string is prodcued to avoid visiting the same path
        # use hset
        hset = set()
        hset.add(s)
        flag = False
        while q:
            curr = q.popleft()
            if self.isValid(curr):
                print(curr)
                flag = True
                validStr.append(curr)

            # the given index should not be part of the
            # new string
            if not flag:
                for i in range(len(curr)):
                    # skip if the current ch is alphabet
                    if not curr[i].isalpha():
                        new_str = curr[:i] + curr[i + 1:]
                        if new_str not in hset:
                            q.append(new_str)

    def removeInvalidParentheses(self, s: str) -> List[str]:
        validStr = []
        self.bfs(s, validStr)
        return validStr


class Solution_dfs:
    def isValid(self, s):
        count = 0
        for c in s:
            if count < 0:
                return False
            if c == "(":
                count += 1
            elif c == ")":
                count -= 1

        if count == 0:
            return True
        return False

    def dfs(self, s):

        # base case
        # since we are finding the string with minimum length
        # we dont explore path whose len is smaller than the already found
        # valid string.
        if len(s) < self.max_len:
            return

        if self.isValid(s):
            # if a string with higher length is found than the already one
            # then clear the result and update
            if len(s) > self.max_len:
                self.max_len = len(s)
                self.ans = []
            # if of same lenght then append also append if the ans is reset.
            self.ans.append(s)
            return

        # logic
        # form the babies
        for i in range(0, len(s)):
            if not s[i].isalpha():
                sub_str = s[:i] + s[i + 1:]
                if sub_str not in self.hset:
                    self.hset.add(sub_str)
                    self.dfs(sub_str)

    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.hset = set()
        self.max_len = float("-inf")
        self.ans = []
        self.hset.add(s)
        self.dfs(s)

        return self.ans
