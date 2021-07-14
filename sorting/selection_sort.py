# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 17:22:36 2020

@author: =GV=
"""

# O(n^2) ; O(0.5n^2) is still polynomial complexity because asymptotitc behaviour ignores multiplicative and additive runtime
def ascendingSelectionsort(L):
    temp = [letter for letter in L]     #n
    size = len(temp) - 1                #1
    for i in range(size,0,-1):          #n = len(L)
        target = i                          #1
        for j in range(i):                  #n = len(L)/2
            if temp[j] > temp[target]:          #1
                target = j                      #1
            else:                               #1
                continue
        temp[i], temp[target] = temp[target], temp[i]   #1
    return ''.join(temp)


# # test
# test = 'wqioeuthasdjlkgfhzxcnm,bnghtrewouip194567232097643'
# print(ascendingSelectionsort(test))
            
            