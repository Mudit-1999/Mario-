import board as GB 
import numpy as np
import mscvrtunix as res
import background as bg
import char as all_char
import os
import time
import webbrowser
import urllib
from timeit import default_timer as timer
import list2 as cs
clear = lambda: os.system('clear')

start1=timer()
start10=timer()
def movement(cin):
	if cin=='q':
		return 1
	elif cin=='a':
		all_char.objmario.check_and_inc('a')	
	elif cin=='d':
		all_char.objmario.check_and_inc('d')	
	elif cin=='w':
		all_char.objmario.check_and_inc('w')
	return 0

def func2():
	global start1
	global start10
	end=timer()

	if int(end - start1) ==1:
		start1=timer()
		GB.time-=1
	if int (end-start10) == 10 and GB.level==1 and GB.chk_bit==0:	
		all_char.spawn_alien()
		start10=timer()
	elif GB.counter >= 90 and GB.chk_bit ==0:
		GB.chk_bit=1
		all_char.spawn_alien()
		bg.pipe_generator()
	elif GB.level==2 and GB.chk_bit==1:
		GB.chk_bit=2
		clear()
		os.system("aplay stage_clear.wav&")
		print("Level 2")
		time.sleep(2.20)
		all_char.level2_gen_prog()
	else:
		x_m,y_m=all_char.objmario.display_cod() 
		if x_m <= 96 and 96 <= x_m +2  and y_m <= 6 and  6 <= y_m +3:
	 		all_char.econ=False
	 		over()

def over():
	if GB.lives ==0:
		os.system("aplay gameover.wav&")
	else:
		clear()
		if all_char.econ==False:
			print("You Won")
		print ("Thank for playing:-)")
	kb.set_normal_term()


if __name__ == "__main__":    
	kb = res.KBHit()
	while GB.lives > 0 and all_char.econ==True:
		if kb.kbhit():
			cin=kb.getch()
			if  movement(cin)==1:
				break
		else:
			all_char.objmario.fall_detect(3)
			func2()
		all_char.game_display()
	
	if GB.lives ==0:
		os.system("aplay gameover.wav&")
		clear()
		print('                                               ',end='')
		print ("          Play Again! has a special message for You       ")
		print('                                               ',end='')
		print ("Thank for playing:-)")

	else:
		clear()
		if all_char.econ==False:
			GB.score+=(10000 + 2*GB.time)
			cs.print_castle()

			print('                                                    ',end='')
			print(" !!!      Happy Rakhi   !!!!  ")
			print('                                                    ',end='')
			print ("Thank for playing:-) Wait for a moment ")
			webbrowser.open('https://www.youtube.com/watch?v=KoCag5mCPlg')

	print('                                                    ',end='')
	print('LEVEL =', GB.level,)
	print('                                                    ',end='')
	print('COINS =',GB.coin,)
	print('                                                    ',end='')
	print('SCORE = ',GB.score)
	kb.set_normal_term()

