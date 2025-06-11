from pyedo import edo

import time

robot = edo('10.42.0.49')
robot.listenMovementAck() #movement confirmation topic
robot.listenValues()# Space coordonates (x,y,z,A,E,R) topic
time.sleep(5)

def is_position_safe(x, y, z):
    """Simple safety constraints for reachable Cartesian space."""
    return (
        200 <= abs(x) <= 400 and
        200 <= abs(y) <= 400 and
        0 <= z <= 350
    )

def move_safely_to_target():
    robot.disengageStd() # release brakes and movement
    # Create robot instance
    #robot = edo('10.42.0.49')

    #if not robot.roslibpy.is_connected:
     #   print("[ERROR] ROS is not connected. Check your WebSocket or robot status.")
      #  return

    #print("[INFO] Connected to e.DO")

    # Init and calibrate robot
    # Safe hover position before moving into workspace
    
    
    
    hover_pose = {
        "x": 0,
        "y": 0,
        "z": 450,
        "a": 0,
        "e": 90,
        "r": 0
    }

    print("[INFO] Moving to hover position above base...")
    robot.moveToWaitingPos()
    time.sleep(3)  # give time to complete

    # Target position
    target_pose = {
        "x": -100,
        "y": 300,
        "z": 0,
        "a": 0,
        "e": 180,
        "r": 0
    }

    if not is_position_safe(target_pose["x"], target_pose["y"], target_pose["z"]):
        print("[WARNING] Unsafe position requested. Movement canceled.")
        return

    print(f"[INFO] Moving to target position: {target_pose}")
    robot.moveCartesian(**target_pose)

    print("[SUCCESS] Movement completed.")

if __name__ == "__main__":
    move_safely_to_target()

