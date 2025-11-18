"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.himsdemo.bste.live
Prompt: Create a template for printing healthcare data with headers like `PrintSettings.printHeader.HospitalName` and `PrintSettings.printHeader.Address` in a Health Information Management System.
Generated: DETERMINISTIC_45946e07644a9c08
Batch ID: 20250612_151504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PrintSettings:
    """Class to hold print settings for healthcare data."""
    
    class PrintHeader:
        """Inner class to define the structure of print headers."""
        def __init__(self, hospital_name, address):
            self.hospital_name = hospital_name
            self.address = address

        def __str__(self):
            """Return the formatted header string."""
            return f"{self.hospital_name}\n{self.address}\n"

    def __init__(self, header):
        """Initialize PrintSettings with a specific header."""
        if not isinstance(header, self.PrintHeader):
            raise ValueError("Header must be an instance of PrintHeader.")
        self.print_header = header

    def print_data(self, data):
        """Print healthcare data with the specified header.
        
        Args:
            data (str): The healthcare data to print.
            
        Raises:
            ValueError: If the data is not a string.
        """
        if not isinstance(data, str):
            raise ValueError("Data must be a string.")
        
        print(self.print_header)
        print(data)


# Example usage
if __name__ == "__main__":
    try:
        # Create a print header
        header = PrintSettings.PrintHeader("City Hospital", "123 Health St, Wellness City")
        
        # Initialize print settings
        print_settings = PrintSettings(header)
        
        # Sample healthcare data
        healthcare_data = "Patient ID: 12345\nPatient Name: John Doe\nDiagnosis: Healthy\n"
        
        # Print the data
        print_settings.print_data(healthcare_data)
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
