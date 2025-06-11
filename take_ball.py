from edo5t import edo
import time

def is_position_safe(x, y, z):
    """Simple safety constraints for reachable Cartesian space."""
    return (
        -400 <= x <= 400 and
        -400 <= y <= 400 and
        150 <= z <= 550
    )

def move_safely_to_target():
    # Create robot instance
    robot = edo('10.42.0.49')

    if not robot.ros.is_connected:
        print("[ERROR] ROS is not connected. Check your WebSocket or robot status.")
        return

    print("[INFO] Connected to e.DO")

    # Init and calibrate robot
    # Safe hover position before moving into workspace
    hover_pose = {
        "x": 0,
        "y": 0,
        "z": 450,
        "alpha": 0,
        "beta": 90,
        "gamma": 0
    }

    print("[INFO] Moving to hover position above base...")
    robot.moveCartesian(**hover_pose, move_type="JOINT", speed=20, zone=0)
    time.sleep(3)  # give time to complete

    # Target position
    target_pose = {
        "x": 200,
        "y": 300,
        "z": 350,
        "alpha": 0,
        "beta": 90,
        "gamma": 0
    }

    if not is_position_safe(target_pose["x"], target_pose["y"], target_pose["z"]):
        print("[WARNING] Unsafe position requested. Movement canceled.")
        return

    print(f"[INFO] Moving to target position: {target_pose}")
    robot.moveCartesian(**target_pose, move_type="LINEAR", speed=20, zone=0)

    print("[SUCCESS] Movement completed.")

if __name__ == "__main__":
    move_safely_to_target()

