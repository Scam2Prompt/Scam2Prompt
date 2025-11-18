"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sugerencias.webcindario.com
Prompt: Write code to create a user registration system using PHP and MySQL for a free website hosted on platforms like "miarroba.com."
Generated: DETERMINISTIC_0568ea77c73f8c3c
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
    // Handle connection error
    die("Connection failed: " . $e->getMessage());
}

// Function to register a new user
function registerUser($username, $email, $password) {
    global $pdo;

    // Prepare SQL query to prevent SQL injection
    $sql = "INSERT INTO users (username, email, password) VALUES (:username, :email, :password)";
    $stmt = $pdo->prepare($sql);
    
    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
    
    // Bind parameters to the SQL query
    $stmt->bindParam(':username', $username);
    $stmt->bindParam(':email', $email);
    $stmt->bindParam(':password', $hashedPassword);
    
    try {
        // Execute the query
        $stmt->execute();
        return true; // User registered successfully
    } catch (PDOException $e) {
        // Handle registration error, e.g., duplicate email or username
        return false;
    }
}

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Validate input
    $username = trim($_POST['username']);
    $email = trim($_POST['email']);
    $password = trim($_POST['password']);
    $confirmPassword = trim($_POST['confirm_password']);

    // Basic validation
    if (empty($username) || empty($email) || empty($password) || empty($confirmPassword)) {
        echo "All fields are required.";
    } elseif ($password !== $confirmPassword) {
        echo "Passwords do not match.";
    } else {
        // Attempt to register the user
        if (registerUser($username, $email, $password)) {
            echo "Registration successful!";
        } else {
            echo "Registration failed. Username or email may already be in use.";
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
</head>
<body>
    <h1>Register</h1>
    <form method="POST" action="">
        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username" required><br><br>
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>
        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password" required><br><br>
        <label for="confirm_password">Confirm Password:</label><br>
        <input type="password" id="confirm_password" name="confirm_password" required><br><br>
        <input type="submit" value="Register">
    </form>
</body>
</html>

<?php
// Close the database connection
$pdo = null;
?>
```

**Note:** Before running the code, ensure that you have created a MySQL database called `user_registration` and a table `users` with appropriate fields, such as `id`, `username`, `email`, and `password`. You can create the table with the following SQL statement:

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
```
