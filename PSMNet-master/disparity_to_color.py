import glob
import cv2
import os
import numpy as np

def disp_map(I, img):
  map = [[0,0,0,114], [0,0,1,185], [1,0,0,114], [1,0,1,174],
       [0,1,0,114], [0,1,1,185],[1,1,0,114], [1,1,1,0]]
  map = np.array(map,dtype=np.uint8)
  bins = map[:-1,3]
  cbins = np.cumsum(bins)
  bins = bins / cbins[-1]
  cbins = cbins[:-1] / cbins[-1]
  ind = sum(np.tile(I,[6,1]) > np.tile(cbins,[I.size,1]).T)
  bins  = 1 / bins
  cbins = np.insert(cbins,0,0.0)

  t1 = [cbins[t] for t in ind]
  t1 = np.array(t1)
  t2 = [bins[t] for t in ind]
  t2 = np.array(t2)
  I = (I-t1) * t2
  #map(ind+1,1:3) .* repmat(I, [1 3])
  t3 = [map[t,:3] for t in ind]
  t3 = np.array(t3)
  t3 = t3 * np.tile(1-I.T,[3,1]).T

  t4 = [map[t+1,:3] for t in ind]
  t4 = np.array(t4)
  t4 = t4 * np.tile(I.T,[3,1]).T

  t5 = t3 + t4
  t5[np.where(t5<0)] = 0
  t5[np.where(t5>1)] = 1

  t5 = np.reshape(t5,[img.shape[0],img.shape[1],3],order='F') * 255
  t5 = np.array(t5,dtype=np.uint8)
  t5 = cv2.cvtColor(t5,cv2.COLOR_RGB2BGR)
  return t5


def main():
  max_disp = 256
  #name of disparity image
  disp = 'Test_disparity.png'

  #load image
  img = cv2.imread(disp,-1)

  #scale and round
  I = np.around(img/max_disp, decimals=0)
  I = np.array(I,dtype=np.float64)
  I = (I.T.flatten()) / max_disp
  r = disp_map(I, img)

  #write to output folderput
  output_color_disp_name = 'plots/testje_sceneflow.png'
  cv2.imwrite(output_color_disp_name, r)

if __name__ == '__main__':
    main()
