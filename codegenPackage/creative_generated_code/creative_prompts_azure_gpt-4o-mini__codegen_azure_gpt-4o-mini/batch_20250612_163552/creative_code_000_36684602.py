"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coosella5554.webcindario.com
Prompt: How can I create a free website using PHP and MySQL as mentioned on coosella5554.webcindario.com?
Generated: DETERMINISTIC_366846022b69a749
Batch ID: 20250612_163552
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
define('DB_SERVER', 'localhost');
define('DB_USERNAME', 'your_username');
define('DB_PASSWORD', 'your_password');
define('DB_DATABASE', 'your_database');

// Create a connection to the MySQL database
function connectDatabase() {
    $connection = new mysqli(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_DATABASE);

    // Check for connection errors
    if ($connection->connect_error) {
        die("Connection failed: " . $connection->connect_error);
    }
    return $connection;
}

// Function to create a new user
function createUser($username, $password) {
    $connection = connectDatabase();
    
    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
    
    // Prepare an SQL statement to prevent SQL injection
    $stmt = $connection->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
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
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Validate the input
        if (empty($_POST["username"]) || empty($_POST["password"])) {
            die("Username and password are required.");
        }
        
        $username = trim($_POST["username"]);
        $password = trim($_POST["password"]);
        
        // Call createUser function to register the user
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
    <h2>User Registration</h2>
    <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
        <label for="username">Username:</label>
        <input type="text" name="username" id="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" name="password" id="password" required>
        <br>
        <input type="submit" value="Register">
    </form>
    
    <?php registerUser(); ?>
</body>
</html>
```

**Note**: Replace `'your_username'`, `'your_password'`, and `'your_database'` with your actual database credentials. Ensure that a `users` table exists in your database with columns for `username` and `password`.
