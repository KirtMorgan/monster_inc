from monster_base import Monster_base
class Monster_giant(Monster_base):
    def __init__(self, name_input):
        super().__init__(name_input)
        self.height = 'Giant Monster'

