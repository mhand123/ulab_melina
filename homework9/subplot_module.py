# file name: subplot_module.py

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

image1 = np.array(Image.open('rcb_var1.jpg'))  #define variables
image2 = np.array(Image.open('rcb_var2.jpg'))
image3 = np.array(Image.open('rcb_var3.jpg'))
image4 = np.array(Image.open('rcb_var4.jpg'))

def plot_images_rcb_var(image1, image2, image3, image4):
    """
    Takes 4 images and arranges them into a 2x2 subplot
    Input: image paths
    Output: grid
    """
   
    
    fig, axs = plt.subplots(2, 2, figsize=(10, 10)) #create subplot
    images = [image1, image2, image3, image4]
    axs = axs.flatten()
    
    for i, ax in enumerate(axs):  #show images
        ax.imshow(images[i])
        ax.axis('off') 
        
    plt.tight_layout()  # Adjust layout to prevent overlap
    plt.show()



