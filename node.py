from state import State
from action import Action


class Node:
    def __init__(self, n, st, act):
        self.parent = n
        self.state = st
        self.action = act

    def __eq__(self, other):
        return self.state == other.state

    def print(self):
        if self.action:
            print(self.action, self.state)
        else:
            print("   ", self.state)

    def getState(self):
        return self.state

    def findNeighbors(self):
        neighbors = []

        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

        canL = self.state.canL
        missL = self.state.missL
        canR = self.state.canR
        missR = self.state.missR

        if self.state.boat == "L":
            boat = "R"
            for move in moves:
                neighbors.append(Node(
                    self,
                    State(boat, canL - move[0], missL - move[1], canR + move[0], missR + move[1]),
                    Action("R", move[0], move[1])
                ))

        if self.state.boat == "R":
            boat = "L"
            for move in moves:
                neighbors.append(Node(
                    self,
                    State(boat, canL + move[0], missL + move[1], canR - move[0], missR - move[1]),
                    Action("L", move[0], move[1])
                ))

        return [neighbor for neighbor in neighbors if neighbor.state.isValid()]

    def traceBack(self):
        trace = []

        trace.append(self)

        p = self.parent
        while p:
            trace.append(p)
            p = p.parent

        trace.reverse()
        for node in trace:
            node.print()


if __name__ == "__main__":
    s = State("L", 3, 3, 0, 0)
    a = Action("R", 1, 1)
    node = Node(None, s, a)
    node.print()
