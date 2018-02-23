#######
#
# assignment2a.py
#
# Created by: Sebastian N
# Created on: February 21
#
# This program calculates de area and circumference of a circle  
#

def calculate_area_of_a_circle(diameter_passed_in):
	total = (3.14)*(diameter_passed_in/2)^2
	print('The area is: ', total)

	return total;

diameter = input('Put the diameter of the circle here: ')
area = calculate_area_of_a_circle(diameter)
print ("Area of circle is: " + area)

input()