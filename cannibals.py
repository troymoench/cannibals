# Cannibals and Missionaries
# Breadth First Search
# Python 3

from agent import Agent
from state import State


def main():
    start = State("L", 3, 3, 0, 0)
    goal = State("R", 0, 0, 3, 3)
    a = Agent()
    a.gDebug = False
    print("Cannibals and Missionaries")
    print("Breadth First Search\n")
    print("Searching for solution...")
    solution = a.search(start, goal)
    if solution:
        print("Solution found!")
        solution.traceBack()
    else:
        print("No solution found!")


if __name__ == "__main__":
    main()
