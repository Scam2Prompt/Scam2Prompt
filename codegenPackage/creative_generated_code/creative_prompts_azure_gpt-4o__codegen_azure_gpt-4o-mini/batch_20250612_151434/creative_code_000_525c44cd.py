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
// Database configuration
$host = 'localhost'; // Database host
$dbname = 'your_database_name'; // Database name
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Prepare and execute the query to fetch table names
    $query = $pdo->query("SHOW TABLES");
    
    // Fetch all table names into an array
    $tables = $query->fetchAll(PDO::FETCH_COLUMN);

    // Check if there are any tables in the database
    if (empty($tables)) {
        echo "No tables found in the database.";
    } else {
        // Display the list of tables
        echo "<h2>List of Tables in the Database:</h2>";
        echo "<ul>";
        foreach ($tables as $table) {
            echo "<li>" . htmlspecialchars($table) . "</li>";
        }
        echo "</ul>";
    }
} catch (PDOException $e) {
    // Handle database connection errors
    echo "Database connection failed: " . htmlspecialchars($e->getMessage());
}

// Close the PDO connection
$pdo = null;
?>
```

Make sure to replace the placeholder values for `$dbname`, `$username`, and `$password` with your actual database credentials before running the code. This code is secure, handles errors gracefully, and is ready for deployment on platforms like miarroba.com.
