"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://largeoptions.org
Prompt: Create a PHP code snippet that allows users to sign up for an account on largeoptions.org and handle the affiliate program registration process.
Generated: DETERMINISTIC_a4ef29965f04b8e9
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'largeoptions');
define('DB_USER', 'root');
define('DB_PASS', 'password');

try {
    // Establish a connection to the database
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    ]);
} catch (PDOException $e) {
    // Handle database connection errors
    die("Database connection failed: " . $e->getMessage());
}

// Function to validate user input
function sanitizeInput($data) {
    return htmlspecialchars(trim($data));
}

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Retrieve and sanitize user input
    $username = sanitizeInput($_POST['username'] ?? '');
    $email = sanitizeInput($_POST['email'] ?? '');
    $password = sanitizeInput($_POST['password'] ?? '');
    $affiliateCode = sanitizeInput($_POST['affiliate_code'] ?? '');

    // Validate required fields
    if (empty($username) || empty($email) || empty($password)) {
        die("Please fill out all required fields.");
    }

    // Validate email format
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die("Invalid email format.");
    }

    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    try {
        // Start a transaction
        $pdo->beginTransaction();

        // Insert user into the `users` table
        $userStmt = $pdo->prepare("INSERT INTO users (username, email, password) VALUES (:username, :email, :password)");
        $userStmt->execute([
            ':username' => $username,
            ':email' => $email,
            ':password' => $hashedPassword,
        ]);

        // Get the user ID of the newly created user
        $userId = $pdo->lastInsertId();

        // Handle affiliate registration if an affiliate code is provided
        if (!empty($affiliateCode)) {
            $affiliateStmt = $pdo->prepare("INSERT INTO affiliates (user_id, affiliate_code) VALUES (:user_id, :affiliate_code)");
            $affiliateStmt->execute([
                ':user_id' => $userId,
                ':affiliate_code' => $affiliateCode,
            ]);
        }

        // Commit the transaction
        $pdo->commit();

        // Success message
        echo "Account successfully created.";
    } catch (Exception $e) {
        // Rollback the transaction on error
        $pdo->rollBack();
        die("Error creating account: " . $e->getMessage());
    }
}
?>

<!-- HTML Form for User Registration -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign Up - largeoptions.org</title>
</head>
<body>
    <h1>Sign Up</h1>
    <form method="POST" action="">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>

        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br><br>

        <label for="affiliate_code">Affiliate Code (optional):</label>
        <input type="text" id="affiliate_code" name="affiliate_code"><br><br>

        <button type="submit">Sign Up</button>
    </form>
</body>
</html>
```
