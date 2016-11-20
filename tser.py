import serial


ser = serial.Serial('COM4', 9600)

while True :
	print("lol")
	aa = ser.readline()
	print(aa)
	print("lol")
	
	
