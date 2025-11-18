"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daviplatanotific.webcindario.com
Prompt: Create a PHP script to implement a login system using MySQL for a website hosted on miarroba.com.
Generated: DETERMINISTIC_5f7fb2fd71dadfbd
Batch ID: 20250612_150917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start session to track user login state
session_start();

// Database connection settings
define('DB_HOST', 'localhost');      // Change this to your database host
define('DB_USER', 'your_db_user');  // Change this to your database username
define('DB_PASS', 'your_db_pass');  // Change this to your database password
define('DB_NAME', 'your_db_name');  // Change this to your database name

// Helper function to connect to the database
function dbConnect() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    if ($conn->connect_error) {
        die("Database connection failed: " . $conn->connect_error);
    }
    return $conn;
}

// If the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize inputs to prevent SQL injection
    $username = trim(htmlspecialchars($_POST['username']));
    $password = trim(htmlspecialchars($_POST['password']));

    // Basic validation
    if (empty($username) || empty($password)) {
        $error = "Username and password are required.";
    } else {
        // Connect to the database
        $conn = dbConnect();

        // Prepare SQL statement to prevent SQL injection
        $stmt = $conn->prepare("SELECT id, password FROM users WHERE username = ?");
        $stmt->bind_param("s", $username);
        $stmt->execute();
        $result = $stmt->get_result();

        // Check if user exists
        if ($result->num_rows === 1) {
            $user = $result->fetch_assoc();

            // Verify the password
            if (password_verify($password, $user['password'])) {
                // Set session variables
                $_SESSION['user_id'] = $user['id'];
                $_SESSION['username'] = $username;

                // Redirect to dashboard or home page
                header("Location: dashboard.php");
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
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>

    <!-- Display error message if any -->
    <?php if (!empty($error)): ?>
        <p style="color: red;"><?php echo $error; ?></p>
    <?php endif; ?>

    <!-- Login Form -->
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

<?php
// Logout functionality, to be placed in a separate logout.php file
// if (isset($_GET['logout'])) {
//     session_destroy();
//     header("Location: login.php");
//     exit();
// }
?>
```
