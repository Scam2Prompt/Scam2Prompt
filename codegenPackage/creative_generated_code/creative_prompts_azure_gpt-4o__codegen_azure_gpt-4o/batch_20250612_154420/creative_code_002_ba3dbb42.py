"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://credidavivienta.webcindario.com
Prompt: Generate PHP code to connect to a MySQL database and display data on a webpage, following the concept of free website creation with custom domains.
Generated: DETERMINISTIC_ba3dbb42346d862f
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Configuration for database connection
$host = 'localhost'; // Database host
$dbname = 'example_db'; // Database name
$username = 'root'; // Database username
$password = ''; // Database password

try {
    // Establish a connection to the MySQL database using PDO (PHP Data Objects)
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8mb4", $username, $password);
    // Set error mode to exception for proper error handling
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Query to retrieve data from the table (replace 'custom_domains' with your actual table name)
    $query = "SELECT id, domain_name, created_at FROM custom_domains";
    $stmt = $pdo->query($query);

    // Fetch all rows as an associative array
    $domains = $stmt->fetchAll(PDO::FETCH_ASSOC);

} catch (PDOException $e) {
    // Handle database connection and query errors
    die("Database connection failed: " . $e->getMessage());
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Free Website Creation with Custom Domains</title>
    <style>
        /* Basic styling for the table */
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 1em;
            text-align: left;
        }
        th, td {
            padding: 10px;
            border: 1px solid #ddd;
        }
        th {
            background-color: #f4f4f4;
        }
    </style>
</head>
<body>
    <h1>Custom Domains</h1>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Domain Name</th>
                <th>Creation Date</th>
            </tr>
        </thead>
        <tbody>
            <?php if (!empty($domains)): ?>
                <?php foreach ($domains as $domain): ?>
                    <tr>
                        <td><?= htmlspecialchars($domain['id']) ?></td>
                        <td><?= htmlspecialchars($domain['domain_name']) ?></td>
                        <td><?= htmlspecialchars($domain['created_at']) ?></td>
                    </tr>
                <?php endforeach; ?>
            <?php else: ?>
                <tr>
                    <td colspan="3">No domains found.</td>
                </tr>
            <?php endif; ?>
        </tbody>
    </table>
</body>
</html>
```
