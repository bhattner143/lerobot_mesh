# Use Ubuntu as the base image
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && \
    apt-get install -y wget bzip2 ca-certificates git python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Miniconda
ENV CONDA_DIR=/opt/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh && \
    bash /tmp/miniconda.sh -b -p $CONDA_DIR && \
    rm /tmp/miniconda.sh
ENV PATH=$CONDA_DIR/bin:$PATH

# Create conda environment and install Python 3.10
RUN conda create -y -n lerobot_mesh python=3.10

# Activate conda environment and install PyTorch + extras
SHELL ["bash", "-c"]
RUN source activate lerobot_mesh && \
    pip install torch==2.6.0 torchvision==0.21.0 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cu124 && \
    pip install torch-scatter && \
    pip install "git+https://github.com/facebookresearch/pytorch3d.git" && \
    pip install opencv-python matplotlib tqdm draccus termcolor datasets jsonlines safetensors imageio "einops>=0.8.0" && \
    pip install bpy

# Set the working directory
WORKDIR /workspace

# Activate the environment by default
ENV CONDA_DEFAULT_ENV=lerobot_mesh
ENV PATH=$CONDA_DIR/envs/lerobot_mesh/bin:$PATH

CMD ["bash"]