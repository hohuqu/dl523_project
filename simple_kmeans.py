# -*- coding: utf-8 -*-
"""AutoEncoder_kmeans.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1839seIIN3uEsIVE8e1dgubF1HOmo0bMY
"""

import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import torch

#%% import data
root = '/Dataset1_benchmark'
# 'projectnb/dl523/students/izhou/'

def read_tiff(path):
    """
    path - Path to the multipage-tiff file
    """
    img = Image.open(path)
    images = []
    for i in range(img.n_frames):
        img.seek(i)
        images.append(np.array(img))
    return np.array(images)

images1 = read_tiff('./Dataset1_benchmark/Gene1.tif')
dim = images1.shape
images_allGenes = np.zeros((15,dim[0],dim[1],dim[2]))
images_allGenes[0,:,:,:] = images1

for i in range(2,16):
  path = f'./Dataset1_benchmark/Gene{i}.tif'
  image = read_tiff(path)
  images_allGenes[i-1,:,:,:] = image



#%%  basic k-means
# images_allGenes: [gene, z, x, y]
#                  (15, 25, 2006, 2005)

from sklearn.cluster import KMeans
z1 = images_allGenes[:,0,:,:]


kmeans = KMeans(n_clusters=47)
data = list()

for i in range(z1.shape[1]):
    for j in range(z1.shape[2]):
        data.append(z1[:,i,j])
        
        
kmeans_result = kmeans.fit(data)

labels = kmeans_result.labels_

z1_labeled = labels.reshape((z1.shape[1],z1.shape[2]))

from matplotlib import pyplot as plt
plt.imshow(z1_labeled, interpolation='nearest')
plt.savefig('./Dataset1_benchmark/simple_kmeans/z1_simpleKMeans_47.jpg', dpi = 300)

plt.show()

#%%  basic k-means, less cluster for visual purpose
# images_allGenes: [gene, z, x, y]
#                  (15, 25, 2006, 2005)
z1 = images_allGenes[:,0,:,:]


kmeans = KMeans(n_clusters=10)
data = list()

for i in range(z1.shape[1]):
    for j in range(z1.shape[2]):
        data.append(z1[:,i,j])
        
        
kmeans_result = kmeans.fit(data)

labels = kmeans_result.labels_

z1_labeled = labels.reshape((z1.shape[1],z1.shape[2]))

from matplotlib import pyplot as plt
plt.imshow(z1_labeled, interpolation='nearest')
plt.savefig('./Dataset1_benchmark/simple_kmeans/z1_simpleKMeans_8.jpg', dpi = 300)

plt.show()


#%% auto-encoder


























