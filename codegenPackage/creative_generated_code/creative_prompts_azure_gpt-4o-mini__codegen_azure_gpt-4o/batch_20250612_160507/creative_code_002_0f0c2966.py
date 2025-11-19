"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tenarisfunds.com
Prompt: Create a sample code snippet in PHP that allows users to sign up for an account on the Tenaris Funds platform and securely store their information.
Generated: DETERMINISTIC_0f0c296670ef21cc
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Enable strict mode for safer coding
declare(strict_types=1);

// Database configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'tenaris_funds');
define('DB_USER', 'root');
define('DB_PASSWORD', '');

// Function to establish a connection to the database
function getDatabaseConnection(): PDO {
    try {
        $dsn = 'mysql:host=' . DB_HOST . ';dbname=' . DB_NAME . ';charset=utf8mb4';
        $options = [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            PDO::ATTR_EMULATE_PREPARES => false,
        ];
        return new PDO($dsn, DB_USER, DB_PASSWORD, $options);
    } catch (PDOException $e) {
        die('Database connection failed: ' . $e->getMessage());
    }
}

// Helper function to hash passwords securely
function hashPassword(string $password): string {
    return password_hash($password, PASSWORD_BCRYPT);
}

// Validate input data
function validateInput(string $name, string $email, string $password): array {
    $errors = [];
    if (empty($name) || strlen($name) > 100) {
        $errors[] = 'Name must not be empty and should be less than 100 characters.';
    }
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = 'Invalid email format.';
    }
    if (strlen($password) < 8) {
        $errors[] = 'Password must be at least 8 characters long.';
    }
    return $errors;
}

// Function to handle user registration
function registerUser(string $name, string $email, string $password): void {
    // Validate user input
    $errors = validateInput($name, $email, $password);
    if (!empty($errors)) {
        foreach ($errors as $error) {
            echo $error . '<br>';
        }
        return;
    }

    // Hash the password securely
    $hashedPassword = hashPassword($password);

    // Save user data to the database
    try {
        $pdo = getDatabaseConnection();
        $stmt = $pdo->prepare('INSERT INTO users (name, email, password) VALUES (:name, :email, :password)');
        $stmt->execute([
            ':name' => htmlspecialchars($name),
            ':email' => htmlspecialchars($email),
            ':password' => $hashedPassword,
        ]);
        echo 'Registration successful!';
    } catch (PDOException $e) {
        echo 'Error during registration: ' . $e->getMessage();
    }
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = $_POST['name'] ?? '';
    $email = $_POST['email'] ?? '';
    $password = $_POST['password'] ?? '';
    registerUser($name, $email, $password);
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign Up - Tenaris Funds</title>
</head>
<body>
    <h1>Sign Up</h1>
    <form action="" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>
        
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required minlength="8"><br><br>
        
        <button type="submit">Register</button>
    </form>
</body>
</html>
```
