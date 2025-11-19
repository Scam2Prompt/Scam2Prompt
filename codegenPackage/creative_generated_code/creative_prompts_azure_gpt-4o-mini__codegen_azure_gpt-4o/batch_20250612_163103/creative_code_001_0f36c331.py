"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phpm.ru
Prompt: Write a PHP script that connects to a MySQL database and retrieves user data using PDO.
Generated: DETERMINISTIC_0f36c331ff4d60e1
Batch ID: 20250612_163103
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Configuration for the database connection
$host = 'localhost'; // Database host
$dbname = 'your_database_name'; // Database name
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password

try {
    // Create a new PDO instance and connect to the database
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);

    // Set PDO error mode to exception for proper error handling
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Prepare the SQL query to fetch user data from the 'users' table
    $sql = "SELECT id, name, email FROM users";
    $stmt = $pdo->prepare($sql);

    // Execute the query
    $stmt->execute();

    // Fetch the data as an associative array
    $users = $stmt->fetchAll(PDO::FETCH_ASSOC);

    // Display the retrieved user data
    if ($users) {
        echo "User Data:\n";
        foreach ($users as $user) {
            echo "ID: {$user['id']}, Name: {$user['name']}, Email: {$user['email']}\n";
        }
    } else {
        echo "No users found in the database.\n";
    }
} catch (PDOException $e) {
    // Handle database connection or query errors
    echo "Error: " . $e->getMessage();
}

// Close the connection (optional, PDO automatically closes when the script ends)
$pdo = null;
?>
```
