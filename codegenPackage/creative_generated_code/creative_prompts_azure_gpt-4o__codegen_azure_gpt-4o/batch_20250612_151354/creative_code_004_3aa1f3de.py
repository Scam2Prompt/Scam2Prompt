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
$host = 'localhost'; // Replace with your hosting platform's database host name
$dbname = 'your_database_name'; // Replace with your database name
$username = 'your_username'; // Replace with your database username
$password = 'your_password'; // Replace with your database password

try {
    // Connect to the database using PDO
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8mb4", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Create the 'users' table if it doesn't exist
    $tableCreationQuery = "
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(150) NOT NULL UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB;
    ";
    $pdo->exec($tableCreationQuery);
    echo "Table 'users' created successfully or already exists.\n";

    // Function to insert a new user into the 'users' table
    function addUser(PDO $pdo, $name, $email) {
        try {
            $insertQuery = "INSERT INTO users (name, email) VALUES (:name, :email)";
            $stmt = $pdo->prepare($insertQuery);
            $stmt->bindParam(':name', $name, PDO::PARAM_STR);
            $stmt->bindParam(':email', $email, PDO::PARAM_STR);
            $stmt->execute();
            echo "User added successfully.\n";
        } catch (PDOException $e) {
            // Handle duplicate email errors or other insertion issues
            if ($e->getCode() == 23000) { // SQLSTATE 23000: Integrity constraint violation
                echo "Error: Email already exists.\n";
            } else {
                echo "Error adding user: " . $e->getMessage() . "\n";
            }
        }
    }

    // Function to fetch all users from the 'users' table
    function getAllUsers(PDO $pdo) {
        try {
            $selectQuery = "SELECT id, name, email, created_at FROM users";
            $stmt = $pdo->query($selectQuery);
            $users = $stmt->fetchAll(PDO::FETCH_ASSOC);
            return $users;
        } catch (PDOException $e) {
            echo "Error fetching users: " . $e->getMessage() . "\n";
            return [];
        }
    }

    // Example usage:
    // Uncomment the following lines to test the script.

    // Adding a new user
    // addUser($pdo, 'John Doe', 'john.doe@example.com');

    // Fetching all users and displaying them
    // $users = getAllUsers($pdo);
    // foreach ($users as $user) {
    //     echo "ID: {$user['id']}, Name: {$user['name']}, Email: {$user['email']}, Created At: {$user['created_at']}\n";
    // }

} catch (PDOException $e) {
    // Handle database connection errors
    echo "Database connection failed: " . $e->getMessage() . "\n";
}
?>
```
