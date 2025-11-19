"""
Generated Code Metadata:
========================
Original URL: https://pneusml.com
Prompt: Develop a PHP script that allows users to submit a request for a tire inspection and alignment service, similar to the services offered by Pneus ML.
Generated: DETERMINISTIC_a9b4a5061e641ec9
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Tire Inspection and Alignment Service Request Script
// Author: [Your Name]
// Date: [Date]
// Description: This script allows users to submit a request for tire inspection and alignment services.

// Enable error reporting for development (disable in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Database connection settings (update with your credentials)
define('DB_HOST', 'localhost');
define('DB_NAME', 'service_requests');
define('DB_USER', 'root');
define('DB_PASS', 'password');

try {
    // Establish a connection to the database
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle database connection errors
    die("Database connection failed: " . $e->getMessage());
}

// Function to sanitize user input
function sanitizeInput($data) {
    return htmlspecialchars(strip_tags(trim($data)));
}

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate and sanitize user input
    $name = sanitizeInput($_POST['name'] ?? '');
    $email = sanitizeInput($_POST['email'] ?? '');
    $phone = sanitizeInput($_POST['phone'] ?? '');
    $vehicle = sanitizeInput($_POST['vehicle'] ?? '');
    $message = sanitizeInput($_POST['message'] ?? '');

    // Validate required fields
    if (empty($name) || empty($email) || empty($phone) || empty($vehicle)) {
        $error = "All fields are required.";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $error = "Invalid email format.";
    } else {
        try {
            // Insert the request into the database
            $stmt = $pdo->prepare("INSERT INTO requests (name, email, phone, vehicle, message, created_at) VALUES (:name, :email, :phone, :vehicle, :message, NOW())");
            $stmt->execute([
                ':name' => $name,
                ':email' => $email,
                ':phone' => $phone,
                ':vehicle' => $vehicle,
                ':message' => $message
            ]);

            // Success message
            $success = "Your request has been submitted successfully.";
        } catch (PDOException $e) {
            // Handle database errors
            $error = "Failed to submit your request: " . $e->getMessage();
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tire Inspection and Alignment Service Request</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        form {
            max-width: 500px;
            margin: auto;
        }
        .form-group {
            margin-bottom: 15px;
        }
        .form-group label {
            display: block;
            margin-bottom: 5px;
        }
        .form-group input, .form-group textarea {
            width: 100%;
            padding: 8px;
            box-sizing: border-box;
        }
        .form-group textarea {
            resize: vertical;
        }
        .error {
            color: red;
        }
        .success {
            color: green;
        }
    </style>
</head>
<body>
    <h1>Tire Inspection and Alignment Service Request</h1>
    <?php if (!empty($error)): ?>
        <p class="error"><?= $error ?></p>
    <?php endif; ?>
    <?php if (!empty($success)): ?>
        <p class="success"><?= $success ?></p>
    <?php endif; ?>
    <form method="POST" action="">
        <div class="form-group">
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required>
        </div>
        <div class="form-group">
            <label for="email">Email Address:</label>
            <input type="email" id="email" name="email" required>
        </div>
        <div class="form-group">
            <label for="phone">Phone Number:</label>
            <input type="text" id="phone" name="phone" required>
        </div>
        <div class="form-group">
            <label for="vehicle">Vehicle Model:</label>
            <input type="text" id="vehicle" name="vehicle" required>
        </div>
        <div class="form-group">
            <label for="message">Additional Message (optional):</label>
            <textarea id="message" name="message" rows="4"></textarea>
        </div>
        <button type="submit">Submit Request</button>
    </form>
</body>
</html>
```

**Note:** Ensure the database table `requests` exists with the following structure:
```sql
CREATE TABLE requests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(50) NOT NULL,
    vehicle VARCHAR(255) NOT NULL,
    message TEXT,
    created_at DATETIME NOT NULL
);
```
