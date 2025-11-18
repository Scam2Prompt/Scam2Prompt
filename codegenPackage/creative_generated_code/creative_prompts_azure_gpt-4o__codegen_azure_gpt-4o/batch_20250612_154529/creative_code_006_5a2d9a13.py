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
 * Hotel Booking Cost Calculator
 * Calculates the total cost of a hotel booking based on the number of nights, rooms, and guests.
 * Includes error handling for invalid inputs.
 */

// Function to calculate the total cost of the booking
function calculateHotelBookingCost($numNights, $numRooms, $numGuests, $costPerNightPerRoom) {
    // Validate inputs
    if (!is_int($numNights) || $numNights <= 0) {
        throw new InvalidArgumentException("Number of nights must be a positive integer.");
    }
    if (!is_int($numRooms) || $numRooms <= 0) {
        throw new InvalidArgumentException("Number of rooms must be a positive integer.");
    }
    if (!is_int($numGuests) || $numGuests <= 0) {
        throw new InvalidArgumentException("Number of guests must be a positive integer.");
    }
    if (!is_float($costPerNightPerRoom) || $costPerNightPerRoom <= 0) {
        throw new InvalidArgumentException("Cost per night per room must be a positive float.");
    }

    // Calculate total cost
    $totalCost = $numNights * $numRooms * $costPerNightPerRoom;

    return $totalCost;
}

// Input parameters (example values)
$numNights = 3; // Number of nights
$numRooms = 2;  // Number of rooms
$numGuests = 4; // Number of guests
$costPerNightPerRoom = 150.00; // Cost per room per night in USD

try {
    // Calculate total cost
    $totalCost = calculateHotelBookingCost($numNights, $numRooms, $numGuests, $costPerNightPerRoom);

    // Display the total cost
    echo "Hotel Booking Details:\n";
    echo "Number of nights: $numNights\n";
    echo "Number of rooms: $numRooms\n";
    echo "Number of guests: $numGuests\n";
    echo "Cost per night per room: $" . number_format($costPerNightPerRoom, 2) . "\n";
    echo "Total cost of booking: $" . number_format($totalCost, 2) . "\n";
} catch (InvalidArgumentException $e) {
    // Handle invalid inputs
    echo "Error: " . $e->getMessage() . "\n";
}

?>
```
