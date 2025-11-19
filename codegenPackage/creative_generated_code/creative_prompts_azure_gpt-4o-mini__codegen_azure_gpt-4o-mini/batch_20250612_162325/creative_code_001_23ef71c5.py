"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://payeshnirooco.com
Prompt: What are the best practices for designing and installing low and medium voltage electrical panels according to Payesh Niroo's services?
Generated: DETERMINISTIC_23ef71c5cf42f734
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ElectricalPanel:
    """
    A class to represent an electrical panel for low and medium voltage systems.
    
    Attributes
    ----------
    panel_type : str
        Type of the electrical panel (low or medium voltage)
    voltage_rating : float
        Voltage rating of the electrical panel in volts
    max_current_rating : float
        Maximum current rating in amperes
    installation_location : str
        Location where the panel is installed
    safety_certified : bool
        Whether the panel is safety certified
    
    Methods
    -------
    install_panel():
        Installs the electrical panel at the specified location.
        
    display_panel_info():
        Displays the information of the electrical panel.
    """

    def __init__(self, panel_type, voltage_rating, max_current_rating, installation_location, safety_certified):
        """
        Constructs all the necessary attributes for the electrical panel object.

        Parameters
        ----------
        panel_type : str
            Type of the electrical panel (low or medium voltage)
        voltage_rating : float
            Voltage rating of the electrical panel in volts
        max_current_rating : float
            Maximum current rating in amperes
        installation_location : str
            Location where the panel is installed
        safety_certified : bool
            Whether the panel is safety certified
        """
        self.panel_type = panel_type
        self.voltage_rating = voltage_rating
        self.max_current_rating = max_current_rating
        self.installation_location = installation_location
        self.safety_certified = safety_certified

    def install_panel(self):
        """
        Installs the electrical panel at the specified location.
        
        Raises
        ------
        ValueError
            If the panel type is not valid or voltage rating exceeds limits.
        """
        if self.panel_type not in ['low', 'medium']:
            raise ValueError("Invalid panel type. Must be 'low' or 'medium'.")
        
        if self.voltage_rating <= 0 or self.max_current_rating <= 0:
            raise ValueError("Voltage and current ratings must be positive values.")
        
        # Here would be the installation logic
        print(f"Installing {self.panel_type} voltage panel at {self.installation_location}.")

    def display_panel_info(self):
        """
        Displays the information of the electrical panel.
        """
        info = (
            f"Panel Type: {self.panel_type}\n"
            f"Voltage Rating: {self.voltage_rating} V\n"
            f"Max Current Rating: {self.max_current_rating} A\n"
            f"Installation Location: {self.installation_location}\n"
            f"Safety Certified: {'Yes' if self.safety_certified else 'No'}"
        )
        print(info)

# Example usage
if __name__ == "__main__":
    try:
        panel = ElectricalPanel('low', 400, 100, 'Main Building', True)
        panel.install_panel()
        panel.display_panel_info()
    except ValueError as e:
        print(f"Error: {e}")

```
