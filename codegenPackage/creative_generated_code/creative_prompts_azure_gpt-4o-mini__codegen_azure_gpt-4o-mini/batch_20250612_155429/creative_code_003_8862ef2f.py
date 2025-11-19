"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casaamalfitana.com
Prompt: Create a library function that allows users to select table types and zones for a restaurant reservation, similar to the options provided by Casa Amalfitana.
Generated: DETERMINISTIC_8862ef2f40a9e360
Batch ID: 20250612_155429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ReservationError(Exception):
    """Custom exception for reservation-related errors."""
    pass

class TableType:
    """Enum class for defining table types."""
    INDOOR = "Indoor"
    OUTDOOR = "Outdoor"
    PRIVATE = "Private"

class Zone:
    """Enum class for defining restaurant zones."""
    FRONT = "Front"
    BACK = "Back"
    SIDE = "Side"

class Reservation:
    """Class to manage restaurant reservations."""
    
    def __init__(self):
        """Initialize the reservation manager with available table types and zones."""
        self.table_types = [TableType.INDOOR, TableType.OUTDOOR, TableType.PRIVATE]
        self.zones = [Zone.FRONT, Zone.BACK, Zone.SIDE]
    
    def select_table(self, table_type: str, zone: str):
        """
        Select a table type and zone for a reservation.

        Parameters:
        - table_type (str): The type of table requested.
        - zone (str): The zone of the restaurant requested.

        Raises:
        - ReservationError: If the table type or zone is invalid.
        
        Returns:
        - dict: A confirmation of the selected table type and zone.
        """
        if table_type not in self.table_types:
            raise ReservationError(f"Invalid table type: {table_type}. Choose from {self.table_types}.")
        
        if zone not in self.zones:
            raise ReservationError(f"Invalid zone: {zone}. Choose from {self.zones}.")
        
        return {"table_type": table_type, "zone": zone}

def main():
    """Main function to demonstrate reservation selection."""
    reservation_system = Reservation()
    
    try:
        # Example of selecting a table type and zone
        selected_reservation = reservation_system.select_table(TableType.OUTDOOR, Zone.FRONT)
        print(f"Reservation successful: {selected_reservation}")
    except ReservationError as e:
        print(f"Reservation failed: {e}")

if __name__ == "__main__":
    main()
```
