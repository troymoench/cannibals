from node import Node
from state import State
from action import Action


class Frontier:
    def __init__(self):
        self.fnodes = []

    def add(self, n):
        self.fnodes.append(n)

    def pop(self):
        return self.fnodes.pop()

    def isEmpty(self):
        return len(self.fnodes) == 0

    def check(self, n):
        return n in self.fnodes

    def print(self):
        print("<Frontier>")
        for n in self.fnodes:
            n.print()
        print("</Frontier>")


if __name__ == "__main__":
    f = Frontier()
    s = State("L", 3, 3, 0, 0)
    n = Node(None, s, None)
    f.add(n)
    f.print()
    f.add(Node(s, State("R", 2, 3, 1, 0), Action("R", 1, 0)))
    f.print()

    print(f.check(n))
    f.pop()
    f.print()
