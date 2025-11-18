"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cliens143.webcindario.com
Prompt: Write code to create a user registration system in PHP and MySQL for a free website hosted on a service with custom domain options.
Generated: DETERMINISTIC_d373beb9a5e841e9
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// db.php - Database connection file
$host = 'localhost'; // Database host
$db = 'registration_db'; // Database name
$user = 'root'; // Database username
$pass = ''; // Database password

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection errors
    die("Connection failed: " . $e->getMessage());
}
?>

<?php
// register.php - User registration script
require 'db.php'; // Include database connection

// Function to validate user input
function validateInput($data) {
    return htmlspecialchars(stripslashes(trim($data)));
}

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Capture and validate user input
    $username = validateInput($_POST['username']);
    $password = validateInput($_POST['password']);
    $email = validateInput($_POST['email']);

    // Check if fields are empty
    if (empty($username) || empty($password) || empty($email)) {
        echo "All fields are required.";
        exit;
    }

    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Prepare SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("INSERT INTO users (username, password, email) VALUES (:username, :password, :email)");

    // Bind parameters
    $stmt->bindParam(':username', $username);
    $stmt->bindParam(':password', $hashedPassword);
    $stmt->bindParam(':email', $email);

    try {
        // Execute the statement
        $stmt->execute();
        echo "Registration successful!";
    } catch (PDOException $e) {
        // Handle SQL errors
        echo "Error: " . $e->getMessage();
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration</title>
</head>
<body>
    <h1>Register</h1>
    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br><br>
        
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br><br>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>
        
        <input type="submit" value="Register">
    </form>
</body>
</html>
```

```sql
-- SQL script to create the database and users table
CREATE DATABASE IF NOT EXISTS registration_db;

USE registration_db;

CREATE TABLE IF NOT EXISTS users (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Make sure to create the database and the `users` table using the provided SQL script before running the registration script.
