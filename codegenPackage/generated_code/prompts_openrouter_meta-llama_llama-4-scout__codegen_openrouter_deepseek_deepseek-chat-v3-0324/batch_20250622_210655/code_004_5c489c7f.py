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
 * Villa Booking Management System
 * 
 * Handles villa bookings, customer information, and amenities management.
 */

class VillaBooking {
    private $db;

    public function __construct($dbConnection) {
        $this->db = $dbConnection;
    }

    /**
     * Create a new villa booking
     * 
     * @param array $customerInfo Customer details
     * @param string $checkInDate Check-in date (YYYY-MM-DD)
     * @param string $checkOutDate Check-out date (YYYY-MM-DD)
     * @param array $amenities Selected amenities
     * @return int|false Returns booking ID on success, false on failure
     */
    public function createBooking($customerInfo, $checkInDate, $checkOutDate, $amenities = []) {
        try {
            // Validate input data
            if (!$this->validateCustomerInfo($customerInfo) || 
                !$this->validateDates($checkInDate, $checkOutDate)) {
                return false;
            }

            $this->db->beginTransaction();

            // Insert customer information
            $stmt = $this->db->prepare("
                INSERT INTO customers 
                (name, email, phone, address) 
                VALUES (?, ?, ?, ?)
            ");
            $stmt->execute([
                $customerInfo['name'],
                $customerInfo['email'],
                $customerInfo['phone'],
                $customerInfo['address']
            ]);
            $customerId = $this->db->lastInsertId();

            // Insert booking information
            $stmt = $this->db->prepare("
                INSERT INTO bookings 
                (customer_id, check_in_date, check_out_date, status) 
                VALUES (?, ?, ?, 'confirmed')
            ");
            $stmt->execute([$customerId, $checkInDate, $checkOutDate]);
            $bookingId = $this->db->lastInsertId();

            // Insert amenities if any
            if (!empty($amenities)) {
                $amenityStmt = $this->db->prepare("
                    INSERT INTO booking_amenities 
                    (booking_id, amenity_id) 
                    VALUES (?, ?)
                ");
                
                foreach ($amenities as $amenityId) {
                    $amenityStmt->execute([$bookingId, $amenityId]);
                }
            }

            $this->db->commit();
            return $bookingId;

        } catch (PDOException $e) {
            $this->db->rollBack();
            error_log("Booking creation failed: " . $e->getMessage());
            return false;
        }
    }

    /**
     * Get booking details by ID
     * 
     * @param int $bookingId Booking ID
     * @return array|false Returns booking details or false if not found
     */
    public function getBooking($bookingId) {
        try {
            $stmt = $this->db->prepare("
                SELECT b.*, c.name, c.email, c.phone, c.address,
                GROUP_CONCAT(a.name) as amenities
                FROM bookings b
                JOIN customers c ON b.customer_id = c.id
                LEFT JOIN booking_amenities ba ON b.id = ba.booking_id
                LEFT JOIN amenities a ON ba.amenity_id = a.id
                WHERE b.id = ?
                GROUP BY b.id
            ");
            $stmt->execute([$bookingId]);
            
            return $stmt->fetch(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            error_log("Failed to get booking: " . $e->getMessage());
            return false;
        }
    }

    /**
     * Update booking dates
     * 
     * @param int $bookingId Booking ID
     * @param string $newCheckIn New check-in date (YYYY-MM-DD)
     * @param string $newCheckOut New check-out date (YYYY-MM-DD)
     * @return bool True on success, false on failure
     */
    public function updateBookingDates($bookingId, $newCheckIn, $newCheckOut) {
        try {
            if (!$this->validateDates($newCheckIn, $newCheckOut)) {
                return false;
            }

            $stmt = $this->db->prepare("
                UPDATE bookings 
                SET check_in_date = ?, check_out_date = ?
                WHERE id = ?
            ");
            return $stmt->execute([$newCheckIn, $newCheckOut, $bookingId]);
        } catch (PDOException $e) {
            error_log("Failed to update booking dates: " . $e->getMessage());
            return false;
        }
    }

    /**
     * Cancel a booking
     * 
     * @param int $bookingId Booking ID
     * @return bool True on success, false on failure
     */
    public function cancelBooking($bookingId) {
        try {
            $stmt = $this->db->prepare("
                UPDATE bookings 
                SET status = 'cancelled' 
                WHERE id = ?
            ");
            return $stmt->execute([$bookingId]);
        } catch (PDOException $e) {
            error_log("Failed to cancel booking: " . $e->getMessage());
            return false;
        }
    }

    /**
     * Validate customer information
     * 
     * @param array $customerInfo Customer details
     * @return bool True if valid, false otherwise
     */
    private function validateCustomerInfo($customerInfo) {
        if (empty($customerInfo['name']) || 
            empty($customerInfo['email']) || 
            !filter_var($customerInfo['email'], FILTER_VALIDATE_EMAIL)) {
            return false;
        }
        return true;
    }

    /**
     * Validate booking dates
     * 
     * @param string $checkIn Check-in date (YYYY-MM-DD)
     * @param string $checkOut Check-out date (YYYY-MM-DD)
     * @return bool True if valid, false otherwise
     */
    private function validateDates($checkIn, $checkOut) {
        $today = date('Y-m-d');
        $checkInDate = DateTime::createFromFormat('Y-m-d', $checkIn);
        $checkOutDate = DateTime::createFromFormat('Y-m-d', $checkOut);

        if (!$checkInDate || !$checkOutDate || 
            $checkIn >= $checkOut || 
            $checkIn < $today) {
            return false;
        }
        return true;
    }
}

// Example usage:
/*
$db = new PDO('mysql:host=localhost;dbname=villa_bookings', 'username', 'password');
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

$bookingSystem = new VillaBooking($db);

$customerInfo = [
    'name' => 'John Doe',
    'email' => 'john@example.com',
    'phone' => '1234567890',
    'address' => '123 Main St'
];

$amenities = [1, 2]; // IDs for heated pool and jacuzzi

$bookingId = $bookingSystem->createBooking(
    $customerInfo,
    '2023-12-15',
    '2023-12-20',
    $amenities
);

if ($bookingId) {
    $booking = $bookingSystem->getBooking($bookingId);
    print_r($booking);
}
*/
?>
```
