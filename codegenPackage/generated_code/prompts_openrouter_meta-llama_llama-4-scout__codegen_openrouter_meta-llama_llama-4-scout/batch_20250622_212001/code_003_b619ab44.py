"""
Generated Code Metadata:
========================
Original URL: https://panchapakesan.com
Prompt: Write a PHP code snippet to store ticket booking form data in a MySQL database, including fields for email address, phone number, and preferred communication method.
Generated: DETERMINISTIC_b619ab448c362936
Batch ID: 20250622_212001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

// Configuration
$db_host = 'your_host';
$db_username = 'your_username';
$db_password = 'your_password';
$db_name = 'your_database';

// Create connection
$conn = new mysqli($db_host, $db_username, $db_password, $db_name);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Function to store ticket booking form data
function storeTicketBookingData($email, $phone, $communicationMethod) {
    global $conn;

    // Validate input data
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        throw new Exception("Invalid email address");
    }

    if (!preg_match("/^[0-9]{3}-[0-9]{3}-[0-9]{4}$/", $phone)) {
        throw new Exception("Invalid phone number. Use format XXX-XXX-XXXX");
    }

    $communicationMethod = htmlspecialchars($communicationMethod);

    // SQL query to store data
    $sql = "INSERT INTO ticket_bookings (email, phone, communication_method) VALUES (?, ?, ?)";

    // Prepare statement
    $stmt = $conn->prepare($sql);

    // Check if prepare statement was successful
    if (!$stmt) {
        throw new Exception("Prepare statement failed: " . $conn->error);
    }

    // Bind parameters
    $stmt->bind_param("sss", $email, $phone, $communicationMethod);

    // Execute statement
    if (!$stmt->execute()) {
        throw new Exception("Execution failed: " . $stmt->error);
    }

    // Close statement and connection
    $stmt->close();
}

// Example usage
try {
    $email = $_POST['email'];
    $phone = $_POST['phone'];
    $communicationMethod = $_POST['communication_method'];

    storeTicketBookingData($email, $phone, $communicationMethod);

    http_response_code(201);
    echo json_encode(array("message" => "Ticket booking data stored successfully"));
} catch (Exception $e) {
    http_response_code(400);
    echo json_encode(array("message" => $e->getMessage()));
}

// Close connection
$conn->close();
```

```sql
-- Create table SQL query
CREATE TABLE ticket_bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    communication_method VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
