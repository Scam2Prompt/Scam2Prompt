"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infy.uk
Prompt: Can you provide a code example for connecting a MySQL database on InfinityFree?
Generated: DETERMINISTIC_fc7f2ee7d93b7b90
Batch ID: 20250612_155938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Establish a connection to a MySQL database hosted on InfinityFree.

// Database credentials
$host = 'sqlXXX.infinityfree.com'; // Replace 'XXX' with the correct server number
$username = 'your_username';      // Replace with your InfinityFree database username
$password = 'your_password';      // Replace with your InfinityFree database password
$database = 'your_database_name'; // Replace with your InfinityFree database name

// Create a new connection using MySQLi
$conn = new mysqli($host, $username, $password, $database);

// Check the connection
if ($conn->connect_error) {
    // Log the error and exit the script
    die("Connection failed: " . $conn->connect_error);
}

// Connection is successful
echo "Successfully connected to the database.";

// Perform queries or operations as needed
// Example query: Fetch data from a table
$sql = "SELECT * FROM your_table_name"; // Replace 'your_table_name' with your table name
$result = $conn->query($sql);

if ($result === false) {
    // Handle query error
    echo "Error executing query: " . $conn->error;
} else {
    // Process the query result
    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            // Output each row data (example: print to screen)
            echo "ID: " . $row['id'] . " - Name: " . $row['name'] . "<br>";
        }
    } else {
        echo "No records found.";
    }
}

// Close the connection
$conn->close();
?>
```
