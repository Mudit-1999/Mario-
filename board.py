import numpy as np
import os
import random
import color as cl
clear = lambda: os.system('clear')

class Codi(object):        #Gameboard
	Matrix=np.array([[" " for i in range(0,120)] for j in range(0,30)])
	def __init__(self,x_cod,y_cod):
		self.x_cod=x_cod
		self.y_cod=y_cod

	def initialize(self):
		self.Matrix[0:30,20:120]=" "
		self.Matrix[28:30,20:100]=u'\u2588'
		self.Matrix[0:2,20:100]=u'\u2588'
		
	def display(self):
		self.Matrix[0:30,0:20]=" "
		self.Matrix[0:30,100:120]=" "
		self.Matrix[0:30,20]=u'\u2588'
		self.Matrix[0:30,99]=u'\u2588'
		clear()
		print('                      ',end='')
		print('LEVEL =', level,end="    ")
		print('LIVES =', lives,end="    ")
		print('COINS =',coin,end="    ")
		print('KILL =',kill,end="   ")
		print('TIME =',time,end="   ")
		print('SCORE = ',score)

		
		for y in range(0,30):
			for x in range(0,120):
				if self.Matrix[y][x]=='\u24B8':
					print ( cl.yellow + self.Matrix[y][x],end="")
				else:
					print ( cl.reset  +self.Matrix[y][x],end="")

			print()

	def display_cod(self):
		return (self.x_cod,self.y_cod)
	def display_bit(self):
		return (self.x_cod,self.y_cod,self.bit)
level=1
lives=3
coin=0
kill=0
score=100
counter=0
chk_bit=0
curr_level=0
time=10000

objgameboard=Codi(0,0)


if __name__=="__main__":
	objgameboard.display()
