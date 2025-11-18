"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kubitz.com.br
Prompt: Generate code for a waste management system that integrates a magnetic separator and an optical sorter, referencing the equipment described in Kubitz's automated processing configurations.
Generated: DETERMINISTIC_de823087593c6ea7
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class MagneticSeparator:
    """
    Class representing a magnetic separator.
    Used to extract ferrous metals from waste using magnetic separation.
    """

    def __init__(self):
        self.extraction_count = 0

    def separate_metals(self, waste_stream):
        """
        Separates ferrous metals from the waste stream.

        Args:
            waste_stream (list): List of waste items.

        Returns:
            tuple: (filtered_waste, extracted_metals)
                   filtered_waste: Waste stream without ferrous metals.
                   extracted_metals: List of ferrous metals extracted.
        """
        filtered_waste = []
        extracted_metals = []

        for item in waste_stream:
            if "ferrous_metal" in item:
                extracted_metals.append(item)
                self.extraction_count += 1
            else:
                filtered_waste.append(item)

        logging.info("Magnetic Separator: Extracted %d ferrous metal items.", len(extracted_metals))
        return filtered_waste, extracted_metals


class OpticalSorter:
    """
    Class representing an optical sorter.
    Used to sort waste based on material type using optical sensors.
    """

    def __init__(self):
        self.sort_count = 0

    def sort_waste(self, waste_stream):
        """
        Sorts waste into categories based on material type.

        Args:
            waste_stream (list): List of waste items.

        Returns:
            dict: Sorted waste categories.
        """
        sorted_waste = {"plastic": [], "paper": [], "glass": [], "others": []}

        for item in waste_stream:
            category = item.get("material", "others")
            if category in sorted_waste:
                sorted_waste[category].append(item)
                self.sort_count += 1
            else:
                sorted_waste["others"].append(item)

        logging.info("Optical Sorter: Sorted %d items.", self.sort_count)
        return sorted_waste


class WasteManagementSystem:
    """
    Main class for the waste management system.
    Integrates the Magnetic Separator and Optical Sorter equipment.
    """

    def __init__(self):
        self.magnetic_separator = MagneticSeparator()
        self.optical_sorter = OpticalSorter()

    def process_waste(self, waste_stream):
        """
        Processes a waste stream using the magnetic separator and optical sorter.

        Args:
            waste_stream (list): List of waste items.

        Returns:
            dict: Final processed waste categories and extracted metals.
        """
        try:
            # Step 1: Magnetic separation to extract ferrous metals
            filtered_waste, extracted_metals = self.magnetic_separator.separate_metals(waste_stream)

            # Step 2: Optical sorting for material categorization
            sorted_waste = self.optical_sorter.sort_waste(filtered_waste)

            # Combine results
            processed_result = {
                "sorted_waste": sorted_waste,
                "extracted_metals": extracted_metals
            }
            logging.info("Waste Management System: Completed processing waste stream.")
            return processed_result

        except Exception as e:
            logging.error(f"Error processing waste: {e}")
            return {"sorted_waste": {}, "extracted_metals": []}


# Example of waste stream data
if __name__ == "__main__":
    # Sample waste stream input
    waste_stream = [
        {"material": "plastic", "description": "Plastic bottle"},
        {"material": "glass", "description": "Glass jar"},
        {"material": "ferrous_metal", "description": "Iron nail"},
        {"material": "paper", "description": "Cardboard box"},
        {"material": "plastic", "description": "Plastic bag"},
        {"material": "ferrous_metal", "description": "Steel pipe"}
    ]

    # Instantiate and process the waste management system
    system = WasteManagementSystem()
    processed_waste = system.process_waste(waste_stream)

    # Output results
    logging.info("Final Processed Waste: %s", processed_waste)
```
