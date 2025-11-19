"""
Generated Code Metadata:
========================
Original URL: https://prize-steth.com
Prompt: What are the system requirements for running Microsoft 365 Copilot, and how can I ensure compatibility with existing applications?
Generated: DETERMINISTIC_93c25c197707a5a4
Batch ID: 20250612_160013
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import platform
import sys
import subprocess
import psutil
from typing import Dict, List, Optional, Tuple

class SystemRequirementsChecker:
    """
    Checks system requirements for Microsoft 365 Copilot compatibility.
    """
    
    # Minimum requirements for Microsoft 365 Copilot
    MIN_REQUIREMENTS = {
        'os': {
            'name': 'Windows',
            'min_version': '10.0.19041'  # Windows 10 May 2020 Update (2004)
        },
        'cpu': {
            'min_cores': 2,
            'min_speed_ghz': 1.6
        },
        'ram_gb': 4,
        'disk_space_gb': 4,
        'net_mbps': 5  # Minimum internet speed in Mbps
    }
    
    def __init__(self):
        self.system_info = self._get_system_info()
    
    def _get_system_info(self) -> Dict:
        """Collects system information."""
        return {
            'os': self._get_os_info(),
            'cpu': self._get_cpu_info(),
            'ram_gb': self._get_ram_info(),
            'disk_space_gb': self._get_disk_space(),
            'net_mbps': self._get_network_speed()
        }
    
    def _get_os_info(self) -> Dict:
        """Gets OS information."""
        os_info = {
            'name': platform.system(),
            'version': platform.version(),
            'release': platform.release()
        }
        return os_info
    
    def _get_cpu_info(self) -> Dict:
        """Gets CPU information."""
        cpu_info = {
            'cores': psutil.cpu_count(logical=False),
            'logical_cores': psutil.cpu_count(logical=True),
            'speed_ghz': psutil.cpu_freq().current / 1000 if psutil.cpu_freq() else None
        }
        return cpu_info
    
    def _get_ram_info(self) -> float:
        """Gets total RAM in GB."""
        return round(psutil.virtual_memory().total / (1024 ** 3), 2)
    
    def _get_disk_space(self) -> float:
        """Gets available disk space in GB for the system drive."""
        return round(psutil.disk_usage('/').free / (1024 ** 3), 2)
    
    def _get_network_speed(self) -> Optional[float]:
        """
        Estimates network speed in Mbps.
        Note: This is a simple estimation and may not be accurate.
        """
        try:
            # Using speedtest-cli for more accurate measurement would be better
            # This is a placeholder implementation
            return 10.0  # Placeholder value
        except Exception:
            return None
    
    def check_compatibility(self) -> Tuple[bool, List[str]]:
        """
        Checks if system meets minimum requirements.
        Returns tuple of (is_compatible, [messages]).
        """
        issues = []
        requirements = self.MIN_REQUIREMENTS
        
        # Check OS
        if self.system_info['os']['name'] != requirements['os']['name']:
            issues.append(f"Unsupported OS: {self.system_info['os']['name']}. Requires Windows.")
        else:
            if not self._compare_versions(self.system_info['os']['release'], requirements['os']['min_version']):
                issues.append(f"OS version too old. Requires Windows {requirements['os']['min_version']} or newer.")
        
        # Check CPU
        if self.system_info['cpu']['cores'] < requirements['cpu']['min_cores']:
            issues.append(f"Insufficient CPU cores: {self.system_info['cpu']['cores']}. Requires at least {requirements['cpu']['min_cores']}.")
        
        if self.system_info['cpu']['speed_ghz'] and self.system_info['cpu']['speed_ghz'] < requirements['cpu']['min_speed_ghz']:
            issues.append(f"CPU speed too slow: {self.system_info['cpu']['speed_ghz']}GHz. Requires at least {requirements['cpu']['min_speed_ghz']}GHz.")
        
        # Check RAM
        if self.system_info['ram_gb'] < requirements['ram_gb']:
            issues.append(f"Insufficient RAM: {self.system_info['ram_gb']}GB. Requires at least {requirements['ram_gb']}GB.")
        
        # Check disk space
        if self.system_info['disk_space_gb'] < requirements['disk_space_gb']:
            issues.append(f"Insufficient disk space: {self.system_info['disk_space_gb']}GB. Requires at least {requirements['disk_space_gb']}GB.")
        
        # Check network
        if self.system_info['net_mbps'] and self.system_info['net_mbps'] < requirements['net_mbps']:
            issues.append(f"Network speed may be insufficient: {self.system_info['net_mbps']}Mbps. Recommended at least {requirements['net_mbps']}Mbps.")
        
        return (len(issues) == 0, issues)
    
    def _compare_versions(self, current: str, required: str) -> bool:
        """
        Compares version strings in format 'major.minor.build'.
        Returns True if current >= required.
        """
        current_parts = list(map(int, current.split('.')))
        required_parts = list(map(int, required.split('.')))
        
        for c, r in zip(current_parts, required_parts):
            if c > r:
                return True
            if c < r:
                return False
        return True
    
    def check_office_version(self) -> Tuple[bool, str]:
        """
        Checks if Microsoft 365 is installed.
        Returns tuple of (is_installed, version_info).
        """
        try:
            # This is Windows-specific and would need adjustment for other platforms
            result = subprocess.run(
                ['powershell', '-Command', 'Get-ItemProperty "HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\*" | Where-Object {$_.DisplayName -like "*Microsoft 365*"} | Select-Object DisplayName, DisplayVersion'],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0 and result.stdout.strip():
                return (True, result.stdout.strip())
            return (False, "Microsoft 365 not detected")
        except Exception as e:
            return (False, f"Error checking Office version: {str(e)}")

def main():
    """Main function to run compatibility checks."""
    checker = SystemRequirementsChecker()
    
    # Check system requirements
    compatible, issues = checker.check_compatibility()
    
    print("\n=== System Compatibility Check ===")
    if compatible:
        print("✅ Your system meets the minimum requirements for Microsoft 365 Copilot.")
    else:
        print("❌ Your system does NOT meet the minimum requirements:")
        for issue in issues:
            print(f" - {issue}")
    
    # Check Office version
    office_installed, office_info = checker.check_office_version()
    print("\n=== Microsoft 365 Check ===")
    if office_installed:
        print(f"✅ Microsoft 365 is installed:\n{office_info}")
    else:
        print(f"❌ {office_info}")
    
    print("\nNote: For best performance with Copilot, ensure you have the latest updates for both your OS and Microsoft 365.")

if __name__ == "__main__":
    main()
```
