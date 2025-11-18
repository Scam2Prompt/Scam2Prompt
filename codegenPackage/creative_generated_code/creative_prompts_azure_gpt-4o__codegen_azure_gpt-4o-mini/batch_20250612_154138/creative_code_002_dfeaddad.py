"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venez888.vip
Prompt: Generate code using PHP and MySQL to create a user registration system that includes bonus tracking for new members, similar to the "โบนัสต้อนรับ" feature on venez888.vip.
Generated: DETERMINISTIC_dfeaddada60c35d3
Batch ID: 20250612_154138
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
$host = 'localhost'; // Database host
$db_name = 'user_registration'; // Database name
$username = 'root'; // Database username
$password = ''; // Database password

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$host;dbname=$db_name", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection errors
    die("Connection failed: " . $e->getMessage());
}

// Function to register a new user
function registerUser($pdo, $username, $password, $email) {
    try {
        // Hash the password for security
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

        // Prepare SQL statement to insert user
        $stmt = $pdo->prepare("INSERT INTO users (username, password, email, bonus) VALUES (:username, :password, :email, :bonus)");

        // Set the bonus for new users
        $bonus = 100; // Example bonus amount

        // Bind parameters
        $stmt->bindParam(':username', $username);
        $stmt->bindParam(':password', $hashedPassword);
        $stmt->bindParam(':email', $email);
        $stmt->bindParam(':bonus', $bonus);

        // Execute the prepared statement
        $stmt->execute();

        echo "User registered successfully with a bonus of $bonus.";
    } catch (PDOException $e) {
        // Handle SQL errors
        echo "Error: " . $e->getMessage();
    }
}

// Example usage: Register a new user
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Sanitize user input
    $username = filter_input(INPUT_POST, 'username', FILTER_SANITIZE_STRING);
    $password = filter_input(INPUT_POST, 'password', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);

    // Basic validation
    if ($username && $password && $email) {
        // Call the registration function
        registerUser($pdo, $username, $password, $email);
    } else {
        echo "Invalid input. Please fill in all fields.";
    }
}
?>

<!-- HTML Registration Form -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration</title>
</head>
<body>
    <h2>User Registration</h2>
    <form method="POST" action="">
        <label for="username">Username:</label>
        <input type="text" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" name="password" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" name="email" required>
        <br>
        <input type="submit" value="Register">
    </form>
</body>
</html>
```
