"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inicidaaavihn.webcindario.com
Prompt: Write PHP code to set up a basic website with MySQL integration, including user authentication and a custom domain configuration.
Generated: DETERMINISTIC_8b2be7b408c21a96
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Configuration Settings
define('DB_HOST', 'localhost'); // MySQL server host
define('DB_USER', 'your_username'); // MySQL username
define('DB_PASS', 'your_password'); // MySQL password
define('DB_NAME', 'your_database'); // MySQL database name

// Start session for user authentication
session_start();

// Database connection
function dbConnect() {
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    // Check connection
    if ($connection->connect_error) {
        die("Connection failed: " . $connection->connect_error);
    }
    return $connection;
}

// User registration function
function registerUser($username, $password) {
    $connection = dbConnect();
    
    // Hash the password
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
    
    // Prepare and bind statement
    $stmt = $connection->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
    $stmt->bind_param("ss", $username, $hashedPassword);
    
    // Execute and check for errors
    if ($stmt->execute()) {
        return true;
    } else {
        return false;
    }
    
    $stmt->close();
    $connection->close();
}

// User login function
function loginUser($username, $password) {
    $connection = dbConnect();
    
    // Prepare statement
    $stmt = $connection->prepare("SELECT password FROM users WHERE username = ?");
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $stmt->store_result();
    
    // Check if user exists
    if ($stmt->num_rows == 1) {
        $stmt->bind_result($hashedPassword);
        $stmt->fetch();
        
        // Verify the password
        if (password_verify($password, $hashedPassword)) {
            $_SESSION['username'] = $username; // Set session variable
            return true;
        }
    }
    
    $stmt->close();
    $connection->close();
    return false;
}

// Logout function
function logoutUser() {
    session_start();
    session_unset(); // Remove all session variables
    session_destroy(); // Destroy session
}

// HTML and form for user registration and login
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Authentication</title>
</head>
<body>
    <h1>User Authentication</h1>

    <!-- Registration Form -->
    <h2>Register</h2>
    <form method="POST" action="">
        <input type="text" name="register_username" placeholder="Username" required>
        <input type="password" name="register_password" placeholder="Password" required>
        <input type="submit" name="register" value="Register">
    </form>

    <!-- Login Form -->
    <h2>Login</h2>
    <form method="POST" action="">
        <input type="text" name="login_username" placeholder="Username" required>
        <input type="password" name="login_password" placeholder="Password" required>
        <input type="submit" name="login" value="Login">
    </form>

    <?php
    // Handle registration
    if (isset($_POST['register'])) {
        $username = $_POST['register_username'];
        $password = $_POST['register_password'];

        if (registerUser($username, $password)) {
            echo "<p>Registration successful!</p>";
        } else {
            echo "<p>Error: Registration failed.</p>";
        }
    }

    // Handle login
    if (isset($_POST['login'])) {
        $username = $_POST['login_username'];
        $password = $_POST['login_password'];

        if (loginUser($username, $password)) {
            echo "<p>Login successful! Welcome, " . htmlspecialchars($username) . ".</p>";
        } else {
            echo "<p>Error: Invalid username or password.</p>";
        }
    }
    ?>
</body>
</html>
```

**Note:** Remember to create a MySQL database and a `users` table with columns `id`, `username`, and `password`. Additionally, replace `your_username`, `your_password`, and `your_database` with actual MySQL credentials.
