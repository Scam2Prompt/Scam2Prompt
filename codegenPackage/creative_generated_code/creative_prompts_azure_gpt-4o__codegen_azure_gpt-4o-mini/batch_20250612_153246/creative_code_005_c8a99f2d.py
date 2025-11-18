"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://granstore.co
Prompt: Create a script in PHP to handle user registration and login functionality for the GranStore website, ensuring secure password storage.
Generated: DETERMINISTIC_c8a99f2d16cdd399
Batch ID: 20250612_153246
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
define('DB_HOST', 'localhost');
define('DB_NAME', 'granstoredb');
define('DB_USER', 'username');
define('DB_PASS', 'password');

// Create a connection to the database
function getDbConnection() {
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    
    // Check for connection errors
    if ($connection->connect_error) {
        die("Connection failed: " . $connection->connect_error);
    }
    
    return $connection;
}

// Function to register a new user
function registerUser($username, $password) {
    // Validate input
    if (empty($username) || empty($password)) {
        throw new Exception("Username and password cannot be empty.");
    }

    // Hash the password for secure storage
    $hashedPassword = password_hash($password, PASSWORD_BCRYPT);

    // Prepare and bind to prevent SQL injection
    $connection = getDbConnection();
    $stmt = $connection->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
    $stmt->bind_param("ss", $username, $hashedPassword);

    // Execute the statement and check for errors
    if (!$stmt->execute()) {
        throw new Exception("Registration failed: " . $stmt->error);
    }

    $stmt->close();
    $connection->close();

    return "User registered successfully.";
}

// Function to login a user
function loginUser($username, $password) {
    // Validate input
    if (empty($username) || empty($password)) {
        throw new Exception("Username and password cannot be empty.");
    }

    $connection = getDbConnection();
    // Prepare statement to fetch the user's hashed password
    $stmt = $connection->prepare("SELECT password FROM users WHERE username = ?");
    $stmt->bind_param("s", $username);
    $stmt->execute();
    
    // Bind result
    $stmt->bind_result($hashedPassword);
    $stmt->fetch();
    
    // Check if the username exists and verify the password
    if ($hashedPassword && password_verify($password, $hashedPassword)) {
        session_start();
        $_SESSION['username'] = $username; // Store username in session
        $stmt->close();
        $connection->close();
        return "Login successful.";
    } else {
        $stmt->close();
        $connection->close();
        throw new Exception("Invalid username or password.");
    }
}

// Example usage
try {
    // Uncomment to register a user
    // echo registerUser('testUser', 'securePassword123');

    // Uncomment to login a user
    // echo loginUser('testUser', 'securePassword123');
} catch (Exception $e) {
    echo 'Error: ' . $e->getMessage();
}
?>
```

**Note:** Ensure to replace `'localhost'`, `'granstoredb'`, `'username'`, and `'password'` with your actual database connection details. Additionally, uncomment the example usage section to test registration and login functionalities.
