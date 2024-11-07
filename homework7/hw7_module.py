# File: hw7_module.py

import numpy as np

def hypotenuse_of_array(array):
    """
    Gives the hypotenuse of a 2x2 array

    Parameters:
    x1, x2: legs of triangle
    out: location where result is stored. Set to hypotenuses
    where: set to optional

    Output: ndarray = hypotenuse

    """
    hypotenuses = [] #out location
    for x in array:
        hypotenuses.append(np.hypot(x[0], x[1]))
    return np.array(hypotenuses)


def is_cosine_possible(value):
     """
     Tells if a given value can be the result of a cosine function

     Input: any value
     Output: true or false (boolean)
     """
     if -1<= value <=1:
         print(value == True)
     else:
         print(value == False)


         
def tangent_and_sort(array):
    """
    Calculates the tangent of a 2x2 array and then sorts the results from smallest to greatest

    Input: 2x2 array
    Output: sorted tangents in an array
    """
    if array.shape != (2, 2):
        raise ValueError("Input must be a 2x2 numpy array.")
    
    tangent_array = np.tan(array) #calculate tangent
    
    sort_tangent = np.sort(tangent_array.flatten()) #sort from smallest to largest
    
    return sort_tangent




        
         
    
    