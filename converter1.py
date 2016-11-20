# hackathon

import serial
import time
"""

sequence :

+|	00
 v	01  ^
	10  | -
	11

 if negative, turn 4 laps

ex :
a1 : 00 : 0
b1 : 00 : 0
c1 : 00 : 0
___________

a2 : 11 : 3
b2 : 00 : 0
c2 : 11 : 3

"""

# original set
a1 = '00'
b1 = '00'
c1 = '00'

# final set
a2 = '10'
b2 = '01'
c2 = '10'





class braille_support() :
	
	
	
	def __init__(self, com_port, baudrate):
		print("starting braille support class")
		self.POS = "positive"
		self.NEG = "negative"
		self.alphabet_file = "alphabet.txt"
		self.ser = None
		#self.ser = serial.Serial(COM_PORT, BAUDRATE)
		self.COM_PORT = com_port
		self.BAUDRATE = baudrate
		
	def motor_control(self,a1,b1,c1,a2,b2,c2):
	
		# determine nb of laps for bottom (c) char
		
		print("a1 = {0}, a2 = {1}\nb1 = {2}, b2 = {3}\nc1 = {4}, c2 = {5}".format(a1,a2,b1,b2,c1,c2))
		
		total_mouvement = []
		relative = self.POS
		laps = 0
		
		# reset the squares so that all sqaures are driven by the motor
		
		# top square equals to middle square
		mv_a_reset = int(b1,2) - int(a1,2)
		 
		if mv_a_reset < 0 :
			 mv_a_reset = 4 + (mv_a_reset)
			 total_mouvement.append(self.POS) 
			 total_mouvement.append(mv_a_reset)
		elif mv_a_reset > 0 :
			total_mouvement.append(self.POS) 
			total_mouvement.append(mv_a_reset)
		else : # a1 = b1, nothing to do
			pass
			
		
		#a_new = (int(a1,2) + mv_a_reset) % 4
		a_new = int(b1,2)
		print("mv_a_reset = {0}, a_new = {1}".format(mv_a_reset, a_new))
		 
		# middle square ans top square equals to bottom square
		mv_b_reset = int(c1,2) - int(b1,2)
		 
		if mv_b_reset < 0 :
			mv_b_reset = 4 + mv_b_reset
			total_mouvement.append(self.POS) 
			total_mouvement.append(mv_b_reset)
		elif mv_b_reset > 0 :
			total_mouvement.append(self.POS) 
			total_mouvement.append(mv_b_reset)
		else : #b1 = c1, nothing to do
			pass
			
		#b_new = (int(b1,2) + mv_b_reset) % 4 # bn = an
		b_new = int(c1,2)
		print("mv_b_reset = {0}, b_new = {1}".format(mv_b_reset, b_new))
		
		# calibration is finished, all squares are driven by the motor, all
		# squares have the same value C1 since bottom square has not moved
		
		
		# mouv bottom square to its final position, always in the positive 
		# sense of rotation
		mv_c = int(c2,2) - int(c1,2)
		if mv_c > 0:
			#mv_c =  mv_c
			total_mouvement.append(self.POS) 
			total_mouvement.append(mv_c)
		elif mv_c <0:
			mv_c = 4 + mv_c
			total_mouvement.append(self.POS) 
			total_mouvement.append(mv_c)
		else :# c2=c1 : no mouvement required, total_mouvement is not updated
			pass
		a_new = int(c2,2)
		b_new = int(c2,2)
		
		#total_mouvement.append(self.POS) 
		#total_mouvement.append(mv_c)
		
		print("mv_c : {0}, total_mouvement is {1}".format(mv_c, total_mouvement))
		
		# mouv middle square to its final position, always in the negative 
		# sense of rotation
		a_neg_flag = self.POS
		neg_laps = 4 # negative sense of rotation
		mv_b = int(b2,2) - b_new 
		if mv_b >0 :
			mv_b = neg_laps + (4 - mv_b)
			total_mouvement.append(self.NEG) 
			total_mouvement.append(mv_b)
		elif mv_b <0:
			mv_b = neg_laps + abs(mv_b)
			total_mouvement.append(self.NEG) 
			total_mouvement.append(mv_b)
		else : # mv_b =0, so top square needs to move in the negative sense 
			# total mouvement is not updated
			a_neg_flag = self.NEG
		
		a_new = int(b2,2)
		
		print("mv_b : {0}, total_mouvement is {1}".format(mv_b, total_mouvement))
		
		# mouv top square to its final position, positively or negatively
		
		
			
		mv_a = int(a2,2) - a_new
		if mv_a >  0: 
			mv_a = 4 - mv_a
			
			if a_neg_flag == self.NEG :
				total_mouvement.append(self.NEG)
			else : 
				total_mouvement.append(self.POS)
			
			total_mouvement.append(mv_a)
			
		elif mv_a < 0 :
			mv_a = abs(mv_a)
			
			if a_neg_flag == self.NEG :
				total_mouvement.append(self.NEG)
			else : 
				total_mouvement.append(self.POS)
				
			total_mouvement.append(mv_a)
			
		else : # a2=an : do nothing
			pass
			
		print("mv_a : {0}, total_mouvement is {1}".format(mv_a, total_mouvement))
			
		return total_mouvement
		
		
			
	def get_matrix(self, lettre):
		
		alphabet = open(self.alphabet_file, 'r')
		alpha = alphabet.readlines()
		for line in alpha:
			
			#print(line)
			if line[0] == lettre :
				print("found right line !")
				matrix = line.strip().split("=")[-1]
				print(matrix)
				a = matrix.split(";")[0]
				b = matrix.split(";")[1]
				c = matrix.split(";")[2]
				print("a = {0} ; b = {1} ; c = {2}".format(a,b,c))
				return (a,b,c)
		
		print("couldn't find the lettre {0} ...".format(lettre))
		alphabet.close()
		return 0
		
	def prompt_text(self):
		
		text = raw_input("Enter your text to be converted to braille :\n")
		text = "0" + text
		return text.replace(" ", "0")
		
		
	def send_command_to_motor(self, sequence):
		self.ser = serial.Serial(self.COM_PORT, self.BAUDRATE)
		
		
		print("seq to send : {0}".format(sequence[0]))
		
		for i in sequence:
			print(i)
			self.ser.write(str(i))
			self.ser.write("\n")
		# waiting for aknowledgement
		print("sent")
		self.ser.write("z")
		self.ser.readline()
		print("acknowledge")
		
		
		
	def lettre_feeder(self, text):
		
		for i in range(len(text)-1):
			
			print("lettres are {0} to {1}".format(text[i], text[i+1]))
			(a1, b1, c1) = self.get_matrix(text[i])
			(a2, b2, c2) = self.get_matrix(text[i+1])
			mv_sequence = self.motor_control(a1, b1, c1, a2, b2, c2)
			#self.send_command_to_motor(mv_sequence)
			time.sleep(1.5)
			
			
			
		
		
		
				
			
				

if __name__=='__main__':
	
	COM_PORT = 'COM4'
	BAUDRATE = 9600
	braille = braille_support(COM_PORT, BAUDRATE)
	
	text_to_convert = braille.prompt_text()
	braille.lettre_feeder(text_to_convert)
	
	#(a1, b1, c1) = braille.get_matrix("a")
	#(a2, b2, c2) = braille.get_matrix("t")
	#mouv_sequence = braille.motor_control(a1, b1, c1, a2, b2, c2)
