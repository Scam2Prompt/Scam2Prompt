"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vxp.pertinencemediaa.com
Prompt: Develop a PHP-based login system for a VIP membership portal, including session management and user authentication.
Generated: DETERMINISTIC_a406b566da474dad
Batch ID: 20250612_150119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start a session to handle user authentication
session_start();

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', 'password');
define('DB_NAME', 'vip_portal');

// Connect to the database
function connectToDatabase()
{
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check for a connection error and exit if necessary
    if ($conn->connect_error) {
        die('Database connection failed: ' . $conn->connect_error);
    }

    return $conn;
}

// Sanitize input to prevent SQL injection and XSS attacks
function sanitizeInput($input)
{
    return htmlspecialchars(strip_tags(trim($input)));
}

// Process the login form
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['login'])) {
    // Sanitize user input
    $username = sanitizeInput($_POST['username']);
    $password = sanitizeInput($_POST['password']);

    if (empty($username) || empty($password)) {
        $error = "Please fill in both fields.";
    } else {
        $conn = connectToDatabase();

        // Prepare a SQL statement to fetch the user
        $stmt = $conn->prepare("SELECT id, username, password_hash FROM users WHERE username = ?");
        $stmt->bind_param("s", $username);
        $stmt->execute();
        $stmt->store_result();

        if ($stmt->num_rows === 1) {
            // Bind the result and fetch the user details
            $stmt->bind_result($id, $dbUsername, $dbPasswordHash);
            $stmt->fetch();

            // Verify the password
            if (password_verify($password, $dbPasswordHash)) {
                // Set session variables
                $_SESSION['user_id'] = $id;
                $_SESSION['username'] = $dbUsername;

                // Redirect to the VIP dashboard
                header("Location: vip_dashboard.php");
                exit();
            } else {
                $error = "Invalid username or password.";
            }
        } else {
            $error = "Invalid username or password.";
        }

        // Close the statement and connection
        $stmt->close();
        $conn->close();
    }
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VIP Membership Login</title>
</head>
<body>
    <h2>VIP Membership Login</h2>
    <?php if (isset($error)): ?>
        <p style="color: red;"><?php echo $error; ?></p>
    <?php endif; ?>
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

<?php
// VIP dashboard page (vip_dashboard.php)
/*
    To be created separately. This page should check if the user is logged in by validating the session variables.
    Redirect unauthenticated users back to the login page.
*/
?>
```
