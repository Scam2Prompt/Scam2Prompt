"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pers-daviplata.webcindario.com
Prompt: How can I create a free website using PHP and MySQL as mentioned on the pers-daviplata webpage?
Generated: DETERMINISTIC_f0a7f68b5bc4f1d6
Batch ID: 20250612_164213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is an example of a simple PHP application that uses MySQL to create a basic website. This example includes user registration and login functionalities, which could be part of a larger application like the one mentioned.

```php
<?php
// Database configuration
$host = 'localhost'; // Database host
$db_name = 'my_database'; // Database name
$username = 'root'; // Database username
$password = ''; // Database password

// Create a connection to the MySQL database
$conn = new mysqli($host, $username, $password, $db_name);

// Check for connection errors
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Function to register a new user
function registerUser($conn, $email, $password) {
    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_BCRYPT);
    
    // Prepare SQL statement to prevent SQL injection
    $stmt = $conn->prepare("INSERT INTO users (email, password) VALUES (?, ?)");
    $stmt->bind_param("ss", $email, $hashedPassword);
    
    // Execute the statement and check for errors
    if ($stmt->execute()) {
        return true; // User registered successfully
    } else {
        return false; // Registration failed
    }
}

// Function to login a user
function loginUser($conn, $email, $password) {
    // Prepare SQL statement to retrieve user data
    $stmt = $conn->prepare("SELECT password FROM users WHERE email = ?");
    $stmt->bind_param("s", $email);
    
    // Execute the statement
    $stmt->execute();
    $stmt->store_result();
    
    // Check if user exists
    if ($stmt->num_rows === 1) {
        // Bind the result to a variable
        $stmt->bind_result($hashedPassword);
        $stmt->fetch();
        
        // Verify the password
        if (password_verify($password, $hashedPassword)) {
            return true; // Login successful
        }
    }
    
    return false; // Login failed
}

// Handling registration request
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['register'])) {
    $email = $_POST['email'];
    $password = $_POST['password'];

    if (registerUser($conn, $email, $password)) {
        echo "Registration successful!";
    } else {
        echo "Registration failed. Email might already be in use.";
    }
}

// Handling login request
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['login'])) {
    $email = $_POST['email'];
    $password = $_POST['password'];

    if (loginUser($conn, $email, $password)) {
        echo "Login successful!";
    } else {
        echo "Login failed. Invalid email or password.";
    }
}

// Close the database connection
$conn->close();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple PHP Website</title>
</head>
<body>

<h2>Register</h2>
<form method="POST">
    <input type="email" name="email" required placeholder="Email">
    <input type="password" name="password" required placeholder="Password">
    <button type="submit" name="register">Register</button>
</form>

<h2>Login</h2>
<form method="POST">
    <input type="email" name="email" required placeholder="Email">
    <input type="password" name="password" required placeholder="Password">
    <button type="submit" name="login">Login</button>
</form>

</body>
</html>
```

**Database Setup (SQL)**:
Before using the code, you need to set up the MySQL database. Use the following SQL commands to create the required table:

```sql
CREATE DATABASE my_database;

USE my_database;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
```

Make sure to adjust the database credentials as needed and that your server has PHP and MySQL set up correctly to run this code.
