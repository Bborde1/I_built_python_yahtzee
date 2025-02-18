# Defines the core objects of the game Yahtzee, players, scorecards

UPPER_SCORECARD = {
    "Ones": 0,
    "Twos": 0,
    "Threes": 0,
    "Fours": 0,
    "Fives": 0,
    "Sixes": 0,
}
LOWER_SCORECARD = {
    "Three kind": 0,
    "Four kind": 0,
    "Full House": 0,
    "Small straight": 0,
    "Large straight": 0,
    "Yahtzee": 0,
}


class Player:
    def __init__(self, name):
        self.name = name

    def create_scorecard():
        pass
