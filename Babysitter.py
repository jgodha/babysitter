class Babysitter:
    def __init__(self):
        pass

    def calculate(self, start, end):
        charges = 0
        if end <= 24 and end >= 18:
            charges = (end-start) * 15
        if end == 24:
            charges += 5
        if end in (1, 2, 3, 4):
            charges = ((24 - start) * 15) + 5
            for hour in range(0, end):
                charges += 20
        return charges
