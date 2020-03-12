#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 22:57:00 2020

@author: suman
"""

import numpy as np
import time

t1 = time.process_time() #starting elapsed time
A=np.array([[0,1,1],[0,1,0],[1,1,0],[0,1,0],[1,0,1]]) #given matrix
B=np.matmul(A,A.T) #matrix multiplication of A and transpose of A
e,v=np.linalg.eigh(B) #e is the eigenvalues and v is eigenvectors of B
print("The singular values of A are")
for i in range (len(e)):
   if abs(e[i]-0.0)>0.001:
      print(np.sqrt(e[i])) #square root of non-zero eigenvalues
t2=time.process_time()-t1 #elapsed time during this programme
print("Time taken for this code",t2)

P,D,Q = np.linalg.svd(A) # D is the array of singular values of A
print("The singular values of A", D)
t3=time.process_time()-t1-t2 #elapsed time for using function
print("Time taken by using numpy function",t3)
