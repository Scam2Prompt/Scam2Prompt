"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://felipemunozreparaciones.es
Prompt: Write PHP code to create a backend system for storing customer service requests, including fields for service type (e.g., plumbing, electrical work), contact details, and preferred appointment time.
Generated: DETERMINISTIC_a0bda76dbfc9eea8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'service_requests');
define('DB_USER', 'root');
define('DB_PASSWORD', '');

// Function to establish a database connection
function getDatabaseConnection() {
    try {
        $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASSWORD);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        // Log error message and stop execution
        error_log("Database connection failed: " . $e->getMessage());
        die("Database connection error.");
    }
}

// Function to create the table for storing service requests
function createServiceRequestsTable() {
    try {
        $pdo = getDatabaseConnection();
        $sql = "
            CREATE TABLE IF NOT EXISTS service_requests (
                id INT AUTO_INCREMENT PRIMARY KEY,
                service_type VARCHAR(255) NOT NULL,
                contact_details TEXT NOT NULL,
                preferred_appointment_time DATETIME NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            ) ENGINE=InnoDB;
        ";
        $pdo->exec($sql);
    } catch (PDOException $e) {
        error_log("Failed to create table: " . $e->getMessage());
        die("Table creation error.");
    }
}

// Function to store a new service request
function storeServiceRequest($serviceType, $contactDetails, $appointmentTime) {
    try {
        $pdo = getDatabaseConnection();
        $sql = "
            INSERT INTO service_requests (service_type, contact_details, preferred_appointment_time)
            VALUES (:serviceType, :contactDetails, :appointmentTime)
        ";
        $stmt = $pdo->prepare($sql);
        $stmt->bindParam(':serviceType', $serviceType, PDO::PARAM_STR);
        $stmt->bindParam(':contactDetails', $contactDetails, PDO::PARAM_STR);
        $stmt->bindParam(':appointmentTime', $appointmentTime, PDO::PARAM_STR);

        if ($stmt->execute()) {
            return "Service request stored successfully.";
        } else {
            return "Failed to store service request.";
        }
    } catch (PDOException $e) {
        error_log("Failed to store service request: " . $e->getMessage());
        return "Error storing service request.";
    }
}

// Initialize the service_requests table
createServiceRequestsTable();

// Example usage: Storing a new service request
// Replace these values with actual data from a user form submission
$exampleServiceType = "Plumbing";
$exampleContactDetails = "John Doe, Phone: 123-456-7890, Email: john@example.com";
$exampleAppointmentTime = "2023-10-15 14:00:00";

echo storeServiceRequest($exampleServiceType, $exampleContactDetails, $exampleAppointmentTime);
?>
```
