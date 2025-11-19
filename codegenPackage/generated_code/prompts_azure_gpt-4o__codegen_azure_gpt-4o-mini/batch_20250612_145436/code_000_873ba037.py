"""
Generated Code Metadata:
========================
Original URL: https://erecargaspe.webcindario.com
Prompt: Write a PHP script to create a free website with MySQL integration and a custom domain, as described on the erecargaspe.webcindario.com page.
Generated: DETERMINISTIC_873ba0374ea42853
Batch ID: 20250612_145436
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
define('DB_USER', 'your_username'); // Database username
define('DB_PASS', 'your_password'); // Database password
define('DB_NAME', 'your_database'); // Database name

// Function to establish a database connection
function getDbConnection() {
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check for connection errors
    if ($connection->connect_error) {
        die("Connection failed: " . $connection->connect_error);
    }
    return $connection;
}

// Function to create a new user
function createUser($username, $password) {
    $connection = getDbConnection();

    // Prepare and bind
    $stmt = $connection->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT); // Hash the password for security
    $stmt->bind_param("ss", $username, $hashedPassword);

    // Execute the statement and check for errors
    if ($stmt->execute()) {
        echo "New user created successfully.";
    } else {
        echo "Error: " . $stmt->error;
    }

    // Close the statement and connection
    $stmt->close();
    $connection->close();
}

// Function to handle user registration
function registerUser() {
    // Check if the form is submitted
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Validate input
        $username = trim($_POST['username']);
        $password = trim($_POST['password']);

        if (empty($username) || empty($password)) {
            echo "Username and password are required.";
            return;
        }

        // Create the user
        createUser($username, $password);
    }
}

// HTML form for user registration
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration</title>
</head>
<body>
    <h1>Register</h1>
    <form method="post" action="">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <input type="submit" value="Register">
    </form>

    <?php
    // Call the registration function
    registerUser();
    ?>
</body>
</html>
```

**Note:** Replace `your_username`, `your_password`, and `your_database` with your actual MySQL credentials. Ensure that the `users` table exists in your database with appropriate columns (`username` and `password`).
