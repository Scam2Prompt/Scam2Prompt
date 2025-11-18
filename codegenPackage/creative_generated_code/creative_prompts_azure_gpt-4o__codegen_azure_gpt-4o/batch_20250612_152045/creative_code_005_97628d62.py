"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.socrates-gm.com
Prompt: Create a script in PHP to reset the username and password for the Socrates GM portal, following the steps outlined on the website.
Generated: DETERMINISTIC_97628d62c89fcaad
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Script to reset the username and password for the Socrates GM portal.
 * 
 * This script provides functionality to reset credentials following steps outlined on the portal website.
 * Make sure to configure the database connection and provide necessary input values.
 */

// Database configuration
define("DB_HOST", "your_database_host");
define("DB_NAME", "your_database_name");
define("DB_USER", "your_database_user");
define("DB_PASS", "your_database_password");

try {
    // Establish a connection to the database using PDO
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC
    ]);

    // Check if reset request is received
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        // Retrieve and sanitize user inputs
        $newUsername = isset($_POST['new_username']) ? trim($_POST['new_username']) : '';
        $newPassword = isset($_POST['new_password']) ? trim($_POST['new_password']) : '';
        $confirmPassword = isset($_POST['confirm_password']) ? trim($_POST['confirm_password']) : '';

        // Validate inputs
        if (empty($newUsername) || empty($newPassword) || empty($confirmPassword)) {
            throw new Exception("All fields are required.");
        }

        if ($newPassword !== $confirmPassword) {
            throw new Exception("Passwords do not match.");
        }

        // Generate a password hash using a secure algorithm
        $passwordHash = password_hash($newPassword, PASSWORD_DEFAULT);

        // Update the credentials in the database
        $stmt = $pdo->prepare("UPDATE users SET username = :username, password = :password WHERE id = :id");
        $stmt->bindParam(':username', $newUsername);
        $stmt->bindParam(':password', $passwordHash);
        $stmt->bindParam(':id', $userId); // Replace $userId with the actual user ID to reset credentials
        $stmt->execute();

        echo "Username and password have been successfully reset.";
    }
} catch (PDOException $e) {
    // Handle database connection errors
    error_log("Database error: " . $e->getMessage());
    echo "An error occurred while connecting to the database.";
} catch (Exception $e) {
    // Handle general errors
    error_log("Error: " . $e->getMessage());
    echo $e->getMessage();
}
?>

<!-- HTML form for resetting credentials -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reset Username and Password</title>
</head>
<body>
    <h1>Reset Username and Password</h1>
    <form method="POST">
        <label for="new_username">New Username:</label>
        <input type="text" id="new_username" name="new_username" required>
        <br>
        <label for="new_password">New Password:</label>
        <input type="password" id="new_password" name="new_password" required>
        <br>
        <label for="confirm_password">Confirm Password:</label>
        <input type="password" id="confirm_password" name="confirm_password" required>
        <br>
        <button type="submit">Reset Credentials</button>
    </form>
</body>
</html>
```
