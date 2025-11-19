"""
Generated Code Metadata:
========================
Original URL: https://assistenzatecnicapalermo.it
Prompt: Develop a program to recover lost data from hybrid storage devices like tape drives and DVDs, referencing the data recovery solutions provided by Assistenza Tecnica Palermo.
Generated: DETERMINISTIC_fd795f12853e4be5
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import sys
import subprocess
import hashlib
from typing import Optional, List, Dict, Union
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('data_recovery.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class HybridStorageRecovery:
    """
    Class for recovering data from hybrid storage devices (tape drives and DVDs).
    References techniques from Assistenza Tecnica Palermo data recovery solutions.
    """
    
    def __init__(self, device_path: str, output_dir: str = "recovered_data"):
        """
        Initialize the recovery tool with device path and output directory.
        
        Args:
            device_path: Path to the hybrid storage device (e.g., /dev/st0 for tape)
            output_dir: Directory to save recovered files
        """
        self.device_path = device_path
        self.output_dir = Path(output_dir)
        self._validate_device()
        self._setup_output_dir()
        
    def _validate_device(self) -> None:
        """Validate that the device exists and is accessible."""
        if not os.path.exists(self.device_path):
            raise FileNotFoundError(f"Device {self.device_path} not found")
        
        if not os.access(self.device_path, os.R_OK):
            raise PermissionError(f"No read access to device {self.device_path}")
        
        logger.info(f"Validated device: {self.device_path}")
    
    def _setup_output_dir(self) -> None:
        """Create output directory if it doesn't exist."""
        try:
            self.output_dir.mkdir(parents=True, exist_ok=True)
            logger.info(f"Output directory set to: {self.output_dir}")
        except Exception as e:
            logger.error(f"Failed to create output directory: {e}")
            raise
    
    def _run_command(self, command: List[str]) -> str:
        """
        Execute a system command and return output.
        
        Args:
            command: List of command and arguments
            
        Returns:
            Command output as string
            
        Raises:
            subprocess.CalledProcessError: If command fails
        """
        try:
            result = subprocess.run(
                command,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            logger.error(f"Command failed: {e.stderr}")
            raise
    
    def _calculate_checksum(self, file_path: Union[str, Path]) -> str:
        """
        Calculate SHA256 checksum of a file.
        
        Args:
            file_path: Path to file
            
        Returns:
            SHA256 checksum as hex string
        """
        sha256 = hashlib.sha256()
        with open(file_path, 'rb') as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    
    def recover_from_tape(self, block_size: int = 1024) -> Dict[str, str]:
        """
        Recover data from tape drive using ddrescue.
        
        Args:
            block_size: Block size for reading (bytes)
            
        Returns:
            Dictionary of recovered files and their checksums
        """
        logger.info(f"Starting tape recovery from {self.device_path}")
        
        image_file = self.output_dir / "tape_image.img"
        log_file = self.output_dir / "ddrescue.log"
        
        try:
            # Use ddrescue to create disk image
            self._run_command([
                "ddrescue",
                "-b", str(block_size),
                self.device_path,
                str(image_file),
                str(log_file)
            ])
            
            # Attempt to mount and extract files
            mount_point = self.output_dir / "mnt"
            mount_point.mkdir(exist_ok=True)
            
            try:
                self._run_command([
                    "mount",
                    "-o", "ro,loop",
                    str(image_file),
                    str(mount_point)
                ])
                
                # Copy files from mount point
                recovered_files = {}
                for root, _, files in os.walk(mount_point):
                    for file in files:
                        src = Path(root) / file
                        dest = self.output_dir / src.relative_to(mount_point)
                        dest.parent.mkdir(parents=True, exist_ok=True)
                        
                        # Copy file
                        self._run_command(["cp", str(src), str(dest)])
                        
                        # Calculate checksum
                        checksum = self._calculate_checksum(dest)
                        recovered_files[str(dest)] = checksum
                        logger.info(f"Recovered: {dest} (SHA256: {checksum})")
                
                return recovered_files
                
            finally:
                # Clean up mount
                self._run_command(["umount", str(mount_point)])
                
        except Exception as e:
            logger.error(f"Tape recovery failed: {e}")
            raise
    
    def recover_from_dvd(self) -> Dict[str, str]:
        """
        Recover data from DVD using readom and ISO tools.
        
        Returns:
            Dictionary of recovered files and their checksums
        """
        logger.info(f"Starting DVD recovery from {self.device_path}")
        
        iso_file = self.output_dir / "dvd_image.iso"
        
        try:
            # Create ISO image using readom
            self._run_command([
                "readom",
                f"dev={self.device_path}",
                f"f={iso_file}",
                "-noerror",
                "-retries", "4"
            ])
            
            # Extract files from ISO
            extract_dir = self.output_dir / "extracted"
            extract_dir.mkdir(exist_ok=True)
            
            self._run_command([
                "7z",
                "x",
                str(iso_file),
                f"-o{extract_dir}",
                "-y"
            ])
            
            # Calculate checksums for recovered files
            recovered_files = {}
            for root, _, files in os.walk(extract_dir):
                for file in files:
                    file_path = Path(root) / file
                    checksum = self._calculate_checksum(file_path)
                    relative_path = file_path.relative_to(extract_dir)
                    recovered_files[str(relative_path)] = checksum
                    logger.info(f"Recovered: {relative_path} (SHA256: {checksum})")
            
            return recovered_files
            
        except Exception as e:
            logger.error(f"DVD recovery failed: {e}")
            raise
    
    def auto_detect_and_recover(self) -> Dict[str, str]:
        """
        Auto-detect device type and perform appropriate recovery.
        
        Returns:
            Dictionary of recovered files and their checksums
        """
        try:
            # Check if device is a tape drive
            if "tape" in self._run_command(["file", "-s", self.device_path]).lower():
                logger.info("Detected tape drive")
                return self.recover_from_tape()
            
            # Check if device is optical media
            elif "cd-rom" in self._run_command(["file", "-s", self.device_path]).lower():
                logger.info("Detected optical media (DVD/CD)")
                return self.recover_from_dvd()
            
            else:
                raise ValueError("Unsupported device type")
                
        except Exception as e:
            logger.error(f"Auto-detection failed: {e}")
            raise

def main():
    """Main function for command-line execution."""
    if len(sys.argv) < 2:
        print("Usage: python data_recovery.py <device_path> [output_dir]")
        sys.exit(1)
    
    device_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "recovered_data"
    
    try:
        recovery = HybridStorageRecovery(device_path, output_dir)
        results = recovery.auto_detect_and_recover()
        
        print("\nRecovery completed successfully!")
        print(f"Recovered {len(results)} files to {output_dir}")
        
    except Exception as e:
        logger.error(f"Data recovery failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
