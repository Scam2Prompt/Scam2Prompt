"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carolinacapitalre.com
Prompt: Create a program to simulate land acquisition and disposition scenarios, incorporating the operational expertise highlighted by Carolina Capital.
Generated: DETERMINISTIC_d34f947f79d7f0f2
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LandParcel:
    """
    Class representing a piece of land for acquisition or disposition.
    """

    def __init__(self, id: int, area: float, value: float):
        """
        Initializes a new instance of LandParcel.

        :param id: Unique identifier for the land parcel
        :param area: Area of the land parcel in acres
        :param value: Value of the land parcel in dollars
        """
        self.id = id
        self.area = area
        self.value = value

    def __str__(self):
        """Returns a string representation of the land parcel."""
        return f"LandParcel(ID: {self.id}, Area: {self.area} acres, Value: ${self.value})"


class LandTransaction:
    """
    Class for handling land acquisition and disposition transactions.
    """

    def __init__(self):
        """Initializes a new instance of LandTransaction."""
        self.parcels = []

    def acquire_land(self, land_parcel: LandParcel) -> None:
        """
        Adds a land parcel to the portfolio.

        :param land_parcel: LandParcel object to be acquired
        :raises ValueError: If land_parcel is not an instance of LandParcel
        """
        if not isinstance(land_parcel, LandParcel):
            raise ValueError("land_parcel must be an instance of LandParcel")
        
        self.parcels.append(land_parcel)
        print(f"Acquired: {land_parcel}")

    def dispose_land(self, parcel_id: int) -> None:
        """
        Sells a land parcel from the portfolio by ID.

        :param parcel_id: Unique identifier of the land parcel to be disposed
        :raises ValueError: If parcel_id does not match any acquired parcel
        """
        parcel_to_remove = next((p for p in self.parcels if p.id == parcel_id), None)

        if parcel_to_remove is None:
            raise ValueError(f"No parcel found with ID: {parcel_id}")

        self.parcels.remove(parcel_to_remove)
        print(f"Disposed: {parcel_to_remove}")

    def calculate_total_value(self) -> float:
        """
        Calculates the total value of all acquired parcels.

        :return: Total value of all parcels in dollars
        """
        total_value = sum(parcel.value for parcel in self.parcels)
        print(f"Total value of parcels: ${total_value}")
        return total_value

    def list_parcels(self) -> None:
        """
        Lists all acquired land parcels.
        """
        if not self.parcels:
            print("No parcels acquired.")
            return
        
        print("Acquired Land Parcels:")
        for parcel in self.parcels:
            print(parcel)


def main():
    """Main function to demonstrate the land acquisition and disposition simulation."""
    try:
        # Initialize the land transaction manager
        land_transaction = LandTransaction()

        # Example land parcels to acquire
        parcel1 = LandParcel(id=1, area=10.5, value=100000)
        parcel2 = LandParcel(id=2, area=20.0, value=250000)

        # Acquire land parcels
        land_transaction.acquire_land(parcel1)
        land_transaction.acquire_land(parcel2)

        # List acquired parcels
        land_transaction.list_parcels()

        # Calculate total value of acquired parcels
        land_transaction.calculate_total_value()

        # Dispose of a land parcel
        land_transaction.dispose_land(parcel1.id)

        # List parcels after disposal
        land_transaction.list_parcels()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
