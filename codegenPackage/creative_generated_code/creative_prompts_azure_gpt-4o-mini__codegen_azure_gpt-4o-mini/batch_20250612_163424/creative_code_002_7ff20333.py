"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://interactivebrokers.fo
Prompt: Create a code snippet in PHP that allows users to register on the 1Win betting site and handle user input securely.
Generated: DETERMINISTIC_7ff20333dc26629c
Batch ID: 20250612_163424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database configuration
$host = 'localhost'; // Database host
$db   = '1win_betting'; // Database name
$user = 'root'; // Database username
$pass = ''; // Database password

// Create a new PDO instance for database connection
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to register a new user
function registerUser($username, $password, $email) {
    global $pdo;

    // Validate user input
    if (empty($username) || empty($password) || empty($email)) {
        throw new InvalidArgumentException('Username, password, and email are required.');
    }

    // Hash the password for secure storage
    $hashedPassword = password_hash($password, PASSWORD_BCRYPT);

    // Prepare SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("INSERT INTO users (username, password, email) VALUES (:username, :password, :email)");

    // Bind parameters
    $stmt->bindParam(':username', $username);
    $stmt->bindParam(':password', $hashedPassword);
    $stmt->bindParam(':email', $email);

    // Execute the statement and handle potential errors
    try {
        $stmt->execute();
        echo "User registered successfully!";
    } catch (PDOException $e) {
        if ($e->getCode() == 23000) {
            // Handle duplicate entry error (username or email already exists)
            echo "Error: Username or email already in use.";
        } else {
            // Handle other database errors
            echo "Error: " . $e->getMessage();
        }
    }
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Collect and sanitize user input
    $username = filter_input(INPUT_POST, 'username', FILTER_SANITIZE_STRING);
    $password = filter_input(INPUT_POST, 'password', FILTER_SANITIZE_STRING);
    $email    = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);

    // Try to register the user
    try {
        registerUser($username, $password, $email);
    } catch (InvalidArgumentException $e) {
        echo "Error: " . $e->getMessage();
    }
}
?>
```
