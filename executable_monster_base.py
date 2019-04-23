from monster_base import Monster_base
monster_1 = (Monster_base('Bob',3, 50, 'lots'))
# print('The monsters name is', monster_1.name)
# print('The monster has', monster_1.eyes, 'eyes')
# print('The monster has', monster_1.limbs, 'limbs')
# print('The monster has', monster_1.fur, 'of fur')
print('I am a', monster_1.show_type())
print(monster_1.attack())
print(monster_1.defend())
print(monster_1.death_roar())

