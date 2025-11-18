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
/**
 * Database connection script
 * This script connects to a MySQL database and displays data on a webpage.
 * Adjust the database connection parameters accordingly.
 */

// Database connection parameters
$host = 'localhost'; // Database host
$db_name = 'your_database_name'; // Database name
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$host;dbname=$db_name;charset=utf8", $username, $password);
    
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // SQL query to select data from a table (replace 'your_table_name' with actual table name)
    $sql = "SELECT * FROM your_table_name";
    $stmt = $pdo->prepare($sql);
    $stmt->execute();

    // Fetching all rows from the result set
    $data = $stmt->fetchAll(PDO::FETCH_ASSOC);

} catch (PDOException $e) {
    // Handle connection errors
    echo "Connection failed: " . $e->getMessage();
    exit; // Exit the script if the connection fails
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Database Data Display</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>

<h1>Data from Database</h1>

<?php if (!empty($data)): ?>
    <table>
        <thead>
            <tr>
                <?php foreach (array_keys($data[0]) as $header): ?>
                    <th><?php echo htmlspecialchars($header); ?></th>
                <?php endforeach; ?>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($data as $row): ?>
                <tr>
                    <?php foreach ($row as $cell): ?>
                        <td><?php echo htmlspecialchars($cell); ?></td>
                    <?php endforeach; ?>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
<?php else: ?>
    <p>No data found.</p>
<?php endif; ?>

</body>
</html>
```
This PHP script connects to a MySQL database, retrieves data from a specified table, and displays it in an HTML table format. Make sure to replace the placeholder connection parameters and table name with actual values relevant to your database.
