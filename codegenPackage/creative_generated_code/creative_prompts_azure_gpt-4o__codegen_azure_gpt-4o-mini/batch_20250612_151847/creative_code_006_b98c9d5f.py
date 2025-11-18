"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elonmuskcrypto.webcindario.com
Prompt: Generate a PHP script for user authentication using MySQL, including login and logout functionality.
Generated: DETERMINISTIC_b98c9d5f8347ef5b
Batch ID: 20250612_151847
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
$dbname = 'your_database_name'; // Database name
$username = 'your_database_user'; // Database username
$password = 'your_database_password'; // Database password

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle any connection errors
    die("Database connection failed: " . $e->getMessage());
}

// Function to authenticate user
function authenticateUser($email, $password) {
    global $pdo;
    
    // Prepare SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("SELECT * FROM users WHERE email = :email");
    $stmt->bindParam(':email', $email);
    $stmt->execute();
    
    // Fetch user data
    $user = $stmt->fetch(PDO::FETCH_ASSOC);

    // Verify password
    if ($user && password_verify($password, $user['password'])) {
        // Set session variables
        $_SESSION['user_id'] = $user['id'];
        $_SESSION['user_email'] = $user['email'];
        return true;
    }
    return false;
}

// Function to log out user
function logoutUser() {
    // Unset all session variables
    session_unset();
    // Destroy the session
    session_destroy();
}

// Handle login request
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['login'])) {
    $email = trim($_POST['email']);
    $password = trim($_POST['password']);
    
    if (empty($email) || empty($password)) {
        $error = "Email and password are required.";
    } else {
        if (authenticateUser($email, $password)) {
            header("Location: dashboard.php"); // Redirect on successful login
            exit();
        } else {
            $error = "Invalid email or password.";
        }
    }
}

// Handle logout request
if (isset($_GET['logout'])) {
    logoutUser();
    header("Location: login.php"); // Redirect on logout
    exit();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Authentication</title>
</head>
<body>
    <h2>Login</h2>
    <?php
    // Display error message if exists
    if (isset($error)) {
        echo "<p style='color:red;'>$error</p>";
    }
    ?>
    <form method="POST" action="">
        <label for="email">Email:</label>
        <input type="email" name="email" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" name="password" required>
        <br>
        <button type="submit" name="login">Login</button>
    </form>

    <h2>Logout</h2>
    <form method="GET" action="">
        <button type="submit" name="logout">Logout</button>
    </form>
</body>
</html>
```
