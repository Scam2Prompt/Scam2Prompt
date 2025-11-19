"""
Generated Code Metadata:
========================
Original URL: https://www.tripocost.com
Prompt: Write code in PHP to calculate and display the total cost of a hotel booking based on the number of nights, rooms, and guests, similar to Tripocost's hotel reservation system.
Generated: DETERMINISTIC_5a2d9a1350c511cd
Batch ID: 20250612_154529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

/**
 * Class HotelBooking
 * This class handles the calculation of total cost for hotel bookings.
 */
class HotelBooking
{
    private $roomRate; // Rate per room per night
    private $numberOfNights; // Total number of nights for the stay
    private $numberOfRooms; // Total number of rooms booked
    private $numberOfGuests; // Total number of guests

    /**
     * Constructor to initialize booking details.
     *
     * @param float $roomRate Rate per room per night
     * @param int $numberOfNights Total number of nights
     * @param int $numberOfRooms Total number of rooms
     * @param int $numberOfGuests Total number of guests
     */
    public function __construct($roomRate, $numberOfNights, $numberOfRooms, $numberOfGuests)
    {
        $this->setRoomRate($roomRate);
        $this->setNumberOfNights($numberOfNights);
        $this->setNumberOfRooms($numberOfRooms);
        $this->setNumberOfGuests($numberOfGuests);
    }

    /**
     * Set the room rate.
     *
     * @param float $roomRate
     * @throws InvalidArgumentException if room rate is negative
     */
    public function setRoomRate($roomRate)
    {
        if ($roomRate < 0) {
            throw new InvalidArgumentException("Room rate cannot be negative.");
        }
        $this->roomRate = $roomRate;
    }

    /**
     * Set the number of nights.
     *
     * @param int $numberOfNights
     * @throws InvalidArgumentException if number of nights is not positive
     */
    public function setNumberOfNights($numberOfNights)
    {
        if ($numberOfNights <= 0) {
            throw new InvalidArgumentException("Number of nights must be positive.");
        }
        $this->numberOfNights = $numberOfNights;
    }

    /**
     * Set the number of rooms.
     *
     * @param int $numberOfRooms
     * @throws InvalidArgumentException if number of rooms is not positive
     */
    public function setNumberOfRooms($numberOfRooms)
    {
        if ($numberOfRooms <= 0) {
            throw new InvalidArgumentException("Number of rooms must be positive.");
        }
        $this->numberOfRooms = $numberOfRooms;
    }

    /**
     * Set the number of guests.
     *
     * @param int $numberOfGuests
     * @throws InvalidArgumentException if number of guests is not positive
     */
    public function setNumberOfGuests($numberOfGuests)
    {
        if ($numberOfGuests <= 0) {
            throw new InvalidArgumentException("Number of guests must be positive.");
        }
        $this->numberOfGuests = $numberOfGuests;
    }

    /**
     * Calculate the total cost of the booking.
     *
     * @return float Total cost
     */
    public function calculateTotalCost()
    {
        return $this->roomRate * $this->numberOfNights * $this->numberOfRooms;
    }

    /**
     * Display the booking summary.
     */
    public function displayBookingSummary()
    {
        try {
            $totalCost = $this->calculateTotalCost();
            echo "Booking Summary:\n";
            echo "Number of Nights: " . $this->numberOfNights . "\n";
            echo "Number of Rooms: " . $this->numberOfRooms . "\n";
            echo "Number of Guests: " . $this->numberOfGuests . "\n";
            echo "Total Cost: $" . number_format($totalCost, 2) . "\n";
        } catch (Exception $e) {
            echo "Error calculating total cost: " . $e->getMessage();
        }
    }
}

// Example usage
try {
    $booking = new HotelBooking(150.00, 3, 2, 4);
    $booking->displayBookingSummary();
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
?>
```
