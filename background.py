import board as GB
import numpy as np
import random
import os
import color as cl


cloud_list=[]
obstacle_list=[]
coins_list=[]
pipe_list=[]
mountain_list=[]
kill_all=0


class Pipe(GB.Codi):
	def __init__(self,x_cod,y_cod):
		super(Pipe, self).__init__(x_cod,y_cod)
		self.pipe_img=np.array([[" " for i in range(0,4)] for j in range(0,4)])
		self.pipe_img[1:4,0]="|"
		self.pipe_img[1:4,3]="|"
		self.pipe_img[0,0]="\\"
		self.pipe_img[0,3]="/"
	def print_pipe(self):
		self.Matrix[self.y_cod:self.y_cod+4,self.x_cod:self.x_cod+4]=self.pipe_img

class Mountain(GB.Codi):
	def __init__(self,x_cod,y_cod,size_mountain):
		super(Mountain, self).__init__(x_cod,y_cod)
		self.mountain_img=np.array([[" " for i in range(0,10)] for j in range(0,4)])
		self.size_mountain = size_mountain
		for i in range(1,4):
			self.mountain_img[4-i][i]="/"
		for i in range(1,4):
			self.mountain_img[i][i+6]='\\'
		self.mountain_img[0,4:7]="_"

	def print_mountain(self):
		self.Matrix[self.y_cod:self.y_cod+4 , self.x_cod:self.x_cod +10] = self.mountain_img

class Coins(GB.Codi):
	def __init__(self, x_cod,y_cod):
		self.x_cod = x_cod
		self.y_cod = y_cod

	def mario_pass(self,x_m,y_m):
		if x_m  <= self.x_cod and self.x_cod <= x_m +2  and y_m <= self.y_cod and  self.y_cod <= y_m +3: 
			GB.coin+=1
			GB.score+=100
			os.system("aplay coin.wav&")
			return -1
		else:
			return 1

	def print_coin(self):
		self.Matrix[self.y_cod,self.x_cod]= u'\u24B8'



class Cloud(GB.Codi):
	def __init__(self,x_cod,y_cod):
		self.cloud_img=np.array([[" " for i in range(0,10)] for j in range(0,4)])
		self.x_cod=x_cod
		self.y_cod=y_cod
		self.cloud_img[3,1:9]=u'\u2500'
		self.cloud_img[3,1:4]=u'\u2500'
		self.cloud_img[2,0]=u'\u2572'
		self.cloud_img[1,0]=u'\u2571'
		self.cloud_img[1,1:4]=u'\u2504'
		self.cloud_img[1,6:9]=u'\u2504'
		self.cloud_img[1,9]=u'\u2572'
		self.cloud_img[2,9]=u'\u2571'


	def print_cloud(self):
		self.Matrix[self.y_cod:self.y_cod +4, self.x_cod:self.x_cod+min(99-self.x_cod,10)] = self.cloud_img[0:4,0:min(99-self.x_cod,10)]

class Obstacle(GB.Codi):
	obstacle_solid=np.array([[" " for i in range(0,20)] for j in range(0,6)])
	def __init__(self,x_cod,y_cod,bit):
		super(Obstacle, self).__init__(x_cod,y_cod)
		self.bit=bit
		self.obstacle_solid[5:6,0:10]=u'\u2588'
		

	def print_obstacle(self):
		self.Matrix[self.y_cod+11:self.y_cod+14 , self.x_cod+2:self.x_cod+11] = " "
		if self.bit == 1:
			self.obstacle_solid[0:1,11:20]= u'\u2588'
		else:
			self.obstacle_solid[0:1,11:20]= " "#u'\u2588'
		self.Matrix[self.y_cod:self.y_cod+6 , self.x_cod:self.x_cod+min(99-self.x_cod,20)] = self.obstacle_solid[0:6,0:min(99-self.x_cod,20)]


cloud_list.append(Cloud(27,4))
cloud_list.append(Cloud(42,3))
cloud_list.append(Cloud(81,5))
obstacle_list.append(Obstacle(50,17,1))
mountain_list.append(Mountain(24,24,0))

def pipe_generator():
	pipe_list.append(Pipe(98,24))

for i in range(0,5):
	coins_list.append(Coins(24+2*i,25))


def level2_generation():
	del coins_list[:]
	del obstacle_list[:]
	del cloud_list[:]
	del pipe_list[:]
	for i in range(15):
		coins_list.append(Coins(23,i+6))
	for i in range (5):
		coins_list.append(Coins(44+2*i,20))
	for i in range (5):
		coins_list.append(Coins(64+2*i,20))


def board_move():
	for i in range(0,len(cloud_list)):
		x,y=cloud_list[i].display_cod()
		x-=1
		if x<=random.randint(1,15):
			del cloud_list[i]
			break;
		else:
			cloud_list[i]=Cloud(max(1,x),y)
	qww=random.randint(0,50)
	if qww<= 1 and len(cloud_list) < 4:
		x=98
		y=random.randint(2,6)
		cloud_list.append(Cloud(x,y))

	for i in range(0,len(mountain_list)):
		x,y=mountain_list[i].display_cod()
		x-=1
		if x<=random.randint(1,15):
			del mountain_list[i]
			break;
		else:
			mountain_list[i]=Mountain(x,y,0)
	qww=random.randint(0,50)
	if qww<= 1 and len(cloud_list) < 4:
		x=98
		y=random.randint(20,24)
		mountain_list.append(Mountain(x,y,0))
	

	for i in range(0,len(obstacle_list)):
		x,y,bit=obstacle_list[i].display_bit()
		x-=1
		if x<=random.randint(1,15):
			del obstacle_list[i]
			break;
		else:
			obstacle_list[i]=Obstacle(x,y,bit)
	qwo=random.randint(0,50)
	if qwo <= 1 and len(obstacle_list) < 3 and GB.counter<=80:
		x=98
		y=17
		if qwo%2==0:
			obstacle_list.append(Obstacle(x,y,0))
		else:
			if qww%2==0:
				for i in range(0,4):
					coins_list.append(Coins(x+2*i,15))
			else:
				for i in range(0,4):
					coins_list.append(Coins(x + 10 +2*i,15))
			obstacle_list.append(Obstacle(x,y,1))

	for i in range(0,len(coins_list)):
		x,y=coins_list[i].display_cod()
		x-=1
		if x<=random.randint(1,15):
			del coins_list[i]
			break;
		else:
			coins_list[i]=Coins(x,y)

	for i in range (0,len(pipe_list)):
		x,y=pipe_list[i].display_cod()
		x-=1
		pipe_list[i]=Pipe(x,y)