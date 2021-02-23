"""
-------------------------------------------------------------------------------
Name:   problem2.py
Purpose:  determine whether figure is a triangle 
 
Author: Yao.T
 
Created:  23/02/2021
------------------------------------------------------------------------------
"""

#get triangle length 
len1 = int(input("Enter the length of the first side: "))
len2 = int(input("Enter the length of the second side: "))
len3 = int(input("Enter the length of the third side: "))

#check if sum of any two sides is greater than third side, output
if len1+len2 > len3 and len1+len3 > len2 and len2+len3 > len1:
  print("The figure is a triangle.")
else:
  print("The figure is NOT a triangle.")