"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asterdx.com
Prompt: Write code to switch between Simple Mode and Pro Mode on Aster's trading interface, allowing users to toggle advanced trading tools and real-time data.
Generated: DETERMINISTIC_220826341933bcf5
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TradingInterface:
    def __init__(self):
        """Initialize the Trading Interface with default mode set to Simple."""
        self.mode = 'Simple'
        self.advanced_tools_enabled = False
        self.real_time_data_enabled = False

    def toggle_mode(self):
        """Toggle between Simple Mode and Pro Mode."""
        try:
            if self.mode == 'Simple':
                self.switch_to_pro_mode()
            else:
                self.switch_to_simple_mode()
        except Exception as e:
            print(f"Error while toggling mode: {e}")

    def switch_to_pro_mode(self):
        """Switch to Pro Mode, enabling advanced trading tools and real-time data."""
        self.mode = 'Pro'
        self.advanced_tools_enabled = True
        self.real_time_data_enabled = True
        print("Switched to Pro Mode: Advanced trading tools and real-time data enabled.")

    def switch_to_simple_mode(self):
        """Switch to Simple Mode, disabling advanced trading tools and real-time data."""
        self.mode = 'Simple'
        self.advanced_tools_enabled = False
        self.real_time_data_enabled = False
        print("Switched to Simple Mode: Advanced trading tools and real-time data disabled.")

    def get_current_mode(self):
        """Return the current mode of the Trading Interface."""
        return self.mode

    def is_pro_mode(self):
        """Check if the current mode is Pro Mode."""
        return self.mode == 'Pro'

    def display_status(self):
        """Display the current status of the Trading Interface."""
        status = (
            f"Current Mode: {self.get_current_mode()}\n"
            f"Advanced Tools Enabled: {self.advanced_tools_enabled}\n"
            f"Real-time Data Enabled: {self.real_time_data_enabled}"
        )
        print(status)


# Example usage
if __name__ == "__main__":
    trading_interface = TradingInterface()
    trading_interface.display_status()  # Show initial status

    trading_interface.toggle_mode()  # Switch to Pro Mode
    trading_interface.display_status()  # Show status after switching

    trading_interface.toggle_mode()  # Switch back to Simple Mode
    trading_interface.display_status()  # Show status after switching back
```
