from dronekit import connect, VehicleMode,LocationGlobalRelative
import time
connection_string="127.0.0.1:14550"

vehicle = connect(connection_string,wait_ready=True,timeout=100)

vehicle.armed = True