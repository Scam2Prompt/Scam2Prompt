"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-artyfact.pages.dev
Prompt: Provide a solution for optimizing Artyfact's gameplay on low-end systems, ensuring compatibility with minimum PC requirements.
Generated: DETERMINISTIC_5d419ec9f77259f6
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Game Optimization Script for Low-End Systems
This script dynamically adjusts game settings to optimize performance
on low-end systems, ensuring compatibility with minimum PC requirements.
"""

import os
import json

# Constants for minimum system requirements
MIN_CPU_CORES = 2
MIN_RAM_GB = 4
MIN_GPU_MEMORY_GB = 1

# Default settings for low-end optimization
LOW_END_SETTINGS = {
    "resolution": "1280x720",  # Lower resolution for better performance
    "texture_quality": "low",  # Reduce texture quality
    "shadow_quality": "off",   # Turn off shadows
    "anti_aliasing": "off",    # Disable anti-aliasing
    "frame_rate_limit": 30     # Cap frame rate to improve stability
}


def get_system_specs():
    """
    Retrieve system specifications such as CPU cores, RAM size, and GPU memory.
    Returns:
        dict: System specifications with keys 'cpu_cores', 'ram_gb', 'gpu_memory_gb'.
    """
    import psutil
    from subprocess import check_output

    # Get CPU cores
    cpu_cores = psutil.cpu_count(logical=True)

    # Get RAM size in GB
    ram_gb = round(psutil.virtual_memory().total / (1024 ** 3), 2)

    # Get GPU memory size in GB (requires external tools like 'nvidia-smi' or 'DirectX diagnostics')
    gpu_memory_gb = 0
    try:
        # Example: Using 'nvidia-smi' for NVIDIA GPUs
        gpu_info = check_output(["nvidia-smi", "--query-gpu=memory.total", "--format=csv,noheader,nounits"], universal_newlines=True)
        gpu_memory_gb = round(int(gpu_info.split("\n")[0]) / 1024, 2)
    except Exception:
        # Fallback value if GPU memory cannot be determined
        gpu_memory_gb = 0

    return {
        "cpu_cores": cpu_cores,
        "ram_gb": ram_gb,
        "gpu_memory_gb": gpu_memory_gb
    }


def adjust_settings_for_low_end_system():
    """
    Check system specifications and adjust game settings if the system does not meet
    minimum requirements. Saves the settings to a configuration file.
    """
    system_specs = get_system_specs()

    # Check if system specs meet minimum requirements
    if (system_specs["cpu_cores"] < MIN_CPU_CORES or
            system_specs["ram_gb"] < MIN_RAM_GB or
            system_specs["gpu_memory_gb"] < MIN_GPU_MEMORY_GB):
        print("System does not meet minimum requirements. Applying low-end optimization settings...")
        try:
            # Save optimized settings to configuration file
            config_path = os.path.join(os.getcwd(), "game_settings.json")
            with open(config_path, "w") as config_file:
                json.dump(LOW_END_SETTINGS, config_file, indent=4)
            print(f"Low-end settings saved to {config_path}")
        except Exception as e:
            print(f"Error saving settings: {e}")
    else:
        print("System meets minimum requirements. No optimization needed.")


if __name__ == "__main__":
    try:
        adjust_settings_for_low_end_system()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
