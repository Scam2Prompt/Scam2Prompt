"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eigenlayer.eigenda.cc
Prompt: Generate a PHP script to log access requests to `key.php` and store them in a secure database.
Generated: DETERMINISTIC_d255cbbb99f54f31
Batch ID: 20250612_153812
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
$db = 'access_log'; // Database name
$user = 'username'; // Database user
$pass = 'password'; // Database password

// Create a new PDO instance for database connection
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Log the error message to a file and exit
    error_log("Database Connection Error: " . $e->getMessage(), 3, 'error.log');
    exit("Database connection failed.");
}

// Function to log access requests
function logAccess($pdo) {
    // Prepare the SQL statement to insert log details
    $sql = "INSERT INTO access_requests (timestamp, ip_address, user_agent) VALUES (:timestamp, :ip_address, :user_agent)";
    $stmt = $pdo->prepare($sql);

    // Gather log details
    $timestamp = date('Y-m-d H:i:s'); // Current timestamp
    $ipAddress = $_SERVER['REMOTE_ADDR']; // User's IP address
    $userAgent = $_SERVER['HTTP_USER_AGENT']; // User's browser info

    // Bind parameters and execute the statement
    $stmt->bindParam(':timestamp', $timestamp);
    $stmt->bindParam(':ip_address', $ipAddress);
    $stmt->bindParam(':user_agent', $userAgent);

    try {
        $stmt->execute(); // Execute the insertion
    } catch (PDOException $e) {
        // Log any error that occurs during insertion
        error_log("Insert Error: " . $e->getMessage(), 3, 'error.log');
    }
}

// Call the function to log the access request
logAccess($pdo);

// You can include the main logic of key.php below
// ...
?>
```

**Note**: Ensure that the database named `access_log` and the table `access_requests` with appropriate columns (`timestamp`, `ip_address`, and `user_agent`) are created in advance. The credentials for the database connection should be secured and not hard-coded in production environments.
