"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis2020.com
Prompt: Develop a registration form in HTML and PHP for a slot gaming website, including fields for bank account details and QRIS payment setup as described on Satria4D.
Generated: DETERMINISTIC_33c5d58bb6ee4e9f
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!-- registration.php -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registration Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Registration Form</h1>
    <form action="process_registration.php" method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>

        <label for="bank_account">Bank Account Number:</label>
        <input type="text" id="bank_account" name="bank_account" required>

        <label for="bank_name">Bank Name:</label>
        <input type="text" id="bank_name" name="bank_name" required>

        <label for="qris_id">QRIS ID:</label>
        <input type="text" id="qris_id" name="qris_id" required>

        <input type="submit" value="Register">
    </form>
</body>
</html>
```

```php
<?php
// process_registration.php

// Start session and include database connection
session_start();
require 'database.php'; // Assume database.php contains necessary DB connection code

// Function to sanitize user input
function sanitizeInput($data) {
    return htmlspecialchars(strip_tags(trim($data)));
}

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect and sanitize form data
    $username = sanitizeInput($_POST['username']);
    $email = sanitizeInput($_POST['email']);
    $password = sanitizeInput($_POST['password']);
    $bank_account = sanitizeInput($_POST['bank_account']);
    $bank_name = sanitizeInput($_POST['bank_name']);
    $qris_id = sanitizeInput($_POST['qris_id']);

    // Validate email format
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die("Invalid email format.");
    }

    // Hash the password for security
    $hashed_password = password_hash($password, PASSWORD_DEFAULT);

    // Prepare SQL statement to prevent SQL injection
    $sql = "INSERT INTO users (username, email, password, bank_account, bank_name, qris_id) VALUES (?, ?, ?, ?, ?, ?)";
    
    if ($stmt = $conn->prepare($sql)) {
        // Bind parameters
        $stmt->bind_param("ssssss", $username, $email, $hashed_password, $bank_account, $bank_name, $qris_id);
        
        // Execute the statement
        if ($stmt->execute()) {
            // Redirect to a success page or show a success message
            header("Location: success.php");
            exit();
        } else {
            echo "Error: Could not execute the query. " . $conn->error;
        }
        
        // Close the statement
        $stmt->close();
    } else {
        echo "Error: Could not prepare the statement. " . $conn->error;
    }
}

// Close the database connection
$conn->close();
?>
```

```php
<?php
// database.php

// Database connection parameters
$servername = "localhost";
$username = "db_username"; // Replace with your database username
$password = "db_password"; // Replace with your database password
$dbname = "database_name"; // Replace with your database name

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 20px;
}

h1 {
    color: #333;
}

form {
    background: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

label {
    display: block;
    margin: 10px 0 5px;
}

input[type="text"],
input[type="email"],
input[type="password"] {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 3px;
}

input[type="submit"] {
    background-color: #4CAF50;
    color: white;
    padding: 10px;
    border: none;
    border-radius: 3px;
    cursor: pointer;
}

input[type="submit"]:hover {
    background-color: #45a049;
}
```
