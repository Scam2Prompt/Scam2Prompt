"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbasepromo.webcindario.com
Prompt: How can I create a free website using PHP and MySQL as described on the Coinbase promo site?
Generated: DETERMINISTIC_f3bae5f2fecaa569
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/*
 * Simple example of a PHP website using MySQL.
 * This code demonstrates user registration and login functionality for a basic website.
 * Ensure you have a MySQL database set up and credentials ready before running this code.
 */
 
// Config file for database connection
define('DB_HOST', 'localhost'); // Change to your database host
define('DB_USER', 'root');      // Change to your database username
define('DB_PASS', '');          // Change to your database password
define('DB_NAME', 'website_db'); // Change to your database name

// Establish database connection
$conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Create users table if it does not exist
$sql = "CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)";
if (!$conn->query($sql)) {
    die("Error creating table: " . $conn->error);
}

// Helper function for safely handling user input
function sanitize_input($data) {
    return htmlspecialchars(trim($data));
}

// Handle user registration
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['register'])) {
    $username = sanitize_input($_POST['username']);
    $password = sanitize_input($_POST['password']);

    // Check if fields are empty
    if (empty($username) || empty($password)) {
        $error = "All fields are required.";
    } else {
        // Hash password for security
        $hashed_password = password_hash($password, PASSWORD_DEFAULT);

        // Insert user into database
        $stmt = $conn->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
        $stmt->bind_param("ss", $username, $hashed_password);

        if ($stmt->execute()) {
            $success = "Registration successful. You can now log in.";
        } else {
            $error = "Error: " . $stmt->error;
        }
        $stmt->close();
    }
}

// Handle user login
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['login'])) {
    $username = sanitize_input($_POST['username']);
    $password = sanitize_input($_POST['password']);

    // Check if fields are empty
    if (empty($username) || empty($password)) {
        $error = "All fields are required.";
    } else {
        // Retrieve user from database
        $stmt = $conn->prepare("SELECT password FROM users WHERE username = ?");
        $stmt->bind_param("s", $username);
        $stmt->execute();
        $stmt->store_result();

        if ($stmt->num_rows > 0) {
            $stmt->bind_result($hashed_password);
            $stmt->fetch();

            // Verify password
            if (password_verify($password, $hashed_password)) {
                $success = "Login successful!";
            } else {
                $error = "Invalid username or password.";
            }
        } else {
            $error = "Invalid username or password.";
        }
        $stmt->close();
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple PHP Website</title>
</head>
<body>
    <h1>Welcome to Our Website</h1>

    <!-- Display error or success messages -->
    <?php if (isset($error)): ?>
        <p style="color: red;"><?php echo $error; ?></p>
    <?php endif; ?>
    <?php if (isset($success)): ?>
        <p style="color: green;"><?php echo $success; ?></p>
    <?php endif; ?>

    <!-- Registration Form -->
    <h2>Register</h2>
    <form method="POST" action="">
        <label for="username">Username:</label>
        <input type="text" name="username" id="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" name="password" id="password" required>
        <br>
        <button type="submit" name="register">Register</button>
    </form>

    <!-- Login Form -->
    <h2>Login</h2>
    <form method="POST" action="">
        <label for="username">Username:</label>
        <input type="text" name="username" id="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" name="password" id="password" required>
        <br>
        <button type="submit" name="login">Login</button>
    </form>
</body>
</html>

<?php
// Close database connection
$conn->close();
?>
```
