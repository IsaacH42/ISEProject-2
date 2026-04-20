# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 09:38:00 2026

@author: isaac
"""

infile1 = open("C:\\Users\\isaac\\.spyder-py3\\ISEProject-2\\coverage1.txt")
infile2 = open("C:\\Users\\isaac\\.spyder-py3\\ISEProject-2\\coverage2.txt")
#These are the data files that have the coverage1 and 2 data 
#In these files they indicate which centers cover which county and they also give you the price of each of the centers
Centers1 = [line.strip().split(",") for line in infile1.readlines()]
Centers2 = [line.strip().split(",") for line in infile2.readlines()]
#.readlines returns both of the centers strings as lines and can be stiped and split. This is so you can use the txt data as lists for each of the centers.
County_overlap = {}
#creating this dictionary will allow us to use a program, to find the best center to optomize coverage

