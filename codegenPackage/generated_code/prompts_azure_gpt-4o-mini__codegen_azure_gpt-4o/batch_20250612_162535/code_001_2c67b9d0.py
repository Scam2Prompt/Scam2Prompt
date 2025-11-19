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
 * Imports data from MailerLite into a database table using the `fetch_mailerlite_to_tblformdatanew.php` script.
 *
 * @param PDO $pdo The PDO database connection object.
 * @param string $mailerliteApiKey The API key for MailerLite.
 * @param string $tableName The name of the database table to insert data into.
 * @return void
 * @throws Exception If an error occurs during the process.
 */
function importMailerLiteData(PDO $pdo, string $mailerliteApiKey, string $tableName): void
{
    try {
        // Validate table name to prevent SQL injection
        if (!preg_match('/^[a-zA-Z0-9_]+$/', $tableName)) {
            throw new InvalidArgumentException('Invalid table name provided.');
        }

        // Include the external script to fetch data from MailerLite
        require_once 'fetch_mailerlite_to_tblformdatanew.php';

        // Fetch data from MailerLite using the external script
        $data = fetchMailerLiteData($mailerliteApiKey); // Assuming this function exists in the included script

        // Validate the fetched data
        if (!is_array($data) || empty($data)) {
            throw new RuntimeException('No data fetched from MailerLite or data is invalid.');
        }

        // Prepare the SQL statement for inserting data
        $columns = array_keys($data[0]);
        $placeholders = implode(',', array_fill(0, count($columns), '?'));
        $sql = sprintf(
            'INSERT INTO %s (%s) VALUES (%s)',
            $tableName,
            implode(',', $columns),
            $placeholders
        );
        $stmt = $pdo->prepare($sql);

        // Insert each row of data into the database
        foreach ($data as $row) {
            $stmt->execute(array_values($row));
        }

        echo "Data imported successfully into table: $tableName\n";
    } catch (Exception $e) {
        // Log the error and rethrow it
        error_log('Error importing MailerLite data: ' . $e->getMessage());
        throw $e;
    }
}

/**
 * Mock function to simulate fetching data from MailerLite.
 * Replace this with the actual implementation from the included script.
 *
 * @param string $apiKey The API key for MailerLite.
 * @return array The fetched data as an associative array.
 */
function fetchMailerLiteData(string $apiKey): array
{
    // Simulated data for demonstration purposes
    return [
        ['email' => 'user1@example.com', 'name' => 'User One', 'status' => 'active'],
        ['email' => 'user2@example.com', 'name' => 'User Two', 'status' => 'inactive'],
    ];
}

// Example usage
try {
    // Create a PDO connection (replace with your actual database credentials)
    $pdo = new PDO('mysql:host=localhost;dbname=your_database', 'username', 'password');
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Call the function to import data
    importMailerLiteData($pdo, 'your_mailerlite_api_key', 'your_table_name');
} catch (Exception $e) {
    echo 'An error occurred: ' . $e->getMessage();
}
```
