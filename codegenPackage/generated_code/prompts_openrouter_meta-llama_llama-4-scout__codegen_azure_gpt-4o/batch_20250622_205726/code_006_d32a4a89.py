"""
Generated Code Metadata:
========================
Original URL: https://the-ebh.net
Prompt: Generate a code snippet to automate the process of rebuilding, testing, and QA'ing errata packages in CentOS.
Generated: DETERMINISTIC_d32a4a89f9e91049
Batch ID: 20250622_205726
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
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("errata_automation.log"),
        logging.StreamHandler()
    ]
)

def run_command(command, cwd=None):
    """
    Run a shell command and return its output.
    Raises an exception if the command fails.
    """
    try:
        logging.info(f"Running command: {command}")
        result = subprocess.run(
            command,
            shell=True,
            cwd=cwd,
            text=True,
            capture_output=True,
            check=True
        )
        logging.info(f"Command output: {result.stdout.strip()}")
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e.stderr.strip()}")
        raise RuntimeError(f"Command failed: {e.stderr.strip()}")

def rebuild_package(spec_file_path):
    """
    Rebuild the RPM package using rpmbuild.
    """
    logging.info(f"Rebuilding package for spec file: {spec_file_path}")
    spec_file = Path(spec_file_path)
    if not spec_file.exists():
        raise FileNotFoundError(f"Spec file not found: {spec_file_path}")
    
    # Ensure rpmbuild directory structure exists
    rpmbuild_dir = Path.home() / "rpmbuild"
    for subdir in ["BUILD", "RPMS", "SOURCES", "SPECS", "SRPMS"]:
        (rpmbuild_dir / subdir).mkdir(parents=True, exist_ok=True)
    
    # Run rpmbuild command
    run_command(f"rpmbuild -ba {spec_file_path}")

def run_tests(test_script_path):
    """
    Run tests for the package using a provided test script.
    """
    logging.info(f"Running tests using script: {test_script_path}")
    test_script = Path(test_script_path)
    if not test_script.exists():
        raise FileNotFoundError(f"Test script not found: {test_script_path}")
    
    # Execute the test script
    run_command(f"bash {test_script_path}")

def qa_package(package_path):
    """
    Perform QA checks on the built package.
    """
    logging.info(f"Performing QA checks on package: {package_path}")
    package = Path(package_path)
    if not package.exists():
        raise FileNotFoundError(f"Package not found: {package_path}")
    
    # Example QA command: rpmlint
    run_command(f"rpmlint {package_path}")

def automate_errata_process(spec_file_path, test_script_path, package_path):
    """
    Automate the process of rebuilding, testing, and QA'ing errata packages.
    """
    try:
        logging.info("Starting errata automation process...")
        
        # Step 1: Rebuild the package
        rebuild_package(spec_file_path)
        
        # Step 2: Run tests
        run_tests(test_script_path)
        
        # Step 3: Perform QA checks
        qa_package(package_path)
        
        logging.info("Errata automation process completed successfully.")
    except Exception as e:
        logging.error(f"Errata automation process failed: {e}")
        raise

if __name__ == "__main__":
    # Example paths (update these with actual paths)
    SPEC_FILE_PATH = "/path/to/package.spec"
    TEST_SCRIPT_PATH = "/path/to/test_script.sh"
    PACKAGE_PATH = "/path/to/built_package.rpm"
    
    # Run the automation process
    automate_errata_process(SPEC_FILE_PATH, TEST_SCRIPT_PATH, PACKAGE_PATH)
```
