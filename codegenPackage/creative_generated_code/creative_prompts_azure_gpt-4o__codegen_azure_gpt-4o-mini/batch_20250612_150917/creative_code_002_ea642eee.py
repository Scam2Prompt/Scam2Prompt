"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daviplatanotific.webcindario.com
Prompt: Generate a PHP script to create a user registration form and store the data in a MySQL database for a website hosted on miarroba.com.
Generated: DETERMINISTIC_ea642eeeb574fc85
Batch ID: 20250612_150917
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
$dbname = 'your_database_name'; // Database name
$username = 'your_database_username'; // Database username
$password = 'your_database_password'; // Database password

// Create MySQL database connection
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection errors
    echo "Connection failed: " . $e->getMessage();
    exit;
}

// Function to handle user registration
function registerUser($name, $email, $password) {
    global $pdo;

    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Prepare SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("INSERT INTO users (name, email, password) VALUES (:name, :email, :password)");

    // Bind parameters
    $stmt->bindParam(':name', $name);
    $stmt->bindParam(':email', $email);
    $stmt->bindParam(':password', $hashedPassword);

    try {
        // Execute the statement
        $stmt->execute();
        return true; // Registration successful
    } catch (PDOException $e) {
        // Handle registration errors
        echo "Error: " . $e->getMessage();
        return false; // Registration failed
    }
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate form data
    $name = trim($_POST['name']);
    $email = trim($_POST['email']);
    $password = trim($_POST['password']);

    if (!empty($name) && filter_var($email, FILTER_VALIDATE_EMAIL) && !empty($password)) {
        // Register user
        if (registerUser($name, $email, $password)) {
            echo "User registered successfully!";
        } else {
            echo "User registration failed.";
        }
    } else {
        echo "Please fill in all fields correctly.";
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
    <h2>User Registration Form</h2>
    <form action="" method="POST">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>
        
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>
        
        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password" required><br><br>
        
        <input type="submit" value="Register">
    </form>
</body>
</html>
```

### Note:
- Replace `your_database_name`, `your_database_username`, and `your_database_password` with your actual database credentials.
- Ensure that a `users` table exists in your database with the appropriate columns: `name`, `email`, `password`.
