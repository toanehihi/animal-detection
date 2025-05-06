import torch
print(torch.cuda.device_count())  # Check number of GPUs available
print(torch.cuda.get_device_name)  # Check if CUDA is available