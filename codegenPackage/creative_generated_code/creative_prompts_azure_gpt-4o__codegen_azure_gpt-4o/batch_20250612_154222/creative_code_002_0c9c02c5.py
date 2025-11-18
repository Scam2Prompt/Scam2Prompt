"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soportedaviplata.webcindario.com
Prompt: Generate a PHP script to create a basic user registration form and store user data in a MySQL database for a free website project.
Generated: DETERMINISTIC_0c9c02c5b53e585f
Batch ID: 20250612_154222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Enable error reporting for debugging purposes (disable in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Database configuration
$servername = "localhost"; // Change to your database server
$username = "root";        // Change to your MySQL username
$password = "";            // Change to your MySQL password
$dbname = "user_registration"; // Change to your database name

// Function to create a database connection
function getDatabaseConnection($servername, $username, $password, $dbname) {
    try {
        $conn = new mysqli($servername, $username, $password, $dbname);

        // Check connection
        if ($conn->connect_error) {
            throw new Exception("Connection failed: " . $conn->connect_error);
        }
        
        return $conn;
    } catch (Exception $e) {
        die("Database connection error: " . $e->getMessage());
    }
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize user inputs to prevent SQL injection and XSS attacks
    $name = htmlspecialchars(trim($_POST['name']));
    $email = htmlspecialchars(trim($_POST['email']));
    $password = htmlspecialchars(trim($_POST['password']));

    // Basic validation checks
    if (empty($name) || empty($email) || empty($password)) {
        echo "All fields are required!";
        exit;
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo "Invalid email format!";
        exit;
    }

    // Hash the password before storing it
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Create a database connection
    $conn = getDatabaseConnection($servername, $username, $password, $dbname);

    // Prepare SQL query to insert user data
    $stmt = $conn->prepare("INSERT INTO users (name, email, password) VALUES (?, ?, ?)");
    if ($stmt === false) {
        die("Database query preparation error: " . $conn->error);
    }

    // Bind parameters and execute the query
    $stmt->bind_param("sss", $name, $email, $hashedPassword);

    if ($stmt->execute()) {
        echo "Registration successful!";
    } else {
        echo "Failed to register: " . $stmt->error;
    }

    // Close statement and connection
    $stmt->close();
    $conn->close();
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
    <h1>User Registration</h1>
    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>
        
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br><br>
        
        <button type="submit">Register</button>
    </form>
</body>
</html>
```

**Note:** Make sure to create a MySQL database named `user_registration` and a table `users` with the following schema before using the script:

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
