"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daviviendahn.webcindario.com
Prompt: Write a PHP script to create a contact form and store submissions in a MySQL database, optimized for free hosting setups.
Generated: DETERMINISTIC_657de9a6c3de23eb
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Contact form script with submission storage in MySQL database

// Database connection settings
define('DB_HOST', 'localhost'); // Change if necessary
define('DB_NAME', 'your_database_name'); // Replace with your database name
define('DB_USER', 'your_database_user'); // Replace with your database user
define('DB_PASS', 'your_database_password'); // Replace with your database password

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate input data
    $name = htmlspecialchars(trim($_POST['name']));
    $email = htmlspecialchars(trim($_POST['email']));
    $message = htmlspecialchars(trim($_POST['message']));

    $errors = [];

    // Validate name
    if (empty($name)) {
        $errors[] = 'Name is required.';
    }

    // Validate email
    if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = 'Valid email is required.';
    }

    // Validate message
    if (empty($message)) {
        $errors[] = 'Message is required.';
    }

    // If valid, store data in the database
    if (empty($errors)) {
        try {
            // Establish database connection using PDO
            $dsn = 'mysql:host=' . DB_HOST . ';dbname=' . DB_NAME . ';charset=utf8mb4';
            $pdo = new PDO($dsn, DB_USER, DB_PASS, [
                PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
                PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            ]);

            // Prepare and execute SQL statement
            $stmt = $pdo->prepare('INSERT INTO contacts (name, email, message) VALUES (:name, :email, :message)');
            $stmt->execute([
                ':name' => $name,
                ':email' => $email,
                ':message' => $message,
            ]);

            echo 'Thank you for your submission!';
        } catch (PDOException $e) {
            // Log error or display user-friendly error message
            error_log($e->getMessage());
            echo 'An error occurred while saving your submission. Please try again later.';
        }
    } else {
        // Display validation errors
        foreach ($errors as $error) {
            echo '<p>' . $error . '</p>';
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form action="" method="POST">
        <label for="name">Name:</label>
        <input type="text" name="name" id="name" required><br><br>

        <label for="email">Email:</label>
        <input type="email" name="email" id="email" required><br><br>

        <label for="message">Message:</label>
        <textarea name="message" id="message" rows="5" required></textarea><br><br>

        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

### Notes:
1. Make sure to create a MySQL table named `contacts` with columns `id` (AUTO_INCREMENT, PRIMARY KEY), `name`, `email`, and `message` (all of type `VARCHAR` or `TEXT` depending on your requirements).
2. Replace database credentials (`DB_NAME`, `DB_USER`, `DB_PASS`) with actual values for your setup.
3. This code assumes free hosting setups where error logging and environment configurations may be minimal.
