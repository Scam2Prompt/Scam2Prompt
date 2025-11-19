"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://davihncas230.webcindario.com
Prompt: How do I connect a MySQL database to a PHP website as suggested in the content?
Generated: DETERMINISTIC_8aa2b2169522038c
Batch ID: 20250612_155340
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Define database configuration parameters
$hostname = "localhost"; // Hostname where the database is located
$username = "your_username"; // Database username
$password = "your_password"; // Database password
$database = "your_database_name"; // Database name

// Establish a connection to the MySQL database using mysqli
$conn = new mysqli($hostname, $username, $password, $database);

// Check if the connection was successful
if ($conn->connect_error) {
    // Handle connection error gracefully
    die("Connection failed: " . $conn->connect_error);
}

// If the connection is successful, output a confirmation message
echo "Connected successfully to the MySQL database.";

// Example query execution (optional)
// $sql = "SELECT * FROM your_table_name";
// $result = $conn->query($sql);

// Handle query results (if applicable)
// if ($result && $result->num_rows > 0) {
//     while ($row = $result->fetch_assoc()) {
//         // Process each row in the result set
//         echo "Data: " . $row["column_name"] . "<br>";
//     }
// } else {
//     echo "No data found or query failed.";
// }

// Close the database connection when done
$conn->close();
?>
```
