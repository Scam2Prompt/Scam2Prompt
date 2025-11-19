"""
Generated Code Metadata:
========================
Original URL: https://canopusem.com
Prompt: Write a script to automate a music production task in Ableton Live using Max for Live and MIDI controllers.
Generated: DETERMINISTIC_de310ef14b24ef0a
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Ableton Live Automation Script using Max for Live and MIDI Controllers

This script automates music production tasks in Ableton Live by:
1. Connecting to MIDI controllers
2. Mapping MIDI controls to Ableton parameters
3. Sending/receiving MIDI messages via Max for Live
4. Handling common music production automation tasks

Requirements:
- Ableton Live with Max for Live
- Python (with packages: python-rtmidi, mido)
- MIDI controller connected
"""

import rtmidi
import mido
from mido import Message
import time
import sys
import logging
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AbletonAutomation:
    def __init__(self):
        """Initialize MIDI connections and parameter mappings."""
        self.midi_in = None
        self.midi_out = None
        self.parameter_map: Dict[int, str] = {}  # MIDI CC to parameter name
        self.active_clip = None
        self.initialized = False
        
        try:
            self._initialize_midi()
            self._load_parameter_mappings()
            self.initialized = True
        except Exception as e:
            logger.error(f"Initialization failed: {str(e)}")
            self.cleanup()
            raise

    def _initialize_midi(self):
        """Set up MIDI input and output ports."""
        try:
            # Initialize MIDI input
            self.midi_in = rtmidi.MidiIn()
            available_ports = self.midi_in.get_ports()
            
            if not available_ports:
                raise RuntimeError("No MIDI input ports available")
                
            self.midi_in.open_port(0)
            self.midi_in.ignore_types(sysex=False, timing=False, active_sense=False)
            
            # Initialize MIDI output
            self.midi_out = rtmidi.MidiOut()
            available_out_ports = self.midi_out.get_ports()
            
            if not available_out_ports:
                raise RuntimeError("No MIDI output ports available")
                
            self.midi_out.open_port(0)
            
            logger.info("MIDI ports initialized successfully")
            
        except Exception as e:
            logger.error(f"MIDI initialization error: {str(e)}")
            raise

    def _load_parameter_mappings(self):
        """Load default parameter mappings (can be extended from config)."""
        # Example mappings: MIDI CC number to Ableton parameter name
        self.parameter_map = {
            1: "volume",
            2: "pan",
            3: "filter_cutoff",
            4: "filter_resonance",
            5: "attack",
            6: "decay",
            7: "sustain",
            8: "release"
        }
        logger.info("Loaded parameter mappings")

    def map_parameter(self, cc_number: int, parameter_name: str):
        """Map a MIDI CC to an Ableton parameter."""
        if not 0 <= cc_number <= 127:
            raise ValueError("CC number must be between 0 and 127")
            
        self.parameter_map[cc_number] = parameter_name
        logger.info(f"Mapped CC {cc_number} to parameter {parameter_name}")

    def process_midi_message(self, message):
        """Process incoming MIDI messages and map to Ableton parameters."""
        if not self.initialized:
            raise RuntimeError("Automation not initialized")
            
        try:
            msg = mido.Message.from_bytes(message[0])
            
            if msg.type == 'control_change':
                parameter = self.parameter_map.get(msg.control)
                if parameter:
                    self._update_ableton_parameter(parameter, msg.value)
                    logger.debug(f"Updated {parameter} to {msg.value}")
                    
            elif msg.type == 'note_on':
                self._handle_note_on(msg.note, msg.velocity)
                
            elif msg.type == 'note_off':
                self._handle_note_off(msg.note)
                
        except Exception as e:
            logger.error(f"Error processing MIDI message: {str(e)}")

    def _update_ableton_parameter(self, parameter: str, value: int):
        """Send parameter update to Ableton via Max for Live."""
        # This would typically communicate with Max for Live device
        # Placeholder for actual implementation
        logger.info(f"Updating {parameter} to {value}")
        
        # Example: Send MIDI message back to Ableton
        if self.midi_out:
            msg = Message('control_change', control=1, value=value)
            self.midi_out.send_message(msg.bytes())

    def _handle_note_on(self, note: int, velocity: int):
        """Handle note on events."""
        logger.debug(f"Note on: {note} with velocity {velocity}")
        # Could trigger clips, record, etc.

    def _handle_note_off(self, note: int):
        """Handle note off events."""
        logger.debug(f"Note off: {note}")
        # Could stop recording, etc.

    def start_listening(self):
        """Start listening for MIDI input."""
        if not self.initialized:
            raise RuntimeError("Automation not initialized")
            
        logger.info("Starting MIDI listener")
        try:
            while True:
                message = self.midi_in.get_message()
                if message:
                    self.process_midi_message(message)
                time.sleep(0.001)
        except KeyboardInterrupt:
            logger.info("Stopping listener")
        except Exception as e:
            logger.error(f"Error in listener: {str(e)}")
        finally:
            self.cleanup()

    def cleanup(self):
        """Clean up resources."""
        logger.info("Cleaning up resources")
        if self.midi_in and self.midi_in.is_port_open():
            self.midi_in.close_port()
        if self.midi_out and self.midi_out.is_port_open():
            self.midi_out.close_port()
        del self.midi_in
        del self.midi_out

def main():
    """Main entry point for the automation script."""
    try:
        automation = AbletonAutomation()
        if automation.initialized:
            automation.start_listening()
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
