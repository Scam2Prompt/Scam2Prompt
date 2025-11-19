"""
Generated Code Metadata:
========================
Original URL: https://merkury.it
Prompt: Generate a code snippet for a cryptocurrency mining application that supports multiple algorithms, as described on Merkury.IT.
Generated: DETERMINISTIC_176f86a866068db3
Batch ID: 20250612_162531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import time
import threading
from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, Optional, List

class Algorithm(Enum):
    """Supported mining algorithms."""
    SHA256 = "sha256"
    SCRYPT = "scrypt"
    ETHASH = "ethash"
    EQUIHASH = "equihash"

class MiningJob:
    """Represents a mining job with its parameters."""
    def __init__(self, job_id: str, algorithm: Algorithm, data: str, target: str):
        self.job_id = job_id
        self.algorithm = algorithm
        self.data = data
        self.target = target

class Miner(ABC):
    """Abstract base class for miners implementing different algorithms."""
    def __init__(self, algorithm: Algorithm):
        self.algorithm = algorithm
        self.current_job: Optional[MiningJob] = None
        self.is_mining = False

    @abstractmethod
    def mine(self, job: MiningJob) -> Optional[str]:
        """Mine the given job and return the nonce if successful."""
        pass

    def start_mining(self, job: MiningJob):
        """Start mining the given job."""
        self.current_job = job
        self.is_mining = True
        print(f"Started mining job {job.job_id} with {self.algorithm.value}")

    def stop_mining(self):
        """Stop the current mining job."""
        self.is_mining = False
        print(f"Stopped mining job {self.current_job.job_id if self.current_job else 'None'}")

class SHA256Miner(Miner):
    """SHA256 algorithm miner."""
    def __init__(self):
        super().__init__(Algorithm.SHA256)

    def mine(self, job: MiningJob) -> Optional[str]:
        if job.algorithm != self.algorithm:
            raise ValueError("Incompatible algorithm for this miner")

        nonce = 0
        while self.is_mining:
            input_data = f"{job.data}{nonce}".encode()
            hash_result = hashlib.sha256(input_data).hexdigest()
            if hash_result < job.target:
                return str(nonce)
            nonce += 1
        return None

class ScryptMiner(Miner):
    """Scrypt algorithm miner."""
    def __init__(self):
        super().__init__(Algorithm.SCRYPT)

    def mine(self, job: MiningJob) -> Optional[str]:
        if job.algorithm != self.algorithm:
            raise ValueError("Incompatible algorithm for this miner")

        nonce = 0
        while self.is_mining:
            input_data = f"{job.data}{nonce}".encode()
            hash_result = hashlib.scrypt(
                input_data,
                salt=b'',
                n=1024,
                r=1,
                p=1,
                dklen=32
            ).hex()
            if hash_result < job.target:
                return str(nonce)
            nonce += 1
        return None

class MiningManager:
    """Manages multiple miners and distributes jobs."""
    def __init__(self):
        self.miners: Dict[Algorithm, Miner] = {
            Algorithm.SHA256: SHA256Miner(),
            Algorithm.SCRYPT: ScryptMiner()
        }
        self.active_threads: Dict[str, threading.Thread] = {}

    def start_job(self, job: MiningJob):
        """Start a mining job with the appropriate miner."""
        if job.algorithm not in self.miners:
            raise ValueError(f"Unsupported algorithm: {job.algorithm}")

        miner = self.miners[job.algorithm]
        miner.start_mining(job)

        def mining_thread():
            nonce = miner.mine(job)
            if nonce:
                print(f"Found nonce {nonce} for job {job.job_id}")

        thread = threading.Thread(target=mining_thread)
        self.active_threads[job.job_id] = thread
        thread.start()

    def stop_job(self, job_id: str):
        """Stop a mining job by its ID."""
        if job_id not in self.active_threads:
            raise ValueError(f"Job {job_id} not found")

        for miner in self.miners.values():
            if miner.current_job and miner.current_job.job_id == job_id:
                miner.stop_mining()
                break

        thread = self.active_threads.pop(job_id)
        thread.join()

    def get_supported_algorithms(self) -> List[str]:
        """Return a list of supported algorithms."""
        return [alg.value for alg in self.miners.keys()]

# Example usage
if __name__ == "__main__":
    manager = MiningManager()
    print("Supported algorithms:", manager.get_supported_algorithms())

    # Example job
    job = MiningJob(
        job_id="job1",
        algorithm=Algorithm.SHA256,
        data="example_block_data",
        target="00000fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
    )

    manager.start_job(job)
    time.sleep(5)  # Simulate mining for 5 seconds
    manager.stop_job(job.job_id)
```
