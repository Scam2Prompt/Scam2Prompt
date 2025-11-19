"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mail.cornucopiastrategy.com
Prompt: Generate a PHP function that utilizes `fetch_mailerlite_to_tblformdatanew.php` to import data from MailerLite into a database table.
Generated: DETERMINISTIC_2c67b9d099821150
Batch ID: 20250612_162535
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
 * Imports data from MailerLite into a database table.
 * 
 * @throws Exception if the file fetch_mailerlite_to_tblformdatanew.php is not found or errors occur during execution.
 */

// Import function to fetch data from MailerLite
require_once 'fetch_mailerlite_to_tblformdatanew.php';

/**
 * Function to import MailerLite data into a database table.
 *
 * @param PDO $pdo The database connection instance (PDO).
 * @param string $tableName The name of the database table to insert data into.
 * @return void
 * @throws Exception If any error occurs during the process.
 */
function importMailerLiteData(PDO $pdo, string $tableName): void
{
    try {
        // Fetch data from MailerLite using the external script
        $data = fetch_mailerlite_to_tblformdatanew();

        // Validate the fetched data
        if (!is_array($data) || empty($data)) {
            throw new Exception('No valid data fetched from MailerLite.');
        }

        // Prepare SQL statement for inserting data
        $placeholders = implode(',', array_fill(0, count($data[0]), '?'));
        $columns = implode(',', array_keys($data[0]));
        $sql = "INSERT INTO {$tableName} ({$columns}) VALUES ({$placeholders})";
        $stmt = $pdo->prepare($sql);

        // Begin a transaction
        $pdo->beginTransaction();

        // Insert each record into the database
        foreach ($data as $record) {
            $stmt->execute(array_values($record));
        }

        // Commit the transaction
        $pdo->commit();

    } catch (Exception $e) {
        // Rollback the transaction in case of an error
        if ($pdo->inTransaction()) {
            $pdo->rollBack();
        }

        // Log the error and rethrow the exception
        error_log($e->getMessage());
        throw new Exception('Error importing MailerLite data: ' . $e->getMessage());
    }
}
```
