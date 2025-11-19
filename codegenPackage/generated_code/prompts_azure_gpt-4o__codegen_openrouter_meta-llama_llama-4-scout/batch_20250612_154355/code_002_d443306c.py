"""
Generated Code Metadata:
========================
Original URL: https://davivienprotec.webcindario.com
Prompt: Generate a PHP script to create a user registration form and store the data in a MySQL database, optimized for free hosting environments.
Generated: DETERMINISTIC_d443306c37fcddbd
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * User Registration Form and MySQL Database Storage
 * 
 * This script creates a user registration form, validates user input, 
 * and stores the data in a MySQL database. It is optimized for free hosting environments.
 */

// Configuration
$db_host = 'localhost';
$db_username = 'your_username';
$db_password = 'your_password';
$db_name = 'your_database';

// Create connection
$conn = new mysqli($db_host, $db_username, $db_password, $db_name);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Function to validate and sanitize user input
function validate_input($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}

// Function to register user
function register_user($conn, $username, $email, $password) {
    // Validate and sanitize user input
    $username = validate_input($username);
    $email = validate_input($email);
    $password = validate_input($password);

    // Hash password
    $hashed_password = password_hash($password, PASSWORD_DEFAULT);

    // Check if user already exists
    $query = "SELECT * FROM users WHERE username='$username' OR email='$email'";
    $result = $conn->query($query);

    if ($result->num_rows > 0) {
        return false; // User already exists
    }

    // Insert user data into database
    $query = "INSERT INTO users (username, email, password) VALUES ('$username', '$email', '$hashed_password')";
    if ($conn->query($query) === TRUE) {
        return true; // User registered successfully
    } else {
        return false; // Error registering user
    }
}

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $email = $_POST["email"];
    $password = $_POST["password"];

    // Register user
    if (register_user($conn, $username, $email, $password)) {
        echo "User registered successfully!";
    } else {
        echo "Error registering user. Please try again.";
    }
}

// Close connection
$conn->close();
?>

<!-- User Registration Form -->
<form action="<?php echo $_SERVER["PHP_SELF"]; ?>" method="post">
    <label for="username">Username:</label><br>
    <input type="text" id="username" name="username"><br>
    <label for="email">Email:</label><br>
    <input type="email" id="email" name="email"><br>
    <label for="password">Password:</label><br>
    <input type="password" id="password" name="password"><br>
    <input type="submit" value="Register">
</form>
```

```sql
-- Create users table
CREATE TABLE users (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(30) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL
);
```
