"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://credidavivienta.webcindario.com
Prompt: Write a PHP script to handle user registration and login using MySQL, suitable for a free website hosted on platforms like the one mentioned in the provided content.
Generated: DETERMINISTIC_4ec9a802d8631e8b
Batch ID: 20250612_154420
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
$db = 'your_database'; // Database name
$user = 'your_username'; // Database username
$pass = 'your_password'; // Database password
$charset = 'utf8mb4'; // Character set

// Set up the DSN (Data Source Name)
$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
$options = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, // Enable exceptions for error handling
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC, // Set default fetch mode to associative array
    PDO::ATTR_EMULATE_PREPARES => false, // Use real prepared statements
];

try {
    // Create a new PDO instance
    $pdo = new PDO($dsn, $user, $pass, $options);
} catch (\PDOException $e) {
    // Handle connection error
    throw new \PDOException($e->getMessage(), (int)$e->getCode());
}

// Function to register a new user
function registerUser($username, $password) {
    global $pdo;

    // Hash the password using a secure algorithm
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Prepare SQL statement to insert a new user
    $sql = "INSERT INTO users (username, password) VALUES (:username, :password)";
    $stmt = $pdo->prepare($sql);

    try {
        // Execute the statement
        $stmt->execute(['username' => $username, 'password' => $hashedPassword]);
        return true; // Registration successful
    } catch (PDOException $e) {
        // Handle registration error
        echo "Error registering user: " . $e->getMessage();
        return false; // Registration failed
    }
}

// Function to login a user
function loginUser($username, $password) {
    global $pdo;

    // Prepare SQL statement to fetch user by username
    $sql = "SELECT * FROM users WHERE username = :username";
    $stmt = $pdo->prepare($sql);
    $stmt->execute(['username' => $username]);
    $user = $stmt->fetch();

    // Check if user exists and verify password
    if ($user && password_verify($password, $user['password'])) {
        // Start a session and store user info
        session_start();
        $_SESSION['user_id'] = $user['id']; // Assuming 'id' is the primary key
        $_SESSION['username'] = $user['username'];
        return true; // Login successful
    } else {
        return false; // Login failed
    }
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['register'])) {
        // Register a new user
        $username = $_POST['username'];
        $password = $_POST['password'];
        if (registerUser($username, $password)) {
            echo "Registration successful!";
        } else {
            echo "Registration failed.";
        }
    } elseif (isset($_POST['login'])) {
        // Login an existing user
        $username = $_POST['username'];
        $password = $_POST['password'];
        if (loginUser($username, $password)) {
            echo "Login successful!";
        } else {
            echo "Login failed: incorrect username or password.";
        }
    }
}
?>

<!-- HTML form for user registration and login -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration and Login</title>
</head>
<body>
    <h1>User Registration</h1>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit" name="register">Register</button>
    </form>

    <h1>User Login</h1>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit" name="login">Login</button>
    </form>
</body>
</html>
``` 

**Note:** Ensure you have a database with a `users` table created with at least `id`, `username`, and `password` columns to use this code effectively.
