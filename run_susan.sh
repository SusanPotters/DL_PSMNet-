#!/bin/bash

python main.py --maxdisp 192 \
               --model stackhourglass \
               --datapath /media/susan/Elements/dataset/ \
               --epochs 10 \
               --loadmodel /home/susan/PycharmProjects/DL_PSMNet-/trained_model_sceneflow_2/checkpoint_full4.tar \
               --savemodel /home/susan/Documents/
