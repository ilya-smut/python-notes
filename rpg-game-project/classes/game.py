import random

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDRLINE = '\033[4m'

class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ['Attack', 'Magic']

    
    def generate_dmg(self):
        return random.randrange(self.atkl, self.atkh)
    

    def take_dmg(self, dmg):

        self.hp -= dmg
        
        if self.hp < 0:
            self.hp = 0

        return self.hp


    def heal(self, hp):
        if self.hp + hp < self.maxhp:
            self.hp += hp
        else:
            self.hp = self.maxhp

    
    def get_hp(self):
        return self.hp

    
    def get_maxhp(self):
        return self.maxhp


    def get_mp(self):
        return self.mp


    def get_maxmp(self):
        return self.maxmp


    def reduce_mp(self, cost):
        self.mp -= cost

    
    def choose_action(self):
        i = 1
        print(Colors.OKBLUE + 'Actions' + Colors.ENDC)
        for action in self.actions:
            print(str(i) + ':' + action)
            i += 1
        
    def choose_magic(self):
        i = 1
        for spell in self.magic:
            print(str(i) + ': ' + spell.name + ', cost: ' + str(spell.cost) + ' magic points')
            i += 1
    

    