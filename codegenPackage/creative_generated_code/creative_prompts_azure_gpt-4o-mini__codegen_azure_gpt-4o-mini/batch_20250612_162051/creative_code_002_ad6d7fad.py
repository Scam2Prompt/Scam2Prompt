"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://evinblue.com
Prompt: What are the best practices for using DEF in diesel engines, specifically for brands like Mercedes Benz and Tata?
Generated: DETERMINISTIC_ad6d7fad973c565e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DEFUsageGuide:
    """
    Class to provide best practices for using Diesel Exhaust Fluid (DEF) in diesel engines.
    Specifically tailored for Mercedes Benz and Tata brands.
    """

    def __init__(self, brand):
        """
        Initializes the DEFUsageGuide with the specified brand.

        :param brand: str - The brand of the diesel engine (Mercedes Benz or Tata)
        """
        self.brand = brand
        self.best_practices = self._set_best_practices()

    def _set_best_practices(self):
        """
        Sets the best practices for using DEF based on the brand.

        :return: dict - A dictionary of best practices for the specified brand.
        """
        practices = {
            "Mercedes Benz": [
                "Always use high-quality DEF that meets ISO 22241 standards.",
                "Store DEF in a cool, dry place to prevent contamination.",
                "Regularly check DEF levels and refill as necessary, especially before long trips.",
                "Avoid letting the DEF tank run dry; this can lead to engine derating.",
                "Use DEF within the recommended shelf life (usually around 1 year)."
            ],
            "Tata": [
                "Choose DEF from authorized dealers to ensure quality.",
                "Ensure the DEF tank is sealed properly to avoid contamination.",
                "Monitor DEF consumption regularly as per vehicle usage.",
                "Do not mix DEF with other fluids or fuels; use only DEF for the DEF tank.",
                "Follow manufacturer guidelines regarding DEF usage and maintenance."
            ]
        }
        
        # Return best practices or indicate if the brand is unsupported
        return practices.get(self.brand, ["Brand not supported. Please use 'Mercedes Benz' or 'Tata'."])

    def display_best_practices(self):
        """
        Displays the best practices for using DEF for the specified brand.

        :return: None
        """
        if isinstance(self.best_practices, list):
            print(f"Best practices for using DEF in {self.brand}:")
            for practice in self.best_practices:
                print(f"- {practice}")
        else:
            print(self.best_practices)


def main():
    """
    Main function to run the DEF usage guide.
    
    :return: None
    """
    try:
        # User input for vehicle brand
        brand = input("Enter the brand (Mercedes Benz or Tata): ").strip()
        guide = DEFUsageGuide(brand)
        guide.display_best_practices()
    
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
