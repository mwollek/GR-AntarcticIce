import json

# reading data from txt file
with open("x.txt") as x:
	content_x = x.read()

with open("y.txt") as y:
	content_y = y.read()

# cleaning data
content_x = content_x.replace("\n", "")
content_x = content_x.split(",")

content_y = content_y.replace("\n", ",")
content_y = content_y.split(",")
content_y.remove(content_y[-1])


# changing to float
for i in range(0, len(content_x)):
	content_x[i] = float(content_x[i])
	
for i in range(0, len(content_y)):
	content_y[i] = float(content_y[i])	

# tabs containing: tabs with cut 361 coordinates from one day
x_day = []
y_day = []

start = 0
end = 361
for i in range(0, int(len(content_x) / 361)):

	# x_cut = [] x and y _cut are lists
	# y_cut = []

	# cutting
	x_cut = content_x[start:end]
	y_cut = content_y[start:end]
	
	x_day.append(x_cut)
	y_day.append(y_cut)
	
	start = end
	end += 361

# preparing data for output
xDict = {}
yDict = {}
for i in range(0, int(len(content_x) / 361)):
	xDict[str(i)] = x_day[i]

for i in range(0, int(len(content_x) / 361)):
	yDict[str(i)] = y_day[i]


print(len(xDict.keys()))
# output
with open("output/xCordsDict.txt", 'w') as obj:
	json.dump(xDict, obj)

with open("output/yCordsDict.txt", 'w') as obj:
	json.dump(yDict, obj)



	


