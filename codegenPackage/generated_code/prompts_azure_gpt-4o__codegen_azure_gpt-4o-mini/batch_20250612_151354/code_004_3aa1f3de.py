"""
Generated Code Metadata:
========================
Original URL: https://casodavhn212.webcindario.com
Prompt: Write a PHP script to create and manage a database table for storing user information on free hosting platforms.
Generated: DETERMINISTIC_3aa1f3de857a644e
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Database configuration
$host = 'localhost'; // Database host
$dbname = 'user_management'; // Database name
$username = 'root'; // Database username
$password = ''; // Database password

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    // SQL to create the user table if it doesn't exist
    $sql = "CREATE TABLE IF NOT EXISTS users (
        id INT(11) AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        email VARCHAR(100) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ) ENGINE=InnoDB";

    // Execute the query
    $pdo->exec($sql);
    echo "Table 'users' created successfully or already exists.";

} catch (PDOException $e) {
    // Handle any errors during the connection or table creation
    echo "Error: " . $e->getMessage();
}

// Function to add a new user
function addUser($username, $email, $password) {
    global $pdo;

    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Prepare the SQL statement
    $sql = "INSERT INTO users (username, email, password) VALUES (:username, :email, :password)";
    
    try {
        $stmt = $pdo->prepare($sql);
        // Bind parameters
        $stmt->bindParam(':username', $username);
        $stmt->bindParam(':email', $email);
        $stmt->bindParam(':password', $hashedPassword);
        // Execute the statement
        $stmt->execute();
        echo "User added successfully.";
    } catch (PDOException $e) {
        // Handle any errors during the insertion
        echo "Error: " . $e->getMessage();
    }
}

// Function to retrieve all users
function getUsers() {
    global $pdo;

    // Prepare the SQL statement
    $sql = "SELECT * FROM users";
    
    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute();
        // Fetch all users
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        // Handle any errors during the retrieval
        echo "Error: " . $e->getMessage();
        return [];
    }
}

// Example usage
// Uncomment the following lines to add a user or retrieve users
// addUser('john_doe', 'john@example.com', 'securepassword');
// $users = getUsers();
// print_r($users);

?>
```
