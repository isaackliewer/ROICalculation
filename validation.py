#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 18:47:05 2021

@author: isaackliewer
"""



class ValidationClass: 
    def checkFloat(self, str_input): 
        flag = True 
        while flag: 
            try: 
                str_input = float(str_input)
            except ValueError: 
                print('Value must be a valid float.')
                flag = True
            else: 
                flag = False
                print('')
            