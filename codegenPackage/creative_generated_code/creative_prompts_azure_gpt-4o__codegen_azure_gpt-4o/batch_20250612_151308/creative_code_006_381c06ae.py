"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cancelar5-cambio.webcindario.com
Prompt: Create a PHP script to display data from a MySQL database on a webpage hosted on a free service like miarroba.com.
Generated: DETERMINISTIC_381c06aecdd3a96b
Batch ID: 20250612_151308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Display errors for debugging during development. Disable in production.
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

// Database configuration
define('DB_HOST', 'your_db_host'); // Replace with your database host, e.g., 'localhost'
define('DB_NAME', 'your_db_name'); // Replace with your database name
define('DB_USER', 'your_db_user'); // Replace with your database username
define('DB_PASS', 'your_db_password'); // Replace with your database password

try {
    // Establish a connection to the database using PDO
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    ]);

    // Query to fetch data from the database
    $query = "SELECT * FROM your_table_name"; // Replace 'your_table_name' with the actual table name
    $stmt = $pdo->prepare($query);
    $stmt->execute();
    $results = $stmt->fetchAll();

} catch (PDOException $e) {
    // Handle connection errors or PDO exceptions
    die("Database connection error: " . $e->getMessage());
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Display</title>
    <style>
        /* Basic styling for the table */
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f4f4f4;
        }
    </style>
</head>
<body>
    <h1>Data from Database</h1>

    <?php if ($results): ?>
        <!-- Display data in a table format -->
        <table>
            <thead>
                <tr>
                    <?php
                    // Output table headers dynamically based on column names
                    foreach (array_keys($results[0]) as $columnName) {
                        echo "<th>" . htmlspecialchars($columnName) . "</th>";
                    }
                    ?>
                </tr>
            </thead>
            <tbody>
                <?php
                // Output table rows dynamically based on fetched data
                foreach ($results as $row) {
                    echo "<tr>";
                    foreach ($row as $columnValue) {
                        echo "<td>" . htmlspecialchars($columnValue) . "</td>";
                    }
                    echo "</tr>";
                }
                ?>
            </tbody>
        </table>
    <?php else: ?>
        <p>No data found in the database.</p>
    <?php endif; ?>

</body>
</html>
```
