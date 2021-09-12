#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 12:32:43 2021

@author: isaackliewer
"""
class CalculationClass: 
    def ROIcalculation(initial_input, current_input):
        ROIamount = (current_input - initial_input)/initial_input
        return ROIamount