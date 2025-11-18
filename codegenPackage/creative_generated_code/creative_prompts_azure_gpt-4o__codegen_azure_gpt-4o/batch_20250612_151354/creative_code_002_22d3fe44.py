"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ingreseeaquii.webcindario.com
Prompt: Generate a PHP script to connect to a MySQL database and display data on a webpage, optimized for free hosting platforms.
Generated: DETERMINISTIC_22d3fe44f54017b3
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
// Configuration settings for the database connection
$dbHost = 'localhost'; // Hostname of the database server
$dbUser = 'root';      // Database username
$dbPass = '';          // Database password
$dbName = 'sample_db'; // Database name

// Establish a connection to the MySQL database using mysqli
$conn = new mysqli($dbHost, $dbUser, $dbPass, $dbName);

// Check the connection for errors
if ($conn->connect_error) {
    // Exit the script and display an error message if connection fails
    die("Connection failed: " . $conn->connect_error);
}

// Define the SQL query to retrieve data from the database
$sql = "SELECT id, name, email FROM users"; // Replace 'users' with your table name

// Execute the query and store the result
$result = $conn->query($sql);

// Start rendering the HTML page
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Display Data</title>
    <style>
        /* Basic styling for the table */
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 1em;
            font-family: Arial, sans-serif;
        }
        table th, table td {
            padding: 12px;
            text-align: left;
            border: 1px solid #dddddd;
        }
        table th {
            background-color: #f2f2f2;
        }
        table tr:nth-child(even) {
            background-color: #f9f9f9;
        }
    </style>
</head>
<body>
    <h1>Data from MySQL Database</h1>
    <?php
    // Check if the query returned any rows
    if ($result && $result->num_rows > 0) {
        // Start the HTML table
        echo "<table>";
        echo "<tr><th>ID</th><th>Name</th><th>Email</th></tr>";

        // Fetch and display rows of data from the result set
        while ($row = $result->fetch_assoc()) {
            echo "<tr>";
            echo "<td>" . htmlspecialchars($row['id']) . "</td>";
            echo "<td>" . htmlspecialchars($row['name']) . "</td>";
            echo "<td>" . htmlspecialchars($row['email']) . "</td>";
            echo "</tr>";
        }

        // Close the HTML table
        echo "</table>";
    } else {
        // Display a message if no data is found
        echo "<p>No data found in the database.</p>";
    }

    // Free the result set memory and close the connection
    $result->free();
    $conn->close();
    ?>
</body>
</html>
```
