"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://illuviumprotocol.net
Prompt: Generate a PHP script that uses the PDO driver-specific subclasses introduced in PHP 8.4 to interact with a MySQL database.
Generated: DETERMINISTIC_4f82188346111bca
Batch ID: 20250612_154339
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Ensure options are set to handle exceptions and emulate prepared statements
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_EMULATE_PREPARES   => false,
];

// Database connection parameters
$host = 'localhost'; // Database host
$db   = 'your_database'; // Database name
$user = 'your_username'; // Database username
$pass = 'your_password'; // Database password
$charset = 'utf8mb4'; // Character set

// Data Source Name
$dsn = "mysql:host=$host;dbname=$db;charset=$charset";

try {
    // Create a new PDO instance with driver-specific subclass
    $pdo = new PDO($dsn, $user, $pass, $options);
    
    // Example function to fetch all users from the database
    function fetchAllUsers(PDO $pdo) {
        // Prepare the SQL statement
        $stmt = $pdo->prepare("SELECT * FROM users");

        // Execute the statement
        $stmt->execute();

        // Fetch all results as an associative array
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    // Example usage
    $users = fetchAllUsers($pdo);
    
    // Output users in JSON format
    header('Content-Type: application/json');
    echo json_encode($users);

} catch (PDOException $e) {
    // Handle connection error
    http_response_code(500); // Internal Server Error
    echo json_encode(['error' => 'Database connection failed: ' . $e->getMessage()]);
    exit;
} catch (Exception $e) {
    // Handle general errors
    http_response_code(500); // Internal Server Error
    echo json_encode(['error' => 'An unexpected error occurred: ' . $e->getMessage()]);
    exit;
}
?>
```
