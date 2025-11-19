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
import json

# Define a class to represent voice-over software and tools
class VoiceOverTool:
    def __init__(self, name, type_, compatibility):
        """
        Initialize a VoiceOverTool instance.

        :param name: str - The name of the software or tool
        :param type_: str - The type of the tool (e.g., software, hardware)
        :param compatibility: list - List of compatible operating systems
        """
        self.name = name
        self.type_ = type_
        self.compatibility = compatibility

    def is_compatible(self, os_name):
        """
        Check if the tool is compatible with the given operating system.

        :param os_name: str - The name of the operating system to check
        :return: bool - True if compatible, False otherwise
        """
        return os_name in self.compatibility

# List to hold voice-over tools
voice_over_tools = [
    VoiceOverTool("Reaper", "Software", ["Windows 10 Pro", "Windows 10", "Windows 8", "Windows 7"]),
    VoiceOverTool("Audacity", "Software", ["Windows 10 Pro", "Windows 10", "Windows 8", "Windows 7"]),
    VoiceOverTool("Adobe Audition", "Software", ["Windows 10 Pro", "Windows 10"]),
    VoiceOverTool("Pro Tools", "Software", ["Windows 10 Pro", "Windows 10"]),
    VoiceOverTool("ATH-M40x", "Hardware", ["Windows 10 Pro", "Windows 10"]),
    VoiceOverTool("Focusrite Scarlett 2i2", "Hardware", ["Windows 10 Pro", "Windows 10"]),
]

def get_compatible_tools(os_name):
    """
    Get a list of tools compatible with the specified operating system.

    :param os_name: str - The name of the operating system
    :return: list - List of compatible VoiceOverTool instances
    """
    compatible_tools = [tool for tool in voice_over_tools if tool.is_compatible(os_name)]
    return compatible_tools

def main():
    """
    Main function to execute the script.
    """
    os_name = "Windows 10 Pro"  # Define the target operating system
    try:
        compatible_tools = get_compatible_tools(os_name)
        if not compatible_tools:
            print(f"No voice-over tools found for {os_name}.")
        else:
            print(f"Voice-over tools compatible with {os_name}:")
            for tool in compatible_tools:
                print(f"- {tool.name} ({tool.type_})")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
