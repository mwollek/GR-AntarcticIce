import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import json

# initialize plot frame and data
fig, ax = plt.subplots()
ln, = plt.plot([], [])
ln1, = plt.plot([], [])


# getting data
print("Loading data...")
with open('output/xCordsDict.txt') as obj:
	xDict = json.load(obj)

with open('output/yCordsDict.txt') as obj:
	yDict = json.load(obj)

with open('output/xModelCordsDict.txt') as obj:
	xModelDict = json.load(obj)

with open('output/yModelCordsDict.txt') as obj:
	yModelDict = json.load(obj)


def init():
	ax.set_xlim(-4000, 4000)
	ax.set_ylim(-4000, 4000)
	return ln,


def update(frame):
	if frame == 9500:
		return 0

	xCords = xDict[str(frame)]
	yCords = yDict[str(frame)]

	xModelCords = xModelDict[str(frame)]
	yModelCords = yModelDict[str(frame)]

	ln.set_data(yCords, xCords)
	ln1.set_data(yModelCords, xModelCords)

	return ln1, ln


print("Running")
animation = FuncAnimation(fig, update, frames=np.arange(0, 500), init_func=init, blit=True, interval=60)
plt.show()






