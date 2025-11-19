"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://corfucoastalcollection.com
Prompt: Create a PHP code snippet that connects to a database to store inquiries for villas and plots from the Corfu Coastal Collection site.
Generated: DETERMINISTIC_6987043f77af61c1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database Configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'corfu_coastal_collection');
define('DB_USER', 'your_username'); // Replace with your database username
define('DB_PASS', 'your_password'); // Replace with your database password

/**
 * Function to establish a database connection.
 * 
 * @return PDO
 * @throws Exception if connection fails.
 */
function getDatabaseConnection() {
    try {
        // Create a new PDO instance
        $dsn = 'mysql:host=' . DB_HOST . ';dbname=' . DB_NAME . ';charset=utf8mb4';
        $pdo = new PDO($dsn, DB_USER, DB_PASS, [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, 
            PDO::ATTR_PERSISTENT => false
        ]);
        return $pdo;
    } catch (PDOException $e) {
        // Log error and throw exception
        error_log('Database connection error: ' . $e->getMessage());
        throw new Exception('Failed to connect to database.');
    }
}

/**
 * Function to store inquiry data into the database.
 * 
 * @param string $name Customer name
 * @param string $email Customer email
 * @param string $type Inquiry type (villa or plot)
 * @param string $message Inquiry message
 * @return bool Returns true if the data is stored successfully.
 */
function storeInquiry($name, $email, $type, $message) {
    try {
        // Validate inquiry type
        if (!in_array($type, ['villa', 'plot'])) {
            throw new Exception('Invalid inquiry type.');
        }

        // Get database connection
        $pdo = getDatabaseConnection();

        // Prepare the SQL query
        $sql = 'INSERT INTO inquiries (name, email, type, message, created_at) VALUES (:name, :email, :type, :message, NOW())';
        $stmt = $pdo->prepare($sql);

        // Bind parameters
        $stmt->bindParam(':name', $name, PDO::PARAM_STR);
        $stmt->bindParam(':email', $email, PDO::PARAM_STR);
        $stmt->bindParam(':type', $type, PDO::PARAM_STR);
        $stmt->bindParam(':message', $message, PDO::PARAM_STR);

        // Execute the query
        return $stmt->execute();
    } catch (Exception $e) {
        // Log error and return false
        error_log('Error storing inquiry: ' . $e->getMessage());
        return false;
    }
}

// Example usage
try {
    $name = 'John Doe';
    $email = 'john.doe@example.com';
    $type = 'villa';
    $message = 'I am interested in a villa at Corfu Coastal Collection.';

    if (storeInquiry($name, $email, $type, $message)) {
        echo 'Inquiry successfully stored.';
    } else {
        echo 'Failed to store inquiry.';
    }
} catch (Exception $e) {
    echo 'An error occurred: ' . $e->getMessage();
}
?>
```
