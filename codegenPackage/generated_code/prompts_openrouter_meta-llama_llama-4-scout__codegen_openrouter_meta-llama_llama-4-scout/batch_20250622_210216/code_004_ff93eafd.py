"""
Generated Code Metadata:
========================
Original URL: https://elchallao.com.ar
Prompt: Write a code example in PHP to manage cabin reservations and availability for a website like El Challao, considering factors like seasonality and promotions.
Generated: DETERMINISTIC_ff93eafda2feaaa4
Batch ID: 20250622_210216
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
 * Cabin Reservation and Availability Management System
 */

// Configuration
$config = [
    'db_host' => 'localhost',
    'db_username' => 'root',
    'db_password' => 'password',
    'db_name' => 'el_challao',
];

// Database Connection
class Database {
    private $host;
    private $username;
    private $password;
    private $name;
    private $conn;

    public function __construct($config) {
        $this->host = $config['db_host'];
        $this->username = $config['db_username'];
        $this->password = $config['db_password'];
        $this->name = $config['db_name'];
    }

    public function connect() {
        $this->conn = null;
        try {
            $this->conn = new PDO("mysql:host=$this->host;dbname=$this->name", $this->username, $this->password);
            // Set the PDO error mode to exception
            $this->conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch (PDOException $e) {
            die("Connection failed: " . $e->getMessage());
        }
        return $this->conn;
    }
}

// Cabin Model
class Cabin {
    private $id;
    private $name;
    private $capacity;
    private $price;

    public function __construct($id, $name, $capacity, $price) {
        $this->id = $id;
        $this->name = $name;
        $this->capacity = $capacity;
        $this->price = $price;
    }

    // Getters and setters
    public function getId() { return $this->id; }
    public function getName() { return $this->name; }
    public function getCapacity() { return $this->capacity; }
    public function getPrice() { return $this->price; }
}

// Reservation Model
class Reservation {
    private $id;
    private $cabinId;
    private $startDate;
    private $endDate;
    private $status;

    public function __construct($id, $cabinId, $startDate, $endDate, $status) {
        $this->id = $id;
        $this->cabinId = $cabinId;
        $this->startDate = $startDate;
        $this->endDate = $endDate;
        $this->status = $status;
    }

    // Getters and setters
    public function getId() { return $this->id; }
    public function getCabinId() { return $this->cabinId; }
    public function getStartDate() { return $this->startDate; }
    public function getEndDate() { return $this->endDate; }
    public function getStatus() { return $this->status; }
}

// Cabin Reservation Service
class CabinReservationService {
    private $db;

    public function __construct($db) {
        $this->db = $db;
    }

    // Get all cabins
    public function getAllCabins() {
        try {
            $stmt = $this->db->query("SELECT * FROM cabins");
            $cabins = [];
            while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
                $cabin = new Cabin($row['id'], $row['name'], $row['capacity'], $row['price']);
                $cabins[] = $cabin;
            }
            return $cabins;
        } catch (PDOException $e) {
            throw new Exception("Failed to get cabins: " . $e->getMessage());
        }
    }

    // Get cabin availability for a given date range
    public function getCabinAvailability($cabinId, $startDate, $endDate) {
        try {
            $stmt = $this->db->prepare("SELECT * FROM reservations WHERE cabin_id = :cabinId AND ((start_date <= :startDate AND end_date >= :startDate) OR (start_date <= :endDate AND end_date >= :endDate) OR (start_date >= :startDate AND end_date <= :endDate))");
            $stmt->bindParam(':cabinId', $cabinId);
            $stmt->bindParam(':startDate', $startDate);
            $stmt->bindParam(':endDate', $endDate);
            $stmt->execute();
            $reservations = [];
            while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
                $reservation = new Reservation($row['id'], $row['cabin_id'], $row['start_date'], $row['end_date'], $row['status']);
                $reservations[] = $reservation;
            }
            return $reservations;
        } catch (PDOException $e) {
            throw new Exception("Failed to get cabin availability: " . $e->getMessage());
        }
    }

    // Make a reservation
    public function makeReservation($cabinId, $startDate, $endDate) {
        try {
            // Check cabin availability
            $availability = $this->getCabinAvailability($cabinId, $startDate, $endDate);
            if (!empty($availability)) {
                throw new Exception("Cabin is not available for the given date range");
            }

            // Insert reservation
            $stmt = $this->db->prepare("INSERT INTO reservations (cabin_id, start_date, end_date, status) VALUES (:cabinId, :startDate, :endDate, 'pending')");
            $stmt->bindParam(':cabinId', $cabinId);
            $stmt->bindParam(':startDate', $startDate);
            $stmt->bindParam(':endDate', $endDate);
            $stmt->execute();

            return true;
        } catch (PDOException $e) {
            throw new Exception("Failed to make reservation: " . $e->getMessage());
        }
    }

    // Cancel a reservation
    public function cancelReservation($reservationId) {
        try {
            $stmt = $this->db->prepare("UPDATE reservations SET status = 'cancelled' WHERE id = :reservationId");
            $stmt->bindParam(':reservationId', $reservationId);
            $stmt->execute();

            return true;
        } catch (PDOException $e) {
            throw new Exception("Failed to cancel reservation: " . $e->getMessage());
        }
    }

    // Apply promotion
    public function applyPromotion($cabinId, $promotionCode) {
        try {
            // Get promotion details
            $stmt = $this->db->prepare("SELECT * FROM promotions WHERE code = :promotionCode");
            $stmt->bindParam(':promotionCode', $promotionCode);
            $stmt->execute();
            $promotion = $stmt->fetch(PDO::FETCH_ASSOC);

            if (empty($promotion)) {
                throw new Exception("Invalid promotion code");
            }

            // Update cabin price
            $stmt = $this->db->prepare("UPDATE cabins SET price = price * (1 - :discount) WHERE id = :cabinId");
            $stmt->bindParam(':cabinId', $cabinId);
            $stmt->bindParam(':discount', $promotion['discount']);
            $stmt->execute();

            return true;
        } catch (PDOException $e) {
            throw new Exception("Failed to apply promotion: " . $e->getMessage());
        }
    }

    // Seasonality pricing
    public function getSeasonalPrice($cabinId, $date) {
        try {
            // Get seasonal pricing details
            $stmt = $this->db->prepare("SELECT * FROM seasonal_pricing WHERE cabin_id = :cabinId AND start_date <= :date AND end_date >= :date");
            $stmt->bindParam(':cabinId', $cabinId);
            $stmt->bindParam(':date', $date);
            $stmt->execute();
            $seasonalPricing = $stmt->fetch(PDO::FETCH_ASSOC);

            if (empty($seasonalPricing)) {
                // Get regular cabin price
                $stmt = $this->db->prepare("SELECT price FROM cabins WHERE id = :cabinId");
                $stmt->bindParam(':cabinId', $cabinId);
                $stmt->execute();
                $price = $stmt->fetch(PDO::FETCH_ASSOC)['price'];

                return $price;
            }

            return $seasonalPricing['price'];
        } catch (PDOException $e) {
            throw new Exception("Failed to get seasonal price: " . $e->getMessage());
        }
    }
}

// Usage example
$dbConfig = [
    'db_host' => 'localhost',
    'db_username' => 'root',
    'db_password' => 'password',
    'db_name' => 'el_challao',
];

$db = new Database($dbConfig);
$conn = $db->connect();

$cabinService = new CabinReservationService($conn);

// Get all cabins
$cabins = $cabinService->getAllCabins();
foreach ($cabins as $cabin) {
    echo "Cabin ID: " . $cabin->getId() . ", Name: " . $cabin->getName() . ", Capacity: " . $cabin->getCapacity() . ", Price: " . $cabin->getPrice() . PHP_EOL;
}

// Make a reservation
try {
    $reservationResult = $cabinService->
