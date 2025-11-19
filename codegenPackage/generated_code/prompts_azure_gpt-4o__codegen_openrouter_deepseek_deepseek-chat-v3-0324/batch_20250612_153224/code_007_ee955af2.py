"""
Generated Code Metadata:
========================
Original URL: https://donturesystems.co.ke
Prompt: Write a program to monitor and control access to premises using gate automation systems, incorporating features described by Donture Systems Ltd.
Generated: DETERMINISTIC_ee955af266579431
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import logging
from enum import Enum
from typing import Optional, List, Dict
from dataclasses import dataclass
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AccessStatus(Enum):
    """Enum representing different access statuses."""
    GRANTED = "ACCESS_GRANTED"
    DENIED = "ACCESS_DENIED"
    PENDING = "PENDING_VERIFICATION"
    EXPIRED = "ACCESS_EXPIRED"

class GateState(Enum):
    """Enum representing different gate states."""
    OPEN = "OPEN"
    CLOSED = "CLOSED"
    MOVING = "MOVING"
    MAINTENANCE = "MAINTENANCE"

@dataclass
class User:
    """Data class representing a user with access rights."""
    user_id: str
    name: str
    access_level: int
    access_expiry: Optional[float] = None

@dataclass
class AccessLog:
    """Data class representing an access log entry."""
    timestamp: float
    user_id: str
    access_status: AccessStatus
    gate_id: str

class GateController(ABC):
    """Abstract base class for gate controllers."""
    
    @abstractmethod
    def open_gate(self) -> bool:
        """Open the gate."""
        pass
    
    @abstractmethod
    def close_gate(self) -> bool:
        """Close the gate."""
        pass
    
    @abstractmethod
    def get_gate_state(self) -> GateState:
        """Get current gate state."""
        pass

class DontureGateController(GateController):
    """Concrete implementation of GateController for Donture Systems."""
    
    def __init__(self, gate_id: str):
        self.gate_id = gate_id
        self._state = GateState.CLOSED
    
    def open_gate(self) -> bool:
        """Open the gate."""
        if self._state == GateState.MAINTENANCE:
            logger.error(f"Gate {self.gate_id} is in maintenance mode")
            return False
        
        logger.info(f"Opening gate {self.gate_id}")
        self._state = GateState.MOVING
        time.sleep(2)  # Simulate gate movement
        self._state = GateState.OPEN
        logger.info(f"Gate {self.gate_id} is now open")
        return True
    
    def close_gate(self) -> bool:
        """Close the gate."""
        if self._state == GateState.MAINTENANCE:
            logger.error(f"Gate {self.gate_id} is in maintenance mode")
            return False
        
        logger.info(f"Closing gate {self.gate_id}")
        self._state = GateState.MOVING
        time.sleep(2)  # Simulate gate movement
        self._state = GateState.CLOSED
        logger.info(f"Gate {self.gate_id} is now closed")
        return True
    
    def get_gate_state(self) -> GateState:
        """Get current gate state."""
        return self._state
    
    def set_maintenance_mode(self, enabled: bool) -> None:
        """Enable or disable maintenance mode."""
        self._state = GateState.MAINTENANCE if enabled else GateState.CLOSED
        logger.info(f"Gate {self.gate_id} maintenance mode {'enabled' if enabled else 'disabled'}")

class AccessManager:
    """Manages user access to gates."""
    
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.access_logs: List[AccessLog] = []
        self.gate_controllers: Dict[str, GateController] = {}
    
    def register_gate(self, gate_id: str, controller: GateController) -> None:
        """Register a gate controller."""
        self.gate_controllers[gate_id] = controller
        logger.info(f"Registered gate {gate_id}")
    
    def add_user(self, user: User) -> None:
        """Add a user to the system."""
        self.users[user.user_id] = user
        logger.info(f"Added user {user.name} (ID: {user.user_id})")
    
    def remove_user(self, user_id: str) -> None:
        """Remove a user from the system."""
        if user_id in self.users:
            del self.users[user_id]
            logger.info(f"Removed user {user_id}")
    
    def request_access(self, user_id: str, gate_id: str) -> AccessStatus:
        """Request access to a gate."""
        if gate_id not in self.gate_controllers:
            logger.error(f"Gate {gate_id} not found")
            return AccessStatus.DENIED
        
        if user_id not in self.users:
            logger.warning(f"Unknown user {user_id} attempted access")
            self._log_access(user_id, gate_id, AccessStatus.DENIED)
            return AccessStatus.DENIED
        
        user = self.users[user_id]
        current_time = time.time()
        
        # Check access expiry
        if user.access_expiry and user.access_expiry < current_time:
            logger.warning(f"User {user_id} access expired")
            self._log_access(user_id, gate_id, AccessStatus.EXPIRED)
            return AccessStatus.EXPIRED
        
        # Check access level (simplified logic)
        if user.access_level < 1:  # Minimum access level
            logger.warning(f"User {user_id} has insufficient access level")
            self._log_access(user_id, gate_id, AccessStatus.DENIED)
            return AccessStatus.DENIED
        
        # Grant access
        controller = self.gate_controllers[gate_id]
        if controller.open_gate():
            self._log_access(user_id, gate_id, AccessStatus.GRANTED)
            return AccessStatus.GRANTED
        
        self._log_access(user_id, gate_id, AccessStatus.DENIED)
        return AccessStatus.DENIED
    
    def _log_access(self, user_id: str, gate_id: str, status: AccessStatus) -> None:
        """Log an access attempt."""
        log_entry = AccessLog(
            timestamp=time.time(),
            user_id=user_id,
            access_status=status,
            gate_id=gate_id
        )
        self.access_logs.append(log_entry)
        logger.info(f"Access {status.value} for user {user_id} at gate {gate_id}")
    
    def get_access_logs(self) -> List[AccessLog]:
        """Get all access logs."""
        return self.access_logs
    
    def get_gate_status(self, gate_id: str) -> Optional[GateState]:
        """Get the status of a specific gate."""
        if gate_id in self.gate_controllers:
            return self.gate_controllers[gate_id].get_gate_state()
        return None

# Example usage
if __name__ == "__main__":
    # Initialize access manager
    access_manager = AccessManager()
    
    # Create and register gates
    main_gate = DontureGateController("gate-001")
    access_manager.register_gate("gate-001", main_gate)
    
    # Add users
    admin_user = User(
        user_id="user-001",
        name="Admin User",
        access_level=5,
        access_expiry=time.time() + 86400  # 1 day expiry
    )
    regular_user = User(
        user_id="user-002",
        name="Regular User",
        access_level=1,
        access_expiry=time.time() + 3600  # 1 hour expiry
    )
    access_manager.add_user(admin_user)
    access_manager.add_user(regular_user)
    
    # Simulate access requests
    print(access_manager.request_access("user-001", "gate-001"))  # Should grant
    print(access_manager.request_access("user-002", "gate-001"))  # Should grant
    print(access_manager.request_access("unknown-user", "gate-001"))  # Should deny
    
    # Close the gate after some time
    time.sleep(5)
    main_gate.close_gate()
    
    # Print access logs
    for log in access_manager.get_access_logs():
        print(f"{log.timestamp} - {log.user_id} - {log.access_status.value} - {log.gate_id}")
```
