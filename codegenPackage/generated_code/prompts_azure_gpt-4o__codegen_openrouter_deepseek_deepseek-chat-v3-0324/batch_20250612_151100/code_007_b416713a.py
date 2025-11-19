"""
Generated Code Metadata:
========================
Original URL: https://aptrongurgaon.in
Prompt: Write a program to simulate industrial automation processes using PLC SCADA, as outlined in APTRON Gurgaon’s Industrial Automation training.
Generated: DETERMINISTIC_b416713a246893bc
Batch ID: 20250612_151100
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
from enum import Enum
import logging
from dataclasses import dataclass

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('plc_scada.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('PLC_SCADA')

class MachineState(Enum):
    """Enum representing possible machine states"""
    IDLE = 0
    RUNNING = 1
    FAULT = 2
    MAINTENANCE = 3

@dataclass
class SensorData:
    """Data class for sensor readings"""
    temperature: float
    pressure: float
    vibration: float
    flow_rate: float

class PLC:
    """Programmable Logic Controller simulation"""
    def __init__(self, plc_id: str):
        self.plc_id = plc_id
        self.state = MachineState.IDLE
        self.sensors = SensorData(0.0, 0.0, 0.0, 0.0)
        self.alarms = []
        logger.info(f"PLC {plc_id} initialized")

    def read_sensors(self):
        """Simulate reading sensor data"""
        self.sensors.temperature = round(random.uniform(20.0, 100.0), 2)
        self.sensors.pressure = round(random.uniform(1.0, 10.0), 2)
        self.sensors.vibration = round(random.uniform(0.1, 5.0), 2)
        self.sensors.flow_rate = round(random.uniform(0.5, 20.0), 2)
        
        # Check for abnormal readings
        if self.sensors.temperature > 90.0:
            self.trigger_alarm("High Temperature")
        if self.sensors.pressure > 8.0:
            self.trigger_alarm("High Pressure")
        if self.sensors.vibration > 4.0:
            self.trigger_alarm("High Vibration")
            
        logger.debug(f"Sensor readings: {self.sensors}")
        return self.sensors

    def trigger_alarm(self, alarm_msg: str):
        """Handle alarm conditions"""
        self.alarms.append(alarm_msg)
        self.state = MachineState.FAULT
        logger.warning(f"ALARM triggered: {alarm_msg}")

    def clear_alarms(self):
        """Clear all active alarms"""
        self.alarms.clear()
        self.state = MachineState.IDLE
        logger.info("All alarms cleared")

    def start_machine(self):
        """Start the machine operation"""
        if self.state != MachineState.FAULT:
            self.state = MachineState.RUNNING
            logger.info("Machine started")
            return True
        logger.error("Cannot start machine in FAULT state")
        return False

    def stop_machine(self):
        """Stop the machine operation"""
        self.state = MachineState.IDLE
        logger.info("Machine stopped")

class SCADA:
    """Supervisory Control and Data Acquisition system"""
    def __init__(self):
        self.plcs = {}
        logger.info("SCADA system initialized")

    def add_plc(self, plc: PLC):
        """Add a PLC to the SCADA system"""
        self.plcs[plc.plc_id] = plc
        logger.info(f"Added PLC {plc.plc_id} to SCADA")

    def monitor(self, interval: int = 5):
        """Monitor all connected PLCs"""
        logger.info("Starting SCADA monitoring")
        try:
            while True:
                for plc_id, plc in self.plcs.items():
                    sensor_data = plc.read_sensors()
                    logger.info(
                        f"PLC {plc_id} - State: {plc.state.name}, "
                        f"Temp: {sensor_data.temperature}°C, "
                        f"Pressure: {sensor_data.pressure} bar"
                    )
                    if plc.alarms:
                        logger.warning(f"PLC {plc_id} alarms: {plc.alarms}")
                time.sleep(interval)
        except KeyboardInterrupt:
            logger.info("SCADA monitoring stopped")
        except Exception as e:
            logger.error(f"Monitoring error: {str(e)}")

    def generate_report(self):
        """Generate a system status report"""
        report = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "plcs": []
        }
        
        for plc_id, plc in self.plcs.items():
            plc_report = {
                "plc_id": plc_id,
                "state": plc.state.name,
                "sensors": {
                    "temperature": plc.sensors.temperature,
                    "pressure": plc.sensors.pressure,
                    "vibration": plc.sensors.vibration,
                    "flow_rate": plc.sensors.flow_rate
                },
                "alarms": plc.alarms.copy()
            }
            report["plcs"].append(plc_report)
        
        logger.info("Generated system report")
        return report

def main():
    """Main function to demonstrate PLC-SCADA simulation"""
    try:
        # Create PLC instances
        plc1 = PLC("PLC001")
        plc2 = PLC("PLC002")
        
        # Create SCADA system
        scada = SCADA()
        scada.add_plc(plc1)
        scada.add_plc(plc2)
        
        # Start machines
        plc1.start_machine()
        plc2.start_machine()
        
        # Start monitoring
        scada.monitor(interval=3)
        
    except Exception as e:
        logger.error(f"System error: {str(e)}")

if __name__ == "__main__":
    main()
```
