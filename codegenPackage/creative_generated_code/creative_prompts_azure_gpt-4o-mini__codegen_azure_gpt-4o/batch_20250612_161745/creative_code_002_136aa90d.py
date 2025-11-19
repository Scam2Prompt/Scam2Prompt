"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Create a code snippet in PHP that handles user registration and login for an e-commerce website, inspired by the user account features on ebrasilbrazz.
Generated: DETERMINISTIC_136aa90d957f8942
Batch ID: 20250612_161745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database connection settings
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASSWORD', 'password');
define('DB_NAME', 'ecommerce');

// Establish database connection
function getDbConnection() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    return $conn;
}

// Function to register a new user
function registerUser($username, $email, $password) {
    $conn = getDbConnection();

    try {
        // Validate data
        if (empty($username) || empty($email) || empty($password)) {
            throw new Exception("All fields are required.");
        }

        // Check if email already exists
        $stmt = $conn->prepare("SELECT id FROM users WHERE email = ?");
        $stmt->bind_param("s", $email);
        $stmt->execute();
        $stmt->store_result();
        if ($stmt->num_rows > 0) {
            throw new Exception("Email already registered.");
        }
        $stmt->close();

        // Hash the password
        $hashedPassword = password_hash($password, PASSWORD_BCRYPT);

        // Insert the new user into the database
        $stmt = $conn->prepare("INSERT INTO users (username, email, password) VALUES (?, ?, ?)");
        $stmt->bind_param("sss", $username, $email, $hashedPassword);
        if (!$stmt->execute()) {
            throw new Exception("Failed to register user: " . $stmt->error);
        }

        echo "User registered successfully.";
        $stmt->close();
    } catch (Exception $e) {
        echo "Error: " . $e->getMessage();
    } finally {
        $conn->close();
    }
}

// Function to login an existing user
function loginUser($email, $password) {
    $conn = getDbConnection();

    try {
        // Validate data
        if (empty($email) || empty($password)) {
            throw new Exception("Email and password are required.");
        }

        // Fetch user by email
        $stmt = $conn->prepare("SELECT id, username, password FROM users WHERE email = ?");
        $stmt->bind_param("s", $email);
        $stmt->execute();
        $result = $stmt->get_result();

        if ($result->num_rows === 0) {
            throw new Exception("No user found with the provided email.");
        }

        $user = $result->fetch_assoc();
        $stmt->close();

        // Verify the password
        if (!password_verify($password, $user['password'])) {
            throw new Exception("Invalid password.");
        }

        // Start session and store user information
        session_start();
        $_SESSION['user_id'] = $user['id'];
        $_SESSION['username'] = $user['username'];

        echo "Login successful.";

    } catch (Exception $e) {
        echo "Error: " . $e->getMessage();
    } finally {
        $conn->close();
    }
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['action']) && $_POST['action'] === 'register') {
        registerUser($_POST['username'], $_POST['email'], $_POST['password']);
    } elseif (isset($_POST['action']) && $_POST['action'] === 'login') {
        loginUser($_POST['email'], $_POST['password']);
    }
}
?>
```

**Usage Instructions:**  
- Ensure that the `users` table exists in your database with at least the following fields: `id`, `username`, `email`, and `password`.  
- Place this code in a PHP file on your server.  
- Make POST requests to this script with `action="register"` or `action="login"`, and include the necessary fields (`username`, `email`, `password`).
