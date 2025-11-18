"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonanzavc.com
Prompt: Write code in PHP to implement a login system that validates usernames and passwords, and redirects users to their membership dashboard based on their earning level.
Generated: DETERMINISTIC_28d507dd2e1cef58
Batch ID: 20250612_154058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start a session to manage user login state
session_start();

// Database connection parameters (adjust as needed)
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', 'password');
define('DB_NAME', 'membership');

// Connect to the database
try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die('Database connection failed: ' . $e->getMessage());
}

// Function to validate login credentials
function validateLogin($username, $password, $pdo) {
    // Prepare the SQL statement to fetch the user based on the username
    $stmt = $pdo->prepare("SELECT id, username, password, earning_level FROM users WHERE username = :username");
    $stmt->bindParam(':username', $username);
    $stmt->execute();

    // Fetch the user record
    $user = $stmt->fetch(PDO::FETCH_ASSOC);

    // Validate password and return user details if valid
    if ($user && password_verify($password, $user['password'])) {
        return $user;
    }

    return null; // Return null if validation fails
}

// Check if the login form was submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize input to prevent SQL injection
    $username = htmlspecialchars(trim($_POST['username']));
    $password = trim($_POST['password']);

    // Validate credentials
    $user = validateLogin($username, $password, $pdo);

    if ($user) {
        // Store user details in the session
        $_SESSION['user_id'] = $user['id'];
        $_SESSION['username'] = $user['username'];

        // Redirect based on earning level
        switch ($user['earning_level']) {
            case 'low':
                header('Location: low_earning_dashboard.php');
                break;
            case 'medium':
                header('Location: medium_earning_dashboard.php');
                break;
            case 'high':
                header('Location: high_earning_dashboard.php');
                break;
            default:
                header('Location: general_dashboard.php');
                break;
        }
        exit; // Ensure no further code is executed after redirection
    } else {
        // Set an error message for invalid credentials
        $error = "Invalid username or password.";
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
    <h1>Login</h1>
    <?php
    // Display error message if login failed
    if (isset($error)) {
        echo "<p style='color: red;'>$error</p>";
    }
    ?>
    <form method="post" action="">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br><br>
        <button type="submit">Login</button>
    </form>
</body>
</html>
```

**Note:** Ensure the `users` table in your database has columns: `id`, `username`, `password`, and `earning_level`. Passwords should be stored hashed using `password_hash()`.
