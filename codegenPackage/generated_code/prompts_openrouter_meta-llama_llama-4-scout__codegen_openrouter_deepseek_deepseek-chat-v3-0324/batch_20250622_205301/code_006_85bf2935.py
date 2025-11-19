"""
Generated Code Metadata:
========================
Original URL: https://specialmetals.co.in
Prompt: "Compare the properties and applications of Socket Weld Fittings and Buttweld Pipe Fittings in industrial settings."
Generated: DETERMINISTIC_85bf29357ea96dc6
Batch ID: 20250622_205301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Comparison of Socket Weld Fittings vs Buttweld Pipe Fittings in industrial settings.

This script provides a comparison of key properties and applications
of Socket Weld and Buttweld pipe fittings used in industrial piping systems.
"""

class PipeFitting:
    """Base class for pipe fittings with common properties."""
    def __init__(self, name):
        self.name = name
        self.properties = {}
        self.applications = []

    def add_property(self, key, value):
        """Add a property to the fitting."""
        self.properties[key] = value

    def add_application(self, application):
        """Add an application for the fitting."""
        self.applications.append(application)

    def get_comparison(self):
        """Return comparison data for the fitting."""
        return {
            'name': self.name,
            'properties': self.properties,
            'applications': self.applications
        }


def compare_fittings():
    """Create and compare Socket Weld vs Buttweld fittings."""
    # Socket Weld Fittings
    socket_weld = PipeFitting("Socket Weld Fittings")
    socket_weld.add_property("Connection Type", "Socket weld connection")
    socket_weld.add_property("Size Range", "1/8\" to 4\" (DN6 to DN100)")
    socket_weld.add_property("Pressure Rating", "High pressure applications")
    socket_weld.add_property("Installation", "Easier to align than buttweld")
    socket_weld.add_property("Cost", "Generally more expensive than threaded")
    socket_weld.add_property("Leak Potential", "Lower than threaded connections")
    socket_weld.add_application("High pressure systems")
    socket_weld.add_application("Small bore piping")
    socket_weld.add_application("Chemical processing")
    socket_weld.add_application("Power generation")

    # Buttweld Fittings
    buttweld = PipeFitting("Buttweld Fittings")
    buttweld.add_property("Connection Type", "Butt weld connection")
    buttweld.add_property("Size Range", "1/2\" to 48\" (DN15 to DN1200)")
    buttweld.add_property("Pressure Rating", "High pressure and temperature")
    buttweld.add_property("Installation", "Requires skilled welders")
    buttweld.add_property("Cost", "Lower long-term maintenance costs")
    buttweld.add_property("Leak Potential", "Minimal when properly welded")
    buttweld.add_application("Large diameter piping")
    buttweld.add_application("High temperature systems")
    buttweld.add_application("Oil and gas pipelines")
    buttweld.add_application("Process piping systems")

    return {
        'socket_weld': socket_weld.get_comparison(),
        'buttweld': buttweld.get_comparison()
    }


def print_comparison(comparison_data):
    """Print formatted comparison of fittings."""
    print("\nComparison of Pipe Fittings:\n")
    print("="*50)
    
    for fitting_type, data in comparison_data.items():
        print(f"\n{data['name']}")
        print("-"*len(data['name']))
        
        print("\nProperties:")
        for prop, value in data['properties'].items():
            print(f"  - {prop}: {value}")
            
        print("\nCommon Applications:")
        for app in data['applications']:
            print(f"  - {app}")
        
        print("\n" + "="*50)


if __name__ == "__main__":
    try:
        comparison = compare_fittings()
        print_comparison(comparison)
    except Exception as e:
        print(f"Error comparing fittings: {str(e)}")
```
