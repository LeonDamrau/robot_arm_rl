import numpy as np
import pybullet as p 
import pybullet_data 
import time 

p.connect(p.GUI)
p.resetSimulation()
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,9.81)
p.setRealTimeSimulation(0)

planeId = p.loadURDF("plane.urdf",[0,0,0],[0,0,0,1])
robotId = p.loadURDF("kuka_iiwa/model.urdf",[0,0,0],[0,0,0,1])
print(p.getNumJoints(robotId))

for step in range(300):
    print(p.getJointState(robotId,4))
    p.stepSimulation()
    time.sleep(0.01)







