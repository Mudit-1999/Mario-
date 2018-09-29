import board as GB
import numpy as np
import background as bg


class Hard_code_scene(GB.Codi):
	stage2=np.array([[" " for i in range(0,100)] for j in range(0,30)])
	def __init__(self):
		self.stage2[0:30,0]=u'\u2588'
		self.stage2[0:30,99]=u'\u2588'
		self.stage2[28:30,0:100]=u'\u2588'
		self.stage2[0:4,0:100]=u'\u25A2'
		self.stage2[22,24:44]=u'\u2588'
		self.stage2[22,64:74]=u'\u2588'
		self.stage2[4:28,77]='|'
		self.stage2[4:5,2]='|'
		self.stage2[4:5,6]='|'
		self.stage2[5,2]='/'
		self.stage2[5,6]='\\'

	def open_gate(self):
		self.stage2[4:10,77]=' '
		self.stage2[18,34:64]=u'\u2588'
		self.stage2[12,38:75]=u'\u2588'
		self.stage2[4:19,33:35]=u'\u2588'
		for i in range(0,12):
			bg.coins_list.append(bg.Coins(2*i + 58,16))
		for i in range(0,17):
			bg.coins_list.append(bg.Coins(2*i + 56,9))
		self.stage2[5,76]='\u26F3'	


	def print_scene(self):
		self.Matrix[0:30 , 20:120] = self.stage2


level2=Hard_code_scene()



if __name__=="__main__":
	level2.print_secene()
