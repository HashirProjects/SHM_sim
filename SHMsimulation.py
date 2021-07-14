import matplotlib.pyplot as plt
import numpy as np
import math
import time

class sim():
	def __init__(self,mass,springConstant,displacementOfSpring,initialVelocity = 0):
		self.mass=mass #g - 9.81
		self.springConstant=springConstant
		self.displacement=displacementOfSpring
		self.v = initialVelocity
		self.ke = (1/2)*(initialVelocity^2)*self.mass
		self.time=0
		self.changeInHeight=0

	def simulate(self,time = 0.0001):#simulate the velocity of the particle after small amount of time specifed, retains the conditions from the prior simulation

		a=(self.mass*9.81 - self.displacement*self.springConstant)/self.mass

		self.displacement += self.v*time + (1/2)*a*time*time
		self.v += a*time
		self.time+= time

def timefunc(func):
	def wrapper(*arg):
		startTime = time.time()
		results = func(*arg)
		endTime = time.time()
		print(f"{func} took {endTime-startTime}s to complete.")
		return results
	return wrapper

def main(*arg):

	dataV=[]
	dataTime=[]
	system=sim(arg[0],arg[1],arg[2])

	for i in range (1000000):
		system.simulate()
		dataV.append(system.v)
		dataTime.append(system.time)


	return (dataTime, dataV)


dataTime, dataV =timefunc(main)(1,1,10)
plt.plot(dataTime, dataV)
plt.show()

