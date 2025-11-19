"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vogellust.nl
Prompt: Develop a PHP script to handle user registrations for a birdkeeping club, reflecting the membership processes outlined on the Vogellust page.
Generated: DETERMINISTIC_381f8bcb926b500b
Batch ID: 20250612_162050
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
 * Birdkeeping Club Membership Registration Script
 * 
 * This script handles user registrations for the birdkeeping club, "Vogellust".
 * It validates user input, saves data to a database, and ensures proper error handling.
 * 
 * Requirements:
 * - PHP 7.4 or higher
 * - MySQL database connection
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'birdkeeping_club');
define('DB_USER', 'root');
define('DB_PASS', 'password');

try {
    // Establish database connection using PDO
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to handle registration
function registerUser($name, $email, $password, $birdInterest) {
    global $pdo;

    // Validate input
    if (empty($name) || empty($email) || empty($password) || empty($birdInterest)) {
        throw new Exception("All fields are required.");
    }
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        throw new Exception("Invalid email format.");
    }

    // Hash password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Prepare SQL query to insert user data
    $sql = "INSERT INTO members (name, email, password, bird_interest) VALUES (:name, :email, :password, :bird_interest)";
    $stmt = $pdo->prepare($sql);

    // Bind parameters and execute the statement
    $stmt->bindParam(':name', $name);
    $stmt->bindParam(':email', $email);
    $stmt->bindParam(':password', $hashedPassword);
    $stmt->bindParam(':bird_interest', $birdInterest);

    if ($stmt->execute()) {
        return "Registration successful.";
    } else {
        throw new Exception("Registration failed.");
    }
}

// Process form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        $name = trim($_POST['name']);
        $email = trim($_POST['email']);
        $password = trim($_POST['password']);
        $birdInterest = trim($_POST['bird_interest']);
        
        // Attempt to register user
        $result = registerUser($name, $email, $password, $birdInterest);
        echo $result;
    } catch (Exception $e) {
        // Display error message
        echo "Error: " . $e->getMessage();
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Birdkeeping Club Registration</title>
</head>
<body>
    <h1>Join the Vogellust Birdkeeping Club</h1>
    <form method="POST" action="">
        <label for="name">Full Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>
        
        <label for="email">Email Address:</label><br>
        <input type="email" id="email" name="email" required><br><br>
        
        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password" required><br><br>
        
        <label for="bird_interest">Bird Interest (e.g., parakeets, pigeons):</label><br>
        <input type="text" id="bird_interest" name="bird_interest" required><br><br>
        
        <button type="submit">Register</button>
    </form>
</body>
</html>
```
