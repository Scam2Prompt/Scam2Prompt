"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casodavhn212.webcindario.com
Prompt: Write a PHP script to create and manage a database table for storing user information on free hosting platforms.
Generated: DETERMINISTIC_3aa1f3de857a644e
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
$host = 'localhost'; // Database host
$dbname = 'user_management'; // Database name
$username = 'root'; // Database username
$password = ''; // Database password

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    // SQL query to create the users table
    $createTableSQL = "
    CREATE TABLE IF NOT EXISTS users (
        id INT(11) AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        email VARCHAR(100) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ) ENGINE=InnoDB;
    ";

    // Execute the create table query
    $pdo->exec($createTableSQL);
    echo "Table 'users' created successfully.\n";

} catch (PDOException $e) {
    // Handle any errors during the database connection or table creation
    echo "Database error: " . $e->getMessage();
    exit(); // Exit the script in case of an error
}

// Function to add a new user to the database
function addUser($username, $email, $password) {
    global $pdo;

    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    try {
        // Prepare the SQL statement
        $stmt = $pdo->prepare("INSERT INTO users (username, email, password) VALUES (:username, :email, :password)");
        
        // Bind parameters
        $stmt->bindParam(':username', $username);
        $stmt->bindParam(':email', $email);
        $stmt->bindParam(':password', $hashedPassword);
        
        // Execute the statement
        $stmt->execute();
        echo "User '$username' added successfully.\n";

    } catch (PDOException $e) {
        // Handle errors during user addition
        echo "User addition error: " . $e->getMessage();
    }
}

// Function to fetch all users from the database
function fetchUsers() {
    global $pdo;

    try {
        // Prepare the SQL statement
        $stmt = $pdo->query("SELECT id, username, email, created_at FROM users");

        // Fetch all users
        $users = $stmt->fetchAll(PDO::FETCH_ASSOC);
        return $users;

    } catch (PDOException $e) {
        // Handle errors during fetching users
        echo "Fetch users error: " . $e->getMessage();
        return [];
    }
}

// Function to delete a user by ID
function deleteUser($id) {
    global $pdo;

    try {
        // Prepare the SQL statement
        $stmt = $pdo->prepare("DELETE FROM users WHERE id = :id");
        
        // Bind parameter
        $stmt->bindParam(':id', $id);
        
        // Execute the statement
        $stmt->execute();
        echo "User with ID '$id' deleted successfully.\n";

    } catch (PDOException $e) {
        // Handle errors during user deletion
        echo "User deletion error: " . $e->getMessage();
    }
}

// Example usage
addUser('john_doe', 'john@example.com', 'securepassword123');

// Fetch and display all users
$users = fetchUsers();
print_r($users);

// Delete a user with ID 1 (update the ID as necessary)
deleteUser(1);

?>
```
