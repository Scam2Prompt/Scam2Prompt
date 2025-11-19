"""
Generated Code Metadata:
========================
Original URL: https://openseam.co
Prompt: Write code to simulate spot checks on sewing machine performance every 5 milliseconds, as described in OpenSeam's 7.2 billion spot checks per shift example.
Generated: DETERMINISTIC_4fb2e1c7b256b3e8
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random
from threading import Thread, Event
from queue import Queue
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('sewing_machine_monitor.log'),
        logging.StreamHandler()
    ]
)

class SewingMachineMonitor:
    def __init__(self, machine_id):
        self.machine_id = machine_id
        self.stop_event = Event()
        self.performance_queue = Queue(maxsize=1000)
        self.thread = Thread(target=self._monitor_loop, daemon=True)
        
    def _simulate_performance_check(self):
        """Simulate a performance check with random values"""
        try:
            # Simulate various performance metrics
            metrics = {
                'timestamp': time.time(),
                'stitch_count': random.randint(1, 10000),
                'tension': random.uniform(0.5, 5.0),
                'speed': random.randint(500, 5000),
                'needle_position': random.choice(['up', 'down']),
                'thread_break': random.random() < 0.0001,  # Rare thread break
                'motor_temp': random.uniform(20.0, 80.0)
            }
            return metrics
        except Exception as e:
            logging.error(f"Error in performance check simulation: {e}")
            return None

    def _monitor_loop(self):
        """Main monitoring loop running every 5ms"""
        while not self.stop_event.is_set():
            try:
                start_time = time.time()
                
                # Perform the spot check
                metrics = self._simulate_performance_check()
                if metrics:
                    self.performance_queue.put(metrics)
                
                # Calculate remaining time to maintain 5ms interval
                processing_time = time.time() - start_time
                sleep_time = max(0, 0.005 - processing_time)
                time.sleep(sleep_time)
                
            except Exception as e:
                logging.error(f"Error in monitor loop: {e}")
                time.sleep(0.005)  # Prevent tight loop on errors

    def start(self):
        """Start the monitoring thread"""
        self.thread.start()
        logging.info(f"Started monitoring for machine {self.machine_id}")

    def stop(self):
        """Stop the monitoring thread"""
        self.stop_event.set()
        self.thread.join()
        logging.info(f"Stopped monitoring for machine {self.machine_id}")

    def get_performance_data(self):
        """Get collected performance data"""
        data = []
        while not self.performance_queue.empty():
            data.append(self.performance_queue.get())
        return data

class MonitoringSystem:
    def __init__(self, num_machines=100):
        self.machines = [SewingMachineMonitor(i) for i in range(num_machines)]
        self.running = False
        
    def start(self):
        """Start monitoring all machines"""
        if not self.running:
            for machine in self.machines:
                machine.start()
            self.running = True
            logging.info(f"Started monitoring system with {len(self.machines)} machines")
            
    def stop(self):
        """Stop monitoring all machines"""
        if self.running:
            for machine in self.machines:
                machine.stop()
            self.running = False
            logging.info("Stopped monitoring system")

    def aggregate_data(self):
        """Aggregate data from all machines"""
        all_data = []
        for machine in self.machines:
            all_data.extend(machine.get_performance_data())
        return all_data

if __name__ == "__main__":
    try:
        # Example usage
        system = MonitoringSystem(num_machines=10)
        system.start()
        
        # Run for 10 seconds for demonstration
        time.sleep(10)
        
        system.stop()
        
        # Get and log some sample data
        sample_data = system.aggregate_data()[:5]
        logging.info(f"Sample performance data: {sample_data}")
        
    except KeyboardInterrupt:
        logging.info("Shutting down monitoring system...")
        system.stop()
    except Exception as e:
        logging.error(f"Fatal error in monitoring system: {e}")
```
