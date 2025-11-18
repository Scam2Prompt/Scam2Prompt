"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casodavhn212.webcindario.com
Prompt: Write a PHP script to display data from a MySQL database in an HTML table for a website hosted on free platforms.
Generated: DETERMINISTIC_47276d7b99561980
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database configuration - replace placeholders with actual values
$host = 'localhost'; // e.g., '127.0.0.1' or 'localhost'
$username = 'root';  // e.g., 'root' or your database username
$password = '';      // e.g., '' for no password or your database password
$database = 'test_db'; // Replace with your database name

// Establish a connection to the MySQL database
$conn = new mysqli($host, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// SQL query to fetch data from the desired table
$sql = "SELECT id, name, email FROM users"; // Replace 'users' with your table name

// Execute the query and get the result
$result = $conn->query($sql);

// Check if the query returned any rows
if ($result->num_rows > 0) {
    // Start the HTML output
    echo "<!DOCTYPE html>";
    echo "<html lang='en'>";
    echo "<head>";
    echo "<meta charset='UTF-8'>";
    echo "<meta name='viewport' content='width=device-width, initial-scale=1.0'>";
    echo "<title>Data Table</title>";
    echo "<style>";
    echo "table { border-collapse: collapse; width: 100%; }";
    echo "th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }";
    echo "th { background-color: #f2f2f2; }";
    echo "</style>";
    echo "</head>";
    echo "<body>";
    echo "<h1>Data From Database</h1>";
    echo "<table>";
    echo "<thead>";
    echo "<tr>";
    echo "<th>ID</th>";
    echo "<th>Name</th>";
    echo "<th>Email</th>";
    echo "</tr>";
    echo "</thead>";
    echo "<tbody>";

    // Fetch rows and display them in the table
    while ($row = $result->fetch_assoc()) {
        echo "<tr>";
        echo "<td>" . htmlspecialchars($row['id']) . "</td>";    // Sanitize output
        echo "<td>" . htmlspecialchars($row['name']) . "</td>";
        echo "<td>" . htmlspecialchars($row['email']) . "</td>";
        echo "</tr>";
    }

    echo "</tbody>";
    echo "</table>";
    echo "</body>";
    echo "</html>";
} else {
    // Display a message if no data is found
    echo "<p>No records found.</p>";
}

// Close the database connection
$conn->close();
?>
```
