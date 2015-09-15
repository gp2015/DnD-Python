import math
import random

class playerChar():
	
	def __init__(self, name):
		self.name = name
	
		# Ability Scores: Randomly generated, 
		# if (AbilityScore < 8) then + 5
		
		self.str = rollDice(10) + 10
		self.con = rollDice(10) + 10
		self.dex = rollDice(10) + 10
		self.int = rollDice(10) + 10
		self.wis = rollDice(10) + 10
		self.cha = rollDice(10) + 10
	
		# Ability Score Modifier variables
	
		self.strMod = (self.str - 10) / 2
		self.conMod = (self.con - 10) / 2
		self.dexMod = (self.dex - 10) / 2
		self.intMod = (self.int - 10) / 2
		self.wisMod = (self.wis - 10) / 2
		self.chaMod = (self.cha - 10) / 2
		
		
	def getName(self):
		return self.name
	
	def talk(self):
		print "I am player"


	
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
	
		self.init = rollDice(20) + 7
		
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
		
		
	def talk(self):
		print "I am wererat"	


def rollDice(number):
	return random.randrange(1, number + 1)

	
rollDice(20)

name = raw_input("Enter your character's name: ")
player = playerChar(name)
print "Player str: " + str(getattr(player, 'str'))
print "Player str MOD: " + str(getattr(player, 'strMod'))