"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://newworldtradex.com
Prompt: Create a PHP code snippet that allows users to sign up for New World Trade, capturing their details and selecting an investment plan while ensuring data encryption.
Generated: DETERMINISTIC_1d8fddc7822204e5
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// File: signup.php

// Include database configuration file
include_once 'config.php';

// Function to encrypt sensitive data
function encryptData($data, $key) {
    return openssl_encrypt($data, 'AES-256-CBC', $key, 0, substr($key, 0, 16));
}

// Function to validate input data
function validateInput($data) {
    return htmlspecialchars(stripslashes(trim($data)));
}

// Check if request method is POST to handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Define encryption key (ensure this is stored securely in production)
    $encryptionKey = "YourSecureEncryptionKey12345"; // Replace with a stronger key

    // Retrieve and validate form data
    $name = validateInput($_POST['name']);
    $email = validateInput($_POST['email']);
    $password = validateInput($_POST['password']);
    $investmentPlan = validateInput($_POST['investment_plan']);

    // Validate mandatory fields
    if (empty($name) || empty($email) || empty($password) || empty($investmentPlan)) {
        die("Error: All fields are mandatory.");
    }

    // Validate email format
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die("Error: Invalid email format.");
    }

    // Encrypt sensitive data
    $encryptedPassword = encryptData($password, $encryptionKey);

    // Hash email for additional security
    $hashedEmail = hash('sha256', $email);

    try {
        // Database connection
        $conn = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);

        // Check connection
        if ($conn->connect_error) {
            throw new Exception("Connection failed: " . $conn->connect_error);
        }

        // Prepare SQL statement to prevent SQL Injection
        $stmt = $conn->prepare("INSERT INTO users (name, email, password, investment_plan) VALUES (?, ?, ?, ?)");
        $stmt->bind_param("ssss", $name, $hashedEmail, $encryptedPassword, $investmentPlan);

        // Execute the query
        if ($stmt->execute()) {
            echo "Signup successful!";
        } else {
            throw new Exception("Error: Unable to complete signup.");
        }

        // Close statement and connection
        $stmt->close();
        $conn->close();
    } catch (Exception $e) {
        // Log error and display a generic message to the user
        error_log($e->getMessage());
        die("An error occurred. Please try again later.");
    }
}
?>

<!-- Simple HTML Form for Signup -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>New World Trade Signup</title>
</head>
<body>
    <h1>Signup for New World Trade</h1>
    <form method="POST" action="signup.php">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br>

        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br>

        <label for="investment_plan">Investment Plan:</label>
        <select id="investment_plan" name="investment_plan" required>
            <option value="basic">Basic Plan</option>
            <option value="premium">Premium Plan</option>
            <option value="enterprise">Enterprise Plan</option>
        </select><br>

        <button type="submit">Signup</button>
    </form>
</body>
</html>
```
