# 4e rules for ease

import math
import random

class playerChar(): # Create characters classes as "class" - let player pick class
	
	# PlayerChar based on "Fighter" class - D&D 4e Player's Handbook
	def __init__(self, name):
		self.name = name
		self.level = 1
		self.xp = 0
		
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
		self.init = self.dexMod + (self.seeLevel() / 2)
		
		
		# Health
		self.HP = 15 + self.con + (6 * self.level)
	
	
	def resetHP(self):
		self.HP = 15 + self.con + (6 * self.level)
	
	
	# Leveling calculations, maximum level of 5
	def seeLevel(self):
		if ((self.xp > 999) and (self.xp < 2250)):
			self.level = 2
		elif ((self.xp > 2249) and (self.xp < 3750)):
			self.level = 3
		elif ((self.xp > 3749) and (self.xp < 5500)):
			self.level = 4
		elif ((self.xp > 5499)):
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
	
	
	def getStats(self):
		print "\t------------------- " + player.name + " Character Sheet -------------------"
		print "STR: " + str(getattr(player, 'str'))
		print "STR MOD: " + str(getattr(player, 'strMod'))

		print "CON: " + str(getattr(player, 'con'))
		print "CON MOD: " + str(getattr(player, 'conMod'))

		print "DEX: " + str(getattr(player, 'dex'))
		print "DEX MOD: " + str(getattr(player, 'dexMod'))

		print "INT: " + str(getattr(player, 'int'))
		print "INT MOD: " + str(getattr(player, 'intMod'))

		print "WIS: " + str(getattr(player, 'wis'))
		print "WIS MOD: " + str(getattr(player, 'wisMod'))

		print "CHA: " + str(getattr(player, 'cha'))
		print "CHA MOD: " + str(getattr(player, 'chaMod'))

		print "XP: " + str(getattr(player, 'xp'))
		print "level: " + str(player.seeLevel())
		print "HP: " + str(getattr(player, 'HP'))
		print "Init MOD: " + str(getattr(player, 'init'))
		print "\t------------------- " + player.name + " Character Sheet -------------------"
	
	
# Create character "class" classes!
# use mob class
	
	
class mob():
	
	def __init__(self):
		pass
		
	def talk(self):
		print "I am mob"
	
	
class werewolf(mob):

	def __init__(self):
	
		self.HP = 108
		self.init = rollDice(20) + 7
		self.xp = 350
		
		# Ability Scores
		self.str = 19
		self.con = 18
		self.dex = 16
		self.int = 10	
		self.wis = 14	
		self.cha = 11
		
		# Ability Modifiers
		self.strMod = 8
		self.conMod = 8
		self.dexMod = 7
		self.intMod = 4
		self.wisMod = 6
		self.chaMod = 4
		
		# Defenses
		self.ac = 20
		self.fort = 20
		self.ref = 19
		self.will = 18
		
	
	def attack(self):
		print "Werewolf uses its greatclub!"
		attackRoll = rollDice(20) + 12
		return attackRoll
	
	
	def damage(self):
		damageRoll = rollDice(4) + rollDice(4) + 4
		return damageRoll
	
	
class wererat(mob):

	def __init__(self):
	
		self.HP = 48
		self.init = rollDice(20) + 7
		self.xp = 150
		
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
		defender.HP -= damage
		print "HP: " + str(defender.HP)
	else:
		print "The attack misses!"
	

name = raw_input("Enter your character's name: ")
player = playerChar(name)

# console = raw_input("> ")

print player.HP
player.resetHP()
werewolf1 = werewolf()
combat(werewolf1, player)
player.getStats()