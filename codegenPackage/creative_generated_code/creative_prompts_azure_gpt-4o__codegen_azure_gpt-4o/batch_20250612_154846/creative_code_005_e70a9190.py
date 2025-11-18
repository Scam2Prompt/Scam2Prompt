"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tronlink.at
Prompt: Develop a PHP script to handle login functionality for a site like VSO777, ensuring secure authentication and session management.
Generated: DETERMINISTIC_e70a9190ec6f090c
Batch ID: 20250612_154846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start the session to manage user login state
session_start();

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'root'); // Update as needed
define('DB_PASS', 'password'); // Update as needed
define('DB_NAME', 'vso777'); // Update as needed

// Helper function to connect to the database
function connectToDatabase() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    if ($conn->connect_error) {
        die("Database connection failed: " . $conn->connect_error);
    }
    return $conn;
}

// Function to sanitize user input to prevent SQL injection
function sanitizeInput($input, $conn) {
    return htmlspecialchars($conn->real_escape_string($input));
}

// Function to handle login
function login($username, $password) {
    $conn = connectToDatabase();

    // Sanitize user input
    $username = sanitizeInput($username, $conn);
    $password = sanitizeInput($password, $conn);

    // Query to fetch the user from the database
    $query = "SELECT id, username, password_hash FROM users WHERE username = ?";
    $stmt = $conn->prepare($query);
    $stmt->bind_param('s', $username);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows === 1) {
        $user = $result->fetch_assoc();

        // Verify the password with the stored hash
        if (password_verify($password, $user['password_hash'])) {
            // Regenerate session ID to prevent session fixation
            session_regenerate_id();

            // Set session variables for the user
            $_SESSION['user_id'] = $user['id'];
            $_SESSION['username'] = $user['username'];
            $_SESSION['logged_in'] = true;

            $stmt->close();
            $conn->close();

            return true; // Login successful
        } else {
            $stmt->close();
            $conn->close();

            return false; // Invalid password
        }
    } else {
        $stmt->close();
        $conn->close();

        return false; // User not found
    }
}

// Check if the login form was submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = $_POST['username'] ?? '';
    $password = $_POST['password'] ?? '';

    if (!empty($username) && !empty($password)) {
        if (login($username, $password)) {
            // Redirect to dashboard or home page after successful login
            header("Location: dashboard.php");
            exit();
        } else {
            echo "<p style='color:red;'>Invalid username or password.</p>";
        }
    } else {
        echo "<p style='color:red;'>Please fill in both fields.</p>";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - VSO777</title>
</head>
<body>
    <h1>Login</h1>
    <form action="" method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br><br>
        <button type="submit">Login</button>
    </form>
</body>
</html>
```
