"""
Generated Code Metadata:
========================
Original URL: https://www.luxuryvilladiamondcorfu.com
Prompt: Write a code snippet in PHP to manage villa bookings, including customer information, check-in and check-out dates, and villa amenities like heated pool and jacuzzi.
Generated: DETERMINISTIC_5c489c7f626288d3
Batch ID: 20250622_210655
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
 * Class VillaBookingManager
 * Manages villa bookings including customer information, check-in and check-out dates, and villa amenities.
 */
class VillaBookingManager {
    private $bookings = [];

    /**
     * Adds a new booking to the system.
     *
     * @param string $customerName Name of the customer
     * @param string $checkIn Date of check-in (YYYY-MM-DD)
     * @param string $checkOut Date of check-out (YYYY-MM-DD)
     * @param array $amenities List of amenities (e.g., heated pool, jacuzzi)
     * @throws Exception If the booking dates are invalid or if the booking overlaps with an existing one
     */
    public function addBooking($customerName, $checkIn, $checkOut, $amenities) {
        // Validate input
        if (empty($customerName) || empty($checkIn) || empty($checkOut)) {
            throw new Exception("Customer name, check-in, and check-out dates are required.");
        }

        $checkInDate = new DateTime($checkIn);
        $checkOutDate = new DateTime($checkOut);

        // Check if check-in date is before check-out date
        if ($checkInDate >= $checkOutDate) {
            throw new Exception("Check-in date must be before check-out date.");
        }

        // Check for overlapping bookings
        foreach ($this->bookings as $booking) {
            if ($this->isOverlapping($checkInDate, $checkOutDate, $booking['checkIn'], $booking['checkOut'])) {
                throw new Exception("Booking dates overlap with an existing booking.");
            }
        }

        // Add the booking
        $this->bookings[] = [
            'customerName' => $customerName,
            'checkIn' => $checkInDate,
            'checkOut' => $checkOutDate,
            'amenities' => $amenities
        ];
    }

    /**
     * Checks if two date ranges overlap.
     *
     * @param DateTime $start1 Start date of the first range
     * @param DateTime $end1 End date of the first range
     * @param DateTime $start2 Start date of the second range
     * @param DateTime $end2 End date of the second range
     * @return bool True if the ranges overlap, false otherwise
     */
    private function isOverlapping($start1, $end1, $start2, $end2) {
        return $start1 < $end2 && $start2 < $end1;
    }

    /**
     * Retrieves all bookings.
     *
     * @return array List of all bookings
     */
    public function getBookings() {
        return $this->bookings;
    }
}

// Example usage
try {
    $villaManager = new VillaBookingManager();
    $villaManager->addBooking("John Doe", "2023-10-01", "2023-10-05", ["heated pool", "jacuzzi"]);
    $villaManager->addBooking("Jane Smith", "2023-10-06", "2023-10-10", ["heated pool"]);
    
    // Print all bookings
    print_r($villaManager->getBookings());
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
?>
```
