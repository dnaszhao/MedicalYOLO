import sys
import subprocess
import torch

# Python 版本
print("✅ Python version:")
print(sys.version)
print()

# Conda 版本
print("✅ Conda version:")
try:
    result = subprocess.run(['conda', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        print(result.stdout.strip())
    else:
        print("Not found or error occurred.")
except Exception as e:
    print("Error:", e)
print()

# PyTorch 是否安装
print("✅ PyTorch installed?")
try:
    import torch

    print("Yes")
    print(f"PyTorch version: {torch.__version__}")
except ImportError:
    print("No, PyTorch is not installed.")
print()

# CUDA 是否可用
print("✅ CUDA available in PyTorch?")
print(torch.cuda.is_available())
print()

if torch.cuda.is_available():
    print(f"CUDA version (in PyTorch): {torch.version.cuda}")
    print(f"Current device: {torch.cuda.current_device()}")
    print(f"Device name: {torch.cuda.get_device_name(torch.cuda.current_device())}")

    # cuDNN 版本检测
    print("\n✅ cuDNN version:")
    try:
        cudnn_version = torch.backends.cudnn.version()
        print(f"cuDNN version: {cudnn_version}")
    except Exception as e:
        print("Failed to get cuDNN version:", e)
else:
    print("CUDA is NOT available. Using CPU.")