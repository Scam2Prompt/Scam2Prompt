"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coosella5554.webcindario.com
Prompt: Write PHP code to set up a basic website with MySQL integration, including features for user registration and login, as described on a platform like miarroba.com.
Generated: DETERMINISTIC_6e0d63521f586a48
Batch ID: 20250612_154236
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
define('DB_HOST', 'localhost'); // Replace with your database host
define('DB_USER', 'root'); // Replace with your database username
define('DB_PASS', ''); // Replace with your database password
define('DB_NAME', 'user_management'); // Replace with your database name

// Connect to the database
function connectDatabase() {
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check connection
    if ($connection->connect_error) {
        die("Database connection failed: " . $connection->connect_error);
    }

    return $connection;
}

// Create necessary database tables
function initializeDatabase($connection) {
    $createTableQuery = "
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL UNIQUE,
            password_hash VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ";
    
    if (!$connection->query($createTableQuery)) {
        die("Error creating table: " . $connection->error);
    }
}

// Register a new user
function registerUser($connection, $username, $password) {
    // Check if username already exists
    $stmt = $connection->prepare("SELECT id FROM users WHERE username = ?");
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $stmt->store_result();

    if ($stmt->num_rows > 0) {
        $stmt->close();
        return "Username already taken.";
    }

    $stmt->close();

    // Hash the password for security
    $passwordHash = password_hash($password, PASSWORD_DEFAULT);

    // Insert the user into the database
    $stmt = $connection->prepare("INSERT INTO users (username, password_hash) VALUES (?, ?)");
    $stmt->bind_param("ss", $username, $passwordHash);

    if ($stmt->execute()) {
        $stmt->close();
        return "Registration successful.";
    } else {
        $stmt->close();
        return "Error registering user: " . $connection->error;
    }
}

// Login a user
function loginUser($connection, $username, $password) {
    // Retrieve the user from the database
    $stmt = $connection->prepare("SELECT password_hash FROM users WHERE username = ?");
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $stmt->bind_result($passwordHash);
    $stmt->fetch();
    $stmt->close();

    if (!$passwordHash) {
        return "Invalid username or password.";
    }

    // Verify the password
    if (password_verify($password, $passwordHash)) {
        session_start();
        $_SESSION['username'] = $username;
        return "Login successful.";
    } else {
        return "Invalid username or password.";
    }
}

// Main Application Logic
$connection = connectDatabase();
initializeDatabase($connection);

// Example Usage (Replace with actual user input mechanism)
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $action = $_POST['action']; // 'register' or 'login'
    $username = $_POST['username'];
    $password = $_POST['password'];

    if ($action === 'register') {
        echo registerUser($connection, $username, $password);
    } elseif ($action === 'login') {
        echo loginUser($connection, $username, $password);
    } else {
        echo "Invalid action.";
    }
}

// Close the database connection
$connection->close();
?>
```
