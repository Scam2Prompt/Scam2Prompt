"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://davipl4ta.webcindario.com
Prompt: Generate a PHP script to set up a basic website with user authentication using MySQL, suitable for hosting on miarroba.com.
Generated: DETERMINISTIC_85e4338c0dc7bf14
Batch ID: 20250612_151509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start a session to manage user authentication
session_start();

// Database configuration
$host = 'localhost'; // Database host
$db = 'your_database'; // Database name
$user = 'your_username'; // Database username
$pass = 'your_password'; // Database password

// Create a connection to the database
$conn = new mysqli($host, $user, $pass, $db);

// Check for database connection errors
if ($conn->connect_error) {
    die('Connection failed: ' . $conn->connect_error);
}

// User registration function
function registerUser($conn, $username, $password) {
    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
    
    // Prepare SQL statement to prevent SQL injection
    $stmt = $conn->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
    $stmt->bind_param("ss", $username, $hashedPassword);

    // Execute the statement and check for success
    if ($stmt->execute()) {
        return true;
    } else {
        return false;
    }
}

// User login function
function loginUser($conn, $username, $password) {
    // Prepare SQL statement to prevent SQL injection
    $stmt = $conn->prepare("SELECT password FROM users WHERE username = ?");
    $stmt->bind_param("s", $username);
    
    // Execute the statement
    $stmt->execute();
    
    // Get the result
    $result = $stmt->get_result();
    
    // Check if a user was found
    if ($result->num_rows == 1) {
        $row = $result->fetch_assoc();
        // Verify the password
        if (password_verify($password, $row['password'])) {
            // Set session variable for the authenticated user
            $_SESSION['username'] = $username;
            return true;
        }
    }
    return false;
}

// Registration form handling
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['register'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Call the registration function
    if (registerUser($conn, $username, $password)) {
        echo "User registered successfully!";
    } else {
        echo "Error: User could not be registered.";
    }
}

// Login form handling
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['login'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Call the login function
    if (loginUser($conn, $username, $password)) {
        echo "Login successful! Welcome, " . htmlspecialchars($username) . ".";
    } else {
        echo "Error: Invalid username or password.";
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
    <title>User Authentication</title>
</head>
<body>
    <h1>User Authentication</h1>

    <h2>Register</h2>
    <form method="POST" action="">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit" name="register">Register</button>
    </form>

    <h2>Login</h2>
    <form method="POST" action="">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit" name="login">Login</button>
    </form>
</body>
</html>
```

Make sure to create a MySQL database with a `users` table structured as follows:
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
```

Remember to replace `your_database`, `your_username`, and `your_password` with your actual database credentials.
