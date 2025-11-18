"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daviplataportal.webcindario.com
Prompt: Provide an example of a PHP-based login system that integrates with MySQL for free hosting environments.
Generated: DETERMINISTIC_9df99080864bf556
Batch ID: 20250612_151446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start session management
session_start();

// Database configuration
$host = 'localhost'; // Database host
$db_name = 'your_database_name'; // Database name
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password

// Connect to MySQL database
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db_name", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to sanitize user inputs
function sanitize($data) {
    return htmlspecialchars(stripslashes(trim($data)));
}

// Handle login form submission
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Sanitize user inputs
    $username = sanitize($_POST['username']);
    $password = sanitize($_POST['password']);

    // Validate inputs
    if (empty($username) || empty($password)) {
        $error = "Username and password are required.";
    } else {
        // Prepare and execute SQL statement to retrieve user
        $stmt = $pdo->prepare("SELECT * FROM users WHERE username = :username LIMIT 1");
        $stmt->bindParam(':username', $username);
        $stmt->execute();

        // Check if user exists
        if ($stmt->rowCount() == 1) {
            $user = $stmt->fetch(PDO::FETCH_ASSOC);

            // Verify password
            if (password_verify($password, $user['password'])) {
                // Set session variables
                $_SESSION['user_id'] = $user['id'];
                $_SESSION['username'] = $user['username'];
                // Redirect to dashboard or home page
                header("Location: dashboard.php");
                exit();
            } else {
                $error = "Invalid username or password.";
            }
        } else {
            $error = "Invalid username or password.";
        }
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>
    <?php if (isset($error)): ?>
        <p style="color: red;"><?= $error; ?></p>
    <?php endif; ?>
    <form method="POST" action="">
        <label for="username">Username:</label>
        <input type="text" name="username" id="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" name="password" id="password" required>
        <br>
        <button type="submit">Login</button>
    </form>
</body>
</html>
```

### Notes:
- Replace `your_database_name`, `your_username`, and `your_password` with your actual database credentials.
- Ensure your MySQL table `users` has at least the columns `id`, `username`, and `password`, where `password` is hashed using `password_hash()` when users are registered.
- The code includes basic error handling and sanitization of inputs to mitigate SQL injection and XSS attacks.
