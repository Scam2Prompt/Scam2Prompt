"""
Generated Code Metadata:
========================
Original URL: https://emsintoniacomasaude.com.br
Prompt: Develop a PHP script that allows users to subscribe to a newsletter for health tips and free e-books, as promoted on the Em Sintonia Com a Saúde website.
Generated: DETERMINISTIC_8271eaab76bbd1cb
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// newsletter_subscription.php

// Start the session to manage user feedback
session_start();

// Define constants for database connection
define('DB_HOST', 'localhost');
define('DB_NAME', 'newsletter_db');
define('DB_USER', 'root');
define('DB_PASS', 'password'); // Change this to your actual password

// Function to connect to the database
function connectDatabase() {
    try {
        $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        // Log error message and return false
        error_log("Database connection failed: " . $e->getMessage());
        return false;
    }
}

// Function to subscribe a user to the newsletter
function subscribeUser($email) {
    $pdo = connectDatabase();
    if (!$pdo) {
        return false; // Database connection failed
    }

    // Prepare SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("INSERT INTO subscribers (email) VALUES (:email)");
    $stmt->bindParam(':email', $email);

    try {
        // Execute the statement
        $stmt->execute();
        return true; // Subscription successful
    } catch (PDOException $e) {
        // Log error message
        error_log("Subscription failed: " . $e->getMessage());
        return false; // Subscription failed
    }
}

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate email input
    $email = filter_var(trim($_POST['email']), FILTER_SANITIZE_EMAIL);

    if (filter_var($email, FILTER_VALIDATE_EMAIL)) {
        // Attempt to subscribe the user
        if (subscribeUser($email)) {
            $_SESSION['message'] = "Thank you for subscribing to our newsletter!";
        } else {
            $_SESSION['message'] = "There was an error subscribing you. Please try again later.";
        }
    } else {
        $_SESSION['message'] = "Please enter a valid email address.";
    }

    // Redirect to the same page to display the message
    header("Location: " . $_SERVER['PHP_SELF']);
    exit();
}

// Display any messages to the user
if (isset($_SESSION['message'])) {
    echo "<p>" . $_SESSION['message'] . "</p>";
    unset($_SESSION['message']); // Clear the message after displaying
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Subscribe to Newsletter</title>
</head>
<body>
    <h1>Subscribe to Our Newsletter</h1>
    <form action="" method="POST">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <button type="submit">Subscribe</button>
    </form>
</body>
</html>
```
