#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 19:23:14 2021

@author: carolineskalla
"""

def solvable(A, B):
    if len(A.intersection(B)) == 0:
        return False
    else:
        return True
    
A = {0, 5, 6, 8, 9}
B = {1, 2, 3, 4, 7}

#print(solvable(A,B))

def solvable2(A,B):
    return A.intersection(B)
##print(solvable2(A,B))


a = 3
def remove(aset, ele):
    aset.remove(ele)
    print(B)

remove(B, a)