#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 19:40:58 2020

@author: suman
"""

import numpy as np

A=np.array([[5,-2],[-2,8]]) #given matrix
q,r = np.linalg.qr(A) #QR decomposition using numpy function
print("The Q matrix is\n",q)
print("The R matrix is\n",r)
for i in range (100):
    q,r = np.linalg.qr(A)
    A=np.dot(r,q) #This is similarity transformation to diagonalise A
print("The form of A after diagonalisation\n",A)
print("The eigen values of matrix A ",A[0][0],"and",A[1][1]) #diagonal elements of A are the eigenvalues
e,v=np.linalg.eigh(A) # e is eigenvalue and v is eigenvector of matrix A
print("The eigen values of matrix A ",e) #the eigen values are same in the two process
    