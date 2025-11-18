"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daviviendaportal.webcindario.com
Prompt: Recommend free tools or libraries for creating a PHP-based website with MySQL database support and explain how to integrate them.
Generated: DETERMINISTIC_f933ba6da24335c5
Batch ID: 20250612_151459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Simple PHP-based website with MySQL database support
 *
 * This example demonstrates a basic structure of a PHP application that connects to a 
 * MySQL database using PDO (PHP Data Objects) for secure database interactions.
 */

// Database configuration
$host = 'localhost'; // Database host
$db   = 'your_database'; // Database name
$user = 'your_username'; // Database username
$pass = 'your_password'; // Database password
$charset = 'utf8mb4'; // Database charset

// Set up the Data Source Name (DSN) for the PDO connection
$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION, // Enable exceptions
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC, // Fetch results as associative arrays
    PDO::ATTR_EMULATE_PREPARES   => false, // Disable emulation of prepared statements
];

try {
    // Create a new PDO instance for database connection
    $pdo = new PDO($dsn, $user, $pass, $options);
} catch (\PDOException $e) {
    // Handle connection errors gracefully
    throw new \PDOException($e->getMessage(), (int)$e->getCode());
}

// Function to fetch all records from the 'users' table
function fetchUsers($pdo) {
    $stmt = $pdo->query('SELECT * FROM users'); // Prepare SQL query
    return $stmt->fetchAll(); // Fetch all results
}

// Function to add a new user to the users table
function addUser($pdo, $name, $email) {
    $stmt = $pdo->prepare('INSERT INTO users (name, email) VALUES (:name, :email)'); // Prepare SQL query
    try {
        // Execute the statement with user data
        $stmt->execute(['name' => $name, 'email' => $email]);
        return $pdo->lastInsertId(); // Return the last inserted ID
    } catch (PDOException $e) {
        // Handle query execution errors
        echo "Error inserting user: " . $e->getMessage();
        return false;
    }
}

// Example usage
// Adding a new user
$newUserId = addUser($pdo, 'John Doe', 'john.doe@example.com');
if ($newUserId) {
    echo "User added with ID: " . $newUserId . "\n";
}

// Fetch and display all users
$users = fetchUsers($pdo);
foreach ($users as $user) {
    echo "User ID: " . $user['id'] . " - Name: " . $user['name'] . " - Email: " . $user['email'] . "\n";
}
?>
```

### Usage Notes:
- Replace `your_database`, `your_username`, and `your_password` with actual database credentials.
- The script assumes a table named `users` exists with columns `id`, `name`, and `email`. Adjust the SQL queries accordingly based on your actual database schema.
- Make sure to handle HTML form input validation and sanitization when you integrate this code into a broader application.
