import matplotlib.pyplot as plt
import numpy as np
import math

class sim():
	def __init__(self,mass,springConstant,displacementOfSpring,initialVelocity = 0):
		self.mass=mass #g - 9.81
		self.springConstant=springConstant
		self.displacement=displacementOfSpring
		self.v = initialVelocity
		self.ke = (1/2)*(initialVelocity^2)*self.mass
		self.time=0
		self.changeInHeight=0

	def simulate(self,time):#simulate the velocity of the particle after small amount of time specifed, retains the conditions from the prior simulation

		a=(self.mass*9.81 - self.displacement*self.springConstant)/self.mass

		self.displacement += self.v*time + (1/2)*a*time*time
		self.v += a*time
		self.time+= time

dataV=[]
dataTime=[]
system=sim(1,1,10)
for i in range (100000):
	system.simulate(0.001)
	dataV.append(system.v)
	dataTime.append(system.time)
	if system.v > 1:
		break


plt.plot(dataTime,dataV)

plt.show()


