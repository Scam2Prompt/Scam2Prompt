"""
Generated Code Metadata:
========================
Original URL: https://specialmetals.co.in
Prompt: Create a Python program to compare the specifications of Alloy Steel Pipes and Duplex Steel Pipes, using data from the Dinkar Alloys website.
Generated: DETERMINISTIC_4b41760ab60a35fd
Batch ID: 20250612_151611
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.dinkaralloys.com/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

class Pipe:
    def __init__(self, name, material, size, thickness, tensile_strength, yield_strength):
        """
        Initialize a Pipe object.

        Args:
            name (str): Name of the pipe.
            material (str): Material of the pipe.
            size (str): Size of the pipe.
            thickness (str): Thickness of the pipe.
            tensile_strength (str): Tensile strength of the pipe.
            yield_strength (str): Yield strength of the pipe.
        """
        self.name = name
        self.material = material
        self.size = size
        self.thickness = thickness
        self.tensile_strength = tensile_strength
        self.yield_strength = yield_strength

class PipeComparator:
    def __init__(self, url):
        """
        Initialize a PipeComparator object.

        Args:
            url (str): URL of the Dinkar Alloys website.
        """
        self.url = url
        self.alloy_steel_pipes = []
        self.duplex_steel_pipes = []

    def scrape_pipe_data(self):
        """
        Scrape pipe data from the Dinkar Alloys website.

        Returns:
            None
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an exception for HTTP errors
        except requests.exceptions.RequestException as err:
            print(f"Request Exception: {err}")
            return

        soup = BeautifulSoup(response.text, 'html.parser')

        # Assuming the website has tables with pipe data
        tables = soup.find_all('table')

        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                if len(cols) > 0:
                    name = cols[0].text.strip()
                    material = cols[1].text.strip()
                    size = cols[2].text.strip()
                    thickness = cols[3].text.strip()
                    tensile_strength = cols[4].text.strip()
                    yield_strength = cols[5].text.strip()

                    if "Alloy Steel" in material:
                        self.alloy_steel_pipes.append(Pipe(name, material, size, thickness, tensile_strength, yield_strength))
                    elif "Duplex Steel" in material:
                        self.duplex_steel_pipes.append(Pipe(name, material, size, thickness, tensile_strength, yield_strength))

    def compare_pipe_specs(self):
        """
        Compare the specifications of Alloy Steel Pipes and Duplex Steel Pipes.

        Returns:
            None
        """
        alloy_steel_df = pd.DataFrame([pipe.__dict__ for pipe in self.alloy_steel_pipes])
        duplex_steel_df = pd.DataFrame([pipe.__dict__ for pipe in self.duplex_steel_pipes])

        print("Alloy Steel Pipes:")
        print(alloy_steel_df)
        print("\nDuplex Steel Pipes:")
        print(duplex_steel_df)

        # Compare tensile strength
        alloy_steel_tensile_strength = alloy_steel_df['tensile_strength'].astype(float)
        duplex_steel_tensile_strength = duplex_steel_df['tensile_strength'].astype(float)

        print(f"\nAverage Tensile Strength of Alloy Steel Pipes: {alloy_steel_tensile_strength.mean()}")
        print(f"Average Tensile Strength of Duplex Steel Pipes: {duplex_steel_tensile_strength.mean()}")

def main():
    url = "https://www.dinkaralloys.com/"  # Replace with actual URL
    comparator = PipeComparator(url)
    comparator.scrape_pipe_data()
    comparator.compare_pipe_specs()

if __name__ == "__main__":
    main()
```
