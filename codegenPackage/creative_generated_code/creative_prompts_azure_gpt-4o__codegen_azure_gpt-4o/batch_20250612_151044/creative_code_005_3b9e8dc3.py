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
// Slot Deposit Platform - User Registration Script with Promotional Offers

// Database connection configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', 'password');
define('DB_NAME', 'slot_deposit_platform');

// Promotional Offer Configuration
define('PROMO_BONUS_AMOUNT', 50); // Bonus amount for new users
define('PROMO_VALIDITY_DAYS', 30); // Validity period for the promotional bonus

/**
 * Establish database connection.
 * 
 * @return mysqli Database connection object.
 */
function getDatabaseConnection() {
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check for connection errors
    if ($connection->connect_error) {
        die("Database connection failed: " . $connection->connect_error);
    }

    return $connection;
}

/**
 * Generate a random unique username.
 * 
 * @param string $base Base string for username.
 * @return string Generated username.
 */
function generateUsername($base) {
    return $base . '_' . uniqid();
}

/**
 * Register a new user in the platform.
 * 
 * @param string $name User's name.
 * @param string $email User's email.
 * @param string $password User's password (hashed).
 * @return bool True if registration successful, false otherwise.
 */
function registerUser($name, $email, $password) {
    $connection = getDatabaseConnection();

    // Check if the email is already registered
    $stmt = $connection->prepare("SELECT id FROM users WHERE email = ?");
    $stmt->bind_param("s", $email);
    $stmt->execute();
    $stmt->store_result();

    if ($stmt->num_rows > 0) {
        // Email already exists
        $stmt->close();
        $connection->close();
        return false;
    }
    $stmt->close();

    // Insert new user into database
    $username = generateUsername($name);
    $promo_expiry = date('Y-m-d', strtotime("+" . PROMO_VALIDITY_DAYS . " days"));
    $stmt = $connection->prepare("INSERT INTO users (name, email, password, username, promo_bonus, promo_expiry) VALUES (?, ?, ?, ?, ?, ?)");
    $stmt->bind_param("ssssds", $name, $email, $password, $username, PROMO_BONUS_AMOUNT, $promo_expiry);

    $result = $stmt->execute();
    $stmt->close();
    $connection->close();

    return $result;
}

// Entry Point: Registration Form Handling
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate inputs
    $name = htmlspecialchars(trim($_POST['name']));
    $email = filter_var(trim($_POST['email']), FILTER_VALIDATE_EMAIL);
    $password = trim($_POST['password']);

    // Input validation
    if (empty($name) || empty($email) || empty($password)) {
        die("Error: All fields are required.");
    }

    // Hash the password before storing
    $hashedPassword = password_hash($password, PASSWORD_BCRYPT);

    // Attempt to register the user
    if (registerUser($name, $email, $hashedPassword)) {
        echo "Registration successful! You have received a bonus of $" . PROMO_BONUS_AMOUNT . ".";
    } else {
        echo "Error: Registration failed. Email may already be in use.";
    }
} else {
    // Display simple registration form
    ?>
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>User Registration</title>
    </head>
    <body>
        <h1>Register for Slot Deposit Platform</h1>
        <form method="POST" action="">
            <label for="name">Name:</label><br>
            <input type="text" id="name" name="name" required><br><br>
            
            <label for="email">Email:</label><br>
            <input type="email" id="email" name="email" required><br><br>
            
            <label for="password">Password:</label><br>
            <input type="password" id="password" name="password" required><br><br>
            
            <button type="submit">Register</button>
        </form>
    </body>
    </html>
    <?php
}
?>
```
