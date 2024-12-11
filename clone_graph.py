"""
BFS: TC:o(n) and SC: O(n)
Todo: DFS
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

from typing import Optional


class Solution:
    def clone(self, node):
        # check if the node is in hmap
        # if not create a deep copy and add to hmpa
        if node not in self.hmap:
            self.hmap[node] = Node(node.val)  # Node(node.val) is the copy of the node
        return self.hmap[node]  # return the reference to the copy of node

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:  # node is a reference to the node
            return

        self.hmap = {}
        q = deque()
        # append the node to the queue
        q.append(node)

        # create the deep copy of the node
        copyNode = self.clone(node)

        while q:
            curr = q.popleft()
            for ne in curr.neighbors:
                if ne not in self.hmap:
                    # add  it to the queue
                    q.append(ne)

                # the neighbours are always added to the cloned
                # does not matter if they are in hmap or not
                # if in hmap get the deepcopy from the hmap
                deepCopy = self.hmap[curr]
                # to this deep copy add the neighbours of the curr node
                # create clone of the neighbour
                clonedNeigh = self.clone(ne)
                deepCopy.neighbors.append(clonedNeigh)

        return copyNode






