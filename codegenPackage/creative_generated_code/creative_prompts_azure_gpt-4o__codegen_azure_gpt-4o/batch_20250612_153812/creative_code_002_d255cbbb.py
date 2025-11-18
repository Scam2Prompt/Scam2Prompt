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
// Configuration file for database connection
define('DB_HOST', 'localhost');
define('DB_NAME', 'secure_logs');
define('DB_USER', 'db_user');
define('DB_PASS', 'db_password');

// Ensure that the script is accessed securely
if (!isset($_SERVER['HTTPS']) || $_SERVER['HTTPS'] !== 'on') {
    die('Access denied: Connection must be HTTPS');
}

// Get client IP address
function getClientIP() {
    if (!empty($_SERVER['HTTP_CLIENT_IP'])) {
        return $_SERVER['HTTP_CLIENT_IP'];
    } elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
        return $_SERVER['HTTP_X_FORWARDED_FOR'];
    }
    return $_SERVER['REMOTE_ADDR'];
}

// Connect to the database securely using PDO
try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, // Enable exception handling
        PDO::ATTR_EMULATE_PREPARES => false,         // Disable emulated prepares
    ]);
} catch (Exception $e) {
    error_log("Database connection failed: " . $e->getMessage());
    die('Database connection failed');
}

// Prepare and execute the log entry
try {
    // Capture relevant request information
    $access_time = date('Y-m-d H:i:s');
    $client_ip = getClientIP();
    $user_agent = $_SERVER['HTTP_USER_AGENT'] ?? 'Unknown';

    // Insert log into the database
    $stmt = $pdo->prepare("INSERT INTO access_logs (access_time, client_ip, user_agent) VALUES (:access_time, :client_ip, :user_agent)");
    $stmt->bindParam(':access_time', $access_time);
    $stmt->bindParam(':client_ip', $client_ip);
    $stmt->bindParam(':user_agent', $user_agent);

    $stmt->execute();
} catch (Exception $e) {
    error_log("Failed to log access: " . $e->getMessage());
    die('Internal server error');
}

// Output success message
echo 'Access logged successfully';

// Ensure sensitive data is not exposed
exit;
?>
```

**Note:** Ensure that the database `secure_logs` and table `access_logs` exist with the appropriate schema:
```sql
CREATE TABLE access_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    access_time DATETIME NOT NULL,
    client_ip VARCHAR(45) NOT NULL,
    user_agent TEXT NOT NULL
);
```
