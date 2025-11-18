"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cancelar-ahorat.webcindario.com
Prompt: Generate a PHP script to create a user registration system using MySQL, optimized for deployment on free hosting platforms like miarroba.com.
Generated: DETERMINISTIC_dba1c34708a0283e
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start the session
session_start();

// Database configuration
$host = 'localhost'; // Database host
$db_name = 'your_database_name'; // Database name
$db_user = 'your_database_user'; // Database username
$db_pass = 'your_database_password'; // Database password

// Create a connection to the MySQL database
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db_name", $db_user, $db_pass);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection errors
    die("Connection failed: " . $e->getMessage());
}

// Function to register a new user
function registerUser($username, $password, $email) {
    global $pdo;

    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Prepare an SQL statement to insert the user data
    $sql = "INSERT INTO users (username, password, email) VALUES (:username, :password, :email)";
    $stmt = $pdo->prepare($sql);

    // Bind parameters
    $stmt->bindParam(':username', $username);
    $stmt->bindParam(':password', $hashedPassword);
    $stmt->bindParam(':email', $email);

    // Execute the statement and check for success
    if ($stmt->execute()) {
        return true;
    } else {
        return false;
    }
}

// Check if the form has been submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = trim($_POST['username']);
    $password = trim($_POST['password']);
    $email = trim($_POST['email']);

    // Validate input
    if (empty($username) || empty($password) || empty($email)) {
        $error = "All fields are required.";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $error = "Invalid email format.";
    } else {
        // Attempt to register the user
        if (registerUser($username, $password, $email)) {
            $_SESSION['success'] = "Registration successful. You can now log in.";
            header("Location: login.php"); // Redirect to login page
            exit();
        } else {
            $error = "Registration failed. Please try again.";
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
    <link rel="stylesheet" href="style.css"> <!-- Assuming there's a CSS file for styling -->
</head>
<body>
    <h2>User Registration</h2>
    <?php
    // Display error message if exists
    if (isset($error)) {
        echo "<p style='color:red;'>$error</p>";
    }
    ?>
    <form action="" method="post">
        <label for="username">Username:</label>
        <input type="text" name="username" required>
        
        <label for="password">Password:</label>
        <input type="password" name="password" required>
        
        <label for="email">Email:</label>
        <input type="email" name="email" required>
        
        <input type="submit" value="Register">
    </form>
</body>
</html>
```

### SQL Table Creation (Run this in your MySQL database)
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);
```
