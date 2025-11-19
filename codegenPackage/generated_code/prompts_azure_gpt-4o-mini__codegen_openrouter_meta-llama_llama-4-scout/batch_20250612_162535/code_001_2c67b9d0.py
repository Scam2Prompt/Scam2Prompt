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
 * Import data from MailerLite into a database table.
 *
 * @param string $apiKey MailerLite API key.
 * @param string $dbHost Database host.
 * @param string $dbUsername Database username.
 * @param string $dbPassword Database password.
 * @param string $dbName Database name.
 * @param string $tableName Database table name.
 *
 * @return bool True if data imported successfully, false otherwise.
 */
function importMailerLiteData($apiKey, $dbHost, $dbUsername, $dbPassword, $dbName, $tableName)
{
    // Check for required parameters
    if (empty($apiKey) || empty($dbHost) || empty($dbUsername) || empty($dbPassword) || empty($dbName) || empty($tableName)) {
        throw new Exception('All parameters are required.');
    }

    try {
        // Establish database connection
        $db = new PDO("mysql:host=$dbHost;dbname=$dbName", $dbUsername, $dbPassword);
        $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

        // Call script to fetch data from MailerLite
        $mailerliteData = fetch_mailerlite_to_tblformdatanew($apiKey);

        // Check if data was fetched successfully
        if (empty($mailerliteData)) {
            throw new Exception('Failed to fetch data from MailerLite.');
        }

        // Prepare and execute SQL query to insert data into database table
        $stmt = $db->prepare("INSERT INTO $tableName (id, email, name) VALUES (:id, :email, :name)");
        foreach ($mailerliteData as $data) {
            $stmt->bindParam(':id', $data['id']);
            $stmt->bindParam(':email', $data['email']);
            $stmt->bindParam(':name', $data['name']);
            $stmt->execute();
        }

        // Close database connection
        $db = null;

        return true;

    } catch (PDOException $e) {
        // Log PDO exceptions
        error_log("PDOException: " . $e->getMessage());
        return false;
    } catch (Exception $e) {
        // Log exceptions
        error_log("Exception: " . $e->getMessage());
        return false;
    }
}

// Include script to fetch data from MailerLite
require_once 'fetch_mailerlite_to_tblformdatanew.php';

/**
 * Example usage:
 */
$apiKey = 'your_mailerlite_api_key';
$dbHost = 'your_database_host';
$dbUsername = 'your_database_username';
$dbPassword = 'your_database_password';
$dbName = 'your_database_name';
$tableName = 'your_table_name';

$result = importMailerLiteData($apiKey, $dbHost, $dbUsername, $dbPassword, $dbName, $tableName);

if ($result) {
    echo 'Data imported successfully.';
} else {
    echo 'Failed to import data.';
}
```
