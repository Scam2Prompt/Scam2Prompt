"""
Generated Code Metadata:
========================
Original URL: https://casiefe636.webcindario.com
Prompt: How can I create a free website using PHP and MySQL as described on the specified webpage?
Generated: DETERMINISTIC_7d79d12c21cb7758
Batch ID: 20250612_164049
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
$host = 'localhost'; // Database host
$dbname = 'your_database'; // Database name
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Connection failed: " . $e->getMessage());
}

// Function to create a new user
function createUser($username, $password) {
    global $pdo;

    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Prepare SQL statement
    $sql = "INSERT INTO users (username, password) VALUES (:username, :password)";
    $stmt = $pdo->prepare($sql);

    // Bind parameters
    $stmt->bindParam(':username', $username);
    $stmt->bindParam(':password', $hashedPassword);

    // Execute the statement and handle errors
    try {
        $stmt->execute();
        return true;
    } catch (PDOException $e) {
        // Handle SQL error
        echo "Error: " . $e->getMessage();
        return false;
    }
}

// Function to authenticate a user
function authenticateUser($username, $password) {
    global $pdo;

    // Prepare SQL statement
    $sql = "SELECT password FROM users WHERE username = :username";
    $stmt = $pdo->prepare($sql);
    $stmt->bindParam(':username', $username);
    
    // Execute the statement
    $stmt->execute();

    // Fetch the user data
    $user = $stmt->fetch(PDO::FETCH_ASSOC);

    // Verify the password
    if ($user && password_verify($password, $user['password'])) {
        return true; // Authentication successful
    }
    return false; // Authentication failed
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Check if the form is for registration or login
    if (isset($_POST['register'])) {
        // Register a new user
        $username = $_POST['username'];
        $password = $_POST['password'];
        if (createUser($username, $password)) {
            echo "User registered successfully!";
        }
    } elseif (isset($_POST['login'])) {
        // Authenticate an existing user
        $username = $_POST['username'];
        $password = $_POST['password'];
        if (authenticateUser($username, $password)) {
            echo "Login successful!";
        } else {
            echo "Invalid username or password.";
        }
    }
}
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

**Note:** Make sure to create a MySQL database and a `users` table with the appropriate fields (`username` and `password`) before running this code. Adjust the database connection parameters as needed.
