"""
Generated Code Metadata:
========================
Original URL: https://www.curativesurgicalindustry.com
Prompt: Create a script to filter and display dental instruments by their product codes (e.g., 2312-2321, 1557-1575) as listed on the Curative Surgical Industry website.
Generated: DETERMINISTIC_fbd306431531d5b8
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# dental_instrument_filter.py

import re

class DentalInstrument:
    def __init__(self, product_code, name, description):
        """
        Initialize a DentalInstrument object.

        Args:
            product_code (str): The product code of the instrument.
            name (str): The name of the instrument.
            description (str): A brief description of the instrument.
        """
        self.product_code = product_code
        self.name = name
        self.description = description

class DentalInstrumentFilter:
    def __init__(self, instruments):
        """
        Initialize a DentalInstrumentFilter object.

        Args:
            instruments (list[DentalInstrument]): A list of DentalInstrument objects.
        """
        self.instruments = instruments

    def filter_by_product_code(self, product_code_range):
        """
        Filter dental instruments by a product code range.

        Args:
            product_code_range (str): A string representing a range of product codes (e.g., "2312-2321").

        Returns:
            list[DentalInstrument]: A list of DentalInstrument objects with product codes within the specified range.

        Raises:
            ValueError: If the product code range is invalid.
        """
        try:
            start, end = self._parse_product_code_range(product_code_range)
            return [instrument for instrument in self.instruments if start <= int(instrument.product_code) <= end]
        except ValueError as e:
            print(f"Invalid product code range: {e}")
            return []

    @staticmethod
    def _parse_product_code_range(product_code_range):
        """
        Parse a product code range string into start and end codes.

        Args:
            product_code_range (str): A string representing a range of product codes (e.g., "2312-2321").

        Returns:
            tuple[int, int]: A tuple containing the start and end product codes.

        Raises:
            ValueError: If the product code range is invalid.
        """
        match = re.match(r"(\d+)-(\d+)", product_code_range)
        if match:
            start, end = map(int, match.groups())
            return start, end
        raise ValueError("Invalid product code range")

def main():
    # Example dental instruments
    instruments = [
        DentalInstrument("2312", "Instrument 1", "Description 1"),
        DentalInstrument("2315", "Instrument 2", "Description 2"),
        DentalInstrument("2320", "Instrument 3", "Description 3"),
        DentalInstrument("1557", "Instrument 4", "Description 4"),
        DentalInstrument("1560", "Instrument 5", "Description 5"),
        DentalInstrument("1575", "Instrument 6", "Description 6"),
    ]

    filter = DentalInstrumentFilter(instruments)

    # Filter by product code range
    product_code_range = "2312-2321"
    filtered_instruments = filter.filter_by_product_code(product_code_range)

    # Display filtered instruments
    print(f"Filtered Instruments ({product_code_range}):")
    for instrument in filtered_instruments:
        print(f"Product Code: {instrument.product_code}, Name: {instrument.name}, Description: {instrument.description}")

    # Filter by another product code range
    product_code_range = "1557-1575"
    filtered_instruments = filter.filter_by_product_code(product_code_range)

    # Display filtered instruments
    print(f"\nFiltered Instruments ({product_code_range}):")
    for instrument in filtered_instruments:
        print(f"Product Code: {instrument.product_code}, Name: {instrument.name}, Description: {instrument.description}")

if __name__ == "__main__":
    main()
```
