from dronekit import connect, VehicleMode,LocationGlobalRelative
import time
connection_string="127.0.0.1:14550"

vehicle = connect(connection_string,wait_ready=True,timeout=100)

vehicle.armed = True

vehicle.mode = VehicleMode('TAKEOFF')
print("TAKEOFF moduna geçildi.")

vehicle.simple_takeoff(20)

while vehicle.location.global_relative_frame.alt<=20*0.94:
    print("Su anki yukseklik{}".format(vehicle.location.global_relative_frame.alt))
    time.sleep(0.5)