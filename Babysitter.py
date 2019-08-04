class Babysitter:
    def __init__(self):
        pass

    def calculate(self, start, end):
        charges = (end-start) * 15
        if end > 23:
            charges += (end - 23) * 5
        return charges
