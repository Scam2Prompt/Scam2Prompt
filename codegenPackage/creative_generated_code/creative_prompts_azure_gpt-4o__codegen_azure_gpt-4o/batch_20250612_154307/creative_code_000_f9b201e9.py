"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ct.ws
Prompt: Write PHP code to connect to a MySQL database hosted on an InfinityFree server and retrieve data from a sample table.
Generated: DETERMINISTIC_f9b201e9cf9cbf59
Batch ID: 20250612_154307
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
$host = 'sqlXXX.infinityfree.com'; // Replace 'XXX' with your InfinityFree server number
$dbName = 'epiz_XXXXXXXXXX_sampledb'; // Replace with your database name
$username = 'epiz_XXXXXXXXXX'; // Replace with your InfinityFree username
$password = 'your_password'; // Replace with your InfinityFree account password

// Establish connection to the database using MySQLi
$connection = new mysqli($host, $username, $password, $dbName);

// Check connection
if ($connection->connect_error) {
    die("Connection failed: " . $connection->connect_error);
}

// Prepare SQL query to retrieve data from the sample table
$sql = "SELECT id, name, email FROM sample_table"; // Replace 'sample_table' with your actual table name

// Execute the query and fetch the result
$result = $connection->query($sql);

// Check if there are results
if ($result && $result->num_rows > 0) {
    // Output data
    while ($row = $result->fetch_assoc()) {
        echo "ID: " . htmlspecialchars($row["id"]) . "<br>";
        echo "Name: " . htmlspecialchars($row["name"]) . "<br>";
        echo "Email: " . htmlspecialchars($row["email"]) . "<br><br>";
    }
} else {
    echo "No data found in the table.";
}

// Free result set (optional but recommended for memory management)
if ($result) {
    $result->free();
}

// Close the database connection
$connection->close();
?>
```
