class Character:
    def __init__(self, n, h, a, d, s):
        self.name=n
        self.health=h
        self.Attack_power=a
        self.defence=d
        self.speed=s
        
    def attack(self, target):
        target.take_damage(self.Attack_power)

    def take_damage(self, amount):
        self.health -= amount

    def is_alive(self):
        if self.health <=0:
            return False
        return True

class Warrior(Character):
    def __init__(self, r, n, h, a, d, s):
        super(). __init__(n, h, a, d, s)
        self.rage = r
        self.attack_power=a

    def BerserKMode(self):
        if rage == 10:
            self.attack += 10

    def boost_attack(self):

class Mage(Character):
    def __init__(self, m, n, h, a, d, s):
        super().__init__(n, h, a, d, s)
        self.mana = m

    def massive_damage(self):
        if mana 


class Archer(Character):
    def __init__(self, c,n, h, a, d, s):
        super(). __init__(n, h, a, d, s)
        self.critical_chance = c

    def Precision_Shot(self):

    



   




    

