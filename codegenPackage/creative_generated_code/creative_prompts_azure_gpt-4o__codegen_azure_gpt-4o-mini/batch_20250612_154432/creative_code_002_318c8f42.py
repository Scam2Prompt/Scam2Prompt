"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casiefe636.webcindario.com
Prompt: Generate PHP code to set up user authentication for a website hosted on miarroba.com with a custom domain.
Generated: DETERMINISTIC_318c8f4227327fc2
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start the session to manage user sessions
session_start();

// Database credentials
define('DB_HOST', 'localhost'); // Database host
define('DB_USER', 'your_db_username'); // Database user
define('DB_PASS', 'your_db_password'); // Database password
define('DB_NAME', 'your_database_name'); // Database name

// Establish a database connection using PDO
try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to register a new user
function registerUser($username, $password) {
    global $pdo;

    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Prepare the SQL statement
    $stmt = $pdo->prepare("INSERT INTO users (username, password) VALUES (:username, :password)");
    $stmt->bindParam(':username', $username);
    $stmt->bindParam(':password', $hashedPassword);

    // Execute the query and handle potential errors
    try {
        $stmt->execute();
        return true;
    } catch (PDOException $e) {
        return false; // Registration failed
    }
}

// Function to authenticate a user
function authenticateUser($username, $password) {
    global $pdo;

    // Prepare the SQL statement to retrieve user data
    $stmt = $pdo->prepare("SELECT * FROM users WHERE username = :username");
    $stmt->bindParam(':username', $username);
    $stmt->execute();

    // Fetch the user data
    $user = $stmt->fetch(PDO::FETCH_ASSOC);

    // Verify the password
    if ($user && password_verify($password, $user['password'])) {
        // Store user data in session
        $_SESSION['user_id'] = $user['id'];
        $_SESSION['username'] = $user['username'];
        return true; // Authentication successful
    }

    return false; // Authentication failed
}

// Function to log out a user
function logoutUser() {
    // Unset all of the session variables
    $_SESSION = array();

    // Destroy the session
    session_destroy();
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['register'])) {
        // Handle user registration
        $username = $_POST['username'];
        $password = $_POST['password'];
        if (registerUser($username, $password)) {
            echo "Registration successful!";
        } else {
            echo "Registration failed. Username may already exist.";
        }
    } elseif (isset($_POST['login'])) {
        // Handle user login
        $username = $_POST['username'];
        $password = $_POST['password'];
        if (authenticateUser($username, $password)) {
            echo "Login successful! Welcome, " . htmlspecialchars($username) . ".";
        } else {
            echo "Login failed. Please check your credentials.";
        }
    } elseif (isset($_POST['logout'])) {
        logoutUser();
        echo "You have been logged out.";
    }
}
?>
<!-- HTML Form for Registration and Login -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Authentication</title>
</head>
<body>
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

    <h2>Logout</h2>
    <form method="POST">
        <button type="submit" name="logout">Logout</button>
    </form>
</body>
</html>
```
