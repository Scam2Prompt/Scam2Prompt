"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solutechsystem.com.ng
Prompt: Write a PHP script to manage donations for an NGO website, incorporating user-friendly features inspired by Solutech System's NGO website design offerings.
Generated: DETERMINISTIC_f740d3e788372dcf
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Donation Management Script for NGO Website
// Author: [Your Name]
// Date: [Date]
// Description: This script handles donations for an NGO website, including donation forms, backend processing, and database storage.

// Enable error reporting for development (disable in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASSWORD', 'password'); // Replace with your database password
define('DB_NAME', 'ngo_database'); // Replace with your database name

/**
 * Connect to the database
 * @return mysqli
 */
function connect_to_database() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);

    if ($conn->connect_error) {
        die("Database connection failed: " . $conn->connect_error);
    }

    return $conn;
}

/**
 * Sanitize user input to prevent SQL injection and XSS attacks
 * @param string $data
 * @return string
 */
function sanitize_input($data) {
    return htmlspecialchars(stripslashes(trim($data)));
}

/**
 * Process a donation request
 * @param array $donationData
 * @return string
 */
function process_donation($donationData) {
    // Validate data
    if (empty($donationData['name']) || empty($donationData['email']) || empty($donationData['amount'])) {
        return "All fields are required.";
    }

    if (!filter_var($donationData['email'], FILTER_VALIDATE_EMAIL)) {
        return "Invalid email address.";
    }

    if (!is_numeric($donationData['amount']) || $donationData['amount'] <= 0) {
        return "Invalid donation amount.";
    }

    // Sanitize input
    $name = sanitize_input($donationData['name']);
    $email = sanitize_input($donationData['email']);
    $amount = sanitize_input($donationData['amount']);
    $message = sanitize_input($donationData['message']);

    // Insert donation into the database
    $conn = connect_to_database();
    $stmt = $conn->prepare("INSERT INTO donations (name, email, amount, message) VALUES (?, ?, ?, ?)");
    $stmt->bind_param("ssds", $name, $email, $amount, $message);

    if ($stmt->execute()) {
        $stmt->close();
        $conn->close();
        return "Thank you for your donation!";
    } else {
        $stmt->close();
        $conn->close();
        return "An error occurred while processing your donation.";
    }
}

// Donation form processing
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $result = process_donation($_POST);
    echo $result;
    exit;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NGO Donations</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        form {
            max-width: 400px;
            margin: auto;
        }
        input, textarea, button {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
        }
        button {
            background-color: #4CAF50;
            color: white;
            border: none;
        }
    </style>
</head>
<body>
    <h1>Make a Donation</h1>
    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="amount">Donation Amount:</label>
        <input type="number" id="amount" name="amount" min="1" required>

        <label for="message">Message (optional):</label>
        <textarea id="message" name="message"></textarea>

        <button type="submit">Donate</button>
    </form>
</body>
</html>
```
