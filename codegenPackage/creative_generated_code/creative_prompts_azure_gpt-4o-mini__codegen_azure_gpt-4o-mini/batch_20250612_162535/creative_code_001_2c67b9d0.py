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
 * Import data from MailerLite into a database table.
 * 
 * This function calls the fetch_mailerlite_to_tblformdatanew.php script,
 * retrieves the data, and inserts it into the specified database table.
 *
 * @param string $dbHost     Database host.
 * @param string $dbUsername Database username.
 * @param string $dbPassword Database password.
 * @param string $dbName     Database name.
 * @param string $tableName  Database table name to insert data into.
 * @return void
 */
function importMailerLiteData($dbHost, $dbUsername, $dbPassword, $dbName, $tableName) {
    // Include the MailerLite data fetching script
    require_once 'fetch_mailerlite_to_tblformdatanew.php';

    // Establish a database connection
    $conn = new mysqli($dbHost, $dbUsername, $dbPassword, $dbName);

    // Check for connection errors
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    // Fetch MailerLite data
    $data = fetchMailerLiteData(); // Assuming this function returns the data array

    // Prepare the SQL Insert Statement
    $stmt = $conn->prepare("INSERT INTO $tableName (column1, column2, column3) VALUES (?, ?, ?)");
    
    if (!$stmt) {
        die("Preparation failed: " . $conn->error);
    }

    // Loop through the fetched data and bind parameters
    foreach ($data as $row) {
        // Assuming $row contains the data for column1, column2, and column3
        $stmt->bind_param("sss", $row['column1'], $row['column2'], $row['column3']);
        
        // Execute the statement
        if (!$stmt->execute()) {
            echo "Execution failed: " . $stmt->error . "\n";
        }
    }

    // Close the statement and connection
    $stmt->close();
    $conn->close();
}

// Example usage
// importMailerLiteData('localhost', 'username', 'password', 'database', 'table_name');
?>
```
