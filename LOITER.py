from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

vehicle = connect("127.0.0.1:14550", wait_ready=True)

def takeoff():
    vehicle.mode = VehicleMode('TAKEOFF')
    print("TAKEOFF moduna geçildi.")

    vehicle.simple_takeoff(20)

vehicle.armed = True

takeoff()

target_location = LocationGlobalRelative(40.26852584, -111.63234139, 30)
vehicle.simple_goto(target_location)
print("LOITER moduna geçildi.")

time.sleep(20)