"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fmt.co.id
Prompt: Create a program that simulates the hydraulic system of an excavator equipped with a piping kit, ensuring compatibility with attachments like hydraulic breakers and pulverizers as detailed by PT. Fuji Metal Teknik.
Generated: DETERMINISTIC_597a59c2ffcc6c4f
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class HydraulicSystem:
    """
    A class to simulate the hydraulic system of an excavator equipped with a piping kit.
    This system supports compatibility with attachments such as hydraulic breakers and pulverizers.
    """

    def __init__(self):
        """
        Initializes the hydraulic system with default parameters.
        """
        self.pressure = 0  # Pressure in psi
        self.fluid_level = 100  # Fluid level in liters
        self.attachments = []  # List of attached hydraulic tools

    def pump_fluid(self, amount):
        """
        Pumps fluid into the hydraulic system.

        Parameters:
            amount (float): The amount of fluid to pump in liters.

        Raises:
            ValueError: If the amount is negative or the resulting fluid level exceeds 100 liters.
        """
        if amount < 0:
            raise ValueError("Cannot pump a negative amount of fluid.")
        if self.fluid_level + amount > 100:
            raise ValueError("Fluid level cannot exceed 100 liters.")

        self.fluid_level += amount
        print(f"Pumped {amount} liters of fluid. Current fluid level: {self.fluid_level} liters.")

    def set_pressure(self, pressure):
        """
        Sets the hydraulic pressure.

        Parameters:
            pressure (float): Pressure to set in psi.

        Raises:
            ValueError: If the pressure is negative.
        """
        if pressure < 0:
            raise ValueError("Pressure cannot be negative.")
        
        self.pressure = pressure
        print(f"Hydraulic pressure set to: {self.pressure} psi.")

    def attach_tool(self, tool_name):
        """
        Attaches a hydraulic tool to the system.

        Parameters:
            tool_name (str): The name of the tool to attach.

        Raises:
            ValueError: If tool is already attached.
        """
        if tool_name in self.attachments:
            raise ValueError(f"{tool_name} is already attached.")
        
        self.attachments.append(tool_name)
        print(f"Attached tool: {tool_name}. Current attachments: {self.attachments}.")

    def detach_tool(self, tool_name):
        """
        Detaches a hydraulic tool from the system.

        Parameters:
            tool_name (str): The name of the tool to detach.

        Raises:
            ValueError: If tool is not attached.
        """
        if tool_name not in self.attachments:
            raise ValueError(f"{tool_name} is not attached.")
        
        self.attachments.remove(tool_name)
        print(f"Detached tool: {tool_name}. Current attachments: {self.attachments}.")

    def operate_tool(self, tool_name):
        """
        Operates the attached hydraulic tool.

        Parameters:
            tool_name (str): The name of the tool to operate.

        Raises:
            ValueError: If the tool is not attached or if the pressure is insufficient.
        """
        if tool_name not in self.attachments:
            raise ValueError(f"{tool_name} is not attached. Please attach the tool first.")
        if self.pressure < 50:  # Assuming 50 psi is the minimum required
            raise ValueError("Insufficient hydraulic pressure to operate the tool.")

        print(f"Operating {tool_name} at {self.pressure} psi.")

# Example of utilizing the HydraulicSystem class
if __name__ == "__main__":
    try:
        hydraulic_system = HydraulicSystem()
        
        # Simulating the hydraulic system operations
        hydraulic_system.pump_fluid(20)
        hydraulic_system.set_pressure(60)
        hydraulic_system.attach_tool("Hydraulic Breaker")
        hydraulic_system.operate_tool("Hydraulic Breaker")
        hydraulic_system.detach_tool("Hydraulic Breaker")

    except ValueError as e:
        print(f"Error: {e}")
```
