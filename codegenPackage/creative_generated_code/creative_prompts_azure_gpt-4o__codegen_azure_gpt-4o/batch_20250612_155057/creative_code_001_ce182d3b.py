"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mail.cornucopiastrategy.com
Prompt: Generate a PHP function to fetch MailerLite data and store it in a table, referencing the approach used in `fetch_mailerlite_to_tblformdatanew.php`.
Generated: DETERMINISTIC_ce182d3b89b4fb7f
Batch ID: 20250612_155057
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mailerlite.com/api/v2": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Fetch data from MailerLite API and store it in a database table.
 *
 * This function assumes you have a valid MailerLite API key and a configured database connection.
 * Ensure your environment has the required credentials and permissions set up.
 */

// Define constants for the API and database connection
define('MAILERLITE_API_KEY', 'your-mailerlite-api-key'); // Replace with your MailerLite API key
define('MAILERLITE_API_URL', 'https://api.mailerlite.com/api/v2'); // MailerLite API base URL

/**
 * Fetch data from MailerLite API and insert it into a database table.
 *
 * @param PDO $pdo A valid PDO connection instance.
 * @param string $tableName The name of the database table where data should be stored.
 * @return void
 */
function fetchMailerLiteData(PDO $pdo, string $tableName): void
{
    try {
        // Initialize cURL session
        $ch = curl_init();

        // Set cURL options
        curl_setopt($ch, CURLOPT_URL, MAILERLITE_API_URL . '/subscribers');
        curl_setopt($ch, CURLOPT_HTTPHEADER, [
            'Content-Type: application/json',
            'Authorization: Bearer ' . MAILERLITE_API_KEY,
        ]);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

        // Execute request
        $response = curl_exec($ch);

        // Check for cURL errors
        if (curl_errno($ch)) {
            throw new Exception('cURL error: ' . curl_error($ch));
        }

        // Close cURL session
        curl_close($ch);

        // Decode API response
        $data = json_decode($response, true);

        // Check if response is valid
        if (json_last_error() !== JSON_ERROR_NONE) {
            throw new Exception('JSON decode error: ' . json_last_error_msg());
        }

        // Ensure the response contains subscribers
        if (!isset($data['subscribers']) || !is_array($data['subscribers'])) {
            throw new Exception('Invalid API response: Missing subscribers data.');
        }

        // Prepare SQL statement for inserting data
        $stmt = $pdo->prepare("
            INSERT INTO $tableName (id, email, name, created_at)
            VALUES (:id, :email, :name, :created_at)
            ON DUPLICATE KEY UPDATE
                email = VALUES(email),
                name = VALUES(name),
                created_at = VALUES(created_at)
        ");

        // Iterate through subscribers and insert data into the table
        foreach ($data['subscribers'] as $subscriber) {
            $stmt->execute([
                ':id' => $subscriber['id'],
                ':email' => $subscriber['email'],
                ':name' => $subscriber['name'] ?? null,
                ':created_at' => $subscriber['created_at'],
            ]);
        }

        echo "Data successfully fetched from MailerLite and stored in the database.\n";

    } catch (Exception $e) {
        // Handle any errors that occur during the process
        error_log("Error: " . $e->getMessage());
        echo "An error occurred: " . $e->getMessage() . "\n";
    }
}

// Example usage:
// Replace 'your-database-table-name' with the name of your database table
try {
    // Create a new PDO connection
    $pdo = new PDO('mysql:host=localhost;dbname=your_database_name', 'your_username', 'your_password');
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Fetch data from MailerLite and store it in the specified table
    fetchMailerLiteData($pdo, 'your-database-table-name');
} catch (PDOException $e) {
    // Handle database connection errors
    error_log("Database connection error: " . $e->getMessage());
    echo "An error occurred while connecting to the database: " . $e->getMessage() . "\n";
}
```
