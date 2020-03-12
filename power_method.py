#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 20:04:01 2020

@author: suman
"""

import numpy as np

A=np.array([[2,-1,0],[-1,2,-1],[0,-1,2]]) #given matrix
x=np.array([1,1,1]) #initial guess of eigen vector
for i in range (100):
    x=np.dot(A,x) # matrix multiplication of A and x
    x=x/np.linalg.norm(x) #normalisation of x
e=np.dot(np.dot(A,x),x)/np.dot(x,x) # e is the dominant eigenvalue of A
print("The dominant eigenvalue of matrix A is",e) #print dominant eigenvalue
print("The corresponding eigenvector is\n",x) #print dominant eigenvector
