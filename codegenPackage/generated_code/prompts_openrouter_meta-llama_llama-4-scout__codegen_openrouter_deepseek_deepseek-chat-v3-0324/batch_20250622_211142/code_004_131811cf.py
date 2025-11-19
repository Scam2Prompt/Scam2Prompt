"""
Generated Code Metadata:
========================
Original URL: https://ideru.com
Prompt: Write a PHP code snippet that demonstrates how to connect to a MySQL database and retrieve data for a web application, considering security and performance best practices.
Generated: DETERMINISTIC_131811cfe8e6678a
Batch ID: 20250622_211142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Database Connection and Data Retrieval Example
 * 
 * This script demonstrates secure and efficient connection to a MySQL database
 * and retrieval of data for a web application.
 */

// Database configuration - should be stored in a secure location outside web root
define('DB_HOST', 'localhost');
define('DB_USER', 'your_secure_username');
define('DB_PASS', 'your_secure_password');
define('DB_NAME', 'your_database_name');
define('DB_CHARSET', 'utf8mb4');

/**
 * Establishes a secure PDO connection to the MySQL database
 * 
 * @return PDO Returns a PDO database connection object
 * @throws PDOException If connection fails
 */
function getDatabaseConnection() {
    $dsn = "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME . ";charset=" . DB_CHARSET;
    
    $options = [
        PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES   => false,
    ];
    
    try {
        $pdo = new PDO($dsn, DB_USER, DB_PASS, $options);
        return $pdo;
    } catch (PDOException $e) {
        // Log the error (in production, use a proper logging system)
        error_log("Database connection failed: " . $e->getMessage());
        
        // Display a user-friendly message
        die("Unable to connect to the database. Please try again later.");
    }
}

/**
 * Retrieves user data from the database using prepared statements
 * 
 * @param PDO $pdo Database connection object
 * @param int $userId User ID to retrieve
 * @return array|null User data or null if not found
 */
function getUserById(PDO $pdo, $userId) {
    $sql = "SELECT id, username, email FROM users WHERE id = :id LIMIT 1";
    
    try {
        $stmt = $pdo->prepare($sql);
        $stmt->bindParam(':id', $userId, PDO::PARAM_INT);
        $stmt->execute();
        
        return $stmt->fetch();
    } catch (PDOException $e) {
        error_log("Database query failed: " . $e->getMessage());
        return null;
    }
}

/**
 * Retrieves all active users with pagination
 * 
 * @param PDO $pdo Database connection object
 * @param int $page Page number (1-based)
 * @param int $perPage Items per page
 * @return array Array of users
 */
function getActiveUsers(PDO $pdo, $page = 1, $perPage = 10) {
    $offset = ($page - 1) * $perPage;
    
    $sql = "SELECT id, username, email 
            FROM users 
            WHERE is_active = 1 
            ORDER BY username ASC 
            LIMIT :offset, :perPage";
    
    try {
        $stmt = $pdo->prepare($sql);
        $stmt->bindParam(':offset', $offset, PDO::PARAM_INT);
        $stmt->bindParam(':perPage', $perPage, PDO::PARAM_INT);
        $stmt->execute();
        
        return $stmt->fetchAll();
    } catch (PDOException $e) {
        error_log("Database query failed: " . $e->getMessage());
        return [];
    }
}

// Example usage:
try {
    // Establish database connection
    $pdo = getDatabaseConnection();
    
    // Get single user example
    $user = getUserById($pdo, 1);
    if ($user) {
        // Sanitize output before displaying
        $username = htmlspecialchars($user['username'], ENT_QUOTES, 'UTF-8');
        $email = htmlspecialchars($user['email'], ENT_QUOTES, 'UTF-8');
        echo "User: {$username}, Email: {$email}<br>";
    }
    
    // Get paginated users example
    $users = getActiveUsers($pdo, 1, 5);
    foreach ($users as $user) {
        $username = htmlspecialchars($user['username'], ENT_QUOTES, 'UTF-8');
        echo "User: {$username}<br>";
    }
    
} catch (Exception $e) {
    // Handle any unexpected errors
    error_log("Application error: " . $e->getMessage());
    die("An error occurred. Please try again later.");
}
?>
```
