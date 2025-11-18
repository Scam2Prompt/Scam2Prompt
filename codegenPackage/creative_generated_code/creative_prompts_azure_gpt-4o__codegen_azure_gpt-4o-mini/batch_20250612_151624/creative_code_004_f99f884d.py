"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ingreseaquii.webcindario.com
Prompt: Write a PHP script to display data from a MySQL database in a webpage, suitable for free hosting environments like miarroba.com.
Generated: DETERMINISTIC_f99f884d7b964fde
Batch ID: 20250612_151624
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
$servername = "localhost"; // Database server
$username = "your_username"; // Database username
$password = "your_password"; // Database password
$dbname = "your_database"; // Database name

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// SQL query to select data from a table
$sql = "SELECT id, name, email FROM users"; // Adjust table and column names as necessary
$result = $conn->query($sql);

// Check if there are results
if ($result->num_rows > 0) {
    // Start HTML output
    echo "<!DOCTYPE html>
    <html lang='en'>
    <head>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
        <title>User Data</title>
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
            }
            table, th, td {
                border: 1px solid black;
            }
            th, td {
                padding: 10px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <h1>User Data</h1>
        <table>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Email</th>
            </tr>";
    
    // Output data of each row
    while($row = $result->fetch_assoc()) {
        echo "<tr>
                <td>" . htmlspecialchars($row["id"]) . "</td>
                <td>" . htmlspecialchars($row["name"]) . "</td>
                <td>" . htmlspecialchars($row["email"]) . "</td>
              </tr>";
    }

    // End HTML table
    echo "</table>
        </body>
        </html>";
} else {
    // If no results found
    echo "0 results";
}

// Close the database connection
$conn->close();
?>
```
