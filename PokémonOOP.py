from ASCII import * 
Pokemon_list = {
    "Pikachu":{"name": "Pikachu", "life": 100, "stamina":50, "AP":15, "SA": 30, "stamina_recharge":5, "sattack_cost":10, "ASCII": ASCII_pikachu},
    "Bulbasaur":{"name": "Bulbasaur", "life": 100, "stamina":50, "AP":15, "SA": 30, "stamina_recharge":3, "sattack_cost":10, "ASCII": ASCII_bulbasaur},
    "Squirtle":{"name": "Squirtle", "life": 100, "stamina":50, "AP":15, "SA": 30, "stamina_recharge":3, "sattack_cost":10, "ASCII": ASCII_squirtle},
    "Charmander":{"name": "Charmander", "life": 100, "stamina":50, "AP":15, "SA": 30, "stamina_recharge":3, "sattack_cost":10, "ASCII": ASCII_charmander}
}
class Abort(Exception):
    pass
class pokemon():
    def __init__(self, selection):
        self.name = Pokemon_list[selection]["name"]
        self.life = Pokemon_list[selection]["life"]
        self.stamina = Pokemon_list[selection]["stamina"]
        self.AP = Pokemon_list[selection]["AP"]
        self.SA = Pokemon_list[selection]["SA"]
        self.stamina_recharge = Pokemon_list[selection]["stamina_recharge"]
        self.sattack_cost = Pokemon_list[selection]["sattack_cost"]
        self.ASCII = Pokemon_list[selection]["ASCII"]
    
    def show(self,enemy):
        print("..... " + self.name + " stats " + ".....")
        print("Life:" + str(self.life))
        print("Stamina: " + str(self.stamina))

        print("..... " + enemy.name + " stats " + ".....")
        print("Life:" +  str(enemy.life))
        print("Stamina: " + str(enemy.stamina))


    def attack(self, enemy):
        print()
        print("*****You did a normal attack on " + enemy.name + "********")
        enemy.life -= self.AP
        self.stamina += self.stamina_recharge 
        enemy.stamina += enemy.stamina_recharge
        self.show(enemy)

    def special_attack(self, enemy):
        print()
        print("****You did a special attack on " + enemy.name + "*******")
        enemy.life -= self.SA
        enemy.stamina += enemy.stamina_recharge
        self.stamina -= self.sattack_cost
        self.show(enemy)
    
    def heal(self, enemy):
        self.life += 25
        self.stamina -= 25
        self.show(enemy)


        



