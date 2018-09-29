import board as GB
import numpy as np
import background as bg
import secnery as sc
import os
import time

clear = lambda: os.system('clear')


alien_type1_list=[]
alien_type2_list=[]
second_list=[]

econ=True

class Mario(GB.Codi):
	mario_img=np.array([[" " for i in range(0,2)] for j in range(0,3)])
	def __init__(self,x_cod,y_cod):
		super(Mario, self).__init__(x_cod,y_cod)
		self.mario_img[2,0:2]=u'\u013B'
		self.mario_img[1,0:2]=u'\u2587'
		self.mario_img[0,0:2]=u'\u253B'
		self.print_mario()


	def print_mario(self):
		self.Matrix[self.y_cod:self.y_cod+3 , self.x_cod:self.x_cod+2] = self.mario_img

	def check_and_inc(self,key):
		if key=="d":
			if self.check_to_inc(self.x_cod+1,self.y_cod,2,3) ==1:
				if self.x_cod <= 40 or  GB.counter>=100 or GB.level==2: 
					self.x_cod+=1
					GB.score+=2
					GB.counter+=1
				else:
					bg.board_move()
					GB.score+=2
					GB.counter+=1     #dynamic moving 
			self.fall_detect(3)

		elif key=='a':
			if self.check_to_inc(self.x_cod-1,self.y_cod,2,3) ==1:
				self.x_cod-=1
				GB.score+=2
				GB.counter-=1
			self.fall_detect(3)
		elif key=='w':
			os.system("aplay jump.wav&  > /dev/null 2>&1")
			self.jumpy(2,3)
		return 0	
		# game_display()

	def jumpy(self,size_x,size_y):
		for i in range(0,8):
			if self.check_to_inc(self.x_cod,self.y_cod-1,size_x,size_y) ==1:
				self.y_cod-=1
			else:
				break
		return 0

	def check_to_inc(self,x,y,size_x,size_y):
		for i in range(0,size_y):
			for j in range(0,size_x):
				if self.Matrix[y+i,x+j]==u'\u2588' or self.Matrix[y+i,x+j]== '|' or self.Matrix[y+i,x+j] == u'\u25A2':
					os.system("aplay bump.wav& > /dev/null 2>&1")
					return 0
		return 1

	def fall_detect(self,down_x):
		global objmario
		if self.y_cod+3 > 28:
			GB.lives-=1
			os.system("aplay mariodie.wav&")
			del objmario
			del self
			respawn_mario()	
			return 0
		for i in range(0,len(alien_type1_list)):
			alien_type1_list[-i].move_right()
		for i in range(0,len(alien_type2_list)):
			alien_type2_list[-i].move_alien2()
		for i in range(0,len(alien_type2_list)):
			if alien_type2_list[-i].collision()==0:
				alien_type2_list[-i]=Alien_type2(13,13,0,0)

		for i in range(0,3):
			if self.Matrix[self.y_cod + down_x, self.x_cod +i ] == u'\u2588':
				return 0
			elif self.Matrix[self.y_cod + down_x, self.x_cod -1 +i ] == '|':
				GB.level=2
				os.system("aplay pipe.wav&")
				time.sleep(0.1)
				return 0
		self.y_cod+=1

