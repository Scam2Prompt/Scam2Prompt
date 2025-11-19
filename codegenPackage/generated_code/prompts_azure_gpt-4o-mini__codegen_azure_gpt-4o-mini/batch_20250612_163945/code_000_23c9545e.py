"""
Generated Code Metadata:
========================
Original URL: https://davivihnasd1.webcindario.com
Prompt: How can I create a free website using PHP and MySQL as mentioned on the page?
Generated: DETERMINISTIC_23c9545e9c016905
Batch ID: 20250612_163945
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
define('DB_HOST', 'localhost'); // Database host
define('DB_USER', 'root'); // Database username
define('DB_PASS', ''); // Database password
define('DB_NAME', 'my_database'); // Database name

// Create a connection to the MySQL database
$conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

// Check for connection errors
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Function to create a new user
function createUser($username, $password) {
    global $conn;

    // Prepare and bind
    $stmt = $conn->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
    if ($stmt === false) {
        die("Prepare failed: " . htmlspecialchars($conn->error));
    }

    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Bind parameters
    $stmt->bind_param("ss", $username, $hashedPassword);

    // Execute the statement
    if (!$stmt->execute()) {
        die("Execute failed: " . htmlspecialchars($stmt->error));
    }

    // Close the statement
    $stmt->close();
}

// Function to authenticate a user
function authenticateUser($username, $password) {
    global $conn;

    // Prepare and bind
    $stmt = $conn->prepare("SELECT password FROM users WHERE username = ?");
    if ($stmt === false) {
        die("Prepare failed: " . htmlspecialchars($conn->error));
    }

    // Bind parameters
    $stmt->bind_param("s", $username);

    // Execute the statement
    $stmt->execute();

    // Store the result
    $stmt->store_result();

    // Check if user exists
    if ($stmt->num_rows === 0) {
        return false; // User not found
    }

    // Bind result
    $stmt->bind_result($hashedPassword);
    $stmt->fetch();

    // Verify the password
    return password_verify($password, $hashedPassword);
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Check if the form is for registration or login
    if (isset($_POST['register'])) {
        createUser($_POST['username'], $_POST['password']);
        echo "User registered successfully!";
    } elseif (isset($_POST['login'])) {
        if (authenticateUser($_POST['username'], $_POST['password'])) {
            echo "Login successful!";
        } else {
            echo "Invalid username or password.";
        }
    }
}

// Close the database connection
$conn->close();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Free Website with PHP and MySQL</title>
</head>
<body>
    <h1>Create an Account</h1>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit" name="register">Register</button>
    </form>

    <h1>Login</h1>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit" name="login">Login</button>
    </form>
</body>
</html>
```

**Note:** Ensure that you have a MySQL database set up with a `users` table that has `username` and `password` columns. The `username` should be unique.
