import frontier
import exploredset
from node import Node


class Agent:
    gDebug = False

    def __init__(self):
        self.frontier = frontier.Frontier()
        self.exset = exploredset.ExploredSet()

    def search(self, start, goal):
        self.frontier.add(Node(None, start, None))

        while True:
            if self.gDebug:
                self.frontier.print()
                self.exset.print()

            if self.frontier.isEmpty():
                return None
            p = self.frontier.pop()
            if p.getState() == goal:
                return p
            self.exset.add(p)

            neighbors = p.findNeighbors()
            for n in neighbors:
                if not self.frontier.check(n) and not self.exset.check(n):
                    self.frontier.add(n)
