"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grupo-virtual.webcindario.com
Prompt: Write PHP code to set up a basic website with MySQL database integration, referencing free hosting options similar to miarroba.com.
Generated: DETERMINISTIC_6298626be6e02c98
Batch ID: 20250612_154740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Enable error reporting for debugging purposes during development (disable in production)
ini_set('display_errors', 1);
error_reporting(E_ALL);

// Database configuration
$db_host = "localhost"; // Change to your MySQL host (e.g., provided by free hosting service)
$db_user = "root";      // Change to your MySQL username
$db_password = "";      // Change to your MySQL password
$db_name = "my_database"; // Change to your MySQL database name

// Establish database connection
$conn = new mysqli($db_host, $db_user, $db_password, $db_name);

// Check for connection errors
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Create a table if it doesn't exist
$sql_create_table = "
CREATE TABLE IF NOT EXISTS visitors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    visit_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)";
if (!$conn->query($sql_create_table)) {
    die("Error creating table: " . $conn->error);
}

// Insert visitor data into the table (example static data for demonstration)
$name = "John Doe";
$email = "john.doe@example.com";

$sql_insert_data = $conn->prepare("INSERT INTO visitors (name, email) VALUES (?, ?)");
$sql_insert_data->bind_param("ss", $name, $email);

if (!$sql_insert_data->execute()) {
    die("Error inserting data: " . $sql_insert_data->error);
}

// Fetch all records from the table
$sql_fetch_data = "SELECT * FROM visitors";
$result = $conn->query($sql_fetch_data);
if ($result === false) {
    die("Error querying data: " . $conn->error);
}

// HTML page to display the visitor data
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Basic Website</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ccc;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f4f4f4;
        }
    </style>
</head>
<body>
    <h1>Welcome to My Basic Website</h1>
    <h2>Visitor List</h2>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Email</th>
                <th>Visit Date</th>
            </tr>
        </thead>
        <tbody>
            <?php
            // Iterate through the results and display in the table
            if ($result->num_rows > 0) {
                while ($row = $result->fetch_assoc()) {
                    echo "<tr>";
                    echo "<td>" . htmlspecialchars($row['id']) . "</td>";
                    echo "<td>" . htmlspecialchars($row['name']) . "</td>";
                    echo "<td>" . htmlspecialchars($row['email']) . "</td>";
                    echo "<td>" . htmlspecialchars($row['visit_date']) . "</td>";
                    echo "</tr>";
                }
            } else {
                echo "<tr><td colspan='4'>No visitors found.</td></tr>";
            }
            ?>
        </tbody>
    </table>
</body>
</html>

<?php
// Close the database connection
$conn->close();
?>
```
