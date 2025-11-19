"""
Generated Code Metadata:
========================
Original URL: https://connectwallet.digital
Prompt: "Create a PHP script that interacts with a database to log transactions or operations, inspired by the directory structure and files on connectwallet.digital."
Generated: DETERMINISTIC_5e23d10102d43e03
Batch ID: 20250622_212440
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
$dbname = 'transaction_log'; // Database name
$username = 'root'; // Database username
$password = ''; // Database password

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Connection failed: " . $e->getMessage());
}

/**
 * Logs a transaction to the database.
 *
 * @param string $operation The operation being logged.
 * @param string $details Additional details about the operation.
 * @return bool True on success, false on failure.
 */
function logTransaction($operation, $details) {
    global $pdo;

    // Prepare the SQL statement
    $sql = "INSERT INTO transactions (operation, details, created_at) VALUES (:operation, :details, NOW())";

    try {
        // Prepare the statement
        $stmt = $pdo->prepare($sql);
        // Bind parameters
        $stmt->bindParam(':operation', $operation);
        $stmt->bindParam(':details', $details);
        // Execute the statement
        return $stmt->execute();
    } catch (PDOException $e) {
        // Handle query error
        error_log("Error logging transaction: " . $e->getMessage());
        return false;
    }
}

// Example usage
$operation = 'User Login';
$details = 'User ID: 12345 logged in successfully.';

if (logTransaction($operation, $details)) {
    echo "Transaction logged successfully.";
} else {
    echo "Failed to log transaction.";
}
?>
```

**Database Table Structure:**
```sql
CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    operation VARCHAR(255) NOT NULL,
    details TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
