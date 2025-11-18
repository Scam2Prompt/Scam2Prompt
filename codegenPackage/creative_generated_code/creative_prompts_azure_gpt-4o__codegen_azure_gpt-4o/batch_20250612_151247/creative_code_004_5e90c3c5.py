"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seguritydecuenta.webcindario.com
Prompt: Write a PHP script to handle user registration and login functionality for a website hosted on a free platform with MySQL support.
Generated: DETERMINISTIC_5e90c3c573093e8e
Batch ID: 20250612_151247
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start a session for handling user login state
session_start();

// Database configuration
$host = "localhost";       // Change this if your database host differs
$db_name = "your_database"; // Replace with your database name
$db_user = "your_username"; // Replace with your database username
$db_pass = "your_password"; // Replace with your database password

// Create a database connection
$conn = new mysqli($host, $db_user, $db_pass, $db_name);

// Check connection
if ($conn->connect_error) {
    die("Database connection failed: " . $conn->connect_error);
}

// Function to sanitize user input
function sanitize_input($data) {
    return htmlspecialchars(strip_tags(trim($data)));
}

// Handle user registration
if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_POST['register'])) {
    // Sanitize input
    $username = sanitize_input($_POST['username']);
    $password = sanitize_input($_POST['password']);
    $email = sanitize_input($_POST['email']);

    // Validate input
    if (empty($username) || empty($password) || empty($email)) {
        echo "All fields are required.";
        exit;
    }

    // Check if username or email is already taken
    $stmt = $conn->prepare("SELECT id FROM users WHERE username = ? OR email = ?");
    $stmt->bind_param("ss", $username, $email);
    $stmt->execute();
    $stmt->store_result();

    if ($stmt->num_rows > 0) {
        echo "Username or email already exists.";
        $stmt->close();
        exit;
    }
    $stmt->close();

    // Hash the password for security
    $hashed_password = password_hash($password, PASSWORD_DEFAULT);

    // Insert the new user into the database
    $stmt = $conn->prepare("INSERT INTO users (username, password, email) VALUES (?, ?, ?)");
    $stmt->bind_param("sss", $username, $hashed_password, $email);

    if ($stmt->execute()) {
        echo "Registration successful!";
    } else {
        echo "Error: " . $stmt->error;
    }
    $stmt->close();
}

// Handle user login
if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_POST['login'])) {
    // Sanitize input
    $username = sanitize_input($_POST['username']);
    $password = sanitize_input($_POST['password']);

    // Validate input
    if (empty($username) || empty($password)) {
        echo "Username and password are required.";
        exit;
    }

    // Fetch user data from the database
    $stmt = $conn->prepare("SELECT id, password FROM users WHERE username = ?");
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $stmt->store_result();

    if ($stmt->num_rows === 0) {
        echo "Invalid username or password.";
        $stmt->close();
        exit;
    }

    $stmt->bind_result($user_id, $hashed_password);
    $stmt->fetch();

    // Verify the password
    if (password_verify($password, $hashed_password)) {
        $_SESSION['user_id'] = $user_id;
        $_SESSION['username'] = $username;
        echo "Login successful!";
    } else {
        echo "Invalid username or password.";
    }
    $stmt->close();
}

// Close the database connection
$conn->close();
?>

<!-- HTML Form -->
<!DOCTYPE html>
<html>
<head>
    <title>User Registration and Login</title>
</head>
<body>
    <h1>User Registration and Login</h1>

    <!-- Registration Form -->
    <h2>Register</h2>
    <form method="POST" action="">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <button type="submit" name="register">Register</button>
    </form>

    <!-- Login Form -->
    <h2>Login</h2>
    <form method="POST" action="">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <button type="submit" name="login">Login</button>
    </form>
</body>
</html>
```
