"""
Generated Code Metadata:
========================
Original URL: https://movilabtorremedica2.com
Prompt: Create a simple pharmacy management system using a library like PHP and MySQL to track medications and hours of operation like Movilab's 24-hour pharmacy.
Generated: DETERMINISTIC_e482b7e2b510d431
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Database configuration
define('DB_SERVER', 'localhost');
define('DB_USERNAME', 'root');
define('DB_PASSWORD', '');
define('DB_NAME', 'pharmacy_management');

// Create database connection
$conn = new mysqli(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_NAME);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

/**
 * Medication class to handle medication operations
 */
class Medication {
    private $conn;

    public function __construct($conn) {
        $this->conn = $conn;
    }

    /**
     * Add a new medication to the inventory
     * @param string $name
     * @param string $description
     * @param int $quantity
     * @param float $price
     * @return bool
     */
    public function addMedication($name, $description, $quantity, $price) {
        $stmt = $this->conn->prepare("INSERT INTO medications (name, description, quantity, price) VALUES (?, ?, ?, ?)");
        $stmt->bind_param("ssid", $name, $description, $quantity, $price);
        return $stmt->execute();
    }

    /**
     * Update medication information
     * @param int $id
     * @param string $name
     * @param string $description
     * @param int $quantity
     * @param float $price
     * @return bool
     */
    public function updateMedication($id, $name, $description, $quantity, $price) {
        $stmt = $this->conn->prepare("UPDATE medications SET name=?, description=?, quantity=?, price=? WHERE id=?");
        $stmt->bind_param("ssidi", $name, $description, $quantity, $price, $id);
        return $stmt->execute();
    }

    /**
     * Delete a medication from inventory
     * @param int $id
     * @return bool
     */
    public function deleteMedication($id) {
        $stmt = $this->conn->prepare("DELETE FROM medications WHERE id=?");
        $stmt->bind_param("i", $id);
        return $stmt->execute();
    }

    /**
     * Get all medications
     * @return array
     */
    public function getAllMedications() {
        $result = $this->conn->query("SELECT * FROM medications");
        return $result->fetch_all(MYSQLI_ASSOC);
    }

    /**
     * Get medication by ID
     * @param int $id
     * @return array|null
     */
    public function getMedicationById($id) {
        $stmt = $this->conn->prepare("SELECT * FROM medications WHERE id=?");
        $stmt->bind_param("i", $id);
        $stmt->execute();
        $result = $stmt->get_result();
        return $result->fetch_assoc();
    }
}

/**
 * PharmacyHours class to handle operation hours
 */
class PharmacyHours {
    private $conn;

    public function __construct($conn) {
        $this->conn = $conn;
    }

    /**
     * Set pharmacy operation hours
     * @param string $day
     * @param string $open_time
     * @param string $close_time
     * @param bool $is_24hrs
     * @return bool
     */
    public function setHours($day, $open_time, $close_time, $is_24hrs) {
        // Check if hours already exist for this day
        $stmt = $this->conn->prepare("SELECT id FROM pharmacy_hours WHERE day=?");
        $stmt->bind_param("s", $day);
        $stmt->execute();
        $result = $stmt->get_result();

        if ($result->num_rows > 0) {
            // Update existing record
            $stmt = $this->conn->prepare("UPDATE pharmacy_hours SET open_time=?, close_time=?, is_24hrs=? WHERE day=?");
            $stmt->bind_param("ssis", $open_time, $close_time, $is_24hrs, $day);
        } else {
            // Insert new record
            $stmt = $this->conn->prepare("INSERT INTO pharmacy_hours (day, open_time, close_time, is_24hrs) VALUES (?, ?, ?, ?)");
            $stmt->bind_param("sssi", $day, $open_time, $close_time, $is_24hrs);
        }
        return $stmt->execute();
    }

    /**
     * Get all operation hours
     * @return array
     */
    public function getAllHours() {
        $result = $this->conn->query("SELECT * FROM pharmacy_hours ORDER BY FIELD(day, 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')");
        return $result->fetch_all(MYSQLI_ASSOC);
    }

    /**
     * Get operation hours for a specific day
     * @param string $day
     * @return array|null
     */
    public function getHoursByDay($day) {
        $stmt = $this->conn->prepare("SELECT * FROM pharmacy_hours WHERE day=?");
        $stmt->bind_param("s", $day);
        $stmt->execute();
        $result = $stmt->get_result();
        return $result->fetch_assoc();
    }
}

// Create instances of our classes
$medicationManager = new Medication($conn);
$pharmacyHoursManager = new PharmacyHours($conn);

// Example usage (would typically be in separate files in a real application)
/*
// Add a medication
$medicationManager->addMedication("Aspirin", "Pain reliever", 100, 5.99);

// Update a medication
$medicationManager->updateMedication(1, "Aspirin", "Pain reliever and fever reducer", 95, 5.99);

// Get all medications
$medications = $medicationManager->getAllMedications();

// Set pharmacy hours
$pharmacyHoursManager->setHours("Monday", "08:00", "20:00", 0);
$pharmacyHoursManager->setHours("Sunday", "00:00", "00:00", 1); // 24-hour day

// Get all hours
$hours = $pharmacyHoursManager->getAllHours();
*/

// Close connection when done
// $conn->close();
?>
```

```sql
-- SQL to create the database tables
CREATE DATABASE IF NOT EXISTS pharmacy_management;
USE pharmacy_management;

CREATE TABLE IF NOT EXISTS medications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS pharmacy_hours (
    id INT AUTO_INCREMENT PRIMARY KEY,
    day VARCHAR(10) NOT NULL,
    open_time TIME,
    close_time TIME,
    is_24hrs BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (day)
);
```
