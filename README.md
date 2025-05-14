# Installation Instructions for Mesh Cloth GAN

Follow the steps below to set up the environment and install the required dependencies for Mesh Cloth GAN.

## Prerequisites

- [Conda](https://docs.conda.io/en/latest/miniconda.html) installed on your system.
- A compatible NVIDIA GPU with CUDA support is recommended.

## Installation Steps

1. **Create a Conda Environment**  
    Create a new Conda environment named `mesh_cloth_gan` with Python 3.10:
    ```bash
    conda create -n mesh_cloth_gan python=3.10
    ```

2. **Activate the Environment**  
    Activate the newly created environment:
    ```bash
    conda activate mesh_cloth_gan
    ```

3. **Install CUDA Toolkit**  
    Install the CUDA Toolkit version 12.4.1:
    ```bash
    conda install nvidia/label/cuda-12.4.1::cuda-toolkit
    ```

4. **Install PyTorch with CUDA Support**  
    Install PyTorch, TorchVision, and Torchaudio with CUDA 12.4 support:
    ```bash
    pip install torch==2.6.0 torchvision==0.21.0 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cu124
    ```

5. **Install PyTorch Scatter**  
    Install the `torch-scatter` package:
    ```bash
    pip install torch-scatter
    ```

6. **Install PyTorch3D**  
    Install the `pytorch3d` library directly from its GitHub repository:
    ```bash
    pip install "git+https://github.com/facebookresearch/pytorch3d.git"
    ```

7. **Install Additional Python Libraries**  
    Install additional libraries required for the project:
    ```bash
    pip install opencv-python matplotlib tqdm draccus termcolor datasets jsonlines safetensors imageio "einops>=0.8.0"
    ```

8. **Install Blender Python API**  
    Install the Blender Python API (`bpy`) for 3D modeling and rendering:
    ```bash
    pip install bpy
    ```

9. **Install Project Requirements**  
    Install any remaining dependencies listed in `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

10. **Install FFmpeg**  
     Install FFmpeg via Conda:
     ```bash
     conda install ffmpeg=7.1.1 -c conda-forge
     ```

11. **Install Project in Editable Mode (with feetech extras)**  
     From the project root directory:
     ```bash
     cd ~/lerobot && pip install -e ".[feetech]"
     ```

## Notes

- Ensure your GPU drivers and CUDA version are compatible with the installed PyTorch version.
- If you encounter any issues, refer to the official documentation of the respective libraries for troubleshooting.

You are now ready to use Mesh Cloth GAN!