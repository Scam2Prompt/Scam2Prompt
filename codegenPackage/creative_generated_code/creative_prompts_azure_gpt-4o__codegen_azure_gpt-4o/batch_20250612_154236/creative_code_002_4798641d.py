"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coosella5554.webcindario.com
Prompt: Generate a PHP script to connect to a MySQL database and display data on a webpage, suitable for hosting on a free platform like miarroba.com.
Generated: DETERMINISTIC_4798641dd453d12f
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database Configuration
$host = 'localhost'; // Change this to your MySQL host (e.g., '127.0.0.1' or actual server hostname)
$user = 'your_username'; // Replace with your MySQL username
$password = 'your_password'; // Replace with your MySQL password
$database = 'your_database'; // Replace with your database name

// Establish Connection to the Database
$conn = new mysqli($host, $user, $password, $database);

// Check Connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Query to Fetch Data
$sql = "SELECT id, name, email FROM users"; // Update 'users' table and columns as per your database schema
$result = $conn->query($sql);

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Database Data Display</title>
    <style>
        /* Simple table styling */
        table {
            width: 80%;
            margin: auto;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
        }
        th {
            background-color: #f4f4f4;
            text-align: center;
        }
        td {
            text-align: left;
        }
    </style>
</head>
<body>
    <h1 style="text-align: center;">User Records</h1>
    <?php
    // Check if query returned results
    if ($result->num_rows > 0) {
        echo "<table>";
        echo "<tr><th>ID</th><th>Name</th><th>Email</th></tr>";
        
        // Output data for each row
        while ($row = $result->fetch_assoc()) {
            echo "<tr>";
            echo "<td>" . htmlspecialchars($row['id']) . "</td>";
            echo "<td>" . htmlspecialchars($row['name']) . "</td>";
            echo "<td>" . htmlspecialchars($row['email']) . "</td>";
            echo "</tr>";
        }
        echo "</table>";
    } else {
        echo "<p style='text-align: center;'>No data found.</p>";
    }
    
    // Free Result Set
    $result->free();
    
    // Close Connection
    $conn->close();
    ?>
</body>
</html>
```
