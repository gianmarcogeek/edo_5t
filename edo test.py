from pyedo import edo
import time

myedo = edo('192.168.12.1') # create an instance of an eDO object with IP address

x = float
y = float

### init ###
myedo.init7Axes() 
time.sleep(5)
myedo.disengageStd() # release brakes and movement
time.sleep(5)
myedo.calibAxes() # make the zero on the axis (axis should be already aligned)


### Subscription to the topics ###
myedo.listenMovementAck() # Movement confirmation topic
myedo.listenValues()# Space coordonates (x,y,z,A,E,R) topic

myedo.moveToWaitingPos() # starting point for cartesian moves

### move function ###
if x <= 100:
    myedo.moveCircularX(x, y, 150, 0, 180, 23.57, 60, 250, 400,150, 0, 180, 23.57, 60) 
else: 
    myedo.moveCartesianX(x, y, 150, 0, 180, 23.57, 60)

