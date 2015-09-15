# 4e rules for ease

import math
import random

class playerChar():
	
	# PlayerChar based on "Fighter" class - D&D 4e Player's Handbook
	def __init__(self, name):
		self.name = name
		self.level = 1
		self.exp = 0
		
		# Ability Scores: Randomly generated, between 10 - 20
		self.str = rollDice(11) + 9
		self.con = rollDice(11) + 9
		self.dex = rollDice(11) + 9
		self.int = rollDice(11) + 9
		self.wis = rollDice(11) + 9
		self.cha = rollDice(11) + 9
		
		
		# Ability Score Modifier variables
		self.strMod = ((self.str - 10) / 2) + self.level / 2
		self.conMod = ((self.con - 10) / 2) + self.level / 2
		self.dexMod = ((self.dex - 10) / 2) + self.level / 2
		self.intMod = ((self.int - 10) / 2) + self.level / 2
		self.wisMod = ((self.wis - 10) / 2) + self.level / 2
		self.chaMod = ((self.cha - 10) / 2) + self.level / 2
		
		
		# Defenses		
		self.ac = 10 + (self.level / 2) + self.strMod
		
		# Fortitude modifier equation, + 2 for "Fighter" class
		if (self.strMod >= self.conMod):
			self.fort = 10 + (self.level / 2) + self.strMod + 2
		else:
			self.fort = 10 + (self.level / 2) + self.conMod + 2
			
			
		# Reflex modifier equation
		if (self.dexMod >= self.intMod):
			self.ref = 10 + (self.level / 2) + self.dexMod
		else:
			self.ref = 10 + (self.level / 2) + self.intMod
			
			
		# Will modifier equation
		if (self.wisMod >= self.chaMod):
			self.will = 10 + (self.level / 2) + self.wisMod
		else:
			self.will = 10 + (self.level / 2) + self.chaMod	
		
		
		# Initiative
		self.init = self.dexMod + (self.level / 2)
		
		
		# Health
		self.hp = 15 + self.con + (6 * self.level)
	
	
	def resetHP(self):
		self.hp = 15 + self.con + (6 * self.level)
	
	
	# Leveling calculations, maximum level of 5
	def seeLevel(self):
		if ((self.exp > 999) and (self.exp < 2250)):
			self.level = 2
		elif ((self.exp > 2249) and (self.exp < 3750)):
			self.level = 3
		elif ((self.exp > 3749) and (self.exp < 5500)):
			self.level = 4
		elif ((self.exp > 5499)):
			self.level = 5
		else:
			self.level = 1
		return self.level
	
	# Roll initiative
	def rollInit(self, dexMod):
		return rollDice(20) + self.init
		
	# Return character name
	def getName(self):
		return self.name

	
class mob():
	
	def __init__(self):
		pass
		
	def talk(self):
		print "I am mob"
	
	
class werewolf(mob):

	def __init__(self):
		pass
		
	def talk(self):
		print "I am werewolf"	
	
	
class wererat(mob):

	def __init__(self):
	
		self.hp = 48
		self.init = rollDice(20) + 7
		self.exp = 150
		
		# Ability Scores
		self.str = 10
		self.con = 16
		self.dex = 18
		self.int = 10	
		self.wis = 12	
		self.cha = 11
		
		# Ability Modifiers
		self.strMod = 1
		self.conMod = 4
		self.dexMod = 5
		self.intMod = 1
		self.wisMod = 2
		self.chaMod = 1
		
		# Defenses
		self.ac = 17
		self.fort = 15
		self.ref = 16
		self.will = 13
		
	
	def attack(self):
		print "Wererat uses its short sword!"
		attackRoll = rollDice(20) + 8
		return attackRoll
	
	
	def damage(self):
		damageRoll = rollDice(6) + 4
		return damageRoll

		
# Add 1 to max randrange for correct effect
def rollDice(number):
	return random.randrange(1, number + 1)

	
def combat(attacker, defender):
	if (attacker.attack() > defender.ac):
		damage = attacker.damage()
		print "The attack hits!"
		print str(defender.name) + " takes " + str(damage) + " damage!"
		defender.hp -= damage
		print "HP: " + str(defender.hp)
	else:
		print "The attack misses!"
	

name = raw_input("Enter your character's name: ")
player = playerChar(name)

"""print "\t------------------- Printing character stats -------------------"
print "\t-------------------- For " + player.name + " -------------------"

print "Player str: " + str(getattr(player, 'str'))
print "Player str MOD: " + str(getattr(player, 'strMod'))

print "Player con: " + str(getattr(player, 'con'))
print "Player con MOD: " + str(getattr(player, 'conMod'))

print "Player dex: " + str(getattr(player, 'dex'))
print "Player dex MOD: " + str(getattr(player, 'dexMod'))

print "Player int: " + str(getattr(player, 'int'))
print "Player int MOD: " + str(getattr(player, 'intMod'))

print "Player wis: " + str(getattr(player, 'wis'))
print "Player wis MOD: " + str(getattr(player, 'wisMod'))

print "Player cha: " + str(getattr(player, 'cha'))
print "Player cha MOD: " + str(getattr(player, 'chaMod'))

print "EXP / LVL increased by 2250."
str(setattr(player, 'exp', 2250))
print "Player exp: " + str(getattr(player, 'exp'))
print "Player level: " + str(player.seeLevel()) """

# console = raw_input("> ")

player.resetHP()
rat1 = wererat()
combat(rat1, player)