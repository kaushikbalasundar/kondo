#!/usr/bin/env/python
import kondo_stoch as kpy
target_angle = 100
k=100
while(1):
    if (target_angle<11500):
        target_angle +=k;
        kpy.setPos(0,target_angle)
        krs.setSpd(90)
    else:
        target_angle = 3500;                
        kpy.setFree(0)  
