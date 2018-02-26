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
	total = (3.14)*(diameter_passed_in/2)**2
	print('The area is: ', total, 'cm^2')

	return total;

def calculate_circumference(diameter_passed_in):
	final = 2*(3.14)*(diameter_passed_in/2)
	print('The circumference is: ', final, 'cm')

	return final;

diameter = input('Put the diameter in centimeters of the circle here: ')
diameter_as_number = float(diameter)
area = calculate_area_of_a_circle(diameter_as_number)
circumference = calculate_circumference(diameter_as_number)

input()