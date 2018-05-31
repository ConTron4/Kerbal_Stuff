import krpc
import time

conn = krpc.connect(name = 'Sub-orbital Flight')
vessel = conn.space_center.active_vessel

vessel.auto_pilot.target_pitch_and_heading(90,90)
vessel.auto_pilot.engage()
vessel.control.throttle = 1
time.sleep(1)

print('Launching!')
vessel.control.activate_next_stage()
vessel.control.activate_next_stage()
