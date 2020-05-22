import numpy as np
rawData = np.genfromtxt("dataset.csv", delimiter=",", skip_header=1, )
usefulData=rawData[:,1:3]
weight_kg=usefulData[:,1]
height_cm=usefulData[:,0]
height_m=height_cm/100
BMI=weight_kg/(height_m)**2
numberOfPeople=int((usefulData.size/2))
underweight=0
normal=0
overweight=0
obese=0

print(rawData[250,:])
print(rawData[250:,:])
print(usefulData)
print(np.ndarray.sum(BMI) , np.ndarray.sum(weight_kg) , np.ndarray.sum(height_cm) )


for i in range (numberOfPeople):
	if BMI[i]>=19 and BMI[i]<=25:
		normal+=1
	if BMI[i]>25 and BMI[i]<=30:
		overweight+=1
	if BMI[i]>30:
		obese+=1
	else:
		underweight+=1
print(str(round(underweight/numberOfPeople,(2))*100)+" percent of people are underweight" )
print(str(round(normal/numberOfPeople,(2))*100)+" percent of people are normal weight" )
print(str(round(overweight/numberOfPeople,(1))*100)+" percent of people are overweight" )
print(str(round(obese/numberOfPeople,(2))*100)+" percent of people are obese" )

Class = ""

averageBMI = np.ndarray.mean(BMI)
averageHeight = np.ndarray.mean(height_cm)
averageWeight = np.ndarray.mean(weight_kg)

if averageBMI>=19 and averageBMI<=25:
	Class = "normal"
if averageBMI>25 and averageBMI<=30:
	Class = "overweight"
if averageBMI>30:
	Class = "obese"
else:
	Class = "underweight"
	

print(str(round(averageBMI, (2)))+ " is the average BMI, which means the average person is "+Class)
print(str(round(averageHeight, (2)))+ " cm is the average height")
print(str(round(averageWeight, (2)))+ " kg is the average weight")	


