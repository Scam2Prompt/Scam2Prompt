"""
Generated Code Metadata:
========================
Original URL: https://arbitriumltd.com
Prompt: Write a script to test the reliability of a blockchain application, incorporating QA techniques similar to those described by Arbitrium Ltd.
Generated: DETERMINISTIC_5c170384d0a170cf
Batch ID: 20250612_150342
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "http://node1.example.com:8080": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://node3.example.com:8080": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://node2.example.com:8080": {
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
import requests
import time
import random
import json
from typing import Dict, List, Optional, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed

class BlockchainTester:
    """
    A class to test the reliability of a blockchain application.
    Implements various QA techniques including load testing, consistency checks,
    and fault injection.
    """
    
    def __init__(self, node_urls: List[str], test_duration: int = 300, max_threads: int = 10):
        """
        Initialize the BlockchainTester.
        
        Args:
            node_urls: List of blockchain node URLs to test against
            test_duration: Duration of the test in seconds (default: 300)
            max_threads: Maximum number of concurrent threads for load testing
        """
        self.node_urls = node_urls
        self.test_duration = test_duration
        self.max_threads = max_threads
        self.results = {
            'successful_txs': 0,
            'failed_txs': 0,
            'consistency_errors': 0,
            'node_responses': {url: {'success': 0, 'failure': 0} for url in node_urls}
        }
        
    def _send_transaction(self, node_url: str, payload: Dict) -> Tuple[bool, Optional[str]]:
        """
        Send a transaction to a blockchain node.
        
        Args:
            node_url: URL of the node to send transaction to
            payload: Transaction payload
            
        Returns:
            Tuple of (success: bool, error: Optional[str])
        """
        try:
            headers = {'Content-Type': 'application/json'}
            response = requests.post(
                f"{node_url}/transactions",
                data=json.dumps(payload),
                headers=headers,
                timeout=10
            )
            response.raise_for_status()
            return True, None
        except requests.exceptions.RequestException as e:
            return False, str(e)
    
    def _generate_random_transaction(self) -> Dict:
        """
        Generate a random transaction payload for testing.
        
        Returns:
            Dictionary containing transaction data
        """
        return {
            'from': f"user_{random.randint(1, 1000)}",
            'to': f"user_{random.randint(1, 1000)}",
            'amount': random.randint(1, 100),
            'timestamp': int(time.time())
        }
    
    def _check_consistency(self) -> int:
        """
        Check consistency across all nodes by comparing block heights.
        
        Returns:
            Number of inconsistencies found
        """
        heights = []
        for url in self.node_urls:
            try:
                response = requests.get(f"{url}/blocks/height", timeout=5)
                response.raise_for_status()
                heights.append(response.json()['height'])
            except:
                continue
        
        if not heights:
            return 0
            
        max_height = max(heights)
        return sum(1 for h in heights if h < max_height)
    
    def _fault_injection_test(self) -> None:
        """
        Perform fault injection by sending malformed transactions.
        """
        malformed_txs = [
            {'invalid': 'payload'},
            {'from': '', 'to': 'recipient', 'amount': 10},
            {'from': 'sender', 'to': '', 'amount': 10},
            {'from': 'sender', 'to': 'recipient', 'amount': -10}
        ]
        
        for tx in malformed_txs:
            node_url = random.choice(self.node_urls)
            success, error = self._send_transaction(node_url, tx)
            if not success:
                self.results['failed_txs'] += 1
                self.results['node_responses'][node_url]['failure'] += 1
    
    def _load_test(self) -> None:
        """
        Perform load testing by sending multiple concurrent transactions.
        """
        end_time = time.time() + self.test_duration
        
        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            while time.time() < end_time:
                futures = []
                for _ in range(self.max_threads * 2):
                    tx = self._generate_random_transaction()
                    node_url = random.choice(self.node_urls)
                    futures.append(executor.submit(self._send_transaction, node_url, tx))
                
                for future in as_completed(futures):
                    success, error = future.result()
                    node_url = futures[future].args[0]
                    if success:
                        self.results['successful_txs'] += 1
                        self.results['node_responses'][node_url]['success'] += 1
                    else:
                        self.results['failed_txs'] += 1
                        self.results['node_responses'][node_url]['failure'] += 1
    
    def run_tests(self) -> Dict:
        """
        Run all tests and return results.
        
        Returns:
            Dictionary containing test results
        """
        print("Starting blockchain reliability tests...")
        start_time = time.time()
        
        # Run consistency checks periodically
        consistency_checks = 0
        while time.time() < start_time + self.test_duration:
            self._load_test()
            self._fault_injection_test()
            
            # Check consistency every 30 seconds
            if time.time() > start_time + (consistency_checks * 30):
                inconsistencies = self._check_consistency()
                self.results['consistency_errors'] += inconsistencies
                consistency_checks += 1
        
        print("Tests completed.")
        return self.results

if __name__ == "__main__":
    # Example usage
    node_urls = [
        "http://node1.example.com:8080",
        "http://node2.example.com:8080",
        "http://node3.example.com:8080"
    ]
    
    tester = BlockchainTester(node_urls, test_duration=60, max_threads=5)
    results = tester.run_tests()
    
    print("\nTest Results:")
    print(f"Successful transactions: {results['successful_txs']}")
    print(f"Failed transactions: {results['failed_txs']}")
    print(f"Consistency errors: {results['consistency_errors']}")
    print("\nNode response statistics:")
    for url, stats in results['node_responses'].items():
        print(f"{url}: {stats['success']} success, {stats['failure']} failure")
```
