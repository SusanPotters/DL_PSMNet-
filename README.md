# Pyramid Stereo Matching Network - DL reproducibility project
by Sjoerd Dijkstra and Susan Potters

## Contents

1. [Introduction](#introduction)
2. [Contributions](#constributions)
3. [Usage](#usage)

## Introduction
As a part of the course CS4240 Deep Learning, a reproducibility project was done based on the "[Pyramid Stereo Matching Network](https://arxiv.org/abs/1803.08669)" paper (CVPR 2018) by [Jia-Ren Chang](https://jiarenchang.github.io/) and [Yong-Sheng Chen](https://people.cs.nctu.edu.tw/~yschen/).

In this work the writers proposed a new pyramid stereo matching network to be further referred to as PSMNet. This network aimed to exploit global context information in stereo matching. In order to make it possible that the receptive field could be enlarged, spatial pyramid pooling and dilated convolution were used. By doing so, the network is capable of extending pixel-level feature maps to region-level feature maps with varying scales to receptive fields. Disparity estimation was conducted reliably using the combination of these global and local feature maps to form a cost volume.   A stacked hourglass 3D CNN inconjunction with intermediate supervision was designed to regularize this costvolume. This architecture processed the cost volume in a top-down/bottom-up manner to improve on the existing use of global context information. 

The reproducibility project involves reproducing the authors' results on the Scene Flow test set, for which a 1.09 EPE was achieved by the authors. In addition, we use the trained model on stereo images of plane parts, to see if the model can generalize to data unlike the training set.

## Contributions

### Pre-trained model
The authors of the PSMNet paper, provided multiple pretrained models, one of which was trained on the Scene Flow training set for ten epochs. This model was evaluated by us, however the EPE of 1.09 was not achieved. In contrast, an EPE of 6.263 was found, which does not come close. Therefore, we conclude that the authors made the wrong model available and we cannot reproduce their results this way.

### Trained model
In addition to evaluating the pre-trained model, we have trained two models ourselves. Due to computational constraints of our own laptops, Google Cloud in combination with a jupyter notebook was used to train the models with a Nvidia V100 GPU. First, the model was trained with a batch size of five on the full Scene Flow dataset, consisting of FlyingThings3D, Driving and Monkaa for five epochs. Second, a model was trained only on the Monkaa dataset for ten epochs.

We found that by training for five epochs, an EPE of 1.293 was achieved. Considering that the authors trained for ten epochs with a batch size of 12, we come very close to their results with less resources. Additionally, the model trained on the Monkaa dataset achieves an EPE of 3.213.

### Tests on unseen data
After training, the models were tested on some unseen data of motor blades.

## Usage

### Train locally
As an example, use the following command to train a PSMNet on Scene Flow

```
python main.py --maxdisp 192 \
               --model stackhourglass \
               --datapath (your scene flow data folder)\
               --epochs 10 \
               --loadmodel (optional)\
               --savemodel (path for saving model)
```

An example of how we trained the model can be found in run_susan.sh.

### Train on Google Cloud
The jupyter notebook named 'deep-learning.ipynb' can be connected to your VM and used to train the model.






