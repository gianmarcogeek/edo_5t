from pyedo import edo
import time

myedo = edo('10.42.0.49') # create an instance of an eDO object with IP address

# x = float
# y = float

# ### Subscription to the topics ###
# myedo.listenMovementAck() # Movement confirmation topic
# myedo.listenValues()# Space coordonates (x,y,z,A,E,R) topic


# ### init ###
# myedo.init7Axes() 
# time.sleep(5)
# myedo.disengageStd() # release brakes and movement
# time.sleep(5)
# myedo.calibAxes() # make the zero on the axis (axis should be already aligned)

# myedo.moveToWaitingPos() # starting point for cartesian moves

def StartUp(myedo):
    myedo.init6Axes()
    time.sleep(5)
    myedo.disengageSafe()
    print("daje")
    time.sleep(40)
    myedo.calibAxes() # Mandatory in HOME POSITION
StartUp(myedo)