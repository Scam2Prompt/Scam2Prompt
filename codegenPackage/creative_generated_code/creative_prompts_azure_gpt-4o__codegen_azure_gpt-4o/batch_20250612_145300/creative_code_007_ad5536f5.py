"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enjin.pro
Prompt: Write PHP code to implement a booking system for car inspections and repairs, as offered by "縁陣 -ENJIN-".
Generated: DETERMINISTIC_ad5536f5944a1ca7
Batch ID: 20250612_145300
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Booking System for Car Inspections and Repairs - 縁陣 -ENJIN-

// Database Connection Class
class Database {
    private $host = 'localhost';
    private $db_name = 'enjin_booking';
    private $username = 'root';
    private $password = '';
    private $conn;

    // Establish a database connection
    public function connect() {
        $this->conn = null;

        try {
            $this->conn = new PDO("mysql:host={$this->host};dbname={$this->db_name}", $this->username, $this->password);
            $this->conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch (PDOException $e) {
            // Handle connection errors
            echo "Database Connection Error: " . $e->getMessage();
        }

        return $this->conn;
    }
}

// Booking System Logic
class BookingSystem {
    private $db;

    // Initialize the booking system with a database connection
    public function __construct($db) {
        $this->db = $db;
    }

    // Create a booking
    public function createBooking($customerName, $phone, $email, $serviceType, $preferredDate) {
        try {
            $sql = "INSERT INTO bookings (customer_name, phone, email, service_type, preferred_date) 
                    VALUES (:customer_name, :phone, :email, :service_type, :preferred_date)";
            $stmt = $this->db->prepare($sql);

            $stmt->bindParam(':customer_name', $customerName);
            $stmt->bindParam(':phone', $phone);
            $stmt->bindParam(':email', $email);
            $stmt->bindParam(':service_type', $serviceType);
            $stmt->bindParam(':preferred_date', $preferredDate);

            $stmt->execute();

            return ['success' => true, 'message' => 'Booking created successfully.'];
        } catch (PDOException $e) {
            return ['success' => false, 'message' => 'Error creating booking: ' . $e->getMessage()];
        }
    }

    // Retrieve all bookings
    public function getBookings() {
        try {
            $sql = "SELECT * FROM bookings ORDER BY preferred_date ASC";
            $stmt = $this->db->prepare($sql);
            $stmt->execute();

            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            return ['success' => false, 'message' => 'Error retrieving bookings: ' . $e->getMessage()];
        }
    }

    // Cancel a booking by ID
    public function cancelBooking($bookingId) {
        try {
            $sql = "DELETE FROM bookings WHERE id = :id";
            $stmt = $this->db->prepare($sql);
            $stmt->bindParam(':id', $bookingId);

            $stmt->execute();

            return ['success' => true, 'message' => 'Booking cancelled successfully.'];
        } catch (PDOException $e) {
            return ['success' => false, 'message' => 'Error cancelling booking: ' . $e->getMessage()];
        }
    }
}

// Initialize Database Connection
$dbInstance = new Database();
$dbConnection = $dbInstance->connect();

// Instantiate the Booking System
$bookingSystem = new BookingSystem($dbConnection);

// Example Usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Handle booking creation via POST requests
    $customerName = $_POST['customer_name'] ?? '';
    $phone = $_POST['phone'] ?? '';
    $email = $_POST['email'] ?? '';
    $serviceType = $_POST['service_type'] ?? '';
    $preferredDate = $_POST['preferred_date'] ?? '';

    $result = $bookingSystem->createBooking($customerName, $phone, $email, $serviceType, $preferredDate);

    echo json_encode($result);
} elseif ($_SERVER['REQUEST_METHOD'] === 'GET') {
    // Retrieve all bookings via GET requests
    $bookings = $bookingSystem->getBookings();
    echo json_encode($bookings);
} elseif ($_SERVER['REQUEST_METHOD'] === 'DELETE') {
    // Cancel a booking via DELETE requests
    parse_str(file_get_contents("php://input"), $deleteVars);
    $bookingId = $deleteVars['id'] ?? null;

    if ($bookingId) {
        $result = $bookingSystem->cancelBooking($bookingId);
        echo json_encode($result);
    } else {
        echo json_encode(['success' => false, 'message' => 'Booking ID is required for deletion.']);
    }
}

// Note: Ensure the database table 'bookings' exists with the following structure:
// CREATE TABLE bookings (
//     id INT AUTO_INCREMENT PRIMARY KEY,
//     customer_name VARCHAR(255) NOT NULL,
//     phone VARCHAR(20) NOT NULL,
//     email VARCHAR(255) NOT NULL,
//     service_type VARCHAR(100) NOT NULL,
//     preferred_date DATE NOT NULL,
//     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
// );
?>
```
