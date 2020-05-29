import json

# reading data from txt file
with open("x_model.txt") as obj:
	content_x = obj.read()

with open("y_model.txt") as obj:
	content_y = obj.read()

# cleaning data
content_x = content_x.replace("\n", ",")
content_x = content_x.split(",")
content_x.remove(content_x[-1])

content_y = content_y.replace("\n", ",")
content_y = content_y.split(",")
content_y.remove(content_y[-1])


# changing to float
for i in range(0, len(content_x)):
	content_x[i] = float(content_x[i])
	
for i in range(0, len(content_y)):
	content_y[i] = float(content_y[i])

# tabs containing: tabs with cut 361 coordinates from one d
x_day = []
y_day = []

start = 0
end = 360
for i in range(0, int(len(content_x) / 360)):
	# x_cut = [] x and y _cut are lists
	# y_cut = []

	# cutting
	x_cut = content_x[start:end]
	y_cut = content_y[start:end]
	
	x_day.append(x_cut)
	y_day.append(y_cut)
	
	start = end
	end += 360


xDict = {}
yDict = {}
for i in range(0, int(len(content_x) / 360)):
	xDict[str(i)] = x_day[i]

for i in range(0, int(len(content_x) / 360)):
	yDict[str(i)] = y_day[i]


# output
with open("output/xModelCordsDict.txt", 'w') as obj:
	json.dump(xDict, obj)

with open("output/yModelCordsDict.txt", 'w') as obj:
	json.dump(yDict, obj)

	
	



