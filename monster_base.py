class Monster_base():
    __monster_type = 'Base Monster'
    def __init__(self, name_input = 'Snarl', limbs_input = '4', eyes_input = '4', fur_input = 'lots'):
         self.fur = fur_input
         self.eyes = eyes_input
         self.limbs = limbs_input
         self.height = 'Small Monster'
         self.name = name_input

    def attack(self, damage_dealt = 5):
        return'The monster attacks and deals a total damage of', damage_dealt
    def defend(self):
        return'The monster raises its limbs to defend its body and face'
    def death_roar(self, defence_loss = 20):
        return'The monster lets out a horrible roar leaving your ears ringing, your defence drops by', defence_loss
    def show_type(self):
        return self.__monster_type