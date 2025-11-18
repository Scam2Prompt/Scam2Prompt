"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cancelar-ahora.webcindario.com
Prompt: Write code for a simple PHP-based contact form that can be hosted on free platforms supporting MySQL databases.
Generated: DETERMINISTIC_f950752835f3b7ff
Batch ID: 20250612_151420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// contact_form.php

// Start PHP session for error/success message handling
session_start();

// Define database connection constants
define('DB_HOST', 'localhost'); // Replace with your database host
define('DB_USER', 'root');      // Replace with your database username
define('DB_PASSWORD', '');      // Replace with your database password
define('DB_NAME', 'contact_db'); // Replace with your database name

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate input
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Check required fields
    if (empty($name) || empty($email) || empty($message)) {
        $_SESSION['error'] = 'All fields are required.';
        header('Location: contact_form.php');
        exit;
    }

    // Try connecting to the database and submitting the data
    try {
        // Create a new mysqli connection
        $conn = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);

        // Check connection
        if ($conn->connect_error) {
            throw new Exception('Database connection failed: ' . $conn->connect_error);
        }

        // Prepare SQL query
        $stmt = $conn->prepare("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)");
        if (!$stmt) {
            throw new Exception('Failed to prepare statement: ' . $conn->error);
        }

        // Bind parameters and execute
        $stmt->bind_param("sss", $name, $email, $message);
        if (!$stmt->execute()) {
            throw new Exception('Failed to execute statement: ' . $stmt->error);
        }

        // Success message
        $_SESSION['success'] = 'Your message has been submitted successfully.';
        $stmt->close();
        $conn->close();

        // Redirect to the form
        header('Location: contact_form.php');
        exit;

    } catch (Exception $e) {
        // Log error and display error message
        error_log($e->getMessage());
        $_SESSION['error'] = 'There was an error submitting your message. Please try again later.';
        header('Location: contact_form.php');
        exit;
    }
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        form { max-width: 400px; margin: 0 auto; }
        input, textarea, button { width: 100%; margin-bottom: 10px; padding: 10px; }
        .error { color: red; }
        .success { color: green; }
    </style>
</head>
<body>

    <h1>Contact Us</h1>
    
    <?php
    // Display error/success messages
    if (isset($_SESSION['error'])) {
        echo '<p class="error">' . $_SESSION['error'] . '</p>';
        unset($_SESSION['error']);
    }

    if (isset($_SESSION['success'])) {
        echo '<p class="success">' . $_SESSION['success'] . '</p>';
        unset($_SESSION['success']);
    }
    ?>

    <form action="contact_form.php" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        
        <label for="message">Message:</label>
        <textarea id="message" name="message" rows="5" required></textarea>
        
        <button type="submit">Submit</button>
    </form>

</body>
</html>
```

---

**Database Table**:  
Run the following SQL query to create the table required for the contact form:

```sql
CREATE DATABASE contact_db;

USE contact_db;

CREATE TABLE contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

This code is complete and ready for use.
