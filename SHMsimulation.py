import matplotlib.pyplot as plt
import numpy as np
import math
import time
from statistics import mean

class sim():
	def __init__(self,mass,springConstant,displacementOfSpring,damping = 0.99,initialVelocity = 0):
		self.mass=mass #g - 9.81
		self.springConstant=springConstant
		self.displacement=displacementOfSpring
		self.v = initialVelocity
		self.time=0
		self.dt=0.0001
		self.damping = damping

	def simulate(self):#simulate the velocity of the particle after small amount of time specifed, retains the conditions from the prior simulation

		a=(self.mass*9.81 - self.displacement*self.springConstant)/self.mass

		self.displacement += self.v*self.dt + (1/2)*a*self.dt*self.dt
		self.v += a*self.dt

		self.time+= self.dt
		self.v = self.v*self.damping

def timefunc(func):
	def wrapper(*arg, **kwargs):
		startTime = time.time()
		results = func(*arg, **kwargs)
		endTime = time.time()
		print(f"{func} took {endTime-startTime}s to complete.")
		return results
	return wrapper

def main(*arg, **kwargs):

	system=sim(*arg, **kwargs)
	dataV =np.ones(100)
	counter = 0

	while True:

		system.simulate()
		dataV[counter%100]=system.v

		if (np.sum(np.abs(dataV))) < 0.1:
			break

		counter +=1

	print(system.time)

	return system.time
		

def findCritDamp():

	dampings = np.arange(0.999827,0.999825, -0.0000001)
	print(dampings)
	times = []


	for damp in dampings:
		times.append(main(1,1,100, damping = damp))

	return dampings, times

def plotV():

	system=sim(1,1,100, damping = 0.99989)
	dataT =[]
	dataV =[]

	while True:

		system.simulate()
		dataV.append(system.v)
		dataT.append(system.time)

		if len(dataV) > 100:
			if (sum(map(abs, dataV[-100:]))) < 0.1:
				break

	return dataT, dataV
	
X, Y=timefunc(findCritDamp)()
plt.plot(X,Y)
plt.show()
