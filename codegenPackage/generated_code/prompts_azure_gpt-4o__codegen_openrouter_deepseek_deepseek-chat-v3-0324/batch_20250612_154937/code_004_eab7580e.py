"""
Generated Code Metadata:
========================
Original URL: https://marceldev.github.io
Prompt: Create a Python script that retrieves and displays kernel version information for use in a Discord Rich Presence integration, inspired by MarcelDev's project.
Generated: DETERMINISTIC_eab7580e31569cad
Batch ID: 20250612_154937
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import platform
import logging
from typing import Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('kernel_info.log'),
        logging.StreamHandler()
    ]
)

def get_kernel_info() -> Dict[str, Any]:
    """
    Retrieves detailed kernel version information from the system.
    
    Returns:
        Dict[str, Any]: A dictionary containing kernel information including:
            - system: Operating system name
            - node: Network name
            - release: Kernel release version
            - version: Kernel version string
            - machine: Hardware identifier
            - processor: Processor information
            - full_info: Combined system information string
    """
    try:
        system_info = {
            'system': platform.system(),
            'node': platform.node(),
            'release': platform.release(),
            'version': platform.version(),
            'machine': platform.machine(),
            'processor': platform.processor(),
            'full_info': platform.platform()
        }
        logging.info("Successfully retrieved kernel information")
        return system_info
    except Exception as e:
        logging.error(f"Error retrieving kernel information: {str(e)}")
        raise

def format_kernel_info(kernel_info: Dict[str, Any]) -> str:
    """
    Formats kernel information into a human-readable string.
    
    Args:
        kernel_info (Dict[str, Any]): Kernel information dictionary from get_kernel_info()
    
    Returns:
        str: Formatted string with kernel information
    """
    try:
        formatted = (
            f"System: {kernel_info['system']}\n"
            f"Kernel Release: {kernel_info['release']}\n"
            f"Kernel Version: {kernel_info['version']}\n"
            f"Architecture: {kernel_info['machine']}\n"
            f"Processor: {kernel_info['processor']}\n"
            f"Full Info: {kernel_info['full_info']}"
        )
        return formatted
    except KeyError as e:
        logging.error(f"Missing expected kernel information field: {str(e)}")
        raise
    except Exception as e:
        logging.error(f"Error formatting kernel information: {str(e)}")
        raise

def main():
    """
    Main function to retrieve and display kernel information.
    """
    try:
        logging.info("Starting kernel information retrieval")
        kernel_info = get_kernel_info()
        formatted_info = format_kernel_info(kernel_info)
        print("\nKernel Information:")
        print("==================")
        print(formatted_info)
        logging.info("Kernel information displayed successfully")
    except Exception as e:
        logging.error(f"An error occurred in the main process: {str(e)}")

if __name__ == "__main__":
    main()
```
