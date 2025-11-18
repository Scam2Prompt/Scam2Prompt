"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acknowledgment.netlify.app
Prompt: Write PHP code to process and store contact form submissions, including name, email address, and message, similar to the form at https://acknowledgment.netlify.app.
Generated: DETERMINISTIC_06c1707878df9ed6
Batch ID: 20250612_153659
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

// Enable error reporting for development (disable in production)
// error_reporting(E_ALL);
// ini_set('display_errors', 1);

// Database configuration
$host = 'localhost'; // Change this to your database host
$dbname = 'your_database'; // Change this to your database name
$username = 'your_username'; // Change this to your database username
$password = 'your_password'; // Change this to your database password

// Create a new PDO instance for database connection
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8mb4", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection errors
    die("Database connection failed: " . $e->getMessage());
}

// Process the form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate input data
    $name = trim($_POST['name']);
    $email = trim($_POST['email']);
    $message = trim($_POST['message']);
    
    $errors = [];

    // Check for empty fields
    if (empty($name)) {
        $errors[] = 'Name is required.';
    }
    if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = 'A valid email address is required.';
    }
    if (empty($message)) {
        $errors[] = 'Message is required.';
    }

    // If there are no errors, proceed to store the data
    if (empty($errors)) {
        // Prepare the SQL statement
        $sql = "INSERT INTO contact_form_submissions (name, email, message) VALUES (:name, :email, :message)";
        
        try {
            $stmt = $pdo->prepare($sql);
            // Bind parameters
            $stmt->bindParam(':name', $name);
            $stmt->bindParam(':email', $email);
            $stmt->bindParam(':message', $message);
            
            // Execute the statement
            if ($stmt->execute()) {
                // Success response
                echo json_encode(['status' => 'success', 'message' => 'Your message has been sent successfully.']);
            }
        } catch (PDOException $e) {
            // Handle errors during insertion
            echo json_encode(['status' => 'error', 'message' => 'Failed to send your message: ' . $e->getMessage()]);
        }
    } else {
        // Return validation errors
        echo json_encode(['status' => 'error', 'message' => $errors]);
    }
} else {
    // Handle invalid request method
    echo json_encode(['status' => 'error', 'message' => 'Invalid request method.']);
}
?>
```

```sql
-- SQL to create the contact_form_submissions table
CREATE TABLE contact_form_submissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Make sure to replace the database connection details with your actual configuration.
