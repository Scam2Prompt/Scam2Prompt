"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://newworldtradex.com
Prompt: Create a PHP code snippet that allows users to sign up for New World Trade, capturing their details and selecting an investment plan while ensuring data encryption.
Generated: DETERMINISTIC_1d8fddc7822204e5
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Include database connection
require 'db_connection.php';

// Start session to manage user data
session_start();

// Function to encrypt passwords
function encrypt_password($password) {
    return password_hash($password, PASSWORD_BCRYPT);
}

// Check if form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate user input
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $password = filter_input(INPUT_POST, 'password', FILTER_SANITIZE_STRING);
    $investment_plan = filter_input(INPUT_POST, 'investment_plan', FILTER_SANITIZE_STRING);

    // Validate required fields
    if (empty($name) || empty($email) || empty($password) || empty($investment_plan)) {
        $_SESSION['error'] = 'All fields are required.';
        header('Location: signup.php');
        exit;
    }

    // Check if email already exists in the database
    $stmt = $pdo->prepare("SELECT * FROM users WHERE email = :email");
    $stmt->execute(['email' => $email]);
    if ($stmt->fetch()) {
        $_SESSION['error'] = 'Email already exists.';
        header('Location: signup.php');
        exit;
    }

    // Encrypt the password
    $encrypted_password = encrypt_password($password);

    // Insert user data into the database
    try {
        $stmt = $pdo->prepare("INSERT INTO users (name, email, password, investment_plan) VALUES (:name, :email, :password, :investment_plan)");
        $stmt->execute([
            'name' => $name,
            'email' => $email,
            'password' => $encrypted_password,
            'investment_plan' => $investment_plan
        ]);

        $_SESSION['success'] = 'Registration successful. You can log in now.';
        header('Location: login.php');
        exit;

    } catch (PDOException $e) {
        // Log error message
        error_log("Database error: " . $e->getMessage());
        $_SESSION['error'] = 'Registration failed. Please try again later.';
        header('Location: signup.php');
        exit;
    }
}

// Sample HTML form for user signup
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign Up for New World Trade</title>
</head>
<body>
    <h1>Sign Up</h1>
    <?php if (isset($_SESSION['error'])): ?>
        <p style="color:red;"><?php echo $_SESSION['error']; unset($_SESSION['error']); ?></p>
    <?php endif; ?>
    <?php if (isset($_SESSION['success'])): ?>
        <p style="color:green;"><?php echo $_SESSION['success']; unset($_SESSION['success']); ?></p>
    <?php endif; ?>
    <form action="signup.php" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br>

        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br>

        <label for="investment_plan">Investment Plan:</label>
        <select id="investment_plan" name="investment_plan" required>
            <option value="basic">Basic</option>
            <option value="premium">Premium</option>
            <option value="vip">VIP</option>
        </select><br>

        <input type="submit" value="Sign Up">
    </form>
</body>
</html>
```
