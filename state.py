class State:
    def __init__(self, boat, canL, missL, canR, missR):
        self.boat = boat
        self.canL = canL
        self.missL = missL
        self.canR = canR
        self.missR = missR

    def __str__(self):
        return "[{}, {}, {}, {}, {}]".format(self.boat, self.canL, self.missL, self.canR, self.missR)

    def __repr__(self):
        return "State({}, {}, {}, {}, {})".format(self.boat, self.canL, self.missL, self.canR, self.missR)

    def __eq__(self, other):
        boat = self.boat == other.boat
        canL = self.canL == other.canL
        missL = self.missL == other.missL
        canR = self.canR == other.canR
        missR = self.missR == other.missR
        return boat and canL and missL and canR and missR

    def isValid(self):

        # missionaries >= cannibals
        if (self.canL > self.missL) and (self.missL > 0):
            return False
        if (self.canR > self.missR) and (self.missR > 0):
            return False

        if (self.canL > 3) or (self.canL < 0):
            return False
        if self.canR > 3 or self.canR < 0:
            return False
        if self.missL > 3 or self.missL < 0:
            return False
        if self.missR > 3 or self.missR < 0:
            return False

        return True


if __name__ == "__main__":
    s = State("L", 3, 3, 0, 0)
    print(s)
    print(s.isValid())
    print(s == State("L", 3, 3, 0, 0))
