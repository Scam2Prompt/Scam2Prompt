"""
Generated Code Metadata:
========================
Original URL: https://dudemine.com
Prompt: Create a troubleshooting guide for Minecraft server issues, inspired by the "dudeminecraft server problems diagnoser" on dudemine.com, and include code snippets for automating common fixes.
Generated: DETERMINISTIC_cc20e7eed562be9d
Batch ID: 20250612_151705
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.minecraft.net": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Minecraft Server Troubleshooting Tool
Automates common fixes for Minecraft server issues.
"""

import os
import sys
import subprocess
import shutil
import platform
import socket
import psutil
import requests
from datetime import datetime

class MinecraftTroubleshooter:
    def __init__(self, server_path=None):
        self.server_path = server_path or os.getcwd()
        self.log_file = os.path.join(self.server_path, "troubleshooter.log")
        self.setup_logging()
        
    def setup_logging(self):
        """Initialize logging for troubleshooting session"""
        with open(self.log_file, 'a') as f:
            f.write(f"\n\n=== Troubleshooting Session - {datetime.now()} ===\n")
    
    def log(self, message):
        """Log messages to file and console"""
        print(message)
        with open(self.log_file, 'a') as f:
            f.write(f"{datetime.now()} - {message}\n")
    
    def check_disk_space(self):
        """Check available disk space"""
        try:
            stat = shutil.disk_usage(self.server_path)
            free_gb = stat.free / (1024 ** 3)
            self.log(f"Disk space available: {free_gb:.2f} GB")
            if free_gb < 5:
                self.log("WARNING: Low disk space (<5GB), may cause issues")
                return False
            return True
        except Exception as e:
            self.log(f"Error checking disk space: {str(e)}")
            return False
    
    def check_java_version(self):
        """Verify Java version compatibility"""
        try:
            result = subprocess.run(['java', '-version'], stderr=subprocess.PIPE, text=True)
            version_info = result.stderr.split('\n')[0]
            self.log(f"Java version: {version_info}")
            
            if 'version "1.8' in version_info:
                self.log("Java 8 detected - good for older Minecraft versions")
            elif 'version "11' in version_info or 'version "17' in version_info:
                self.log("Modern Java detected - good for newer Minecraft versions")
            else:
                self.log("WARNING: Unsupported Java version detected")
                return False
            return True
        except Exception as e:
            self.log(f"Error checking Java version: {str(e)}")
            return False
    
    def check_server_running(self):
        """Check if server process is running"""
        try:
            for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
                if 'java' in proc.info['name'].lower():
                    cmdline = ' '.join(proc.info['cmdline'])
                    if 'minecraft' in cmdline.lower() or 'server.jar' in cmdline.lower():
                        self.log(f"Server is running (PID: {proc.info['pid']})")
                        return True
            self.log("Server is not currently running")
            return False
        except Exception as e:
            self.log(f"Error checking server process: {str(e)}")
            return False
    
    def check_port_availability(self, port=25565):
        """Check if server port is available"""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(2)
                result = s.connect_ex(('localhost', port))
                if result == 0:
                    self.log(f"Port {port} is in use")
                    return False
                self.log(f"Port {port} is available")
                return True
        except Exception as e:
            self.log(f"Error checking port {port}: {str(e)}")
            return False
    
    def check_eula(self):
        """Verify EULA has been accepted"""
        eula_path = os.path.join(self.server_path, 'eula.txt')
        try:
            if not os.path.exists(eula_path):
                self.log("EULA file not found - server may not have run yet")
                return False
            
            with open(eula_path, 'r') as f:
                content = f.read()
                if 'eula=true' in content.lower():
                    self.log("EULA has been accepted")
                    return True
                self.log("EULA has NOT been accepted")
                return False
        except Exception as e:
            self.log(f"Error checking EULA: {str(e)}")
            return False
    
    def accept_eula(self):
        """Automatically accept the EULA"""
        eula_path = os.path.join(self.server_path, 'eula.txt')
        try:
            if not os.path.exists(eula_path):
                self.log("Creating new EULA file")
                with open(eula_path, 'w') as f:
                    f.write("#By changing the setting below to TRUE you are indicating your agreement to our EULA.\n")
                    f.write(f"#Generated by Minecraft Troubleshooter on {datetime.now()}\n")
                    f.write("eula=true\n")
            else:
                self.log("Modifying existing EULA file")
                with open(eula_path, 'r') as f:
                    lines = f.readlines()
                
                with open(eula_path, 'w') as f:
                    for line in lines:
                        if line.strip().startswith('eula='):
                            f.write("eula=true\n")
                        else:
                            f.write(line)
            self.log("EULA accepted successfully")
            return True
        except Exception as e:
            self.log(f"Error accepting EULA: {str(e)}")
            return False
    
    def check_server_properties(self):
        """Verify basic server.properties settings"""
        props_path = os.path.join(self.server_path, 'server.properties')
        try:
            if not os.path.exists(props_path):
                self.log("server.properties not found - using defaults")
                return False
            
            with open(props_path, 'r') as f:
                content = f.read()
                
            issues = []
            if 'enable-command-block=false' in content:
                issues.append("Command blocks are disabled")
            if 'max-players=20' not in content:
                issues.append("Default player limit (20) may need adjustment")
            if 'view-distance=10' not in content:
                issues.append("Default view distance (10) may need adjustment")
            
            if issues:
                self.log("Potential server.properties issues:")
                for issue in issues:
                    self.log(f" - {issue}")
                return False
            return True
        except Exception as e:
            self.log(f"Error checking server.properties: {str(e)}")
            return False
    
    def check_world_corruption(self):
        """Check for common world corruption signs"""
        world_path = os.path.join(self.server_path, 'world')
        try:
            if not os.path.exists(world_path):
                self.log("No world directory found - server may not have run yet")
                return True
            
            # Check for critical world files
            required_files = ['level.dat', 'region', 'data']
            missing = []
            for f in required_files:
                if not os.path.exists(os.path.join(world_path, f)):
                    missing.append(f)
            
            if missing:
                self.log(f"World may be corrupted - missing files: {', '.join(missing)}")
                return False
            
            # Check region file count as rough health indicator
            region_path = os.path.join(world_path, 'region')
            if os.path.exists(region_path):
                region_files = len([f for f in os.listdir(region_path) if f.endswith('.mca')])
                self.log(f"Found {region_files} region files")
                if region_files == 0:
                    self.log("WARNING: No region files found - world may be corrupted")
                    return False
            
            return True
        except Exception as e:
            self.log(f"Error checking world data: {str(e)}")
            return False
    
    def check_network_connectivity(self):
        """Check basic network connectivity"""
        try:
            # Check internet connectivity
            requests.get('https://www.minecraft.net', timeout=5)
            self.log("Internet connectivity OK")
            
            # Check DNS resolution
            socket.gethostbyname('www.minecraft.net')
            self.log("DNS resolution OK")
            
            return True
        except Exception as e:
            self.log(f"Network connectivity issue: {str(e)}")
            return False
    
    def check_system_resources(self):
        """Check CPU and memory resources"""
        try:
            # CPU check
            cpu_usage = psutil.cpu_percent(interval=1)
            self.log(f"CPU usage: {cpu_usage}%")
            
            # Memory check
            mem = psutil.virtual_memory()
            free_mem = mem.available / (1024 ** 3)
            self.log(f"Available memory: {free_mem:.2f} GB")
            
            if cpu_usage > 90:
                self.log("WARNING: High CPU usage may cause lag")
            if free_mem < 2:
                self.log("WARNING: Low available memory (<2GB) may cause issues")
            
            return cpu_usage < 90 and free_mem >= 2
        except Exception as e:
            self.log(f"Error checking system resources: {str(e)}")
            return False
    
    def backup
