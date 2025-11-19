"""
Generated Code Metadata:
========================
Original URL: https://openseam.co
Prompt: Write Python code to simulate real-time data collection from industrial sewing machines using a device similar to OpenSeam's hardware, and process the data to calculate machine utilization metrics.
Generated: DETERMINISTIC_d591da3779c4047a
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
import threading
from collections import deque
from datetime import datetime, timedelta
import json
import logging
from typing import Dict, List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('SewingMachineMonitor')

class SewingMachineSimulator:
    """Simulates a single industrial sewing machine with realistic operation patterns."""
    
    def __init__(self, machine_id: str):
        self.machine_id = machine_id
        self.is_running = False
        self.current_job = None
        self.stitch_count = 0
        self.last_maintenance = datetime.now()
        self.uptime = timedelta(0)
        self.downtime = timedelta(0)
        self.last_state_change = datetime.now()
        self.error_state = False
        self.thread_count = 1000  # Simulated thread capacity
        self.thread_remaining = self.thread_count
        
    def generate_sensor_data(self) -> Dict:
        """Generate simulated sensor data for the machine."""
        now = datetime.now()
        
        # Update machine state (simulate random state changes)
        if random.random() < 0.005:  # 0.5% chance to change state
            self.is_running = not self.is_running
            if self.error_state:
                self.error_state = False
            self.last_state_change = now
        
        # Simulate occasional errors (1% chance)
        if random.random() < 0.01 and self.is_running:
            self.error_state = True
            self.is_running = False
            self.last_state_change = now
        
        # Update uptime/downtime metrics
        time_since_last_change = now - self.last_state_change
        if self.is_running and not self.error_state:
            self.uptime += time_since_last_change
        else:
            self.downtime += time_since_last_change
        self.last_state_change = now
        
        # Simulate stitch count if running
        if self.is_running and not self.error_state:
            self.stitch_count += random.randint(50, 200)
            self.thread_remaining = max(0, self.thread_remaining - random.randint(1, 5))
            
            # Simulate thread replacement when empty
            if self.thread_remaining <= 0:
                self.thread_remaining = self.thread_count
                self.is_running = False
                self.last_state_change = now
        
        # Simulate maintenance every ~8 hours of operation
        if self.uptime.total_seconds() > 8 * 3600 and random.random() < 0.1:
            self.last_maintenance = now
            self.uptime = timedelta(0)
            self.is_running = False
            self.last_state_change = now
        
        # Generate sensor data packet
        data = {
            'timestamp': now.isoformat(),
            'machine_id': self.machine_id,
            'is_running': self.is_running,
            'error_state': self.error_state,
            'stitch_count': self.stitch_count,
            'thread_remaining': self.thread_remaining,
            'uptime_seconds': self.uptime.total_seconds(),
            'downtime_seconds': self.downtime.total_seconds(),
            'last_maintenance': self.last_maintenance.isoformat(),
            'current_job': self.current_job
        }
        
        return data

class DataCollector:
    """Collects and processes data from multiple sewing machine simulators."""
    
    def __init__(self, machine_count: int = 5):
        self.machines = [SewingMachineSimulator(f"SM-{i+1}") for i in range(machine_count)]
        self.data_buffer = deque(maxlen=1000)
        self.running = False
        self.collection_thread = None
        self.processing_thread = None
        
    def start_collection(self, interval: float = 1.0):
        """Start collecting data from all machines at specified interval."""
        self.running = True
        self.collection_thread = threading.Thread(
            target=self._collect_data_loop,
            args=(interval,),
            daemon=True
        )
        self.processing_thread = threading.Thread(
            target=self._process_data_loop,
            daemon=True
        )
        self.collection_thread.start()
        self.processing_thread.start()
        logger.info(f"Started data collection for {len(self.machines)} machines")
        
    def stop_collection(self):
        """Stop data collection."""
        self.running = False
        if self.collection_thread:
            self.collection_thread.join()
        if self.processing_thread:
            self.processing_thread.join()
        logger.info("Stopped data collection")
        
    def _collect_data_loop(self, interval: float):
        """Continuous loop to collect data from all machines."""
        while self.running:
            try:
                for machine in self.machines:
                    data = machine.generate_sensor_data()
                    self.data_buffer.append(data)
                time.sleep(interval)
            except Exception as e:
                logger.error(f"Error in data collection: {str(e)}")
                time.sleep(1)  # Prevent tight error loop
    
    def _process_data_loop(self):
        """Continuous loop to process collected data."""
        while self.running:
            try:
                if self.data_buffer:
                    self._calculate_metrics()
                time.sleep(5)  # Process metrics every 5 seconds
            except Exception as e:
                logger.error(f"Error in data processing: {str(e)}")
                time.sleep(1)
    
    def _calculate_metrics(self):
        """Calculate utilization metrics from collected data."""
        now = datetime.now()
        machine_metrics = {}
        
        # Get the most recent data point for each machine
        recent_data = {}
        for data in list(self.data_buffer):
            machine_id = data['machine_id']
            recent_data[machine_id] = data
        
        # Calculate metrics for each machine
        for machine_id, data in recent_data.items():
            uptime = data['uptime_seconds']
            downtime = data['downtime_seconds']
            total_time = uptime + downtime
            
            if total_time > 0:
                utilization = (uptime / total_time) * 100
            else:
                utilization = 0.0
                
            machine_metrics[machine_id] = {
                'utilization': round(utilization, 2),
                'stitches_per_hour': round(data['stitch_count'] / (uptime / 3600) if uptime > 0 else 0, 2),
                'status': 'Running' if data['is_running'] else 'Error' if data['error_state'] else 'Idle',
                'thread_remaining_pct': round((data['thread_remaining'] / 1000) * 100, 1),
                'time_since_maintenance': str(now - datetime.fromisoformat(data['last_maintenance']))
            }
        
        # Calculate overall metrics
        total_utilization = sum(m['utilization'] for m in machine_metrics.values()) / len(machine_metrics)
        running_machines = sum(1 for m in machine_metrics.values() if m['status'] == 'Running')
        
        metrics = {
            'timestamp': now.isoformat(),
            'machine_metrics': machine_metrics,
            'overall_metrics': {
                'average_utilization': round(total_utilization, 2),
                'machines_running': running_machines,
                'total_machines': len(machine_metrics)
            }
        }
        
        logger.info(f"Calculated metrics: {json.dumps(metrics, indent=2)}")
        return metrics

def main():
    """Main function to run the simulation."""
    try:
        collector = DataCollector(machine_count=5)
        collector.start_collection(interval=0.5)
        
        # Run for 5 minutes (300 seconds) in demo mode
        time.sleep(300)
        collector.stop_collection()
        
    except KeyboardInterrupt:
        logger.info("Received keyboard interrupt, shutting down...")
        collector.stop_collection()
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()
```
