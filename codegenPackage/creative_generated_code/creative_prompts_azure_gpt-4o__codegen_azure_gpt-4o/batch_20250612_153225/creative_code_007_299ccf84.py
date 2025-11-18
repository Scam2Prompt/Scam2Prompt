"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redhorsereflex.com
Prompt: Write a PHP script to implement a contact form for a reflexology service website, including fields for name, email, phone number, and message, and ensure the form data is securely stored in a MySQL database.
Generated: DETERMINISTIC_299ccf8441da9a3f
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Define database connection constants
define('DB_HOST', 'localhost');
define('DB_USER', 'your_db_username');
define('DB_PASSWORD', 'your_db_password');
define('DB_NAME', 'your_db_name');

// Function to establish a database connection
function getDatabaseConnection() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);
    // Check connection
    if ($conn->connect_error) {
        die('Connection failed: ' . $conn->connect_error);
    }
    return $conn;
}

// Function to sanitize user input
function sanitizeInput($data) {
    return htmlspecialchars(trim($data), ENT_QUOTES, 'UTF-8');
}

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize user input
    $name = sanitizeInput($_POST['name'] ?? '');
    $email = sanitizeInput($_POST['email'] ?? '');
    $phone = sanitizeInput($_POST['phone'] ?? '');
    $message = sanitizeInput($_POST['message'] ?? '');

    // Validate required fields
    if (empty($name) || empty($email) || empty($phone) || empty($message)) {
        echo 'All fields are required.';
        exit;
    }

    // Validate email format
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo 'Invalid email format.';
        exit;
    }

    // Establish database connection
    $conn = getDatabaseConnection();

    // Prepare SQL statement to prevent SQL injection
    $stmt = $conn->prepare('INSERT INTO contact_form (name, email, phone, message) VALUES (?, ?, ?, ?)');
    if (!$stmt) {
        echo 'Failed to prepare statement.';
        exit;
    }

    // Bind parameters to the statement
    $stmt->bind_param('ssss', $name, $email, $phone, $message);

    // Execute the statement and check for errors
    if ($stmt->execute()) {
        echo 'Thank you for contacting us! Your message has been received.';
    } else {
        echo 'Error: ' . $stmt->error;
    }

    // Close the statement and connection
    $stmt->close();
    $conn->close();
}

?>

<!-- HTML Form -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>

        <label for="phone">Phone Number:</label>
        <input type="text" id="phone" name="phone" required><br><br>

        <label for="message">Message:</label><br>
        <textarea id="message" name="message" rows="5" required></textarea><br><br>

        <button type="submit">Submit</button>
    </form>
</body>
</html>

<!-- Notes:
1. Replace `your_db_username`, `your_db_password`, and `your_db_name` with your actual database credentials.
2. Ensure the `contact_form` table exists in the database with appropriate columns:
   CREATE TABLE contact_form (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(255) NOT NULL,
       email VARCHAR(255) NOT NULL,
       phone VARCHAR(50) NOT NULL,
       message TEXT NOT NULL,
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
-->
```
