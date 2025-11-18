"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alpha-digitalsolutions.com
Prompt: Create a PHP script to manage client inquiries and consultations, referencing Alpha Digital Solutions' free consultation feature.
Generated: DETERMINISTIC_e716b69a974f618b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Client Inquiry Management Script
 * This script handles client inquiries and consultations for Alpha Digital Solutions' free consultation feature.
 * 

 * PHP version 8.0
 */

// Set error reporting for debugging (remove or adjust in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Database connection parameters
$host = 'localhost';
$db = 'client_inquiries';
$user = 'root';
$pass = 'password'; // Update with your password

// Create a new PDO instance for database connection
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8mb4", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Function to submit a client inquiry
 *
 * @param string $name Client's name
 * @param string $email Client's email
 * @param string $message Inquiry message
 * @return bool True on success, false on failure
 */
function submitInquiry($name, $email, $message) {
    global $pdo;

    // Validate input
    if (empty($name) || empty($email) || empty($message)) {
        throw new InvalidArgumentException("All fields are required.");
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        throw new InvalidArgumentException("Invalid email format.");
    }

    // Prepare SQL statement to insert inquiry
    $sql = "INSERT INTO inquiries (name, email, message, created_at) VALUES (:name, :email, :message, NOW())";
    $stmt = $pdo->prepare($sql);

    // Bind parameters
    $stmt->bindParam(':name', $name);
    $stmt->bindParam(':email', $email);
    $stmt->bindParam(':message', $message);

    // Execute the statement and return success status
    return $stmt->execute();
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        $name = trim($_POST['name']);
        $email = trim($_POST['email']);
        $message = trim($_POST['message']);

        // Submit the inquiry
        if (submitInquiry($name, $email, $message)) {
            echo "Thank you for your inquiry! We will get back to you shortly.";
        } else {
            echo "There was an issue submitting your inquiry. Please try again.";
        }
    } catch (Exception $e) {
        echo "Error: " . $e->getMessage();
    }
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Client Inquiry Form</title>
</head>
<body>
    <h1>Contact Us for a Free Consultation</h1>
    <form action="" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>

        <button type="submit">Submit Inquiry</button>
    </form>
</body>
</html>
```

**Note:** Make sure to replace the database connection credentials according to your setup and ensure the `inquiries` table exists in the specified database with the appropriate columns (`name`, `email`, `message`, and `created_at`).
