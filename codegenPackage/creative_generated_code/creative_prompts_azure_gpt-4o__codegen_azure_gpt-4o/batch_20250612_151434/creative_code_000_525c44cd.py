"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://security23.webcindario.com
Prompt: Write PHP code to connect to a MySQL database and display a list of tables, suitable for hosting on a free platform like miarroba.com.
Generated: DETERMINISTIC_525c44cd59474299
Batch ID: 20250612_151434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Configuration for MySQL database connection
$dbHost = 'localhost'; // Host name
$dbUser = 'your_username'; // Database username
$dbPass = 'your_password'; // Database password
$dbName = 'your_database'; // Database name

try {
    // Establish connection to the MySQL database using PDO
    $pdo = new PDO("mysql:host=$dbHost;dbname=$dbName;charset=utf8mb4", $dbUser, $dbPass);

    // Set the PDO error mode to exception for better error handling
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Query to retrieve the list of tables in the database
    $query = $pdo->query("SHOW TABLES");

    // Fetch all tables as an associative array
    $tables = $query->fetchAll(PDO::FETCH_NUM);

    // Check if tables are found
    if (empty($tables)) {
        echo "No tables found in the database.";
    } else {
        echo "<h1>List of Tables in the Database:</h1>";
        echo "<ul>";

        // Display each table name in an unordered list
        foreach ($tables as $table) {
            echo "<li>" . htmlspecialchars($table[0]) . "</li>";
        }

        echo "</ul>";
    }
} catch (PDOException $e) {
    // Handle connection errors or query execution issues
    echo "Error: Unable to connect to the database. " . htmlspecialchars($e->getMessage());
}

// Close the database connection
$pdo = null;
?>
```
