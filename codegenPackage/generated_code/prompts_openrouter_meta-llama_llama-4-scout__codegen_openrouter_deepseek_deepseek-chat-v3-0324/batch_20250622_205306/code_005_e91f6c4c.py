"""
Generated Code Metadata:
========================
Original URL: https://pumaipce.com
Prompt: "Design a system for monitoring and controlling industrial instrumentation, including calibration and maintenance tasks, using software libraries like LabVIEW or MATLAB."
Generated: DETERMINISTIC_e91f6c4c4e45996c
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Industrial Instrumentation Monitoring and Control System
# Using Python with simulated MATLAB/LabVIEW-like functionality

import numpy as np
import time
import logging
from datetime import datetime
from abc import ABC, abstractmethod
from typing import List, Dict, Optional, Tuple
import json
import threading
import queue

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('instrumentation_system.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class Instrument(ABC):
    """Abstract base class for industrial instruments."""
    
    def __init__(self, instrument_id: str, name: str, manufacturer: str):
        self.instrument_id = instrument_id
        self.name = name
        self.manufacturer = manufacturer
        self.last_calibration = None
        self.last_maintenance = None
        self.is_connected = False
        self._calibration_due = False
        self._maintenance_due = False
        
    @abstractmethod
    def connect(self) -> bool:
        """Connect to the instrument."""
        pass
        
    @abstractmethod
    def disconnect(self) -> bool:
        """Disconnect from the instrument."""
        pass
        
    @abstractmethod
    def read_data(self) -> Dict:
        """Read data from the instrument."""
        pass
        
    def calibrate(self) -> bool:
        """Perform calibration procedure."""
        logger.info(f"Calibrating instrument {self.instrument_id}")
        self.last_calibration = datetime.now()
        self._calibration_due = False
        return True
        
    def perform_maintenance(self) -> bool:
        """Perform maintenance procedure."""
        logger.info(f"Performing maintenance on instrument {self.instrument_id}")
        self.last_maintenance = datetime.now()
        self._maintenance_due = False
        return True
        
    def check_calibration_status(self, days_threshold: int = 30) -> bool:
        """Check if calibration is due."""
        if self.last_calibration is None:
            self._calibration_due = True
            return True
            
        days_since = (datetime.now() - self.last_calibration).days
        self._calibration_due = days_since >= days_threshold
        return self._calibration_due
        
    def check_maintenance_status(self, days_threshold: int = 90) -> bool:
        """Check if maintenance is due."""
        if self.last_maintenance is None:
            self._maintenance_due = True
            return True
            
        days_since = (datetime.now() - self.last_maintenance).days
        self._maintenance_due = days_since >= days_threshold
        return self._maintenance_due
        
    def get_status(self) -> Dict:
        """Get instrument status."""
        return {
            'instrument_id': self.instrument_id,
            'name': self.name,
            'manufacturer': self.manufacturer,
            'is_connected': self.is_connected,
            'last_calibration': str(self.last_calibration),
            'last_maintenance': str(self.last_maintenance),
            'calibration_due': self._calibration_due,
            'maintenance_due': self._maintenance_due
        }

class PressureSensor(Instrument):
    """Concrete class for pressure sensor instrument."""
    
    def __init__(self, instrument_id: str, name: str, manufacturer: str, pressure_range: Tuple[float, float]):
        super().__init__(instrument_id, name, manufacturer)
        self.pressure_range = pressure_range
        self._simulated_pressure = 0.0
        
    def connect(self) -> bool:
        """Simulate connecting to pressure sensor."""
        logger.info(f"Connecting to pressure sensor {self.instrument_id}")
        time.sleep(1)  # Simulate connection delay
        self.is_connected = True
        return True
        
    def disconnect(self) -> bool:
        """Simulate disconnecting from pressure sensor."""
        logger.info(f"Disconnecting from pressure sensor {self.instrument_id}")
        self.is_connected = False
        return True
        
    def read_data(self) -> Dict:
        """Simulate reading pressure data."""
        if not self.is_connected:
            raise ConnectionError("Instrument not connected")
            
        # Simulate some pressure variation
        self._simulated_pressure = np.random.uniform(
            self.pressure_range[0],
            self.pressure_range[1]
        )
        
        return {
            'pressure': self._simulated_pressure,
            'unit': 'psi',
            'timestamp': str(datetime.now())
        }

class TemperatureSensor(Instrument):
    """Concrete class for temperature sensor instrument."""
    
    def __init__(self, instrument_id: str, name: str, manufacturer: str, temp_range: Tuple[float, float]):
        super().__init__(instrument_id, name, manufacturer)
        self.temp_range = temp_range
        self._simulated_temp = 0.0
        
    def connect(self) -> bool:
        """Simulate connecting to temperature sensor."""
        logger.info(f"Connecting to temperature sensor {self.instrument_id}")
        time.sleep(1)  # Simulate connection delay
        self.is_connected = True
        return True
        
    def disconnect(self) -> bool:
        """Simulate disconnecting from temperature sensor."""
        logger.info(f"Disconnecting from temperature sensor {self.instrument_id}")
        self.is_connected = False
        return True
        
    def read_data(self) -> Dict:
        """Simulate reading temperature data."""
        if not self.is_connected:
            raise ConnectionError("Instrument not connected")
            
        # Simulate some temperature variation
        self._simulated_temp = np.random.uniform(
            self.temp_range[0],
            self.temp_range[1]
        )
        
        return {
            'temperature': self._simulated_temp,
            'unit': '°C',
            'timestamp': str(datetime.now())
        }

class InstrumentManager:
    """Manages multiple instruments and their operations."""
    
    def __init__(self):
        self.instruments = {}
        self.data_queue = queue.Queue()
        self._stop_event = threading.Event()
        
    def add_instrument(self, instrument: Instrument) -> bool:
        """Add an instrument to the manager."""
        if instrument.instrument_id in self.instruments:
            logger.warning(f"Instrument {instrument.instrument_id} already exists")
            return False
            
        self.instruments[instrument.instrument_id] = instrument
        logger.info(f"Added instrument {instrument.instrument_id}")
        return True
        
    def remove_instrument(self, instrument_id: str) -> bool:
        """Remove an instrument from the manager."""
        if instrument_id not in self.instruments:
            logger.warning(f"Instrument {instrument_id} not found")
            return False
            
        instrument = self.instruments[instrument_id]
        if instrument.is_connected:
            instrument.disconnect()
            
        del self.instruments[instrument_id]
        logger.info(f"Removed instrument {instrument_id}")
        return True
        
    def connect_all(self) -> bool:
        """Connect to all instruments."""
        success = True
        for instrument in self.instruments.values():
            try:
                if not instrument.connect():
                    success = False
                    logger.error(f"Failed to connect instrument {instrument.instrument_id}")
            except Exception as e:
                success = False
                logger.error(f"Error connecting instrument {instrument.instrument_id}: {str(e)}")
        return success
        
    def disconnect_all(self) -> bool:
        """Disconnect from all instruments."""
        success = True
        for instrument in self.instruments.values():
            try:
                if not instrument.disconnect():
                    success = False
                    logger.error(f"Failed to disconnect instrument {instrument.instrument_id}")
            except Exception as e:
                success = False
                logger.error(f"Error disconnecting instrument {instrument.instrument_id}: {str(e)}")
        return success
        
    def start_monitoring(self, interval: float = 1.0) -> None:
        """Start monitoring all instruments in a separate thread."""
        self._stop_event.clear()
        monitor_thread = threading.Thread(
            target=self._monitor_loop,
            args=(interval,),
            daemon=True
        )
        monitor_thread.start()
        logger.info("Started monitoring thread")
        
    def stop_monitoring(self) -> None:
        """Stop the monitoring thread."""
        self._stop_event.set()
        logger.info("Stopped monitoring thread")
        
    def _monitor_loop(self, interval: float) -> None:
        """Main monitoring loop running in a separate thread."""
        while not self._stop_event.is_set():
            for instrument in self.instruments.values():
                try:
                    if instrument.is_connected:
                        data = instrument.read_data()
                        data['instrument_id'] = instrument.instrument_id
                        self.data_queue.put(data)
                        
                        # Check calibration and maintenance status
                        instrument.check_calibration_status()
                        instrument.check_maintenance_status()
                        
                except Exception as e:
                    logger.error(f"Error reading from instrument {instrument.instrument_id}: {str(e)}")
                    
            time.sleep(interval)
            
    def get_latest_data(self) -> List[Dict]:
        """Get
