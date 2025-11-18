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
// Including the database configuration file
include 'config.php';

// Check if the request method is POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Get the incoming data and sanitize it
    $service_type = filter_input(INPUT_POST, 'service_type', FILTER_SANITIZE_STRING);
    $customer_name = filter_input(INPUT_POST, 'customer_name', FILTER_SANITIZE_STRING);
    $contact_details = filter_input(INPUT_POST, 'contact_details', FILTER_SANITIZE_STRING);
    $preferred_time = filter_input(INPUT_POST, 'preferred_time', FILTER_SANITIZE_STRING);

    // Validate the input fields
    if (empty($service_type) || empty($customer_name) || empty($contact_details) || empty($preferred_time)) {
        http_response_code(400);
        echo json_encode(["error" => "All fields are required."]);
        exit;
    }

    // Prepare SQL statement to prevent SQL injection
    $stmt = $conn->prepare("INSERT INTO service_requests (service_type, customer_name, contact_details, preferred_time) VALUES (?, ?, ?, ?)");
    
    // Bind parameters to the SQL query
    $stmt->bind_param("ssss", $service_type, $customer_name, $contact_details, $preferred_time);

    // Execute the statement and check for errors
    if ($stmt->execute()) {
        http_response_code(201);
        echo json_encode(["success" => "Service request created successfully."]);
    } else {
        http_response_code(500);
        echo json_encode(["error" => "Failed to create service request."]);
    }

    // Close the statement
    $stmt->close();
} else {
    // If the request method is not POST, return a 405 Method Not Allowed
    http_response_code(405);
    echo json_encode(["error" => "Method not allowed."]);
}

// Close the database connection
$conn->close();
?>
```

```php
<?php
// config.php - Database configuration file
$servername = "localhost"; // Database server
$username = "username"; // Database username
$password = "password"; // Database password
$dbname = "service_requests_db"; // Database name

// Create a connection to the database
$conn = new mysqli($servername, $username, $password, $dbname);

// Check the connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
```

```sql
-- SQL to create the service_requests table
CREATE TABLE service_requests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    service_type VARCHAR(255) NOT NULL,
    customer_name VARCHAR(255) NOT NULL,
    contact_details VARCHAR(255) NOT NULL,
    preferred_time DATETIME NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
