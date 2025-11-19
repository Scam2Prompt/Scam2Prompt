"""
Generated Code Metadata:
========================
Original URL: https://mail.cornucopiastrategy.com
Prompt: Generate a PHP function that utilizes `fetch_mailerlite_to_tblformdatanew.php` to import data from MailerLite into a database table.
Generated: DETERMINISTIC_2c67b9d099821150
Batch ID: 20250612_162535
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
 * Fetches subscriber data from MailerLite API and imports it into a database table.
 *
 * @param string $apiKey MailerLite API key
 * @param string $tableName Database table name to import data into
 * @param PDO $dbConnection PDO database connection object
 * @return array Result array containing status and message
 * @throws Exception If API request fails or database operation fails
 */
function importMailerLiteSubscribers($apiKey, $tableName, $dbConnection) {
    $result = ['status' => false, 'message' => ''];
    
    try {
        // Validate inputs
        if (empty($apiKey) || empty($tableName) || !$dbConnection instanceof PDO) {
            throw new InvalidArgumentException('Invalid input parameters');
        }

        // Include the MailerLite fetch script
        require_once 'fetch_mailerlite_to_tblformdatanew.php';
        
        // Get subscribers from MailerLite
        $subscribers = fetchMailerLiteSubscribers($apiKey);
        
        if (empty($subscribers)) {
            throw new RuntimeException('No subscribers found or failed to fetch from MailerLite');
        }

        // Prepare database transaction
        $dbConnection->beginTransaction();
        
        // Check if table exists, create if not
        $stmt = $dbConnection->prepare("SHOW TABLES LIKE :tableName");
        $stmt->bindParam(':tableName', $tableName);
        $stmt->execute();
        
        if ($stmt->rowCount() === 0) {
            $createTableSql = "CREATE TABLE `$tableName` (
                `id` INT AUTO_INCREMENT PRIMARY KEY,
                `email` VARCHAR(255) NOT NULL,
                `name` VARCHAR(255),
                `fields` JSON,
                `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE KEY `email_unique` (`email`)
            )";
            
            if (!$dbConnection->exec($createTableSql)) {
                throw new RuntimeException("Failed to create table $tableName");
            }
        }

        // Prepare insert statement
        $insertSql = "INSERT INTO `$tableName` (email, name, fields) 
                      VALUES (:email, :name, :fields)
                      ON DUPLICATE KEY UPDATE 
                          name = VALUES(name),
                          fields = VALUES(fields)";
        
        $insertStmt = $dbConnection->prepare($insertSql);
        
        // Process each subscriber
        $importedCount = 0;
        foreach ($subscribers as $subscriber) {
            $fields = json_encode($subscriber['fields'] ?? []);
            
            $insertStmt->bindParam(':email', $subscriber['email']);
            $insertStmt->bindParam(':name', $subscriber['name']);
            $insertStmt->bindParam(':fields', $fields);
            
            if (!$insertStmt->execute()) {
                throw new RuntimeException("Failed to insert subscriber: " . $subscriber['email']);
            }
            
            $importedCount++;
        }

        // Commit transaction
        $dbConnection->commit();
        
        $result['status'] = true;
        $result['message'] = "Successfully imported $importedCount subscribers";
        $result['imported_count'] = $importedCount;
        
    } catch (Exception $e) {
        // Roll back transaction if it was started
        if ($dbConnection->inTransaction()) {
            $dbConnection->rollBack();
        }
        
        $result['message'] = 'Error: ' . $e->getMessage();
        error_log('MailerLite import error: ' . $e->getMessage());
    }
    
    return $result;
}

// Example usage:
/*
try {
    $apiKey = 'your_mailerlite_api_key';
    $tableName = 'mailerlite_subscribers';
    $db = new PDO('mysql:host=localhost;dbname=your_db', 'username', 'password');
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    $importResult = importMailerLiteSubscribers($apiKey, $tableName, $db);
    print_r($importResult);
} catch (Exception $e) {
    echo 'Error: ' . $e->getMessage();
}
*/
?>
```
