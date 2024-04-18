from dronekit import connect, VehicleMode,LocationGlobalRelative
import time
from pymavlink import mavutil

connection_string="127.0.0.1:14550"

vehicle = connect(connection_string,wait_ready=True,timeout=100)

vehicle.armed = True

vehicle.mode = VehicleMode('TAKEOFF')
print("TAKEOFF moduna geçildi.")

vehicle.simple_takeoff(20)

msg = vehicle.message_factory.command_long_encode(0, 0,mavutil.mavlink.MAV_CMD_CONDITION_YAW,0,100,0,1,0,0, 0, 0)
vehicle.send_mavlink(msg)

msg = vehicle.message_factory.set_position_target_local_ned_encode(0,0,0,mavutil.mavlink.MAV_FRAME_LOCAL_NED,0b0000111111000111,0, 0,0,20,10,-5,0,0,0,0,0)
vehicle.send_mavlink(msg)
print("Hız değiştirildi.")