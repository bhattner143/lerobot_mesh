#!/bin/bash

# Automatically detect the number of GPUs
NUM_GPUS=$(nvidia-smi --query-gpu=name --format=csv,noheader | wc -l)

# Get the number of physical CPU cores
NUM_CPUS=$(lscpu | awk '/^CPU\(s\):/ {print $2}')

# Get the number of physical CPU cores
NUM_USED=4

# Set OMP_NUM_THREADS (adjust based on your system)
export OMP_NUM_THREADS=16

# Training script parameters
MODULE="scripts.train_dips_v2_multi_gpu"  # Change this to your training module
ARGS="--dataset.root=/home/dips/Documents/datasets_lerobot/so100_test_2025_05_15 \
    --policy.type=diffusion \
    --dataset.repo_id=datasets_lerobot/so100_test_2025_05_15 \
    --output_dir=/home/dips/Documents/datasets_lerobot/so100_test_2025_05_15/outputs/train/diffusion_so100 \
    --wandb.enable=false \
    --save_config_train=True"

# Print system info
echo "Detected $NUM_GPUS GPUs and $NUM_CPUS CPU cores."
echo "Setting OMP_NUM_THREADS=$OMP_NUM_THREADS per process."
echo "Used $NUM_USED GPUs for training."
echo "Starting distributed training..."

# Run PyTorch Distributed Data Parallel (DDP) with torchrun
torchrun --nproc_per_node=$NUM_USED -m $MODULE $ARGS