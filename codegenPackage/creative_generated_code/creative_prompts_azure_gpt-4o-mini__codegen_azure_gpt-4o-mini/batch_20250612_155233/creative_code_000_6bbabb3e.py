"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1cancelar-cambio.webcindario.com
Prompt: How can I create a free website using PHP and MySQL, as mentioned on the site 1cancelar-cambio.webcindario.com?
Generated: DETERMINISTIC_6bbabb3ea32ab674
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database connection parameters
$host = 'localhost';  // Database host
$dbname = 'my_database'; // Database name
$username = 'my_user';  // Database username
$password = 'my_password'; // Database password

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Connection failed: " . $e->getMessage());
}

// Function to create a new user
function createUser($username, $email, $password) {
    global $pdo;

    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Prepare the SQL statement
    $sql = "INSERT INTO users (username, email, password) VALUES (:username, :email, :password)";
    $stmt = $pdo->prepare($sql);

    // Bind parameters
    $stmt->bindParam(':username', $username);
    $stmt->bindParam(':email', $email);
    $stmt->bindParam(':password', $hashedPassword);

    // Execute the statement and handle errors
    try {
        $stmt->execute();
        return "User created successfully!";
    } catch (PDOException $e) {
        return "Error: " . $e->getMessage();
    }
}

// Function to authenticate a user
function authenticateUser($username, $password) {
    global $pdo;

    // Prepare the SQL statement
    $sql = "SELECT * FROM users WHERE username = :username";
    $stmt = $pdo->prepare($sql);
    $stmt->bindParam(':username', $username);

    // Execute the statement
    $stmt->execute();
    $user = $stmt->fetch(PDO::FETCH_ASSOC);

    // Verify password and handle authentication
    if ($user && password_verify($password, $user['password'])) {
        return "Authentication successful!";
    } else {
        return "Invalid username or password.";
    }
}

// Example of creating a user
echo createUser('testuser', 'test@example.com', 'securepassword');

// Example of authenticating a user
echo authenticateUser('testuser', 'securepassword');

?>
```

**SQL Schema for users table:**
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
```

**Important Notes:**
- Replace the database connection parameters with actual values.
- Ensure to create the `users` table in your MySQL database using the provided SQL schema.
- This code provides basic user registration and authentication functionality.
