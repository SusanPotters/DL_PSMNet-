#!/bin/bash

python main.py --maxdisp 192 \
               --model stackhourglass \
               --datapath /media/susan/Elements/dataset/ \
               --epochs 10 \
               --loadmodel /home/susan/PycharmProjects/DL_PSMNet-/PSMNet-master/trained_models/pretrained_sceneflow.tar \
               --savemodel /home/susan/Documents/
