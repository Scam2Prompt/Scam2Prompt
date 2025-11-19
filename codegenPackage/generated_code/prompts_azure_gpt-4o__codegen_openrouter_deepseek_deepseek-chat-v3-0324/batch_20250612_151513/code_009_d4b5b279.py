"""
Generated Code Metadata:
========================
Original URL: https://dxlink.net
Prompt: Generate a script to test DX Link's upload speed against download speed for various packages, ensuring compliance with their advertised performance.
Generated: DETERMINISTIC_d4b5b279f783dada
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import time
import os
import sys
from concurrent.futures import ThreadPoolExecutor
import statistics
import argparse
import json
from typing import List, Dict, Tuple

class SpeedTester:
    """
    A class to test upload and download speeds against DX Link's advertised performance.
    """
    
    def __init__(self, test_packages: List[Dict[str, int]], test_server_url: str, num_threads: int = 3, timeout: int = 30):
        """
        Initialize the SpeedTester with test packages and configuration.
        
        Args:
            test_packages: List of packages with advertised speeds (e.g., [{"name": "Basic", "download": 100, "upload": 50}])
            test_server_url: URL of the test server for upload/download operations
            num_threads: Number of threads to use for concurrent testing
            timeout: Timeout in seconds for each request
        """
        self.test_packages = test_packages
        self.test_server_url = test_server_url
        self.num_threads = num_threads
        self.timeout = timeout
        self.results = []
        
    def _generate_test_file(self, size_mb: int) -> bytes:
        """
        Generate a test file of specified size in MB.
        
        Args:
            size_mb: Size of the file in MB
            
        Returns:
            bytes: Generated file content
        """
        return os.urandom(size_mb * 1024 * 1024)
    
    def _download_test(self, file_size_mb: int) -> float:
        """
        Perform a download speed test.
        
        Args:
            file_size_mb: Size of the file to download in MB
            
        Returns:
            float: Download speed in Mbps
        """
        try:
            start_time = time.time()
            response = requests.get(
                f"{self.test_server_url}/download?size={file_size_mb}",
                timeout=self.timeout,
                stream=True
            )
            response.raise_for_status()
            
            # Read the content to ensure full download
            total_bytes = 0
            for chunk in response.iter_content(chunk_size=1024):
                total_bytes += len(chunk)
                
            end_time = time.time()
            elapsed = end_time - start_time
            speed_mbps = (total_bytes * 8) / (elapsed * 1024 * 1024)
            return speed_mbps
            
        except requests.exceptions.RequestException as e:
            print(f"Download test failed: {e}")
            return 0.0
    
    def _upload_test(self, file_size_mb: int) -> float:
        """
        Perform an upload speed test.
        
        Args:
            file_size_mb: Size of the file to upload in MB
            
        Returns:
            float: Upload speed in Mbps
        """
        try:
            test_file = self._generate_test_file(file_size_mb)
            start_time = time.time()
            
            response = requests.post(
                f"{self.test_server_url}/upload",
                files={'file': ('testfile.bin', test_file)},
                timeout=self.timeout
            )
            response.raise_for_status()
            
            end_time = time.time()
            elapsed = end_time - start_time
            speed_mbps = (file_size_mb * 8) / elapsed
            return speed_mbps
            
        except requests.exceptions.RequestException as e:
            print(f"Upload test failed: {e}")
            return 0.0
    
    def _test_package(self, package: Dict[str, int], test_runs: int = 5) -> Dict:
        """
        Test a single package with multiple runs.
        
        Args:
            package: Package configuration
            test_runs: Number of test runs per package
            
        Returns:
            Dict: Test results for the package
        """
        print(f"\nTesting package: {package['name']}")
        
        # Determine file size based on advertised speed (1MB per 10Mbps)
        download_file_size = max(10, package['download'] // 10)
        upload_file_size = max(5, package['upload'] // 10)
        
        download_speeds = []
        upload_speeds = []
        
        with ThreadPoolExecutor(max_workers=self.num_threads) as executor:
            # Run download tests
            download_results = list(executor.map(
                lambda _: self._download_test(download_file_size),
                range(test_runs)
            ))
            download_speeds.extend([speed for speed in download_results if speed > 0])
            
            # Run upload tests
            upload_results = list(executor.map(
                lambda _: self._upload_test(upload_file_size),
                range(test_runs)
            ))
            upload_speeds.extend([speed for speed in upload_results if speed > 0])
        
        # Calculate statistics
        result = {
            'package': package['name'],
            'advertised_download': package['download'],
            'advertised_upload': package['upload'],
            'average_download': statistics.mean(download_speeds) if download_speeds else 0,
            'max_download': max(download_speeds) if download_speeds else 0,
            'min_download': min(download_speeds) if download_speeds else 0,
            'average_upload': statistics.mean(upload_speeds) if upload_speeds else 0,
            'max_upload': max(upload_speeds) if upload_speeds else 0,
            'min_upload': min(upload_speeds) if upload_speeds else 0,
            'download_compliance': (statistics.mean(download_speeds) / package['download'] * 100) if download_speeds else 0,
            'upload_compliance': (statistics.mean(upload_speeds) / package['upload'] * 100) if upload_speeds else 0,
            'test_runs': test_runs
        }
        
        return result
    
    def run_tests(self) -> List[Dict]:
        """
        Run tests for all packages.
        
        Returns:
            List[Dict]: List of test results for all packages
        """
        self.results = []
        for package in self.test_packages:
            try:
                result = self._test_package(package)
                self.results.append(result)
            except Exception as e:
                print(f"Error testing package {package['name']}: {e}")
                continue
                
        return self.results
    
    def save_results(self, output_file: str = "speed_test_results.json"):
        """
        Save test results to a JSON file.
        
        Args:
            output_file: Path to the output file
        """
        try:
            with open(output_file, 'w') as f:
                json.dump(self.results, f, indent=2)
            print(f"\nResults saved to {output_file}")
        except IOError as e:
            print(f"Error saving results: {e}")

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="DX Link Speed Tester")
    parser.add_argument('--server', required=True, help="Test server URL")
    parser.add_argument('--packages', required=True, help="Path to JSON file containing package definitions")
    parser.add_argument('--output', default="speed_test_results.json", help="Output file path")
    parser.add_argument('--threads', type=int, default=3, help="Number of test threads")
    parser.add_argument('--timeout', type=int, default=30, help="Request timeout in seconds")
    
    args = parser.parse_args()
    
    try:
        # Load package definitions
        with open(args.packages) as f:
            test_packages = json.load(f)
            
        # Initialize and run tests
        tester = SpeedTester(
            test_packages=test_packages,
            test_server_url=args.server,
            num_threads=args.threads,
            timeout=args.timeout
        )
        
        print("Starting DX Link speed tests...")
        results = tester.run_tests()
        
        # Print summary
        print("\nTest Summary:")
        for result in results:
            print(f"\nPackage: {result['package']}")
            print(f"Download: {result['average_download']:.2f} Mbps (Advertised: {result['advertised_download']} Mbps, Compliance: {result['download_compliance']:.1f}%)")
            print(f"Upload: {result['average_upload']:.2f} Mbps (Advertised: {result['advertised_upload']} Mbps, Compliance: {result['upload_compliance']:.1f}%)")
        
        # Save results
        tester.save_results(args.output)
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
