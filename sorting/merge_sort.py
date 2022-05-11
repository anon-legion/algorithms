# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 21:53:10 2021

@author: =GV=
"""

def merge(left, right):
    result = []
    while len(left) > 0 <  len(right):
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left) == 0:
        result += right
    else:
        result += left
    return result
            
            
def mergesort(L):
    if len(L) < 2:
        return L[:]
    else:
        mid_index = len(L) // 2
        left = mergesort(L[:mid_index])
        right = mergesort(L[mid_index:])
        return merge(left, right)
    

# # test
# test = 'wqioeuthasdjlkgfhzxcnm,bnghtrewouip194567232097643'
# data = [i for i in test]
# print(''.join(mergesort(data)))
    