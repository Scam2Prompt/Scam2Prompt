"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coastalboatrentals.co.za
Prompt: Create a PHP script to integrate a login system for users to manage their bookings, referencing features like "My Booking Login" and "Basket" from the website.
Generated: DETERMINISTIC_7f2f38a6def33214
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
session_start(); // Start session to manage user sessions

// Database connection parameters
$host = 'localhost'; // Database host
$db = 'booking_system'; // Database name
$user = 'root'; // Database username
$pass = ''; // Database password

// Establish database connection
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die('Database connection failed: ' . $e->getMessage());
}

// Function to handle user login
function loginUser($email, $password) {
    global $pdo;

    // Prepare and execute the SQL statement
    $stmt = $pdo->prepare('SELECT id, password FROM users WHERE email = :email');
    $stmt->execute(['email' => $email]);
    
    // Fetch user data
    $user = $stmt->fetch(PDO::FETCH_ASSOC);
    
    if ($user && password_verify($password, $user['password'])) {
        // Set session variables upon successful login
        $_SESSION['user_id'] = $user['id'];
        return true;
    }
    return false;
}

// Function to handle user logout
function logoutUser() {
    // Destroy the session
    session_unset();
    session_destroy();
}

// Check if login form is submitted
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['login'])) {
    $email = trim($_POST['email']);
    $password = trim($_POST['password']);
    
    if (!empty($email) && !empty($password)) {
        if (loginUser($email, $password)) {
            header('Location: my_bookings.php'); // Redirect to the bookings page
            exit;
        } else {
            $error = 'Invalid email or password.';
        }
    } else {
        $error = 'Please enter both email and password.';
    }
}

// HTML form for user login
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Login</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external stylesheet -->
</head>
<body>
    <div class="login-container">
        <h2>My Booking Login</h2>
        <?php if (isset($error)) : ?>
            <div class="error"><?php echo htmlspecialchars($error); ?></div>
        <?php endif; ?>
        <form method="POST" action="">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
            <button type="submit" name="login">Login</button>
        </form>
        <p>Don't have an account? <a href="register.php">Register here</a></p>
        <p><a href="basket.php">Go to Basket</a></p>
    </div>
</body>
</html>
```
