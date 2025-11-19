"""
Generated Code Metadata:
========================
Original URL: https://trimaticpuertasautomaticas.com
Prompt: Write Python code to simulate the functionality of a garage door opener system, including features like duplicating remote controls and ensuring compliance with CE Marking standards as described on Trimatic Puertas Automáticas.
Generated: DETERMINISTIC_c58068d51be1707d
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import hashlib
import time
from enum import Enum, auto
from typing import List, Dict, Optional

class DoorState(Enum):
    OPEN = auto()
    CLOSED = auto()
    OPENING = auto()
    CLOSING = auto()
    STOPPED = auto()

class RemoteControl:
    def __init__(self, id: str, frequency: float, rolling_code: int = 0):
        self.id = id
        self.frequency = frequency
        self.rolling_code = rolling_code
        self.manufacturer_code = "TRIMATIC-CE"
        self.last_used = 0
        
    def generate_signal(self) -> Dict:
        """Generate a secure rolling code signal"""
        current_time = int(time.time())
        if current_time - self.last_used < 1:
            raise RuntimeError("Remote control cooldown period not elapsed")
            
        self.rolling_code += 1
        self.last_used = current_time
        
        signal = {
            'id': self.id,
            'frequency': self.frequency,
            'code': self.rolling_code,
            'timestamp': current_time,
            'manufacturer': self.manufacturer_code
        }
        
        # Add cryptographic signature for CE compliance
        signal_hash = hashlib.sha256(
            f"{self.id}{self.frequency}{self.rolling_code}{current_time}{self.manufacturer_code}".encode()
        ).hexdigest()
        signal['signature'] = signal_hash
        
        return signal
    
    @classmethod
    def duplicate_remote(cls, original: 'RemoteControl', new_id: str) -> 'RemoteControl':
        """Create a duplicate remote with same frequency and rolling code"""
        if not original:
            raise ValueError("Original remote cannot be None")
        return cls(
            id=new_id,
            frequency=original.frequency,
            rolling_code=original.rolling_code
        )

class GarageDoor:
    def __init__(self):
        self.state = DoorState.CLOSED
        self.registered_remotes: Dict[str, RemoteControl] = {}
        self.last_valid_code: Optional[int] = None
        self.safety_sensors_active = True
        self.ce_compliant = True
        self.operation_count = 0
        self.MAX_OPERATIONS = 10000  # CE compliance maintenance threshold
        
    def register_remote(self, remote: RemoteControl) -> bool:
        """Register a new remote control with the garage door"""
        if not self.ce_compliant:
            raise RuntimeError("System not CE compliant - cannot register remotes")
            
        if remote.id in self.registered_remotes:
            return False
            
        self.registered_remotes[remote.id] = remote
        return True
    
    def verify_signal(self, signal: Dict) -> bool:
        """Verify the authenticity and validity of a remote signal"""
        required_keys = {'id', 'frequency', 'code', 'timestamp', 'manufacturer', 'signature'}
        if not all(key in signal for key in required_keys):
            return False
            
        if signal['manufacturer'] != "TRIMATIC-CE":
            return False
            
        # Verify cryptographic signature
        expected_hash = hashlib.sha256(
            f"{signal['id']}{signal['frequency']}{signal['code']}{signal['timestamp']}{signal['manufacturer']}".encode()
        ).hexdigest()
        
        if signal['signature'] != expected_hash:
            return False
            
        # Check if remote is registered
        if signal['id'] not in self.registered_remotes:
            return False
            
        remote = self.registered_remotes[signal['id']]
        
        # Check rolling code (must be greater than last used)
        if signal['code'] <= remote.rolling_code:
            return False
            
        # Check timestamp (prevent replay attacks)
        current_time = int(time.time())
        if abs(current_time - signal['timestamp']) > 10:  # 10 second window
            return False
            
        return True
    
    def operate_door(self, signal: Dict) -> bool:
        """Process a valid remote signal to operate the door"""
        if not self.verify_signal(signal):
            return False
            
        remote = self.registered_remotes[signal['id']]
        remote.rolling_code = signal['code']
        self.last_valid_code = signal['code']
        
        if self.state == DoorState.CLOSED:
            if self.safety_check():
                self.state = DoorState.OPENING
                self.operation_count += 1
                return True
        elif self.state == DoorState.OPEN:
            self.state = DoorState.CLOSING
            self.operation_count += 1
            return True
        elif self.state in (DoorState.OPENING, DoorState.CLOSING):
            self.state = DoorState.STOPPED
            return True
        elif self.state == DoorState.STOPPED:
            # Resume last operation
            if self.last_valid_code % 2 == 0:  # Simple way to determine direction
                self.state = DoorState.OPENING
            else:
                self.state = DoorState.CLOSING
            return True
            
        return False
    
    def safety_check(self) -> bool:
        """Perform safety checks according to CE standards"""
        if not self.safety_sensors_active:
            return False
            
        if self.operation_count >= self.MAX_OPERATIONS:
            self.maintenance_required()
            return False
            
        return True
    
    def maintenance_required(self):
        """Flag system for maintenance"""
        self.ce_compliant = False
        self.state = DoorState.STOPPED
    
    def perform_maintenance(self):
        """Reset operation count and ensure CE compliance"""
        self.operation_count = 0
        self.ce_compliant = True
        self.safety_sensors_active = True

# Example usage
if __name__ == "__main__":
    # Create garage door system
    garage = GarageDoor()
    
    # Create original remote
    original_remote = RemoteControl(
        id="RC-001",
        frequency=433.92,
        rolling_code=random.randint(0, 1000)
    )
    
    # Register remote
    garage.register_remote(original_remote)
    
    # Duplicate remote
    duplicate_remote = RemoteControl.duplicate_remote(original_remote, "RC-002")
    garage.register_remote(duplicate_remote)
    
    # Simulate door operation
    signal = original_remote.generate_signal()
    if garage.operate_door(signal):
        print("Door operation successful")
    else:
        print("Door operation failed")
```
