#!/bin/sh

python train.py \
  --checkpoint_path -DEV/pretrained/bvae_tts_300k.pt \
  --gpu 0 \
  --logdir -DEV/checkpoints/TITML-IDN-F01-A1/logs
