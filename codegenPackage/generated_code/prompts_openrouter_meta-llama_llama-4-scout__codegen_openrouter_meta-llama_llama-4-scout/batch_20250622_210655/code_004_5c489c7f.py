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
 */

// Configuration
$dbHost = 'localhost';
$dbUsername = 'root';
$dbPassword = '';
$dbName = 'villa_bookings';

// Create database connection
$conn = new mysqli($dbHost, $dbUsername, $dbPassword, $dbName);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

/**
 * Villa class
 */
class Villa {
    private $id;
    private $name;
    private $amenities;

    public function __construct($id, $name, $amenities) {
        $this->id = $id;
        $this->name = $name;
        $this->amenities = $amenities;
    }

    public function getId() {
        return $this->id;
    }

    public function getName() {
        return $this->name;
    }

    public function getAmenities() {
        return $this->amenities;
    }
}

/**
 * Customer class
 */
class Customer {
    private $id;
    private $name;
    private $email;
    private $phone;

    public function __construct($id, $name, $email, $phone) {
        $this->id = $id;
        $this->name = $name;
        $this->email = $email;
        $this->phone = $phone;
    }

    public function getId() {
        return $this->id;
    }

    public function getName() {
        return $this->name;
    }

    public function getEmail() {
        return $this->email;
    }

    public function getPhone() {
        return $this->phone;
    }
}

/**
 * Booking class
 */
class Booking {
    private $id;
    private $villaId;
    private $customerId;
    private $checkIn;
    private $checkOut;

    public function __construct($id, $villaId, $customerId, $checkIn, $checkOut) {
        $this->id = $id;
        $this->villaId = $villaId;
        $this->customerId = $customerId;
        $this->checkIn = $checkIn;
        $this->checkOut = $checkOut;
    }

    public function getId() {
        return $this->id;
    }

    public function getVillaId() {
        return $this->villaId;
    }

    public function getCustomerId() {
        return $this->customerId;
    }

    public function getCheckIn() {
        return $this->checkIn;
    }

    public function getCheckOut() {
        return $this->checkOut;
    }
}

// Villa amenities
$amenities = array(
    'heated_pool' => 'Heated Pool',
    'jacuzzi' => 'Jacuzzi'
);

// Create villa
function createVilla($name, $amenities) {
    global $conn;
    $sql = "INSERT INTO villas (name, amenities) VALUES (?, ?)";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("is", $name, json_encode($amenities));
    $stmt->execute();
    return $stmt->insert_id;
}

// Create customer
function createCustomer($name, $email, $phone) {
    global $conn;
    $sql = "INSERT INTO customers (name, email, phone) VALUES (?, ?, ?)";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("sss", $name, $email, $phone);
    $stmt->execute();
    return $stmt->insert_id;
}

// Create booking
function createBooking($villaId, $customerId, $checkIn, $checkOut) {
    global $conn;
    $sql = "INSERT INTO bookings (villa_id, customer_id, check_in, check_out) VALUES (?, ?, ?, ?)";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("iiss", $villaId, $customerId, $checkIn, $checkOut);
    $stmt->execute();
    return $stmt->insert_id;
}

// Get all villas
function getVillas() {
    global $conn;
    $sql = "SELECT * FROM villas";
    $result = $conn->query($sql);
    $villas = array();
    while ($row = $result->fetch_assoc()) {
        $villa = new Villa($row['id'], $row['name'], json_decode($row['amenities'], true));
        $villas[] = $villa;
    }
    return $villas;
}

// Get all customers
function getCustomers() {
    global $conn;
    $sql = "SELECT * FROM customers";
    $result = $conn->query($sql);
    $customers = array();
    while ($row = $result->fetch_assoc()) {
        $customer = new Customer($row['id'], $row['name'], $row['email'], $row['phone']);
        $customers[] = $customer;
    }
    return $customers;
}

// Get all bookings
function getBookings() {
    global $conn;
    $sql = "SELECT * FROM bookings";
    $result = $conn->query($sql);
    $bookings = array();
    while ($row = $result->fetch_assoc()) {
        $booking = new Booking($row['id'], $row['villa_id'], $row['customer_id'], $row['check_in'], $row['check_out']);
        $bookings[] = $booking;
    }
    return $bookings;
}

// Example usage
$villaId = createVilla('Luxury Villa', array('heated_pool' => true, 'jacuzzi' => true));
$customerId = createCustomer('John Doe', 'john@example.com', '1234567890');
$bookingId = createBooking($villaId, $customerId, '2024-09-16', '2024-09-20');

$villas = getVillas();
$customers = getCustomers();
$bookings = getBookings();

// Print results
echo "Villas:\n";
foreach ($villas as $villa) {
    echo "ID: " . $villa->getId() . ", Name: " . $villa->getName() . ", Amenities: ";
    print_r($villa->getAmenities());
    echo "\n";
}

echo "\nCustomers:\n";
foreach ($customers as $customer) {
    echo "ID: " . $customer->getId() . ", Name: " . $customer->getName() . ", Email: " . $customer->getEmail() . ", Phone: " . $customer->getPhone() . "\n";
}

echo "\nBookings:\n";
foreach ($bookings as $booking) {
    echo "ID: " . $booking->getId() . ", Villa ID: " . $booking->getVillaId() . ", Customer ID: " . $booking->getCustomerId() . ", Check-in: " . $booking->getCheckIn() . ", Check-out: " . $booking->getCheckOut() . "\n";
}

// Close database connection
$conn->close();

?>
```
