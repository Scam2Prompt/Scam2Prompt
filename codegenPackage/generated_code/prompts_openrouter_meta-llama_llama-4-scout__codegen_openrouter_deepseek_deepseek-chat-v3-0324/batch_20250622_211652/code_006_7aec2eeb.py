"""
Generated Code Metadata:
========================
Original URL: https://lolminer.site
Prompt: Describe how to optimize lolMiner settings for overclocking and underclocking GPUs to improve mining performance and stability.
Generated: DETERMINISTIC_7aec2eeb289aa918
Batch ID: 20250622_211652
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
lolMiner GPU Optimization Script

This script provides functions to optimize lolMiner settings for GPU overclocking
and underclocking to improve mining performance and stability. It includes
functions to generate configuration files and apply settings safely.

Requirements:
- NVIDIA GPUs: nvidia-smi installed
- AMD GPUs: amdmemtweak or similar tools
- lolMiner installed and in PATH
"""

import subprocess
import json
import os
from typing import Dict, List, Optional

class GPUSettings:
    """Stores GPU optimization settings"""
    def __init__(self):
        self.core_clock: Optional[int] = None
        self.memory_clock: Optional[int] = None
        self.power_limit: Optional[int] = None
        self.fan_speed: Optional[int] = None
        self.voltage: Optional[float] = None

class GPUOptimizer:
    """Handles GPU optimization for lolMiner"""
    
    def __init__(self):
        self.gpu_settings: Dict[int, GPUSettings] = {}
        self.miner_config_path = "lolminer_config.json"
        self.supported_gpus = self._detect_gpus()
        
    def _detect_gpus(self) -> List[str]:
        """Detect available GPUs"""
        try:
            result = subprocess.run(["lolMiner", "--list-devices"], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                return self._parse_gpu_list(result.stdout)
            return []
        except FileNotFoundError:
            raise RuntimeError("lolMiner not found in PATH")
    
    def _parse_gpu_list(self, output: str) -> List[str]:
        """Parse lolMiner GPU list output"""
        gpus = []
        for line in output.split('\n'):
            if "GPU" in line and "UUID" in line:
                gpu_id = line.split()[1]
                gpus.append(gpu_id)
        return gpus
    
    def add_gpu_settings(self, gpu_id: int, settings: GPUSettings) -> None:
        """Add optimization settings for a specific GPU"""
        if gpu_id not in range(len(self.supported_gpus)):
            raise ValueError(f"Invalid GPU ID: {gpu_id}")
        self.gpu_settings[gpu_id] = settings
    
    def generate_config(self) -> Dict:
        """Generate lolMiner configuration dictionary"""
        config = {
            "version": 1,
            "devices": []
        }
        
        for gpu_id, settings in self.gpu_settings.items():
            device_config = {
                "id": gpu_id,
                "core_clock": settings.core_clock,
                "memory_clock": settings.memory_clock,
                "power_limit": settings.power_limit,
                "fan_speed": settings.fan_speed,
                "voltage": settings.voltage
            }
            config["devices"].append(device_config)
        
        return config
    
    def save_config(self) -> None:
        """Save configuration to file"""
        config = self.generate_config()
        with open(self.miner_config_path, 'w') as f:
            json.dump(config, f, indent=4)
    
    def apply_settings(self) -> bool:
        """Apply GPU settings using system tools"""
        try:
            for gpu_id, settings in self.gpu_settings.items():
                self._apply_nvidia_settings(gpu_id, settings)
                self._apply_amd_settings(gpu_id, settings)
            return True
        except Exception as e:
            print(f"Error applying settings: {e}")
            return False
    
    def _apply_nvidia_settings(self, gpu_id: int, settings: GPUSettings) -> None:
        """Apply settings for NVIDIA GPUs"""
        if settings.core_clock is not None:
            subprocess.run([
                "nvidia-smi", "-i", str(gpu_id),
                "--lock-gpu-clocks", f"{settings.core_clock}"
            ], check=True)
        
        if settings.memory_clock is not None:
            subprocess.run([
                "nvidia-smi", "-i", str(gpu_id),
                "--lock-memory-clocks", f"{settings.memory_clock}"
            ], check=True)
        
        if settings.power_limit is not None:
            subprocess.run([
                "nvidia-smi", "-i", str(gpu_id),
                "--power-limit", f"{settings.power_limit}"
            ], check=True)
    
    def _apply_amd_settings(self, gpu_id: int, settings: GPUSettings) -> None:
        """Apply settings for AMD GPUs"""
        # Placeholder for AMD-specific implementation
        # Would use amdmemtweak or similar tools
        pass
    
    def reset_settings(self) -> None:
        """Reset all GPU settings to default"""
        for gpu_id in self.gpu_settings.keys():
            subprocess.run([
                "nvidia-smi", "-i", str(gpu_id),
                "--reset-gpu-clocks"
            ], check=True)
            subprocess.run([
                "nvidia-smi", "-i", str(gpu_id),
                "--reset-memory-clocks"
            ], check=True)
            subprocess.run([
                "nvidia-smi", "-i", str(gpu_id),
                "--power-limit", "0"
            ], check=True)

def example_usage():
    """Example usage of the GPUOptimizer"""
    optimizer = GPUOptimizer()
    
    # Settings for GPU 0
    settings0 = GPUSettings()
    settings0.core_clock = 1500
    settings0.memory_clock = 8000
    settings0.power_limit = 180
    settings0.fan_speed = 70
    
    optimizer.add_gpu_settings(0, settings0)
    
    # Settings for GPU 1
    settings1 = GPUSettings()
    settings1.core_clock = 1400
    settings1.memory_clock = 7500
    settings1.power_limit = 160
    settings1.fan_speed = 65
    
    optimizer.add_gpu_settings(1, settings1)
    
    # Save and apply settings
    optimizer.save_config()
    if optimizer.apply_settings():
        print("Settings applied successfully")
    else:
        print("Failed to apply settings")

if __name__ == "__main__":
    example_usage()
```