class Alien_type1(Mario):
	alien_t1=np.array([[" " for i in range(0,1)] for j in range(0,2)])
	def __init__(self, x_cod,y_cod,jumpbit):
		super(Alien_type1, self).__init__(x_cod,y_cod)
		self.jumpbit=jumpbit
		self.alien_t1[1,0]=u'\u220F'
		self.alien_t1[0,0]=u'\u220E'

	def move_right(self):
		if self.x_cod <= 21 or self.y_cod > 27:
			del alien_type1_list[0]
			del self
		elif  self.check_fall() ==1:	
			self.x_cod-=1
			self.collision()
		return 0

	def check_fall(self):
		if self.Matrix[self.y_cod+2,self.x_cod-1]==u'\u2588' :
			self.jumpbit=0
			return 1
		elif self.jumpbit==0 and self.Matrix[28,self.x_cod-1]!=u"\u2588"  :

			self.jumpbit=1
			self.jumpy(1,2)
		else:
			if self.Matrix[self.y_cod + 2, self.x_cod +1 ] != u'\u2588' or self.Matrix[28, self.x_cod +1 ] == u'\u2588' :
				self.y_cod+=1
				self.x_cod-=1
		return 0

	def collision(self):
		global objmario
		x_m,y_m=objmario.display_cod()
		if self.x_cod  <= x_m +2 and self.x_cod  >= x_m and  self.y_cod >= y_m +3 and abs(y_m - self.y_cod) < 5:
			GB.kill+=1
			os.system("aplay stomp.wav&  > /dev/null 2>&1")
			GB.score+=1000
			del self
			del alien_type1_list[0]
			return 0
		
		if len(alien_type1_list)!=0:
			if self.x_cod  <= x_m +2 and self.x_cod  >= x_m and  self.y_cod >= y_m and self.y_cod <= y_m+	3:
				GB.lives-=1

				os.system("aplay mariodie.wav&")
				del objmario
				del self
				del alien_type1_list[0]
				respawn_mario()		
				return 0
		return 1


	def print_alien_type1(self):
		self.Matrix[self.y_cod:self.y_cod +2,self.x_cod : self.x_cod+1]=self.alien_t1



class Alien_type2(Alien_type1):
	def __init__(self,x_cod,y_cod,jumpbit,speed):
		super(Alien_type2, self).__init__(x_cod,y_cod,jumpbit)
		self.speed=speed

	def collision(self):
		global objmario
		x_m,y_m=objmario.display_cod()
		if self.x_cod  <= x_m +2 and self.x_cod  >= x_m and  self.y_cod >= y_m +3 and abs(y_m - self.y_cod) < 5:
				GB.kill+=1
				os.system("aplay stomp.wav&  > /dev/null 2>&1")
				bg.kill_all+=1
				GB.score+=abs(self.speed *2000)
				if bg.kill_all>=3:
					sc.level2.open_gate()
				del self
				return 0
		
		if len(alien_type2_list)!=0:
			if self.x_cod  <= x_m +2 and self.x_cod  >= x_m and  self.y_cod >= y_m and self.y_cod <= y_m+	3:
				GB.lives-=1
				os.system("aplay mariodie.wav&")
				del objmario
				respawn_mario()
				return 1
		return 1

	def move_alien2(self):
		if self.x_cod+self.speed <= 20 or self.x_cod + self.speed >= 97:
			self.speed*=-1
		self.x_cod+=self.speed



def level2_gen_prog():
	global objmario
	del objmario

	objmario=Mario(23,5)
	alien_type2_list.append(Alien_type2(45,26,0,-1))
	alien_type2_list.append(Alien_type2(23,26,0,2))
	alien_type2_list.append(Alien_type2(78,26,0,1))
	bg.level2_generation()




def game_display():
	GB.objgameboard.initialize()
	if GB.level==2:
		sc.level2.print_scene()
	else:
		for i in range(0,len(bg.cloud_list)):
			bg.cloud_list[i].print_cloud()
		for i in range(0,len(bg.mountain_list)):
			bg.mountain_list[i].print_mountain()
		for i in range(0,len(bg.obstacle_list)):
			bg.obstacle_list[i].print_obstacle()
		for i in range(0,len(alien_type1_list)):
			alien_type1_list[-i].print_alien_type1()
		for i in range(0,len(bg.pipe_list)):
			bg.pipe_list[i].print_pipe()

	temp_list=[]

	for  i in range(0,len(bg.coins_list)):
		x_m,y_m=objmario.display_cod()
		if bg.coins_list[i].mario_pass(x_m,y_m) == 1:
			temp_list.append(bg.coins_list[i])
	bg.coins_list=temp_list

	for  i in range(0,len(bg.coins_list)):
		bg.coins_list[i].print_coin()
	
	# alien_type2_list=second_list
	for i in range(0,len(alien_type2_list)):
		alien_type2_list[-i].print_alien_type1()

	objmario.print_mario()
	GB.objgameboard.display()
	
	time.sleep(0.07)
	return 0

def respawn_mario():
	global objmario
	objmario=Mario(21,15)

respawn_mario()

def spawn_alien():
	alien_type1_list.append(Alien_type1(98,24,0))
spawn_alien()

if __name__=="__main__":
	objmario.display()