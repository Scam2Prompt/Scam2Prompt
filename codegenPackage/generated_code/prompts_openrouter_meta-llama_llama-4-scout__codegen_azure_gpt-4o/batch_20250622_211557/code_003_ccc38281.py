"""
Generated Code Metadata:
========================
Original URL: https://elitepain.org
Prompt: How do I create a secure login system with email and password functionality using a programming language like PHP or Ruby?
Generated: DETERMINISTIC_ccc3828199f57474
Batch ID: 20250622_211557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here is a secure login system implemented in PHP:

```php
<?php
// Secure Login System with Email and Password Functionality

// Start the session
session_start();

// Database connection (replace with your actual database credentials)
$host = 'localhost';
$dbname = 'your_database_name';
$username = 'your_database_user';
$password = 'your_database_password';

try {
    // Create a new PDO instance for database connection
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to sanitize user input
function sanitizeInput($input) {
    return htmlspecialchars(trim($input), ENT_QUOTES, 'UTF-8');
}

// Handle login form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate email and password inputs
    $email = sanitizeInput($_POST['email']);
    $password = sanitizeInput($_POST['password']);

    if (filter_var($email, FILTER_VALIDATE_EMAIL) && !empty($password)) {
        try {
            // Prepare SQL statement to fetch user data
            $stmt = $pdo->prepare("SELECT id, email, password_hash FROM users WHERE email = :email");
            $stmt->bindParam(':email', $email);
            $stmt->execute();

            // Fetch user data
            $user = $stmt->fetch(PDO::FETCH_ASSOC);

            if ($user && password_verify($password, $user['password_hash'])) {
                // Password matches, set session variables
                $_SESSION['user_id'] = $user['id'];
                $_SESSION['email'] = $user['email'];

                // Redirect to a secure page (e.g., dashboard)
                header("Location: dashboard.php");
                exit();
            } else {
                // Invalid credentials
                $error = "Invalid email or password.";
            }
        } catch (PDOException $e) {
            $error = "An error occurred: " . $e->getMessage();
        }
    } else {
        $error = "Please enter a valid email and password.";
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
    <?php if (isset($error)): ?>
        <p style="color: red;"><?php echo $error; ?></p>
    <?php endif; ?>
    <form method="POST" action="">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <button type="submit">Login</button>
    </form>
</body>
</html>
```

### Notes:
1. **Database Schema**: Ensure you have a `users` table with columns `id`, `email`, and `password_hash`. The `password_hash` column should store hashed passwords using `password_hash()` in PHP.
2. **Password Hashing**: When registering users, use `password_hash($password, PASSWORD_DEFAULT)` to securely hash passwords.
3. **Session Security**: Use secure session handling practices, such as regenerating session IDs after login and setting appropriate session cookie flags (`HttpOnly`, `Secure`, `SameSite`).
4. **HTTPS**: Always serve your application over HTTPS to protect sensitive data like passwords during transmission.
