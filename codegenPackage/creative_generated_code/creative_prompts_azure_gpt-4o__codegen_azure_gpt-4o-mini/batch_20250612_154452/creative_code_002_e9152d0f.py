"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbasegift.epizy.com
Prompt: Generate PHP code for a website that can be hosted on a service with modern cPanel and multiple PHP versions, such as the one offered by iFastNet.
Generated: DETERMINISTIC_e9152d0f8791ecc1
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start the session
session_start();

/**
 * Function to connect to the database
 *
 * @return PDO instance
 * @throws Exception if the connection fails
 */
function connectToDatabase() {
    $host = 'localhost'; // Database host
    $db   = 'your_database_name'; // Database name
    $user = 'your_username'; // Database username
    $pass = 'your_password'; // Database password
    $charset = 'utf8mb4'; // Database charset

    $dsn = "mysql:host=$host;dbname=$db;charset=$charset";
    $options = [
        PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES   => false,
    ];

    try {
        return new PDO($dsn, $user, $pass, $options);
    } catch (\PDOException $e) {
        throw new Exception("Database connection failed: " . $e->getMessage());
    }
}

/**
 * Function to handle user login
 *
 * @param string $username
 * @param string $password
 * @return bool
 */
function loginUser($username, $password) {
    $pdo = connectToDatabase();

    // Prepare SQL query to prevent SQL injection
    $stmt = $pdo->prepare("SELECT password FROM users WHERE username = :username");
    $stmt->execute(['username' => $username]);
    
    $user = $stmt->fetch();

    // Password verification
    if ($user && password_verify($password, $user['password'])) {
        $_SESSION['username'] = $username; // Set session variable
        return true;
    }
    return false;
}

/**
 * Function to handle user logout
 */
function logoutUser() {
    // Unset all of the session variables
    $_SESSION = [];
    // Destroy the session
    session_destroy();
}

/**
 * Function to display messages
 *
 * @param string $message
 */
function displayMessage($message) {
    echo "<p>{$message}</p>";
}

// Main execution flow
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Check if login form is submitted
    if (isset($_POST['login'])) {
        $username = trim($_POST['username']);
        $password = trim($_POST['password']);

        // Attempt to log in the user
        if (loginUser($username, $password)) {
            displayMessage("Login successful! Welcome, {$username}.");
        } else {
            displayMessage("Login failed! Invalid username or password.");
        }
    }

    // Check if logout form is submitted
    if (isset($_POST['logout'])) {
        logoutUser();
        displayMessage("You have been logged out.");
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Page</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS file -->
</head>
<body>
    <div class="container">
        <h1>Login</h1>
        <form method="POST" action="">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit" name="login">Login</button>
        </form>

        <form method="POST" action="">
            <button type="submit" name="logout">Logout</button>
        </form>
    </div>
</body>
</html>
```

### Notes:
- Replace `your_database_name`, `your_username`, and `your_password` with actual database credentials.
- The `styles.css` file should be created separately to style the HTML content.
