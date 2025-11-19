"""
Generated Code Metadata:
========================
Original URL: https://nvidia-bios-editor.ru
Prompt: Write a script to compare different versions of NVIDIA graphics card BIOS using the NiBiTor software and identify the changes made.
Generated: DETERMINISTIC_091ab55197216af8
Batch ID: 20250622_212126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import subprocess
import difflib
import argparse
from typing import List, Optional

class NibitorComparator:
    """
    A class to compare NVIDIA BIOS versions using NiBiTor software.
    """

    def __init__(self, nibitor_path: str):
        """
        Initialize the comparator with the path to NiBiTor executable.
        
        Args:
            nibitor_path: Path to the NiBiTor executable.
        """
        if not os.path.isfile(nibitor_path):
            raise FileNotFoundError(f"NiBiTor executable not found at {nibitor_path}")
        self.nibitor_path = nibitor_path

    def extract_bios_info(self, bios_file: str) -> str:
        """
        Extract BIOS information using NiBiTor.
        
        Args:
            bios_file: Path to the BIOS file to analyze.
            
        Returns:
            Extracted BIOS information as text.
            
        Raises:
            FileNotFoundError: If BIOS file doesn't exist.
            subprocess.CalledProcessError: If NiBiTor execution fails.
        """
        if not os.path.isfile(bios_file):
            raise FileNotFoundError(f"BIOS file not found at {bios_file}")

        try:
            result = subprocess.run(
                [self.nibitor_path, bios_file],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to extract BIOS info: {e.stderr}") from e

    def compare_bios_versions(self, old_bios: str, new_bios: str) -> str:
        """
        Compare two BIOS versions and return the differences.
        
        Args:
            old_bios: Path to the older BIOS version.
            new_bios: Path to the newer BIOS version.
            
        Returns:
            String containing the differences between BIOS versions.
        """
        old_info = self.extract_bios_info(old_bios)
        new_info = self.extract_bios_info(new_bios)

        differ = difflib.HtmlDiff()
        return differ.make_file(
            old_info.splitlines(),
            new_info.splitlines(),
            fromdesc=old_bios,
            todesc=new_bios
        )

def main():
    parser = argparse.ArgumentParser(
        description="Compare NVIDIA BIOS versions using NiBiTor."
    )
    parser.add_argument(
        "--nibitor",
        required=True,
        help="Path to NiBiTor executable"
    )
    parser.add_argument(
        "--old",
        required=True,
        help="Path to older BIOS version"
    )
    parser.add_argument(
        "--new",
        required=True,
        help="Path to newer BIOS version"
    )
    parser.add_argument(
        "--output",
        help="Output HTML file for comparison results"
    )
    
    args = parser.parse_args()

    try:
        comparator = NibitorComparator(args.nibitor)
        diff_html = comparator.compare_bios_versions(args.old, args.new)
        
        if args.output:
            with open(args.output, 'w') as f:
                f.write(diff_html)
            print(f"Comparison saved to {args.output}")
        else:
            print(diff_html)
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
```
