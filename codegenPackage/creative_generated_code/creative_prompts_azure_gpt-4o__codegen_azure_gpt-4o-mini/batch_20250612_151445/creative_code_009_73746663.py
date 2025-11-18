"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demoablabs.com
Prompt: Write a script to calculate fees for asbestos sample preparation and analysis, considering A & B Labs' step rules for overloading and layer-specific charges.
Generated: DETERMINISTIC_737466636139f8b1
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AsbestosAnalysis:
    """
    A class to calculate fees for asbestos sample preparation and analysis.
    """

    # Constants for fee calculation
    BASE_PREPARATION_FEE = 50.00  # Base fee for sample preparation
    BASE_ANALYSIS_FEE = 100.00     # Base fee for sample analysis
    OVERLOAD_CHARGE = 25.00        # Additional charge for overload samples
    LAYER_SPECIFIC_FEES = {
        'Chrysotile': 30.00,
        'Amosite': 45.00,
        'Crocidolite': 60.00,
    }

    def __init__(self, samples):
        """
        Initializes the AsbestosAnalysis class with a list of samples.

        :param samples: A list of tuples, where each tuple contains the type of asbestos and the number of layers.
        """
        self.samples = samples

    def calculate_fees(self):
        """
        Calculate total fees for all samples based on A & B Labs' rules.

        :return: Total calculated fees.
        """
        total_fees = 0.0
        
        try:
            for sample in self.samples:
                asbestos_type, layers = sample

                # Check if the layer count is valid
                if not isinstance(layers, int) or layers < 1:
                    raise ValueError("Layer count must be a positive integer.")

                # Calculate preparation fee
                preparation_fee = self.BASE_PREPARATION_FEE

                # Calculate analysis fee
                analysis_fee = self.BASE_ANALYSIS_FEE
               
                # Check if the asbestos type is valid
                if asbestos_type not in self.LAYER_SPECIFIC_FEES:
                    raise ValueError(f"Unknown asbestos type: {asbestos_type}")

                # Calculate layer-specific charges
                layer_specific_fee = self.LAYER_SPECIFIC_FEES[asbestos_type] * layers

                # Check for overload and apply additional charges
                if layers > 5:  # Assuming 5 layers as the threshold for overload
                    analysis_fee += self.OVERLOAD_CHARGE

                # Sum all fees for the current sample
                total_fees += (preparation_fee + analysis_fee + layer_specific_fee)

            return total_fees
        
        except ValueError as ve:
            print(f"Error: {ve}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Define a list of samples (asbestos type, number of layers)
    sample_data = [
        ('Chrysotile', 3),
        ('Amosite', 6),
        ('Crocidolite', 2),
        ('Chrysotile', 0),  # This will trigger an error due to invalid layer count
    ]

    analysis = AsbestosAnalysis(samples=sample_data)
    total_fees = analysis.calculate_fees()

    if total_fees is not None:
        print(f"Total fees for analysis: ${total_fees:.2f}")
```
