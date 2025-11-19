"""
Generated Code Metadata:
========================
Original URL: https://vertiv.dns.cz
Prompt: "Provide an overview of Vertiv's history, including its founding and major acquisitions."
Generated: DETERMINISTIC_ce44104ccd2c07b7
Batch ID: 20250622_212010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Vertiv History Overview

class VertivHistory:
    def __init__(self):
        """
        Initialize Vertiv's history overview.
        """
        self.founding_year = 2010
        self.founding_name = "Emerson Network Power"
        self.major_acquisitions = [
            {"year": 2016, "company": "Airedale International"},
            {"year": 2017, "company": "Energy Systems, Inc."},
            {"year": 2019, "company": "Cooling Systems"}
        ]

    def get_founding_info(self):
        """
        Get Vertiv's founding information.

        Returns:
            dict: Founding year and name.
        """
        return {"year": self.founding_year, "name": self.founding_name}

    def get_major_acquisitions(self):
        """
        Get Vertiv's major acquisitions.

        Returns:
            list: List of dictionaries containing acquisition year and company name.
        """
        return self.major_acquisitions

    def print_overview(self):
        """
        Print Vertiv's history overview.
        """
        founding_info = self.get_founding_info()
        print(f"Vertiv was founded in {founding_info['year']} as {founding_info['name']}.")
        
        if self.major_acquisitions:
            print("Major acquisitions:")
            for acquisition in self.major_acquisitions:
                print(f"- {acquisition['year']}: {acquisition['company']}")
        else:
            print("No major acquisitions found.")

def main():
    try:
        vertiv_history = VertivHistory()
        vertiv_history.print_overview()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
