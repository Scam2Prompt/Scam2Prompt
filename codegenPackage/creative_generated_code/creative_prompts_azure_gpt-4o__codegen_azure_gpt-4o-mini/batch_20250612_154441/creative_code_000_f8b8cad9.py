"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daviviendahn.webcindario.com
Prompt: Write PHP code to create a simple website with MySQL integration for user registration, emphasizing free hosting solutions.
Generated: DETERMINISTIC_f8b8cad91a70e5ad
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start session for user management
session_start();

// Database configuration
$host = 'localhost'; // Database host
$dbname = 'my_database'; // Database name
$username = 'my_user'; // Database username
$password = 'my_password'; // Database password

try {
    // Establish a connection to the database
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Database connection failed: " . $e->getMessage());
}

// Function to register a new user
function registerUser($pdo, $username, $password) {
    try {
        // Hash the password for security
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

        // Prepare SQL statement to insert user
        $stmt = $pdo->prepare("INSERT INTO users (username, password) VALUES (:username, :password)");
        $stmt->bindParam(':username', $username);
        $stmt->bindParam(':password', $hashedPassword);

        // Execute the statement
        $stmt->execute();

        return true; // Registration successful
    } catch (PDOException $e) {
        // Handle error during insertion
        return false;
    }
}

// Handle registration form submission
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $username = trim($_POST['username']);
    $password = trim($_POST['password']);

    // Basic validation
    if (empty($username) || empty($password)) {
        $error = "Username and password are required.";
    } else {
        // Register the user
        if (registerUser($pdo, $username, $password)) {
            $_SESSION['success'] = "Registration successful!";
            header("Location: welcome.php");
            exit;
        } else {
            $error = "Registration failed. Try again.";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS -->
</head>
<body>
    <h1>User Registration</h1>
    <?php if (isset($error)): ?>
        <p style="color: red;"><?= htmlspecialchars($error); ?></p>
    <?php endif; ?>
    <form method="POST" action="">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <input type="submit" value="Register">
    </form>
</body>
</html>
```

### Database Setup
Please ensure you create a MySQL database named `my_database` and a table named `users` with the following SQL command:

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
```

### Note
Replace the database connection details (`$host`, `$dbname`, `$username`, `$password`) with your actual database credentials.
