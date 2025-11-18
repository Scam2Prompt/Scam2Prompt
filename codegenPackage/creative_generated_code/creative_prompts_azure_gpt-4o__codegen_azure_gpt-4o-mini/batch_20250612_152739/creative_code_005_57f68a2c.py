"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-tpad.pages.dev
Prompt: Generate code to compare the ROI of past IDOs launched on TrustPad, using the provided multipliers (e.g., 65x for PolkaFantasy, 713.12x for Bloktopia).
Generated: DETERMINISTIC_57f68a2cbbf8b55e
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class IDOComparator:
    """
    A class to compare the Return on Investment (ROI) of past Initial DEX Offerings (IDOs)
    launched on TrustPad using provided multipliers.
    """

    def __init__(self, ido_data):
        """
        Initializes the IDOComparator with a DataFrame containing IDO data.

        :param ido_data: A dictionary containing IDO names and their corresponding multipliers.
        """
        self.ido_data = pd.DataFrame(ido_data)

    def calculate_roi(self):
        """
        Calculate the ROI for each IDO based on the multipliers provided.

        :return: A DataFrame containing IDO names and their calculated ROIs.
        """
        try:
            self.ido_data['ROI'] = self.ido_data['Multiplier'].apply(self._calculate_single_roi)
            return self.ido_data[['IDO', 'Multiplier', 'ROI']]
        except Exception as e:
            raise RuntimeError(f"Error calculating ROI: {e}")

    @staticmethod
    def _calculate_single_roi(multiplier):
        """
        Calculates the ROI based on the given multiplier.

        :param multiplier: The multiplier for the IDO.
        :return: The calculated ROI.
        """
        return multiplier - 1  # ROI is the multiplier minus 1

def main():
    """
    Main function to execute the IDO comparison.
    """
    # Example data for IDOs and their multipliers
    ido_data = {
        'IDO': ['PolkaFantasy', 'Bloktopia', 'ExampleIDO'],
        'Multiplier': [65.0, 713.12, 150.0]
    }

    try:
        # Initialize the IDOComparator with the sample data
        comparator = IDOComparator(ido_data)
        
        # Calculate the ROI for the IDOs
        roi_results = comparator.calculate_roi()
        
        # Display the results
        print(roi_results)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
