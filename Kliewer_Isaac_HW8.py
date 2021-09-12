#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 16:55:49 2021

@author: isaackliewer
"""


#Author: Isaac Kliewer 
#Assignment Number: 8
#Date: 4-30-21
#Description: I use two classes each stored in their own module to validate and perform 
# calculations on two float inputs received in the main module. The attributes are public.
# In order to validate two inputs, two different objects of the validation class were made. 


import validation
import calculation

def main(): 
    validation_object = validation.ValidationClass()  #Create an object of the validation class.
    initial_input = input("What is the initial value? ")        
    validation_object.checkFloat(initial_input) #Apply the method to the input via objectname.method() format.
    while validation_object.checkFloat(initial_input):
        #Based on the boolean achieved in the validation class, re-query user on amount. 
        print('Invalid initial value, please enter a float.')
        initial_input = input("What is the initial value? ")        
        validation_object.checkFloat(initial_input)
        
    
    
    
    validation_object = validation.ValidationClass()  # Create another object of the validation class.
    current_input = input("What is the current value? ")
    validation_object.checkFloat(current_input)  #Apply the method to the input via objectname.method() format.
    while validation_object.checkFloat(current_input):
        #Based on the boolean achieved in the validation class, re-query user on amount. 
        print('Invalid final value, please enter a float.')
        current_input = input("What is the current value? ")
        validation_object.checkFloat(current_input)
        
    
  
    
    calculation_object = calculation.CalculationClass(initial_input, current_input) # Create object of
    ROI = calculation_object.calcROI()                                              # calculation class.
    print("The ROI for this investment is ", format(100*ROI, '.2f'), "%", sep="")  #Format ROI float correctly.
    
    
main()
    