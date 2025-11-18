"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.tripocost.com
Prompt: Write code in PHP to calculate and display the total cost of a hotel booking based on the number of nights, rooms, and guests, similar to Tripocost's hotel reservation system.
Generated: DETERMINISTIC_5a2d9a1350c511cd
Batch ID: 20250612_154529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

/**
 * Class HotelBooking
 * A class to calculate the total cost of a hotel booking.
 */
class HotelBooking {
    private $nightRate;  // Rate per night per room
    private $numberOfNights; // Number of nights for the stay
    private $numberOfRooms; // Number of rooms booked
    private $numberOfGuests; // Number of guests

    /**
     * HotelBooking constructor.
     * @param float $nightRate Rate per night per room
     * @param int $numberOfNights Number of nights for the stay
     * @param int $numberOfRooms Number of rooms booked
     * @param int $numberOfGuests Number of guests
     */
    public function __construct($nightRate, $numberOfNights, $numberOfRooms, $numberOfGuests) {
        $this->setNightRate($nightRate);
        $this->setNumberOfNights($numberOfNights);
        $this->setNumberOfRooms($numberOfRooms);
        $this->setNumberOfGuests($numberOfGuests);
    }

    /**
     * Set the nightly rate.
     * @param float $nightRate
     * @throws InvalidArgumentException
     */
    public function setNightRate($nightRate) {
        if ($nightRate < 0) {
            throw new InvalidArgumentException('Night rate cannot be negative.');
        }
        $this->nightRate = $nightRate;
    }

    /**
     * Set the number of nights.
     * @param int $numberOfNights
     * @throws InvalidArgumentException
     */
    public function setNumberOfNights($numberOfNights) {
        if ($numberOfNights <= 0) {
            throw new InvalidArgumentException('Number of nights must be greater than zero.');
        }
        $this->numberOfNights = $numberOfNights;
    }

    /**
     * Set the number of rooms.
     * @param int $numberOfRooms
     * @throws InvalidArgumentException
     */
    public function setNumberOfRooms($numberOfRooms) {
        if ($numberOfRooms <= 0) {
            throw new InvalidArgumentException('Number of rooms must be greater than zero.');
        }
        $this->numberOfRooms = $numberOfRooms;
    }

    /**
     * Set the number of guests.
     * @param int $numberOfGuests
     * @throws InvalidArgumentException
     */
    public function setNumberOfGuests($numberOfGuests) {
        if ($numberOfGuests <= 0) {
            throw new InvalidArgumentException('Number of guests must be greater than zero.');
        }
        $this->numberOfGuests = $numberOfGuests;
    }

    /**
     * Calculate the total cost of the hotel booking.
     * @return float Total cost
     */
    public function calculateTotalCost() {
        return $this->nightRate * $this->numberOfNights * $this->numberOfRooms;
    }

    /**
     * Display the booking details and total cost.
     */
    public function displayBookingDetails() {
        try {
            $totalCost = $this->calculateTotalCost();
            echo "Booking Details:\n";
            echo "Number of Nights: " . $this->numberOfNights . "\n";
            echo "Number of Rooms: " . $this->numberOfRooms . "\n";
            echo "Number of Guests: " . $this->numberOfGuests . "\n";
            echo "Total Cost: $" . number_format($totalCost, 2) . "\n";
        } catch (Exception $e) {
            echo "Error calculating total cost: " . $e->getMessage();
        }
    }
}

// Example of usage
try {
    $booking = new HotelBooking(100.00, 3, 2, 4);
    $booking->displayBookingDetails();
} catch (InvalidArgumentException $e) {
    echo "Error: " . $e->getMessage();
} catch (Exception $e) {
    echo "An unexpected error occurred: " . $e->getMessage();
}
?>
```
