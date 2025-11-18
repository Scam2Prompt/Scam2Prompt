"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infy.uk
Prompt: Write PHP code to connect to a MySQL database hosted on InfinityFree and retrieve data from a table.
Generated: DETERMINISTIC_b64079674a96f4f0
Batch ID: 20250612_154344
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
 * Database connection script
 * This script connects to a MySQL database hosted on InfinityFree,
 * retrieves data from a specified table, and handles errors gracefully.
 */

// Database configuration
$servername = "sqlXXX.epizy.com"; // Replace with your actual server name
$username = "username"; // Replace with your database username
$password = "password"; // Replace with your database password
$dbname = "database_name"; // Replace with your database name
$table = "table_name"; // Replace with your table name

// Create a connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check the connection
if ($conn->connect_error) {
    // Handle connection error
    die("Connection failed: " . $conn->connect_error);
}

// Prepare the SQL query
$sql = "SELECT * FROM $table";
$result = $conn->query($sql);

// Check if the query was successful
if ($result === false) {
    // Handle SQL error
    die("Error executing query: " . $conn->error);
}

// Fetch data and display it
if ($result->num_rows > 0) {
    // Output data for each row
    while ($row = $result->fetch_assoc()) {
        // Process each row
        echo "ID: " . $row["id"] . " - Name: " . $row["name"] . "<br>"; // Adjust fields accordingly
    }
} else {
    echo "No results found.";
}

// Free the result set
$result->free();

// Close the connection
$conn->close();
?>
```
