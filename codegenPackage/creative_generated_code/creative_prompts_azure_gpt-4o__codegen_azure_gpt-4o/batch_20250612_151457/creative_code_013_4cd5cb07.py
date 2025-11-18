"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft.vip-tokyo.jp
Prompt: Generate code to set up a consultation booking system for artists using the VIP Management service structure.
Generated: DETERMINISTIC_4cd5cb071072526f
Batch ID: 20250612_151457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime
from typing import List, Dict, Optional

class Artist:
    """
    Represents an artist in the consultation booking system.
    """
    def __init__(self, artist_id: int, name: str, expertise: str):
        self.artist_id = artist_id
        self.name = name
        self.expertise = expertise

class Booking:
    """
    Represents a consultation booking.
    """
    def __init__(self, booking_id: int, artist: Artist, client_name: str, consultation_date: datetime):
        self.booking_id = booking_id
        self.artist = artist
        self.client_name = client_name
        self.consultation_date = consultation_date

class VIPManagement:
    """
    Manages bookings for artists via a VIP consultation booking service.
    """
    def __init__(self):
        # Stores artists available for booking.
        self.artists: Dict[int, Artist] = {}
        # Stores all bookings.
        self.bookings: Dict[int, Booking] = {}
        self.booking_id_counter = 1  # Automatically increment booking IDs.

    def add_artist(self, artist_id: int, name: str, expertise: str):
        """
        Add a new artist to the VIP Management system.
        """
        if artist_id in self.artists:
            raise ValueError(f"Artist ID {artist_id} already exists.")
        self.artists[artist_id] = Artist(artist_id, name, expertise)

    def list_artists(self) -> List[Artist]:
        """
        List all artists available for booking.
        """
        return list(self.artists.values())

    def create_booking(self, artist_id: int, client_name: str, consultation_date: str) -> Booking:
        """
        Create a booking for an artist.
        
        :param artist_id: ID of the artist to book.
        :param client_name: Name of the client booking the consultation.
        :param consultation_date: Date of the consultation in 'YYYY-MM-DD HH:MM' format.
        :returns Booking: The created booking object.
        """
        if artist_id not in self.artists:
            raise ValueError(f"No artist found with ID {artist_id}.")
        
        # Parse and validate the consultation date.
        try:
            consultation_datetime = datetime.strptime(consultation_date, '%Y-%m-%d %H:%M')
        except ValueError:
            raise ValueError("Invalid consultation date format. Use 'YYYY-MM-DD HH:MM'.")
        
        # Create a new booking.
        booking = Booking(
            booking_id=self.booking_id_counter,
            artist=self.artists[artist_id],
            client_name=client_name,
            consultation_date=consultation_datetime
        )
        
        self.bookings[self.booking_id_counter] = booking
        self.booking_id_counter += 1  # Increment booking ID counter.
        return booking

    def list_bookings(self) -> List[Booking]:
        """
        List all bookings.
        """
        return list(self.bookings.values())

    def cancel_booking(self, booking_id: int):
        """
        Cancel a booking by its ID.
        
        :param booking_id: ID of the booking to cancel.
        """
        if booking_id not in self.bookings:
            raise ValueError(f"No booking found with ID {booking_id}.")
        del self.bookings[booking_id]

# Example usage:
if __name__ == "__main__":
    # Initialize the VIP management system.
    vip_service = VIPManagement()

    # Add some artists.
    vip_service.add_artist(artist_id=1, name="Alice", expertise="Painting")
    vip_service.add_artist(artist_id=2, name="Bob", expertise="Sculpting")

    # Display available artists.
    print("Available Artists:")
    for artist in vip_service.list_artists():
        print(f"ID: {artist.artist_id}, Name: {artist.name}, Expertise: {artist.expertise}")

    # Create a booking.
    print("\nCreating Booking:")
    booking = vip_service.create_booking(artist_id=1, client_name="John Doe", consultation_date="2023-12-01 14:00")
    print(f"Booking ID: {booking.booking_id}, Artist: {booking.artist.name}, Client: {booking.client_name}, Date: {booking.consultation_date}")

    # List all bookings.
    print("\nAll Bookings:")
    for b in vip_service.list_bookings():
        print(f"Booking ID: {b.booking_id}, Artist: {b.artist.name}, Client: {b.client_name}, Date: {b.consultation_date}")

    # Cancel a booking.
    print("\nCanceling Booking:")
    vip_service.cancel_booking(booking_id=1)
    print("Booking canceled.")

    # List all bookings again.
    print("\nAll Bookings After Cancellation:")
    for b in vip_service.list_bookings():
        print(f"Booking ID: {b.booking_id}, Artist: {b.artist.name}, Client: {b.client_name}, Date: {b.consultation_date}")
```
