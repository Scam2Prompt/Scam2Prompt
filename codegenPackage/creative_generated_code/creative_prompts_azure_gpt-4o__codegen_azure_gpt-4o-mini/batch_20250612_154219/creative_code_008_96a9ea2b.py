"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kesug.com
Prompt: Write a MySQL query to retrieve data from a database hosted on InfinityFree and display it on a webpage hosted on a kesug.com subdomain.
Generated: DETERMINISTIC_96a9ea2bd72abe45
Batch ID: 20250612_154219
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
$host = 'your_hostname'; // e.g., 'sql123.epizy.com'
$username = 'your_username'; // Your InfinityFree database username
$password = 'your_password'; // Your InfinityFree database password
$database = 'your_database'; // Your InfinityFree database name

// Create connection
$conn = new mysqli($host, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// SQL query to retrieve data from the database
$query = "SELECT * FROM your_table_name"; // Replace 'your_table_name' with your actual table name

// Execute the query and check for errors
$result = $conn->query($query);
if (!$result) {
    die("Query failed: " . $conn->error);
}

// Display data if the query returned results
if ($result->num_rows > 0) {
    echo "<table border='1'>";
    echo "<tr><th>Column1</th><th>Column2</th></tr>"; // Replace with your actual column names

    // Fetch and display each row of data
    while ($row = $result->fetch_assoc()) {
        echo "<tr>";
        echo "<td>" . htmlspecialchars($row['column1']) . "</td>"; // Replace 'column1' with actual column name
        echo "<td>" . htmlspecialchars($row['column2']) . "</td>"; // Replace 'column2' with actual column name
        echo "</tr>";
    }
    echo "</table>";
} else {
    echo "No records found.";
}

// Close the database connection
$conn->close();
?>
```
