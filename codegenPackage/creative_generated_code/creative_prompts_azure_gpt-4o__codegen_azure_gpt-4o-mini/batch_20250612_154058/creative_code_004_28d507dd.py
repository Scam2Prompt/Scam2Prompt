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
// Start the session to manage user login state
session_start();

/**
 * Database connection settings
 */
$host = 'localhost'; // Database host
$db   = 'your_database'; // Database name
$user = 'your_username'; // Database username
$pass = 'your_password'; // Database password

try {
    // Create a new PDO instance for database connection
    $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8", $user, $pass);
    // Set error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Function to validate user credentials
 *
 * @param string $username
 * @param string $password
 * @return array|null
 */
function validateUser($username, $password) {
    global $pdo;

    // Prepare SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("SELECT id, username, password, earning_level FROM users WHERE username = :username");
    $stmt->bindParam(':username', $username);
    $stmt->execute();

    // Fetch user data
    $user = $stmt->fetch(PDO::FETCH_ASSOC);

    // Verify password and return user data if valid
    if ($user && password_verify($password, $user['password'])) {
        return $user;
    }
    return null;
}

/**
 * Function to redirect users based on their earning level
 *
 * @param int $earningLevel
 */
function redirectToDashboard($earningLevel) {
    switch ($earningLevel) {
        case '1':
            header("Location: dashboard_level_1.php");
            break;
        case '2':
            header("Location: dashboard_level_2.php");
            break;
        case '3':
            header("Location: dashboard_level_3.php");
            break;
        default:
            header("Location: dashboard_default.php");
            break;
    }
    exit();
}

// Check if the form has been submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Retrieve and sanitize input
    $username = filter_input(INPUT_POST, 'username', FILTER_SANITIZE_STRING);
    $password = filter_input(INPUT_POST, 'password', FILTER_SANITIZE_STRING);

    // Validate user credentials
    $user = validateUser($username, $password);

    if ($user) {
        // Store user ID in session
        $_SESSION['user_id'] = $user['id'];
        $_SESSION['username'] = $user['username'];

        // Redirect based on earning level
        redirectToDashboard($user['earning_level']);
    } else {
        // Handle invalid login
        $error = "Invalid username or password.";
    }
}
?>

<!-- Basic HTML form for user login -->
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
        <p style="color:red;"><?php echo $error; ?></p>
    <?php endif; ?>
    <form action="" method="post">
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
