"""
Generated Code Metadata:
========================
Original URL: https://fourmemecz.com
Prompt: Create a tutorial script in Python for comparing Joxi's screenshot capture speed with other similar services, highlighting the 30% speed improvement.
Generated: DETERMINISTIC_24d4afd0b4256c6b
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import requests
import subprocess
import platform
import statistics
from typing import List, Dict, Tuple
import matplotlib.pyplot as plt

class ScreenshotServiceTester:
    """
    A class to compare screenshot capture speeds of different services.
    Focuses on demonstrating Joxi's 30% speed improvement over competitors.
    """
    
    def __init__(self):
        self.services = {
            'Joxi': {
                'command': {
                    'Windows': ['joxi', 'capture'],
                    'Linux': ['joxi', 'capture'],
                    'Darwin': ['joxi', 'capture']
                },
                'url': None
            },
            'Lightshot': {
                'command': {
                    'Windows': ['lightshot', '--capture'],
                    'Linux': ['lightshot', '--capture'],
                    'Darwin': ['lightshot', '--capture']
                },
                'url': None
            },
            'ShareX': {
                'command': {
                    'Windows': ['sharex', '-capture'],
                    'Linux': ['sharex', '--capture'],
                    'Darwin': ['sharex', '--capture']
                },
                'url': None
            }
        }
        self.results: Dict[str, List[float]] = {}
        self.os = platform.system()
        
    def _run_command(self, command: List[str]) -> Tuple[bool, float]:
        """
        Execute a screenshot capture command and measure execution time.
        
        Args:
            command: List of command arguments
            
        Returns:
            Tuple of (success status, execution time in seconds)
        """
        try:
            start_time = time.time()
            subprocess.run(command, check=True, capture_output=True, timeout=10)
            elapsed = time.time() - start_time
            return True, elapsed
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
            print(f"Command failed: {e}")
            return False, 0.0
        
    def _test_service(self, service_name: str, iterations: int = 5) -> bool:
        """
        Test a single screenshot service multiple times.
        
        Args:
            service_name: Name of the service to test
            iterations: Number of test iterations
            
        Returns:
            True if tests completed successfully, False otherwise
        """
        if service_name not in self.services:
            print(f"Service {service_name} not configured")
            return False
            
        command = self.services[service_name]['command'].get(self.os)
        if not command:
            print(f"OS {self.os} not supported for {service_name}")
            return False
            
        times = []
        print(f"\nTesting {service_name}...")
        
        for i in range(iterations):
            print(f"  Attempt {i+1}/{iterations}", end='\r')
            success, elapsed = self._run_command(command)
            if not success:
                return False
            times.append(elapsed)
            time.sleep(1)  # Cooldown between captures
            
        self.results[service_name] = times
        return True
        
    def run_comparison(self, iterations: int = 5) -> bool:
        """
        Run comparison tests for all configured services.
        
        Args:
            iterations: Number of test iterations per service
            
        Returns:
            True if all tests completed successfully, False otherwise
        """
        print("Starting screenshot service speed comparison...")
        print(f"Operating System: {self.os}\n")
        
        all_success = True
        for service in self.services:
            if not self._test_service(service, iterations):
                all_success = False
                print(f"\nFailed to complete tests for {service}")
                
        return all_success
        
    def analyze_results(self) -> Dict[str, Dict[str, float]]:
        """
        Analyze and summarize test results.
        
        Returns:
            Dictionary containing statistics for each service
        """
        if not self.results:
            print("No results to analyze")
            return {}
            
        analysis = {}
        for service, times in self.results.items():
            analysis[service] = {
                'average': statistics.mean(times),
                'median': statistics.median(times),
                'min': min(times),
                'max': max(times),
                'stddev': statistics.stdev(times) if len(times) > 1 else 0.0
            }
            
        return analysis
        
    def show_speed_comparison(self):
        """Visualize the speed comparison results using matplotlib."""
        if not self.results:
            print("No results to visualize")
            return
            
        analysis = self.analyze_results()
        services = list(analysis.keys())
        averages = [stats['average'] for stats in analysis.values()]
        
        # Calculate speed improvement percentage
        if len(services) > 1:
            base_speed = averages[1]  # Compare to first competitor
            joxi_speed = averages[0]
            improvement = ((base_speed - joxi_speed) / base_speed) * 100
            improvement_text = f"Joxi is {improvement:.1f}% faster than {services[1]}"
        else:
            improvement_text = ""
        
        plt.figure(figsize=(10, 6))
        bars = plt.bar(services, averages, color=['#4C72B0', '#DD8452', '#55A868'])
        
        plt.title('Screenshot Capture Speed Comparison\n' + improvement_text)
        plt.ylabel('Time (seconds)')
        plt.xlabel('Service')
        
        # Add value labels on top of bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.3f}s',
                    ha='center', va='bottom')
        
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
        
    def generate_report(self) -> str:
        """
        Generate a text report of the comparison results.
        
        Returns:
            Formatted report string
        """
        if not self.results:
            return "No test results available"
            
        analysis = self.analyze_results()
        report = []
        report.append("=== Screenshot Service Speed Comparison Report ===")
        report.append(f"Tests performed on {self.os}")
        report.append(f"Each service tested {len(next(iter(self.results.values())))} times\n")
        
        # Add individual service stats
        for service, stats in analysis.items():
            report.append(f"Service: {service}")
            report.append(f"  Average: {stats['average']:.3f}s")
            report.append(f"  Median:  {stats['median']:.3f}s")
            report.append(f"  Range:   {stats['min']:.3f}s - {stats['max']:.3f}s")
            report.append(f"  Std Dev: {stats['stddev']:.3f}s\n")
        
        # Add comparison highlights
        if len(analysis) > 1:
            joxi_avg = analysis['Joxi']['average']
            fastest = min(analysis.items(), key=lambda x: x[1]['average'])
            
            if fastest[0] == 'Joxi':
                competitors = [s for s in analysis.keys() if s != 'Joxi']
                for competitor in competitors:
                    comp_avg = analysis[competitor]['average']
                    improvement = ((comp_avg - joxi_avg) / comp_avg) * 100
                    report.append(
                        f"Joxi is {improvement:.1f}% faster than {competitor} "
                        f"({joxi_avg:.3f}s vs {comp_avg:.3f}s)"
                    )
        
        return "\n".join(report)


def main():
    """Main function to run the comparison and display results."""
    tester = ScreenshotServiceTester()
    
    if not tester.run_comparison(iterations=5):
        print("\nSome tests failed. Partial results:")
    
    print("\n" + tester.generate_report())
    tester.show_speed_comparison()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nTest interrupted by user")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
