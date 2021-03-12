"""
-------------------------------------------------------------------------------
Name:   problem1.py
Purpose:  output a "radar" sign when speed over the limit
 
Author: Yao.T
 
Created:  23/02/2021
------------------------------------------------------------------------------
"""

#get speed limit and current speed of driver 
speedLimit = int(input("Enter the speed limit: "))
recordedSpeed = int(input("Enter the recorded speed of the car: "))

#calculate difference between recordedSpeed and speedLimit
difference = recordedSpeed - speedLimit

#check if recordedSpeed is over speedLimit, output  
if recordedSpeed > speedLimit:
  if difference > 0 and difference < 21: 
    print("You are speeding and your fine is $100.")
  elif difference > 20 and difference < 31:
    print("You are speeding and your fine is $270.")
  elif difference > 30:
    print("You are speeding and your fine is $570. ")
else:
  print("Congratulations, you are within the speed limit!")

