"""
Generated Code Metadata:
========================
Original URL: https://ingreseeaquii.webcindario.com
Prompt: Write PHP code to create a simple website with MySQL integration, including user authentication and a custom domain setup.
Generated: DETERMINISTIC_0ae84b56bbe0f086
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Database configuration
$host = 'localhost'; // Database host
$dbname = 'your_database'; // Database name
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password

// Create a connection to the database
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Start session for user authentication
session_start();

// Function to register a new user
function registerUser($username, $password) {
    global $pdo;
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
    $stmt = $pdo->prepare("INSERT INTO users (username, password) VALUES (:username, :password)");
    $stmt->bindParam(':username', $username);
    $stmt->bindParam(':password', $hashedPassword);
    return $stmt->execute();
}

// Function to authenticate a user
function authenticateUser($username, $password) {
    global $pdo;
    $stmt = $pdo->prepare("SELECT password FROM users WHERE username = :username");
    $stmt->bindParam(':username', $username);
    $stmt->execute();
    $hashedPassword = $stmt->fetchColumn();
    
    if ($hashedPassword && password_verify($password, $hashedPassword)) {
        $_SESSION['username'] = $username; // Store username in session
        return true;
    }
    return false;
}

// Handle registration form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['register'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];
    
    if (registerUser($username, $password)) {
        echo "Registration successful!";
    } else {
        echo "Registration failed!";
    }
}

// Handle login form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['login'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];
    
    if (authenticateUser($username, $password)) {
        echo "Login successful! Welcome, " . htmlspecialchars($username);
    } else {
        echo "Login failed! Invalid credentials.";
    }
}

// HTML structure for the website
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple PHP Website</title>
</head>
<body>
    <h1>Welcome to the Simple PHP Website</h1>
    
    <h2>Register</h2>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit" name="register">Register</button>
    </form>
    
    <h2>Login</h2>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit" name="login">Login</button>
    </form>
</body>
</html>
```

**Database Table Structure:**
Make sure to create a `users` table in your MySQL database with the following structure:

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
```

**Note:** Replace `your_database`, `your_username`, and `your_password` with your actual database credentials. Ensure that your server is configured to handle PHP and MySQL.
