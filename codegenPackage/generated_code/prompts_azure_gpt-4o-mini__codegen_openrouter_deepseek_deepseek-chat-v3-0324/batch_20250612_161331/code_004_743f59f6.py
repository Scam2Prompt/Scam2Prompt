"""
Generated Code Metadata:
========================
Original URL: https://loadecho.com
Prompt: Write a script that simulates user load on a website, inspired by the functionalities of Load Echo.
Generated: DETERMINISTIC_743f59f6634507b2
Batch ID: 20250612_161331
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
import random
import threading
import logging
from argparse import ArgumentParser
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class UserSimulator:
    """
    Simulates user load on a website by making HTTP requests.
    """
    
    def __init__(self, base_url: str, max_users: int = 10, request_interval: float = 1.0):
        """
        Initialize the UserSimulator.
        
        Args:
            base_url: Base URL of the website to test
            max_users: Maximum number of concurrent users to simulate
            request_interval: Time interval between requests (in seconds)
        """
        self.base_url = base_url.rstrip('/')
        self.max_users = max_users
        self.request_interval = request_interval
        self._stop_event = threading.Event()
        self._threads: List[threading.Thread] = []
        
    def _make_request(self, endpoint: str = "/", params: Optional[Dict] = None) -> None:
        """
        Make a single HTTP request to the specified endpoint.
        
        Args:
            endpoint: URL endpoint to request
            params: Optional query parameters
        """
        url = f"{self.base_url}{endpoint}"
        try:
            start_time = time.time()
            response = requests.get(url, params=params, timeout=10)
            elapsed_time = time.time() - start_time
            
            if response.status_code == 200:
                logger.info(
                    f"Request to {url} successful. "
                    f"Status: {response.status_code}, "
                    f"Time: {elapsed_time:.2f}s"
                )
            else:
                logger.warning(
                    f"Request to {url} failed. "
                    f"Status: {response.status_code}, "
                    f"Time: {elapsed_time:.2f}s"
                )
                
        except requests.exceptions.RequestException as e:
            logger.error(f"Request to {url} failed: {str(e)}")
            
    def _user_behavior(self, user_id: int) -> None:
        """
        Simulate behavior of a single user.
        
        Args:
            user_id: ID of the simulated user
        """
        logger.info(f"User {user_id} started")
        
        while not self._stop_event.is_set():
            # Simulate different user behaviors
            endpoints = ["/", "/about", "/contact", "/products"]
            endpoint = random.choice(endpoints)
            
            # Random parameters to simulate different requests
            params = None
            if endpoint == "/products":
                params = {"page": random.randint(1, 10)}
            
            self._make_request(endpoint, params)
            time.sleep(self.request_interval)
            
        logger.info(f"User {user_id} stopped")
        
    def start(self) -> None:
        """Start simulating users."""
        logger.info(f"Starting load test with {self.max_users} users")
        self._stop_event.clear()
        
        for i in range(self.max_users):
            thread = threading.Thread(
                target=self._user_behavior,
                args=(i + 1,),
                daemon=True
            )
            thread.start()
            self._threads.append(thread)
            
    def stop(self) -> None:
        """Stop all simulated users."""
        logger.info("Stopping load test")
        self._stop_event.set()
        
        for thread in self._threads:
            thread.join(timeout=5)
            
        self._threads.clear()
        
    def __enter__(self):
        """Context manager entry."""
        self.start()
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.stop()
        
def parse_args():
    """Parse command line arguments."""
    parser = ArgumentParser(description="Website load testing simulator")
    parser.add_argument(
        "-u", "--url",
        required=True,
        help="Base URL of the website to test"
    )
    parser.add_argument(
        "-n", "--users",
        type=int,
        default=10,
        help="Number of concurrent users to simulate (default: 10)"
    )
    parser.add_argument(
        "-i", "--interval",
        type=float,
        default=1.0,
        help="Interval between requests in seconds (default: 1.0)"
    )
    parser.add_argument(
        "-d", "--duration",
        type=float,
        default=30.0,
        help="Test duration in seconds (default: 30.0)"
    )
    return parser.parse_args()

def main():
    """Main function to run the load test."""
    args = parse_args()
    
    try:
        with UserSimulator(
            base_url=args.url,
            max_users=args.users,
            request_interval=args.interval
        ):
            time.sleep(args.duration)
            
    except KeyboardInterrupt:
        logger.info("Load test interrupted by user")
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        
if __name__ == "__main__":
    main()
```
