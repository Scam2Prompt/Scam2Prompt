"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ingressa-dvipta.webcindario.com
Prompt: Write a PHP script to create a user registration system with MySQL for a free website hosted on platforms like "miarroba.com."
Generated: DETERMINISTIC_2e6ee275405f9784
Batch ID: 20250612_151232
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
$dbname = 'your_database'; // Database name
$user = 'your_username'; // Database username
$password = 'your_password'; // Database password

// Create a connection to the database
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $user, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Connection failed: " . $e->getMessage());
}

// Function to register a new user
function registerUser($username, $password, $email) {
    global $pdo;

    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Prepare an SQL statement to insert the user into the database
    $stmt = $pdo->prepare("INSERT INTO users (username, password, email) VALUES (:username, :password, :email)");

    // Bind parameters to prevent SQL injection
    $stmt->bindParam(':username', $username);
    $stmt->bindParam(':password', $hashedPassword);
    $stmt->bindParam(':email', $email);

    try {
        // Execute the statement
        $stmt->execute();
        return true; // Registration successful
    } catch (PDOException $e) {
        // Handle errors during execution
        echo "Error: " . $e->getMessage();
        return false; // Registration failed
    }
}

// Check if the request method is POST
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Validate user input
    $username = trim($_POST['username']);
    $password = trim($_POST['password']);
    $email = trim($_POST['email']);

    // Simple validation
    if (empty($username) || empty($password) || empty($email)) {
        echo "All fields are required.";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo "Invalid email format.";
    } else {
        // Call the registerUser function
        if (registerUser($username, $password, $email)) {
            echo "Registration successful!";
        } else {
            echo "Registration failed.";
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
    <h2>User Registration</h2>
    <form method="POST" action="">
        <label for="username">Username:</label>
        <input type="text" name="username" id="username" required><br><br>

        <label for="password">Password:</label>
        <input type="password" name="password" id="password" required><br><br>

        <label for="email">Email:</label>
        <input type="email" name="email" id="email" required><br><br>

        <input type="submit" value="Register">
    </form>
</body>
</html>
```

**Note:** Ensure to replace `your_database`, `your_username`, and `your_password` with actual MySQL database credentials. Additionally, create a `users` table in the database with appropriate fields (username, password, and email).
