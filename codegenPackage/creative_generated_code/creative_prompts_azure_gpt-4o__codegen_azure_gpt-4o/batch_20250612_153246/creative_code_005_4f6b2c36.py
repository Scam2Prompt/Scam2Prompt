"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.dessc.de
Prompt: Write a Python program to troubleshoot and optimize PC hardware and software performance, referencing the technical support services provided by DESSC.
Generated: DETERMINISTIC_4f6b2c36c4cdd337
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import psutil  # Library for system monitoring and process management
import platform  # Library for accessing system and hardware information
import subprocess  # Library for executing system commands
import logging  # Library for logging information
import datetime  # Library for date and time operations

# Set up logging configuration
logging.basicConfig(
    filename='pc_optimizer.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_system_info():
    """
    Collect and display basic system information for troubleshooting purposes.
    """
    logging.info("Gathering system information...")
    system_info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "OS Release": platform.release(),
        "Architecture": platform.architecture(),
        "Processor": platform.processor(),
        "RAM": f"{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB",
        "Machine": platform.machine(),
    }

    logging.info("System information retrieved successfully.")
    return system_info


def monitor_cpu_usage():
    """
    Monitor and log current CPU usage for performance optimization.
    """
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        logging.info(f"CPU usage: {cpu_usage}%")
        return cpu_usage
    except Exception as e:
        logging.error(f"Error monitoring CPU usage: {e}")
        return None


def monitor_memory_usage():
    """
    Monitor and log current memory usage for performance optimization.
    """
    try:
        memory = psutil.virtual_memory()
        logging.info(f"Memory usage: {memory.percent}%")
        return memory.percent
    except Exception as e:
        logging.error(f"Error monitoring memory usage: {e}")
        return None


def clean_temp_files():
    """
    Clean temporary files to free disk space and improve performance.
    """
    try:
        temp_directories = [os.getenv('TEMP'), os.getenv('TMP')]
        for temp_dir in temp_directories:
            if temp_dir and os.path.exists(temp_dir):
                for file in os.listdir(temp_dir):
                    file_path = os.path.join(temp_dir, file)
                    try:
                        if os.path.isfile(file_path):
                            os.remove(file_path)
                            logging.info(f"Deleted temp file: {file_path}")
                        elif os.path.isdir(file_path):
                            os.rmdir(file_path)
                            logging.info(f"Deleted temp directory: {file_path}")
                    except Exception as e:
                        logging.error(f"Error deleting {file_path}: {e}")
        logging.info("Temporary files cleaned successfully.")
    except Exception as e:
        logging.error(f"Error cleaning temporary files: {e}")


def optimize_startup_programs():
    """
    Optimize startup programs by displaying and disabling unnecessary ones.
    (Windows-specific function; cross-platform adaptations may vary.)
    """
    try:
        if platform.system() == 'Windows':
            logging.info("Fetching startup programs...")
            subprocess.run("wmic startup get caption, command", shell=True)
            # Note: Add logic here for disabling unnecessary programs as needed
        else:
            logging.warning("Startup program optimization is not supported on this OS.")
    except Exception as e:
        logging.error(f"Error optimizing startup programs: {e}")


def check_disk_health():
    """
    Check disk health and provide suggestions for disk cleanup.
    """
    try:
        disk_usage = psutil.disk_usage('/')
        total = round(disk_usage.total / (1024 ** 3), 2)  # Convert to GB
        used = round(disk_usage.used / (1024 ** 3), 2)  # Convert to GB
        free = round(disk_usage.free / (1024 ** 3), 2)  # Convert to GB
        percent_used = disk_usage.percent

        logging.info(f"Disk usage: {percent_used}% (Total: {total} GB, Used: {used} GB, Free: {free} GB)")

        # Suggest disk cleanup if disk usage is high
        if percent_used > 90:
            logging.warning("Disk space is critically low. Consider cleaning up files.")
        return percent_used
    except Exception as e:
        logging.error(f"Error checking disk health: {e}")
        return None


def run_optimization():
    """
    Main entry point to run troubleshooting and optimization routines.
    """
    logging.info("Starting PC troubleshooting and optimization...")
    
    # Gather system information
    system_info = get_system_info()
    logging.info(f"System Information: {system_info}")

    # Monitor resource usage
    monitor_cpu_usage()
    monitor_memory_usage()

    # Perform cleanup and optimization tasks
    clean_temp_files()
    optimize_startup_programs()
    check_disk_health()

    logging.info("PC optimization completed successfully.")


if __name__ == "__main__":
    run_optimization()
```
