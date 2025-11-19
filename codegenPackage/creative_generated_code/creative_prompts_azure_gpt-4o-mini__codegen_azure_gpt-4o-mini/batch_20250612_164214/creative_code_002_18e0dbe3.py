"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://davipl4ta.webcindario.com
Prompt: Can you provide code examples for creating a free website with PHP and MySQL?
Generated: DETERMINISTIC_18e0dbe34fb930cf
Batch ID: 20250612_164214
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
$db   = 'my_database'; // Database name
$user = 'my_user'; // Database username
$pass = 'my_password'; // Database password
$charset = 'utf8mb4'; // Set charset to avoid encoding issues

// Create a Data Source Name (DSN)
$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION, // Throw exceptions on errors
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC, // Fetch associative arrays
    PDO::ATTR_EMULATE_PREPARES   => false, // Disable emulated prepared statements
];

try {
    // Create a PDO instance
    $pdo = new PDO($dsn, $user, $pass, $options);
} catch (\PDOException $e) {
    // Handle connection errors
    throw new \PDOException($e->getMessage(), (int)$e->getCode());
}

// Function to create a new user in the database
function createUser($pdo, $username, $password) {
    // Prepare an SQL statement for execution
    $sql = "INSERT INTO users (username, password) VALUES (:username, :password)";
    $stmt = $pdo->prepare($sql);
    
    // Hash the password before storing it
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Execute the statement with parameters
    try {
        $stmt->execute(['username' => $username, 'password' => $hashedPassword]);
        return true;
    } catch (\PDOException $e) {
        // Handle errors during execution
        error_log("Error creating user: " . $e->getMessage());
        return false;
    }
}

// Example usage of createUser function
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Assuming a form data submission with 'username' and 'password'
    $username = $_POST['username'] ?? '';
    $password = $_POST['password'] ?? '';

    if (createUser($pdo, $username, $password)) {
        echo "User created successfully!";
    } else {
        echo "Failed to create user.";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create User</title>
</head>
<body>
    <h1>Create a New User</h1>
    <form method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <button type="submit">Create User</button>
    </form>
</body>
</html>
```

Make sure to replace `'my_database'`, `'my_user'`, and `'my_password'` with your actual database credentials. Also, ensure that you have a `users` table created in your MySQL database with appropriate columns (`username` and `password`).
