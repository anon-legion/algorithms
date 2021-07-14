# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 12:06:29 2021

@author: =GV=
"""

def get_permutations(s):
    """
    Parameters
    ----------
    s : string
        assumes any string

    Returns
    -------
    result : list
        Function returns a list strings of all possible permutations of s
    """
    
    temp = [i for i in s]
    result = []
    
    def swap(swap_list, index_a, index_b):
        swap_list[index_a], swap_list[index_b] = swap_list[index_b], swap_list[index_a]
    
    def generate(n, heap_list):       
        """        
        Parameters
        ----------
        n : int
            assumes an integer where n is the length of heap_list
        heap_list : list
            assumes a list of strings to permutate
            
        Returns
        -------
        None
            Function appends permutations of heap_list into result
        """
        
        if n == 1:
            result.append(''.join(heap_list))
            return
        else:
            generate(n - 1, heap_list)
            
            for i in range(n - 1):
                if n % 2 == 0:
                    swap(heap_list, i, n - 1)
                else:
                    swap(heap_list, 0, n-1)
                generate(n - 1, heap_list)
    
    generate(len(temp), temp)
    return result


def get_permutations_nonrecursive(s):
    """
    Parameters
    ----------
    s : string
        assumes any string

    Returns
    -------
    result : list
        Function returns a list strings of all possible permutations of s
    """
    
    temp = [i for i in s]
    result = []
    
    def swap(swap_list, index_a, index_b):
        swap_list[index_a], swap_list[index_b] = swap_list[index_b], swap_list[index_a]
        
    def generate(n, heap_list):
        """        
        Parameters
        ----------
        n : int
            assumes an integer where n is the length of heap_list
        heap_list : list
            assumes a list of strings to permutate
            
        Returns
        -------
        None
            Function appends permutations of heap_list into result
        """
        
        c = [] # array of int
        
        for i in range(n):
            c.append(0)
        
        result.append(''.join(heap_list))
        
        i = 1
        while i < n:
            if c[i] < i:
                if i % 2 == 0:
                    swap(heap_list, 0, i)
                else:
                    swap(heap_list, c[i], i)
                result.append(''.join(heap_list))
                c[i] += 1
                i = 1
            else:
                c[i] = 0
                i += 1
    
    generate(len(temp), temp)
    return result

print(f"Result of recursive heap algorithm:\n{get_permutations('123')}")
print()
print(f"Result of non-recursive heal algorithm:\n{get_permutations_nonrecursive('123')}")
    