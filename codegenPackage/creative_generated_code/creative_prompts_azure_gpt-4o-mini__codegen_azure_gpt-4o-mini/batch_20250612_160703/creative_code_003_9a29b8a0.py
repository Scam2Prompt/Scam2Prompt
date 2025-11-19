"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://muskelon547776.webcindario.com
Prompt: What tools or libraries do I need to create a free website using PHP and MySQL?
Generated: DETERMINISTIC_9a29b8a0a0aac522
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Initialize a session
session_start();

// Database configuration
$host = 'localhost'; // Database host
$dbname = 'your_database'; // Database name
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password

// Function to create a connection to the database
function getDatabaseConnection() {
    global $host, $dbname, $username, $password;
    try {
        $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
        // Set the PDO error mode to exception
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        // Handle connection error
        die("Database connection failed: " . $e->getMessage());
    }
}

// Function to create a new user
function createUser($username, $password) {
    $pdo = getDatabaseConnection();
    try {
        // Hash the password for security
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
        $stmt = $pdo->prepare("INSERT INTO users (username, password) VALUES (:username, :password)");
        $stmt->bindParam(':username', $username);
        $stmt->bindParam(':password', $hashedPassword);
        $stmt->execute();
        return $pdo->lastInsertId();
    } catch (PDOException $e) {
        // Handle error on user creation
        die("User creation failed: " . $e->getMessage());
    }
}

// Function to authenticate a user
function authenticateUser($username, $password) {
    $pdo = getDatabaseConnection();
    try {
        $stmt = $pdo->prepare("SELECT * FROM users WHERE username = :username");
        $stmt->bindParam(':username', $username);
        $stmt->execute();
        $user = $stmt->fetch(PDO::FETCH_ASSOC);
        
        // Verify the password
        if ($user && password_verify($password, $user['password'])) {
            $_SESSION['user_id'] = $user['id'];
            return true;
        } else {
            return false;
        }
    } catch (PDOException $e) {
        // Handle error on user authentication
        die("User authentication failed: " . $e->getMessage());
    }
}

// Example usage:
// Create a user (Uncomment to use)
// createUser('testuser', 'testpassword');

// Authenticate a user (Uncomment to use)
// if (authenticateUser('testuser', 'testpassword')) {
//     echo "User authenticated successfully";
// } else {
//     echo "Authentication failed";
// }
?>
```

### Requirements:
- You need to have a running MySQL server.
- Create a database and a `users` table with fields `id`, `username`, and `password`.
- Ensure that the PDO extension is enabled in your PHP installation.
