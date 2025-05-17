def check_versions():
    print("\n🔍 Checking library versions:\n")

    # NumPy
    try:
        import numpy as np
        print(f"✅ numpy: {np.__version__}")
    except ImportError:
        print("❌ numpy not installed")

    # OpenCV
    try:
        import cv2
        print(f"✅ opencv-python: {cv2.__version__}")
    except ImportError:
        print("❌ opencv-python not installed")

    # Torch
    try:
        import torch
        print(f"✅ torch: {torch.__version__}")
        print(f"   - CUDA available: {torch.cuda.is_available()}")
        print(f"   - CUDA version: {torch.version.cuda}")
        print(f"   - cuDNN version: {torch.backends.cudnn.version()}")
        if torch.cuda.is_available():
            print(f"   - Device count: {torch.cuda.device_count()}")
            print(f"   - Current device: {torch.cuda.current_device()} ({torch.cuda.get_device_name(torch.cuda.current_device())})")
    except ImportError:
        print("❌ torch not installed")

    # TorchVision
    try:
        import torchvision
        print(f"✅ torchvision: {torchvision.__version__}")
    except ImportError:
        print("❌ torchvision not installed")

    # Torch-Scatter
    try:
        import torch_scatter
        print(f"✅ torch-scatter: {torch_scatter.__version__}")
    except ImportError:
        print("❌ torch-scatter not installed")
    
    # TorchAudio
    try:
        import torchaudio
        print(f"✅ torchaudio: {torchaudio.__version__}")
    except ImportError:
        print("❌ torchaudio not installed")

    # PyTorch3D
    try:
        import pytorch3d

        print(f"✅ pytorch3d: {pytorch3d.__version__}")
    except ImportError:
        print("❌ pytorch3d not installed")

    # FFmpeg
    try:
        import subprocess
        result = subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True)
        if result.returncode == 0:
            first_line = result.stdout.splitlines()[0]
            print(f"✅ ffmpeg: {first_line}, ✅ required by torchcodec")
        else:
            print("❌ ffmpeg not found or failed to run, ⚠️required by torchcodec")
    except Exception as e:
        print(f"❌ ffmpeg check failed: {e}, ⚠️required by torchcodec")

    # Check for libnpp and libnvrtc CUDA libraries

    try:
        import ctypes.util
        npp = ctypes.util.find_library("nppc")
        nvrtc = ctypes.util.find_library("nvrtc")
        if npp:
            print(f"✅ libnpp found: {npp}, ✅required by torchcodec")
        else:
            print("❌ libnpp not found, ⚠️required by torchcodec")
        if nvrtc:
            print(f"✅ libnvrtc found: {nvrtc}, ✅required by torchcodec")
        else:
            print("❌ libnvrtc not found, ⚠️required by torchcodec")
    except Exception as e:
        print(f"❌ Error checking CUDA libraries: {e}")
 
    # ffmpeg -decoders | grep -i nvidia
    # To check that FFmpeg libraries work with NVDEC correctly you can decode a sample video:
    # ffmpeg -hwaccel cuda -hwaccel_output_format cuda -i /home/dips/Documents/datasets_lerobot/so100_test_2025_05_15/videos/chunk-000/observation.images.rgb_intel_real_sense/episode_000000.mp4 -f null -
        
    # import torchcodec
    # from torchcodec.decoders import VideoDecoder
    try:
        import torchcodec
        print(f"✅ torchcodec: {torchcodec.__version__}")
    except ImportError:
        print("❌ torchcodec not installed")

    

if __name__ == "__main__":
    check_versions()