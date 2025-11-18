"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-crypto.yivesites.com
Prompt: Create a code snippet in PHP to handle user authentication and session management for the APELBET login system, considering cookie settings.
Generated: DETERMINISTIC_01e6a0b2355934c3
Batch ID: 20250612_151659
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

// Database configuration (update with your actual database credentials)
$host = 'localhost';
$dbname = 'apelbet';
$username = 'root';
$password = 'password';

try {
    // Create a new PDO instance for database connection
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC
    ]);
} catch (PDOException $e) {
    // Log the error and terminate script execution
    error_log("Database connection failed: " . $e->getMessage());
    die("Database connection error. Please try again later.");
}

// Function to handle user authentication
function authenticateUser($username, $password, $pdo) {
    // Prepare the SQL query to fetch the user by username
    $stmt = $pdo->prepare("SELECT id, username, password FROM users WHERE username = :username");
    $stmt->bindParam(':username', $username);

    // Execute the query
    $stmt->execute();

    // Fetch the user data
    $user = $stmt->fetch();

    // Verify the password
    if ($user && password_verify($password, $user['password'])) {
        return $user;
    }

    return false;
}

// Check if the login form has been submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Retrieve and sanitize user inputs
    $username = htmlspecialchars($_POST['username']);
    $password = htmlspecialchars($_POST['password']);

    // Authenticate the user
    $user = authenticateUser($username, $password, $pdo);

    if ($user) {
        // Set session variables
        $_SESSION['user_id'] = $user['id'];
        $_SESSION['username'] = $user['username'];

        // Set a secure cookie for session management
        setcookie('session_id', session_id(), [
            'expires' => time() + 3600, // 1 hour expiry
            'path' => '/',
            'domain' => '', // Set your domain if needed
            'secure' => true, // Ensure cookie is sent over HTTPS
            'httponly' => true, // Restrict cookie access via JavaScript
            'samesite' => 'Strict' // Prevent cross-site request forgery (CSRF)
        ]);

        // Redirect to a dashboard or homepage
        header("Location: dashboard.php");
        exit;
    } else {
        // Authentication failed, show an error message
        $error = "Invalid username or password.";
    }
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>APELBET Login</title>
</head>
<body>
    <h1>APELBET Login</h1>
    <?php if (isset($error)): ?>
        <p style="color:red;"><?php echo $error; ?></p>
    <?php endif; ?>
    <form method="POST" action="">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <button type="submit">Login</button>
    </form>
</body>
</html>
```
