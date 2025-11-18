"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nfts-satoshivm.pages.dev
Prompt: Generate code for a prover pool that assigns proof tasks to provers and submits the generated proofs to the Rollup node for verification on Bitcoin, as described in the proving layer of SatoshiVM.
Generated: DETERMINISTIC_09f9479fa9614c31
Batch ID: 20250612_151531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import threading
import queue
import random
import time
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Prover:
    """Represents a prover that can process proof tasks."""
    
    def __init__(self, prover_id):
        self.prover_id = prover_id

    def generate_proof(self, task):
        """Simulate proof generation; return a proof string."""
        logging.info(f"Prover {self.prover_id} is generating proof for task: {task}")
        time.sleep(random.uniform(0.5, 1.5))  # Simulate time taken for proof generation
        proof = f"proof_of_{task}_by_{self.prover_id}"
        logging.info(f"Prover {self.prover_id} generated proof: {proof}")
        return proof


class ProverPool:
    """Manages a pool of provers and assigns tasks to them."""
    
    def __init__(self, num_provers):
        self.provers = [Prover(i) for i in range(num_provers)]
        self.task_queue = queue.Queue()
        self.results_queue = queue.Queue()
        self.threads = []

    def assign_tasks(self):
        """Assign tasks from the task queue to available provers."""
        while True:
            task = self.task_queue.get()
            if task is None:
                break
            prover = random.choice(self.provers)  # Randomly select a prover
            proof = prover.generate_proof(task)
            self.results_queue.put(proof)

    def submit_proof(self, proof):
        """Simulate submitting the proof to a Rollup node for verification."""
        logging.info(f"Submitting proof to Rollup node: {proof}")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate submission time
        # In a real application, you would send a request to the Rollup node here

    def start(self):
        """Start the prover pool and processing threads."""
        for _ in range(len(self.provers)):
            thread = threading.Thread(target=self.process_tasks)
            thread.start()
            self.threads.append(thread)

    def process_tasks(self):
        """Process tasks and submit proofs."""
        while True:
            proof = self.results_queue.get()
            if proof is None:
                break
            self.submit_proof(proof)

    def stop(self):
        """Stop the prover pool and clean up threads."""
        for _ in self.threads:
            self.task_queue.put(None)  # Signal threads to stop
        for thread in self.threads:
            thread.join()

    def add_task(self, task):
        """Add a new task to the task queue."""
        self.task_queue.put(task)


def main():
    """Main function to run the prover pool."""
    prover_pool = ProverPool(num_provers=5)  # Initialize a prover pool with 5 provers
    prover_pool.start()

    # Simulate adding tasks to the pool
    try:
        for i in range(10):
            prover_pool.add_task(f"task_{i}")
            time.sleep(random.uniform(0.1, 0.3))  # Simulate time between task submissions
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        prover_pool.stop()  # Ensure the prover pool is stopped

if __name__ == "__main__":
    main()
```
