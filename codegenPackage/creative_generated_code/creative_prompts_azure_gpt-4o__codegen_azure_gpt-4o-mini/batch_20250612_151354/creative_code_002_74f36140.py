"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casodavhn212.webcindario.com
Prompt: Generate a PHP script for user registration and login functionality, optimized for free hosting services with MySQL support.
Generated: DETERMINISTIC_74f36140d1ef3d86
Batch ID: 20250612_151354
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
$host = 'localhost';  // Database host
$dbname = 'your_database'; // Replace with your database name
$user = 'your_username'; // Replace with your database username
$pass = 'your_password'; // Replace with your database password

// Establish a connection to the database using PDO
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // Set error mode to exception
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to register a new user
function registerUser($username, $password) {
    global $pdo;

    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Prepare SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("INSERT INTO users (username, password) VALUES (:username, :password)");
    $stmt->bindParam(':username', $username);
    $stmt->bindParam(':password', $hashedPassword);

    // Execute the statement and handle any errors
    try {
        $stmt->execute();
        echo "User registered successfully!";
    } catch (PDOException $e) {
        echo "Error: " . $e->getMessage();
    }
}

// Function to login a user
function loginUser($username, $password) {
    global $pdo;

    // Prepare SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("SELECT password FROM users WHERE username = :username");
    $stmt->bindParam(':username', $username);
    $stmt->execute();

    // Check if the user exists
    if ($stmt->rowCount() === 1) {
        $row = $stmt->fetch(PDO::FETCH_ASSOC);
        $hashedPassword = $row['password'];

        // Verify the entered password against the hashed password
        if (password_verify($password, $hashedPassword)) {
            echo "Login successful!";
            // Start a session for the user or perform additional login actions
        } else {
            echo "Invalid username or password.";
        }
    } else {
        echo "Invalid username or password.";
    }
}

// Example usage (uncomment to test registration and login functions)
// registerUser('testuser', 'testpassword'); // Register a new user
// loginUser('testuser', 'testpassword'); // Log in with the registered user

?>
```
**Note**: Ensure you have a table named `users` in your MySQL database with at least two columns: `username` (VARCHAR) and `password` (VARCHAR). The script does not include form handling for user input; that should be implemented to sanitize and validate user input in a production environment.
