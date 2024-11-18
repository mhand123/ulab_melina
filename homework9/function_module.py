# File name: function_module

import numpy as np
import matplotlib.pyplot as plt


# Function 1:
def plot_functions_horizontal(domain=(0, 2 * np.pi)):
    """
    plots cos(x) and sin(x) in horizontal/side by side subplots
    """
    x = np.linspace(domain[0], domain[1], 100)  #domain of x
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))  #make figure. subplots(rows, columns, size)
    
    #Left: h(x) = cos(x)
    ax1.plot(x, np.cos(x), label=r'$h(x) = \cos(x)$', color='blue', linestyle='-')
    ax1.set_title(r'$h(x) = \cos(x)$')
    ax1.set_xlabel('x')
    ax1.set_ylabel('h(x)')
    ax1.grid(True)
    ax1.legend() 
    #Right: k(x) = sin(x)
    ax2.plot(x, np.sin(x), label=r'$k(x) = \sin(x)$', color='green', linestyle='--')
    ax2.set_title(r'$k(x) = \sin(x)$')
    ax2.set_xlabel('x')
    ax2.set_ylabel('k(x)')
    ax2.grid(True)
    ax2.legend()
    #Plot
    plt.tight_layout() 
    plt.show() 

def plot_functions_vertical(domain=(0, 2 * np.pi)):
    """
    plots cos(x) and sin(x) in vertical/on top of each other subplots
    """
    x = np.linspace(domain[0], domain[1], 100)  #domain of x
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 4))  #make figure. subplots(rows, columns, size)
    
    #Left: h(x) = cos(x)
    ax1.plot(x, np.cos(x), label=r'$h(x) = \cos(x)$', color='blue', linestyle='-')
    ax1.set_title(r'$h(x) = \cos(x)$')
    ax1.set_xlabel('x')
    ax1.set_ylabel('h(x)')
    ax1.grid(True)
    ax1.legend() 
    #Right: k(x) = sin(x)
    ax2.plot(x, np.sin(x), label=r'$k(x) = \sin(x)$', color='green', linestyle='--')
    ax2.set_title(r'$k(x) = \sin(x)$')
    ax2.set_xlabel('x')
    ax2.set_ylabel('k(x)')
    ax2.grid(True)
    ax2.legend()
    #Plot
    plt.tight_layout() 
    plt.show()
