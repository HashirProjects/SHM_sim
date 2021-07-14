import matplotlib.pyplot as plt
import numpy as np
import math
import time
import numba

class sim():
	def __init__(self,mass,springConstant,displacementOfSpring,damping = 0.99,initialVelocity = 0):
		self.mass=mass #g - 9.81
		self.springConstant=springConstant
		self.displacement=displacementOfSpring
		self.v = initialVelocity
		self.ke = (1/2)*(initialVelocity^2)*self.mass
		self.time=0
		self.changeInHeight=0
		self.damping = damping

	def simulate(self,time = 0.0001):#simulate the velocity of the particle after small amount of time specifed, retains the conditions from the prior simulation

		a=(self.mass*9.81 - self.displacement*self.springConstant)/self.mass

		self.displacement += self.v*time + (1/2)*a*time*time
		self.v += a*time
		self.time+= time
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

	while True:
		system.simulate()
		if abs(system.v) < 0.0001:
			break

	print(system.time)
	return system.time
		

def findCritDamp():

	dampings = np.arange(1,0.9999, -0.000001)
	print(dampings)
	times = []


	for damp in dampings:
		times.append(main(1,1,100, damping = damp))

	plt.plot(dampings, times)
	plt.show()

timefunc(findCritDamp)()