"""
Generated Code Metadata:
========================
Original URL: https://noymi.in
Prompt: Write code to implement a gaming trigger mechanism for mobile games, referencing features of the NOYMI PUBG Trigger | Gaming Trigger | ET-128.
Generated: DETERMINISTIC_4a58f6d32416a5b4
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import threading
from enum import Enum
import logging
from typing import Optional, Callable

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class TriggerState(Enum):
    """Enum representing the possible states of the gaming trigger."""
    IDLE = 0
    PRESSED = 1
    RELEASED = 2

class TriggerMode(Enum):
    """Enum representing the different trigger modes."""
    SINGLE_SHOT = 0
    RAPID_FIRE = 1
    BURST_MODE = 2

class NOYMITrigger:
    """
    A class representing the NOYMI PUBG Trigger (ET-128) gaming trigger.
    
    Features:
    - Multiple trigger modes (single shot, rapid fire, burst)
    - Configurable firing rate
    - Configurable burst count
    - Haptic feedback
    - Error handling and logging
    """
    
    def __init__(
        self,
        mode: TriggerMode = TriggerMode.SINGLE_SHOT,
        firing_rate: float = 0.1,
        burst_count: int = 3,
        haptic_feedback: bool = True
    ):
        """
        Initialize the gaming trigger.
        
        Args:
            mode: The trigger mode (default: SINGLE_SHOT)
            firing_rate: Time between shots in seconds (default: 0.1)
            burst_count: Number of shots in burst mode (default: 3)
            haptic_feedback: Whether to enable haptic feedback (default: True)
        """
        self._mode = mode
        self._firing_rate = firing_rate
        self._burst_count = burst_count
        self._haptic_feedback = haptic_feedback
        self._state = TriggerState.IDLE
        self._is_active = False
        self._callback: Optional[Callable[[], None]] = None
        self._lock = threading.Lock()
        
        # Validate parameters
        if firing_rate <= 0:
            raise ValueError("Firing rate must be positive")
        if burst_count <= 0:
            raise ValueError("Burst count must be positive")
        
        logger.info("NOYMI Trigger initialized with mode: %s", mode.name)
    
    @property
    def mode(self) -> TriggerMode:
        """Get the current trigger mode."""
        return self._mode
    
    @mode.setter
    def mode(self, value: TriggerMode) -> None:
        """Set the trigger mode."""
        with self._lock:
            self._mode = value
            logger.info("Trigger mode changed to: %s", value.name)
    
    @property
    def firing_rate(self) -> float:
        """Get the current firing rate in seconds."""
        return self._firing_rate
    
    @firing_rate.setter
    def firing_rate(self, value: float) -> None:
        """Set the firing rate in seconds."""
        if value <= 0:
            raise ValueError("Firing rate must be positive")
        with self._lock:
            self._firing_rate = value
            logger.info("Firing rate changed to: %.2f seconds", value)
    
    @property
    def burst_count(self) -> int:
        """Get the current burst count."""
        return self._burst_count
    
    @burst_count.setter
    def burst_count(self, value: int) -> None:
        """Set the burst count."""
        if value <= 0:
            raise ValueError("Burst count must be positive")
        with self._lock:
            self._burst_count = value
            logger.info("Burst count changed to: %d", value)
    
    @property
    def haptic_feedback(self) -> bool:
        """Check if haptic feedback is enabled."""
        return self._haptic_feedback
    
    @haptic_feedback.setter
    def haptic_feedback(self, value: bool) -> None:
        """Enable or disable haptic feedback."""
        with self._lock:
            self._haptic_feedback = value
            logger.info("Haptic feedback %s", "enabled" if value else "disabled")
    
    def register_callback(self, callback: Callable[[], None]) -> None:
        """
        Register a callback function to be called when the trigger is activated.
        
        Args:
            callback: Function to call when trigger is activated
        """
        self._callback = callback
        logger.info("Callback registered")
    
    def press(self) -> None:
        """Simulate pressing the trigger."""
        with self._lock:
            if self._state != TriggerState.PRESSED:
                self._state = TriggerState.PRESSED
                self._is_active = True
                logger.debug("Trigger pressed")
                
                if self._haptic_feedback:
                    self._vibrate()
                
                # Start the firing mechanism in a new thread
                threading.Thread(target=self._fire, daemon=True).start()
    
    def release(self) -> None:
        """Simulate releasing the trigger."""
        with self._lock:
            if self._state == TriggerState.PRESSED:
                self._state = TriggerState.RELEASED
                self._is_active = False
                logger.debug("Trigger released")
    
    def _fire(self) -> None:
        """Internal method to handle the firing mechanism based on mode."""
        try:
            if self._mode == TriggerMode.SINGLE_SHOT:
                self._fire_single_shot()
            elif self._mode == TriggerMode.RAPID_FIRE:
                self._fire_rapid()
            elif self._mode == TriggerMode.BURST_MODE:
                self._fire_burst()
        except Exception as e:
            logger.error("Error in firing mechanism: %s", str(e))
    
    def _fire_single_shot(self) -> None:
        """Fire a single shot."""
        if self._callback and self._is_active:
            self._callback()
            logger.debug("Single shot fired")
    
    def _fire_rapid(self) -> None:
        """Fire continuously while the trigger is pressed."""
        while self._is_active:
            if self._callback:
                self._callback()
                logger.debug("Rapid fire shot")
            time.sleep(self._firing_rate)
    
    def _fire_burst(self) -> None:
        """Fire a burst of shots while the trigger is pressed."""
        while self._is_active:
            for _ in range(self._burst_count):
                if not self._is_active:
                    break
                if self._callback:
                    self._callback()
                    logger.debug("Burst fire shot")
                time.sleep(self._firing_rate)
            time.sleep(self._firing_rate * 2)  # Pause between bursts
    
    def _vibrate(self) -> None:
        """Simulate haptic feedback (would be hardware-specific in real implementation)."""
        logger.debug("Haptic feedback activated")
        # In a real implementation, this would interface with hardware
    
    def __del__(self):
        """Clean up resources when the object is deleted."""
        self._is_active = False
        logger.info("Trigger shutdown complete")

# Example usage
if __name__ == "__main__":
    def sample_callback():
        print("Trigger activated - simulating shot")
    
    try:
        trigger = NOYMITrigger(
            mode=TriggerMode.RAPID_FIRE,
            firing_rate=0.2,
            burst_count=3,
            haptic_feedback=True
        )
        trigger.register_callback(sample_callback)
        
        # Simulate trigger press and release
        print("Press trigger (simulated)")
        trigger.press()
        time.sleep(2)  # Hold for 2 seconds
        print("Release trigger (simulated)")
        trigger.release()
        
    except Exception as e:
        logger.error("Error in trigger operation: %s", str(e))
```
