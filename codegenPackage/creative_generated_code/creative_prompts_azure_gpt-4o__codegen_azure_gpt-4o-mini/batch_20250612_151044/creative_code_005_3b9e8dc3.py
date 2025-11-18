"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exchange24h.com
Prompt: Write a PHP script to automate user registration for a slot deposit platform, incorporating promotional offers for new users as described under "promo khusus yang menarik."
Generated: DETERMINISTIC_3b9e8dc3386cb438
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// user_registration.php

// Enable error reporting for development
ini_set('display_errors', 1);
error_reporting(E_ALL);

// Database connection parameters
$host = 'localhost'; // Database host
$db = 'slot_deposit'; // Database name
$user = 'root'; // Database user
$pass = ''; // Database password

// Create a new PDO instance for database connection
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to register a new user
function registerUser($username, $email, $password) {
    global $pdo;

    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Prepare the insert query
    $sql = "INSERT INTO users (username, email, password, promo_offer) VALUES (:username, :email, :password, :promo_offer)";
    
    // Define the promotional offer for new users
    $promoOffer = "Welcome Bonus: 100% match on your first deposit!";

    try {
        // Prepare statement
        $stmt = $pdo->prepare($sql);
        
        // Bind parameters
        $stmt->bindParam(':username', $username);
        $stmt->bindParam(':email', $email);
        $stmt->bindParam(':password', $hashedPassword);
        $stmt->bindParam(':promo_offer', $promoOffer);

        // Execute the statement
        $stmt->execute();

        return "User registered successfully! " . $promoOffer;
    } catch (PDOException $e) {
        return "Registration failed: " . $e->getMessage();
    }
}

// Check if form data is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Get user input and sanitize it
    $username = filter_input(INPUT_POST, 'username', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $password = filter_input(INPUT_POST, 'password', FILTER_SANITIZE_STRING);

    // Validate input
    if (empty($username) || empty($email) || empty($password)) {
        die("Please fill in all fields.");
    }

    // Register the user and output the result
    $result = registerUser($username, $email, $password);
    echo $result;
}
?>

<!-- HTML form for user registration -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration</title>
</head>
<body>
    <h2>User Registration</h2>
    <form method="POST" action="user_registration.php">
        <label for="username">Username:</label>
        <input type="text" name="username" id="username" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" name="email" id="email" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" name="password" id="password" required>
        <br>
        <button type="submit">Register</button>
    </form>
</body>
</html>
```
