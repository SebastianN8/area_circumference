###########
#
# assignment2.py
#
# Created by: Sebastian N
# Created on: February 23
#
# This program calculates area and circumference of a circle
#
############

def area_of_circle(diameter_passed_in):
	total = (3.14)*(diameter_passed_in/2)**2
	print('The area is: ', total)

	return total;

def circumference_of_circle(diameter_passed_in):
	final = 2*(3.14)+(diameter_passed_in/2)
	print('The circumference is: ', final)

	return final;

diameter = input('Enter the diameter in centimeters here: ')
diameter_as_number = float(diameter)
area = area_of_circle(diameter_as_number)
circumference = circumference_of_circle(diameter_as_number)
print('Area is : ' + str(area))
print('Circumference is: ' + str(circumference))


