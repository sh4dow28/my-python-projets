# coding:utf-8

from cmath import pi


print("\n\t**********START OF PROGRAM : Calculates the volume of a cone.**********\n")

radius = input("\t\tEnter the radius of the cone : ")
radius = float(radius)
height = input("\n\t\tEnter the height of the cone : ")
height = float(height)

volume = (1 / 3) * pi * pow(radius, 2) * height

print("\n\t\tThe volume of cone of radius {}, and height {} is : {}".format(radius,height,volume))

print("\n\n\t********************END OF PROGRAM********************")