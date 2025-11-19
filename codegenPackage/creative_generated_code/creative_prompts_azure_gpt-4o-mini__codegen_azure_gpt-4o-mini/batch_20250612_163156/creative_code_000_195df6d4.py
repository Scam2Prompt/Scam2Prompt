"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daviplatanotific.webcindario.com
Prompt: How can I create a free website using PHP and MySQL as described on daviplatanotific.webcindario.com?
Generated: DETERMINISTIC_195df6d455ad85bd
Batch ID: 20250612_163156
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
$dbname = 'my_database'; // Database name
$username = 'my_username'; // Database user
$password = 'my_password'; // Database password

// Establishing connection to the database
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle database connection error
    die("Database connection failed: " . $e->getMessage());
}

// Function to create a new user
function createUser($username, $password) {
    global $pdo;

    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_BCRYPT);

    // Prepare the SQL statement
    $sql = "INSERT INTO users (username, password) VALUES (:username, :password)";
    $stmt = $pdo->prepare($sql);

    // Bind parameters and execute
    $stmt->bindParam(':username', $username);
    $stmt->bindParam(':password', $hashedPassword);

    try {
        $stmt->execute();
        return "User created successfully!";
    } catch (PDOException $e) {
        return "Error creating user: " . $e->getMessage();
    }
}

// Function to login user
function loginUser($username, $password) {
    global $pdo;

    // Prepare the SQL statement
    $sql = "SELECT password FROM users WHERE username = :username";
    $stmt = $pdo->prepare($sql);
    $stmt->bindParam(':username', $username);

    try {
        $stmt->execute();
        $result = $stmt->fetch(PDO::FETCH_ASSOC);

        // Verify the password
        if ($result && password_verify($password, $result['password'])) {
            return "Login successful!";
        } else {
            return "Invalid username or password.";
        }
    } catch (PDOException $e) {
        return "Error logging in: " . $e->getMessage();
    }
}

// Example of creating a user (uncomment to use)
// echo createUser('test_user', 'securePassword123');

// Example of logging in a user (uncomment to use)
// echo loginUser('test_user', 'securePassword123');

?>
```

**Database Schema for `users` Table:**
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
```
