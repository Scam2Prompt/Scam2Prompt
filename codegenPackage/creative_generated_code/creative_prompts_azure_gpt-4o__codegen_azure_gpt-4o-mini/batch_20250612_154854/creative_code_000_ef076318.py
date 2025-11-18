"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://2acnmzzlink.webcindario.com
Prompt: Write PHP code to create a simple webpage that connects to a MySQL database, referencing free hosting services like the one mentioned on "miarroba.com."
Generated: DETERMINISTIC_ef07631889aa7d5d
Batch ID: 20250612_154854
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
$host = 'your_host'; // e.g. 'localhost' or 'db.miarroba.com'
$dbname = 'your_database'; // Your database name
$username = 'your_username'; // Your database username
$password = 'your_password'; // Your database password

// Establish a connection to the MySQL database using PDO
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection errors and output a user-friendly message
    die("Connection failed: " . $e->getMessage());
}

// Function to fetch data from the database
function fetchData($pdo) {
    try {
        $stmt = $pdo->query("SELECT * FROM your_table"); // Replace 'your_table' with your actual table name
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        // Handle query errors
        die("Query failed: " . $e->getMessage());
    }
}

// Fetch data from the database
$data = fetchData($pdo);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Webpage with MySQL Connection</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to an external stylesheet if needed -->
</head>
<body>
    <h1>Data from MySQL Database</h1>
    <?php if ($data): ?>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Email</th>
                    <!-- Add more columns as needed -->
                </tr>
            </thead>
            <tbody>
                <?php foreach ($data as $row): ?>
                    <tr>
                        <td><?php echo htmlspecialchars($row['id']); ?></td>
                        <td><?php echo htmlspecialchars($row['name']); ?></td>
                        <td><?php echo htmlspecialchars($row['email']); ?></td>
                        <!-- Add more columns as needed -->
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    <?php else: ?>
        <p>No data found.</p>
    <?php endif; ?>
</body>
</html>

<?php
// Close the database connection
$pdo = null;
?>
```

**Note:** Replace `your_host`, `your_database`, `your_username`, `your_password`, and `your_table` with actual values corresponding to your database setup.
