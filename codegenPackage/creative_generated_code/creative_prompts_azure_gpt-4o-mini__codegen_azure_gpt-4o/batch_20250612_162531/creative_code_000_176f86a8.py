"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://merkury.it
Prompt: Generate a code snippet for a cryptocurrency mining application that supports multiple algorithms, as described on Merkury.IT.
Generated: DETERMINISTIC_176f86a866068db3
Batch ID: 20250612_162531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import time
import threading

class CryptoMiner:
    """
    A cryptocurrency mining application supporting multiple algorithms.
    Supported algorithms: SHA256, Scrypt, MD5
    """
    def __init__(self, algorithm="SHA256", mining_data=""):
        self.algorithm = algorithm.upper()
        self.mining_data = mining_data
        self.validate_algorithm()

    def validate_algorithm(self):
        """
        Validates the selected algorithm. Raises an exception if unsupported.
        """
        supported_algorithms = ["SHA256", "SCRYPT", "MD5"]
        if self.algorithm not in supported_algorithms:
            raise ValueError(f"Unsupported algorithm '{self.algorithm}'. Supported algorithms: {supported_algorithms}")

    def mine(self):
        """
        Simulates mining by hashing the provided data using the selected algorithm.
        """
        try:
            if self.algorithm == "SHA256":
                return hashlib.sha256(self.mining_data.encode()).hexdigest()
            elif self.algorithm == "MD5":
                return hashlib.md5(self.mining_data.encode()).hexdigest()
            elif self.algorithm == "SCRYPT":
                return self.simulate_scrypt()
            else:
                raise ValueError("Invalid algorithm provided.")
        except Exception as e:
            print(f"Error during mining: {e}")

    def simulate_scrypt(self):
        """
        Simulates the Scrypt hashing algorithm (for demo purposes).
        Note: Implement actual Scrypt algorithm logic if required.
        """
        time.sleep(1)  # Simulate computational delay
        return hashlib.sha256(hashlib.md5(self.mining_data.encode()).digest()).hexdigest()

    def start_mining(self, duration=10):
        """
        Starts the mining process for the specified duration.
        """
        end_time = time.time() + duration
        while time.time() < end_time:
            result = self.mine()
            print(f"Mined hash: {result}")
            time.sleep(0.5)  # Simulate block delay


def main():
    # User selects algorithm and data to mine
    algorithm = input("Enter mining algorithm (SHA256, Scrypt, MD5): ")
    mining_data = input("Enter data to be mined: ")

    try:
        miner = CryptoMiner(algorithm, mining_data)

        # Start mining in a background thread
        print("Starting mining...")
        mining_thread = threading.Thread(target=miner.start_mining, args=(10,))
        mining_thread.start()
        mining_thread.join()
        print("Mining completed.")
    except ValueError as ve:
        print(f"Initialization error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
```
