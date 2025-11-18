"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lover4d.site
Prompt: Develop a PHP script to manage user registration and login for an online gambling platform, including fields for bank selection and deposit amounts, similar to the 4DLOVER registration process.
Generated: DETERMINISTIC_97a4d54f714ff470
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the clean, production-ready PHP script for managing user registration and login on an online gambling platform:

```php
<?php
// Start PHP session to handle user authentication
session_start();

// Database connection configuration
$host = 'localhost';    // Database host
$dbname = 'gambling_db'; // Database name
$username = 'root';      // Database username
$password = '';          // Database password

try {
    // PDO Connection to the database
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8mb4", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle database connection errors
    die("Database connection failed: " . $e->getMessage());
}

// Function to register a new user
function registerUser($pdo, $username, $password, $bank, $deposit) {
    // Check if the username is already taken
    $stmt = $pdo->prepare("SELECT COUNT(*) FROM users WHERE username = :username");
    $stmt->execute(['username' => $username]);
    if ($stmt->fetchColumn() > 0) {
        return "Username is already taken.";
    }

    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_BCRYPT);

    // Insert the new user into the database
    $stmt = $pdo->prepare("INSERT INTO users (username, password, bank, deposit) VALUES (:username, :password, :bank, :deposit)");
    try {
        $stmt->execute([
            'username' => $username,
            'password' => $hashedPassword,
            'bank' => $bank,
            'deposit' => $deposit
        ]);
        return "Registration successful!";
    } catch (PDOException $e) {
        return "Registration failed: " . $e->getMessage();
    }
}

// Function to log in a user
function loginUser($pdo, $username, $password) {
    // Fetch the user details from the database
    $stmt = $pdo->prepare("SELECT * FROM users WHERE username = :username");
    $stmt->execute(['username' => $username]);
    $user = $stmt->fetch(PDO::FETCH_ASSOC);

    if ($user && password_verify($password, $user['password'])) {
        // Store user session data
        $_SESSION['user_id'] = $user['id'];
        $_SESSION['username'] = $user['username'];
        return "Login successful!";
    }
    return "Invalid username or password.";
}

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['action'])) {
        $action = $_POST['action'];
        $response = '';

        if ($action === 'register') {
            // Handle user registration
            $username = trim($_POST['username']);
            $password = trim($_POST['password']);
            $bank = trim($_POST['bank']);
            $deposit = floatval($_POST['deposit']);
            $response = registerUser($pdo, $username, $password, $bank, $deposit);
        } elseif ($action === 'login') {
            // Handle user login
            $username = trim($_POST['username']);
            $password = trim($_POST['password']);
            $response = loginUser($pdo, $username, $password);
        }

        echo $response; // Return the response to the user
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registration and Login</title>
</head>
<body>
    <h1>User Registration</h1>
    <form method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <label for="bank">Bank:</label>
        <input type="text" id="bank" name="bank" required>
        <br>
        <label for="deposit">Deposit Amount:</label>
        <input type="number" id="deposit" name="deposit" step="0.01" required>
        <br>
        <input type="hidden" name="action" value="register">
        <button type="submit">Register</button>
    </form>

    <h1>User Login</h1>
    <form method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <input type="hidden" name="action" value="login">
        <button type="submit">Login</button>
    </form>
</body>
</html>
```

### Notes:
- Ensure that you create a database named `gambling_db` with a table `users` with columns `id`, `username`, `password`, `bank`, and `deposit`.
- Use HTTPS in production to secure the communication.
- Consider rate-limiting and CAPTCHA to prevent abuse of registration and login forms.
- This code is designed for demonstration; further security and compliance steps may be needed for a production gambling platform.
