from random import randint

from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.satiety = 50
        self.house = None

    def __str__(self):
        return f'''
        I'm {self.name}.
        My satiety is {self.satiety}.
        '''

    def eat(self):
        if self.house.food >= 10:
            print(f'{self.name} has just eaten.')
            self.satiety += 10
            self.house.food -= 10
        else:
            print(f"{self.name} doesn't have enough food.")

    def work(self):
        print(f'{self.name} has worked.')
        self.house.money += 50
        self.satiety -= 10

    def play_games(self):
        print(f'{self.name} spent the whole day playing games.')
        self.satiety -= 10

    def shopping(self):
        if self.house.money >= 50:
            print(f'{self.name} went to the grocery store for food.')
            self.house.money -= 50
            self.house.food += 50
        else:
            print(f'{self.name} ran out of money.')

    def move_in_house(self, house):
        self.house = house
        self.satiety -= 10
        cprint(f'{self.name} moved into the house.', color='blue')

    def act(self):
        if self.satiety <= 0:
            cprint(f'{self.name} died...', color='red')
            return
        dice = randint(1, 6)
        if self.satiety <= 20 and self.name != 'Kenny':
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play_games()


class House:

    def __init__(self):
        self.food = 10
        self.money = 50

    def __str__(self):
        return f'There is {self.food} food and {self.money} money left in the house'


residents = [
    Man('Beavis'),
    Man('Butthead'),
    Man('Kenny')
]

my_sweet_home = House()
for resident in residents:
    resident.move_in_house(house=my_sweet_home)

for day in range(1, 366):
    cprint(f'\n============== DAY NUMBER {day} ==============', color='yellow')
    for resident in residents:
        resident.act()
    for resident in residents:
        print(resident)
    print(my_sweet_home)
