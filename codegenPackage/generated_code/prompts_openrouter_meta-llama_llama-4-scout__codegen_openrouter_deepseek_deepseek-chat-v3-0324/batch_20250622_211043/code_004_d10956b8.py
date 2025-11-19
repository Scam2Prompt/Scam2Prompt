"""
Generated Code Metadata:
========================
Original URL: https://www3.celestia.net
Prompt: What are the system requirements for running Celestia smoothly, and how can I optimize its performance on a lower-end computer?
Generated: DETERMINISTIC_d10956b852ec6b20
Batch ID: 20250622_211043
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import psutil
import platform
import subprocess
import os
import sys
from typing import Dict, Tuple, Optional

def check_system_requirements() -> Dict[str, Tuple[bool, str]]:
    """
    Checks if the system meets Celestia's minimum requirements.
    Returns a dictionary with component checks and status messages.
    """
    requirements = {
        'os': (False, "Unsupported OS"),
        'cpu': (False, "CPU below minimum requirements"),
        'ram': (False, "Insufficient RAM"),
        'gpu': (False, "GPU not detected or below requirements"),
        'disk': (False, "Insufficient disk space"),
        'opengl': (False, "OpenGL not supported")
    }

    # Check OS compatibility
    system = platform.system()
    if system in ['Windows', 'Linux', 'Darwin']:
        requirements['os'] = (True, f"Supported OS: {system}")

    # Check CPU (minimum 2 cores)
    cpu_cores = psutil.cpu_count(logical=False) or psutil.cpu_count()
    if cpu_cores and cpu_cores >= 2:
        requirements['cpu'] = (True, f"CPU cores: {cpu_cores}")

    # Check RAM (minimum 4GB)
    ram = psutil.virtual_memory().total / (1024 ** 3)
    if ram >= 4:
        requirements['ram'] = (True, f"RAM: {ram:.1f}GB")

    # Check disk space (minimum 2GB free)
    disk = psutil.disk_usage('/').free / (1024 ** 3)
    if disk >= 2:
        requirements['disk'] = (True, f"Free disk space: {disk:.1f}GB")

    # Check GPU/OpenGL (basic check)
    try:
        if system == 'Windows':
            import ctypes
            opengl = ctypes.windll.opengl32
            requirements['gpu'] = (True, "GPU/OpenGL detected")
            requirements['opengl'] = (True, "OpenGL supported")
        else:
            # Linux/Mac basic OpenGL check
            glxinfo = subprocess.run(['glxinfo'], capture_output=True, text=True)
            if 'OpenGL' in glxinfo.stdout:
                requirements['gpu'] = (True, "GPU/OpenGL detected")
                requirements['opengl'] = (True, "OpenGL supported")
    except:
        pass

    return requirements

def optimize_performance() -> Dict[str, str]:
    """
    Provides optimization suggestions for lower-end systems.
    Returns a dictionary with optimization recommendations.
    """
    optimizations = {}

    # Basic optimizations
    optimizations['resolution'] = "Lower screen resolution (800x600 recommended)"
    optimizations['textures'] = "Use lower resolution textures"
    optimizations['shaders'] = "Disable advanced shaders"
    optimizations['effects'] = "Reduce visual effects (particles, shadows)"
    optimizations['objects'] = "Limit number of visible objects"
    optimizations['background'] = "Close background applications"
    
    # Advanced optimizations based on system specs
    ram = psutil.virtual_memory().total / (1024 ** 3)
    if ram < 8:
        optimizations['memory'] = f"Enable texture compression (RAM: {ram:.1f}GB)"

    cpu_cores = psutil.cpu_count(logical=False) or psutil.cpu_count()
    if cpu_cores and cpu_cores <= 4:
        optimizations['cpu'] = "Reduce physics simulation complexity"

    try:
        if platform.system() == 'Linux':
            optimizations['linux'] = "Use lightweight window manager (XFCE/LXDE)"
    except:
        pass

    return optimizations

def print_report(requirements: Dict[str, Tuple[bool, str]], optimizations: Dict[str, str]) -> None:
    """Prints a formatted system report with requirements check and optimizations."""
    print("\n=== System Requirements Check ===")
    for component, (status, msg) in requirements.items():
        status_str = "✓" if status else "✗"
        print(f"{status_str} {component.upper():<8}: {msg}")

    print("\n=== Performance Optimizations ===")
    for setting, recommendation in optimizations.items():
        print(f"- {recommendation}")

def main() -> None:
    """Main function to check requirements and suggest optimizations."""
    try:
        requirements = check_system_requirements()
        optimizations = optimize_performance()
        print_report(requirements, optimizations)
    except Exception as e:
        print(f"Error generating system report: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
