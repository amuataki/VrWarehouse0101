hwgrade1 = (input(float("Please enter your homework grade 1:")))
hwgrade2 = (input(float("Please enter your homework grade 2:")))
hwgrade3 = (input(float("Please enter your homework grade 3:")))
labgrade1 = (input(float("Please enter your lab grade 1:")))
labgrade2 = (input(float("Please enter your lab grade 2:")))
examgrade = (input(float("Please enter your exam grade:")))
hwavg = ((hwgrade1 + hwgrade2 + hwgrade3)/3 ) * .5
labavg = labgrade1 + labgrade2 / 2 * .2
exam = examgrade *3
print (hwavg + labavg + exam)