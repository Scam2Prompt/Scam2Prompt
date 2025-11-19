"""
Generated Code Metadata:
========================
Original URL: https://amarhospital.com
Prompt: Design a PHP script that manages 24/7 emergency service requests, taking inspiration from the emergency services offered at Amar Hospital in Patiala.
Generated: DETERMINISTIC_bfb5b0539013caee
Batch ID: 20250612_155840
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
 * Emergency Service Request Management System
 * This script handles 24/7 emergency service requests for Amar Hospital, Patiala.
 * It allows users to submit requests and view the status of their requests.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'emergency_service');
define('DB_USER', 'root');
define('DB_PASS', 'password'); // Change to your database password

// Create a connection to the database
function getDbConnection() {
    try {
        $conn = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $conn;
    } catch (PDOException $e) {
        die("Database connection failed: " . $e->getMessage());
    }
}

// Function to submit a new emergency request
function submitEmergencyRequest($name, $contact, $description) {
    $conn = getDbConnection();
    $sql = "INSERT INTO emergency_requests (name, contact, description, status, created_at) VALUES (:name, :contact, :description, 'Pending', NOW())";
    
    try {
        $stmt = $conn->prepare($sql);
        $stmt->bindParam(':name', $name);
        $stmt->bindParam(':contact', $contact);
        $stmt->bindParam(':description', $description);
        $stmt->execute();
        return $conn->lastInsertId(); // Return the ID of the new request
    } catch (PDOException $e) {
        die("Error submitting request: " . $e->getMessage());
    }
}

// Function to get all emergency requests
function getEmergencyRequests() {
    $conn = getDbConnection();
    $sql = "SELECT * FROM emergency_requests ORDER BY created_at DESC";
    
    try {
        $stmt = $conn->prepare($sql);
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC); // Return all requests as an associative array
    } catch (PDOException $e) {
        die("Error fetching requests: " . $e->getMessage());
    }
}

// Function to update the status of a request
function updateRequestStatus($requestId, $status) {
    $conn = getDbConnection();
    $sql = "UPDATE emergency_requests SET status = :status WHERE id = :id";
    
    try {
        $stmt = $conn->prepare($sql);
        $stmt->bindParam(':status', $status);
        $stmt->bindParam(':id', $requestId);
        $stmt->execute();
        return $stmt->rowCount(); // Return the number of affected rows
    } catch (PDOException $e) {
        die("Error updating request status: " . $e->getMessage());
    }
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Handle form submission for new requests
    $name = $_POST['name'] ?? '';
    $contact = $_POST['contact'] ?? '';
    $description = $_POST['description'] ?? '';

    if (!empty($name) && !empty($contact) && !empty($description)) {
        $requestId = submitEmergencyRequest($name, $contact, $description);
        echo "Emergency request submitted successfully. Your request ID is: " . htmlspecialchars($requestId);
    } else {
        echo "All fields are required.";
    }
}

// Fetch and display all emergency requests
$requests = getEmergencyRequests();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Emergency Service Requests</title>
</head>
<body>
    <h1>Emergency Service Requests</h1>
    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="contact">Contact:</label>
        <input type="text" id="contact" name="contact" required>
        <br>
        <label for="description">Description:</label>
        <textarea id="description" name="description" required></textarea>
        <br>
        <button type="submit">Submit Request</button>
    </form>

    <h2>Current Requests</h2>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Contact</th>
            <th>Description</th>
            <th>Status</th>
            <th>Created At</th>
        </tr>
        <?php foreach ($requests as $request): ?>
            <tr>
                <td><?php echo htmlspecialchars($request['id']); ?></td>
                <td><?php echo htmlspecialchars($request['name']); ?></td>
                <td><?php echo htmlspecialchars($request['contact']); ?></td>
                <td><?php echo htmlspecialchars($request['description']); ?></td>
                <td><?php echo htmlspecialchars($request['status']); ?></td>
                <td><?php echo htmlspecialchars($request['created_at']); ?></td>
            </tr>
        <?php endforeach; ?>
    </table>
</body>
</html>
```

**Note:** Ensure that you create a MySQL database named `emergency_service` and a table named `emergency_requests` with the following structure before running the script:

```sql
CREATE TABLE emergency_requests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    contact VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    status ENUM('Pending', 'In Progress', 'Completed') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
