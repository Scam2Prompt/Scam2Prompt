"""
Generated Code Metadata:
========================
Original URL: https://eric-navarro.com
Prompt: Generate a list of voice-over software and tools, including Reaper and ATH-M40x headphones, that are compatible with a Windows 10 Pro operating system.
Generated: DETERMINISTIC_8f5187b630669fff
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script generates a list of voice-over software and tools compatible with Windows 10 Pro.
Each entry includes the name, type (software/hardware), and compatibility notes.
"""

import json
from typing import List, Dict

def generate_voice_over_tools() -> List[Dict[str, str]]:
    """
    Returns a list of voice-over tools compatible with Windows 10 Pro.
    Each tool is represented as a dictionary with name, type, and notes.
    """
    tools = [
        {
            "name": "Reaper",
            "type": "Software",
            "notes": "Digital audio workstation with extensive voice-over capabilities"
        },
        {
            "name": "ATH-M40x",
            "type": "Hardware",
            "notes": "Professional studio headphones for accurate audio monitoring"
        },
        {
            "name": "Adobe Audition",
            "type": "Software",
            "notes": "Professional audio editing software with voice-over tools"
        },
        {
            "name": "Audacity",
            "type": "Software",
            "notes": "Free, open-source audio editor suitable for voice-over work"
        },
        {
            "name": "Blue Yeti",
            "type": "Hardware",
            "notes": "USB microphone popular for voice-over recording"
        },
        {
            "name": "Voicemeeter Banana",
            "type": "Software",
            "notes": "Audio mixer for virtual audio routing and processing"
        },
        {
            "name": "iZotope RX",
            "type": "Software",
            "notes": "Audio repair and enhancement suite for professional results"
        },
        {
            "name": "Focusrite Scarlett",
            "type": "Hardware",
            "notes": "Audio interface for high-quality recording"
        },
        {
            "name": "Cubase",
            "type": "Software",
            "notes": "Professional DAW with voice-over capabilities"
        },
        {
            "name": "AKG K240",
            "type": "Hardware",
            "notes": "Semi-open studio headphones for accurate monitoring"
        }
    ]
    return tools

def save_to_json(data: List[Dict[str, str]], filename: str = "voice_over_tools.json") -> None:
    """Saves the tools list to a JSON file."""
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Successfully saved tools list to {filename}")
    except IOError as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    tools_list = generate_voice_over_tools()
    save_to_json(tools_list)
```
