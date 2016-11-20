def motor_control(self,a1,b1,c1,a2,b2,c2):
	
	# determine nb of laps for bottom (c) char
	
	print("a1 = {0}, a2 = {1}\nb1 = {2}, b2 = {3}\nc1 = {4}, c2 = {5}".format(a1,a2,b1,b2,c1,c2))
	
	total_mouvement = []
	relative = self.POS
	laps = 0
	
	# reset the squares so that all sqaures are driven by the motor
	
	# top square equals to middle square
	mv_a_reset = b1 - a1
	 
	if mv_a_reset < 0 :
		 mv_a_reset = 4 + (mv_a_reset)
	
	total_mouvement.append(self.POS) 
	total_mouvement.append(mv_a_reset)
	a_new = (a1 + mv_a_reset) % 4
	print("mv_a_reset = {0}, a_new = {1}".format(mv_a_reset, a_new))
	 
	# middle square ans top square equals to bottom square
	mv_b_reset = c1 - b1
	 
	if mv_b_reset < 0 :
		mv_b_reset = 4 + mv_b_reset
	total_mouvement.append(self.POS) 
	total_mouvement.append(mv_b_reset)
	#b_new = (b1 + mv_b_reset) % 4 # bn = an
	print("mv_a_reset = {0}, a_new = {1}".format(mv_a_reset, a_new))
	
	# calibration is finished, all squares are driven by the motor, all
	# squares have the same value C1 since bottom square has not moved
	
	
	# mouv bottom square to its final position, always in the positive 
	# sense of rotation
	mv_c = c2 - c1
	if mv_c > 0:
		mv_c = 4 - mv_c
		total_mouvement.append(self.POS) 
		total_mouvement.append(mv_c)
	elif mv_c <0:
		mv_c = 4 + mv_c
		total_mouvement.append(self.POS) 
		total_mouvement.append(mv_c)
	else :# c2=c1 : no mouvement required, total_mouvement is not updated
		pass
	a_new = c2
	b_new = c2
	
	total_mouvement.append(self.POS) 
	total_mouvement.append(mv_c)
	
	print("mv_c : {0}, total_mouvement is {1}".format(mv_c, total_mouvement))
	
	# mouv middle sqaure to its final position, always in the negative 
	# sense of rotation
	neg_laps = 4 # negative sense of rotation
	mv_b = b2 - b_new 
	if mv_b >0 :
		mv_b = laps + (4 - mv_b)
		total_mouvement.append(self.NEG) 
		total_mouvement.append(mv_b)
	elif mv_b <0:
		mv_b = laps + abs(mv_b)
		total_mouvement.append(self.NEG) 
		total_mouvement.append(mv_b)
	else : # mv_b =0, so top square needs to move in the negative sense 
		# total mouvement is not updated
		a_neg_flag = self.NEG
	
	a_new = b2
	
	print("mv_c : {0}, total_mouvement is {1}".format(mv_c, total_mouvement))
	
	# mouv top square to its final position, positively or negatively
	
	if a_neg_flag == self.NEG :
		total_mouvement.append(self.NEG)
	else 
		total_mouvement.append(self.POS)
		
	mv_a = a2 - a_new
	if mv_a >  :
		mv_a = 4 - mv_a
		total_mouvement.append(mv_a)
	elif :
		mv_a = abs(mv_a)
		total_mouvement.append(mv_a)
	else : # a2=an : do nothing
		pass
		
		
	
	
	
	
	
		 
	
		 
			
		 
		
		 
			 
			 
