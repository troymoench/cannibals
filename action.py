class Action:
    def __init__(self, move, nCan, nMiss):
        self.move = move
        self.nCan = nCan
        self.nMiss = nMiss

        if (self.nCan + self.nMiss) > 2 or (self.nCan + self.nMiss) < 1:
            print("Invalid Action")

    def __str__(self):
        if self.move == "L":
            move = "<-"
            return "{}{}{}".format(move, self.nCan*"C", self.nMiss*"M")
        else:
            move = "->"
            return "{}{}{}".format(self.nCan*"C", self.nMiss*"M", move)


if __name__ == "__main__":
    act = Action("L", 1, 1)
    print(act)
