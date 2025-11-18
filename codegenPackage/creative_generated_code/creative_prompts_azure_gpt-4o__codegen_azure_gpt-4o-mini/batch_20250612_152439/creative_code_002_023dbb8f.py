"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tabriz3dprint.ir
Prompt: Generate code to simulate parallel 3D printing of a single model across multiple devices, as mentioned in the services offered by https://tabriz3dprint.ir.
Generated: DETERMINISTIC_023dbb8fa7b94592
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import threading
import time
import random
import queue

class PrintJob:
    """Represents a 3D print job."""
    def __init__(self, model_name, print_time):
        self.model_name = model_name
        self.print_time = print_time

    def execute(self):
        """Simulate executing the print job."""
        print(f"Starting print job for {self.model_name}. Estimated time: {self.print_time}s.")
        time.sleep(self.print_time)
        print(f"Completed print job for {self.model_name}.")

class Printer(threading.Thread):
    """Represents a 3D printer that can process print jobs in parallel."""
    def __init__(self, name, job_queue):
        super().__init__()
        self.name = name
        self.job_queue = job_queue
        self.daemon = True  # Allows the program to exit even if threads are running

    def run(self):
        """Run the printer thread to process print jobs."""
        while True:
            try:
                job = self.job_queue.get(timeout=3)  # Wait for a job or timeout after 3 seconds
                job.execute()
                self.job_queue.task_done()
            except queue.Empty:
                print(f"{self.name} has no more jobs to process.")
                break

class PrintManager:
    """Manages the print jobs and printers."""
    def __init__(self, num_printers):
        self.job_queue = queue.Queue()
        self.printers = [Printer(f"Printer-{i+1}", self.job_queue) for i in range(num_printers)]

    def add_job(self, model_name, print_time):
        """Add a new print job to the queue."""
        job = PrintJob(model_name, print_time)
        self.job_queue.put(job)

    def start_printing(self):
        """Start all printers to process the jobs in parallel."""
        for printer in self.printers:
            printer.start()

        # Wait for all jobs to be processed
        self.job_queue.join()

def main():
    """Main function to simulate the printing process."""
    print_manager = PrintManager(num_printers=3)

    # Adding print jobs with random print times between 1 to 5 seconds
    for i in range(5):
        model_name = f"Model-{i+1}"
        print_time = random.randint(1, 5)
        print_manager.add_job(model_name, print_time)

    # Start printing jobs in parallel
    print_manager.start_printing()
    print("All print jobs have been submitted.")

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
