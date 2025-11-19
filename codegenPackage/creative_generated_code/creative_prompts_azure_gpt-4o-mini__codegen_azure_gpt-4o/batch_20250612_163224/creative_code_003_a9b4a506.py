"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pneusml.com
Prompt: Develop a PHP script that allows users to submit a request for a tire inspection and alignment service, similar to the services offered by Pneus ML.
Generated: DETERMINISTIC_a9b4a5061e641ec9
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// File: tire_service_request.php

// Enable error reporting for development (disable in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Database configuration - replace these with your actual database credentials
define('DB_HOST', 'localhost');
define('DB_NAME', 'tire_service');
define('DB_USER', 'root');
define('DB_PASS', 'password');

// Connect to the database
function connectToDatabase() {
    try {
        $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        die("Database connection failed: " . $e->getMessage());
    }
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate form inputs
    $name = htmlspecialchars(trim($_POST['name'] ?? ''));
    $email = filter_var($_POST['email'] ?? '', FILTER_VALIDATE_EMAIL);
    $phone = htmlspecialchars(trim($_POST['phone'] ?? ''));
    $preferred_date = htmlspecialchars(trim($_POST['preferred_date'] ?? ''));

    // Check for required fields
    if (!$name || !$email || !$phone || !$preferred_date) {
        die("All fields are required. Please go back and fill in the form completely.");
    }

    // Save the request to the database
    try {
        $pdo = connectToDatabase();
        $stmt = $pdo->prepare("INSERT INTO service_requests (name, email, phone, preferred_date, created_at) VALUES (:name, :email, :phone, :preferred_date, NOW())");
        $stmt->bindParam(':name', $name);
        $stmt->bindParam(':email', $email);
        $stmt->bindParam(':phone', $phone);
        $stmt->bindParam(':preferred_date', $preferred_date);
        $stmt->execute();
        echo "Your service request has been submitted successfully!";
    } catch (Exception $e) {
        die("Failed to save your request. Please try again later. Error: " . $e->getMessage());
    }
}

// HTML form for service request submission
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tire Service Request</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .form-container { max-width: 600px; margin: 50px auto; padding: 20px; border: 1px solid #ccc; border-radius: 8px; }
        .form-container input, .form-container button { width: 100%; margin-bottom: 10px; padding: 10px; }
        .form-container button { background-color: #007BFF; color: white; border: none; cursor: pointer; }
        .form-container button:hover { background-color: #0056b3; }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Tire Inspection and Alignment Service Request</h1>
        <form method="POST" action="">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="phone">Phone:</label>
            <input type="text" id="phone" name="phone" required>

            <label for="preferred_date">Preferred Service Date:</label>
            <input type="date" id="preferred_date" name="preferred_date" required>

            <button type="submit">Submit Request</button>
        </form>
    </div>
</body>
</html>
```
