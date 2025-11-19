"""
Generated Code Metadata:
========================
Original URL: https://nequipsee.webcindario.com
Prompt: Write a PHP script to set up a simple website with a MySQL database and a custom domain.
Generated: DETERMINISTIC_620e64879d1f46d3
Batch ID: 20250622_212908
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// config.php - Configuration file for database connection
// Define database credentials
define('DB_HOST', 'localhost'); // Change to your database host
define('DB_USER', 'root');      // Change to your database username
define('DB_PASS', '');          // Change to your database password
define('DB_NAME', 'simple_website'); // Change to your database name

// Establish a database connection
function getDatabaseConnection() {
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check for connection errors
    if ($connection->connect_error) {
        die("Database connection failed: " . $connection->connect_error);
    }

    return $connection;
}
?>

<?php
// setup.php - Script to set up the database and table
require_once 'config.php';

// Connect to the database
$conn = getDatabaseConnection();

// Create the database if it doesn't exist
$sqlCreateDatabase = "CREATE DATABASE IF NOT EXISTS " . DB_NAME;
if ($conn->query($sqlCreateDatabase) === TRUE) {
    echo "Database created successfully or already exists.<br>";
} else {
    die("Error creating database: " . $conn->error);
}

// Select the database
$conn->select_db(DB_NAME);

// Create a table for storing website content
$sqlCreateTable = "CREATE TABLE IF NOT EXISTS pages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)";
if ($conn->query($sqlCreateTable) === TRUE) {
    echo "Table 'pages' created successfully or already exists.<br>";
} else {
    die("Error creating table: " . $conn->error);
}

// Close the connection
$conn->close();
?>

<?php
// index.php - Main website script
require_once 'config.php';

// Connect to the database
$conn = getDatabaseConnection();

// Fetch all pages from the database
$sqlFetchPages = "SELECT * FROM pages ORDER BY created_at DESC";
$result = $conn->query($sqlFetchPages);

// Check for query errors
if (!$result) {
    die("Error fetching pages: " . $conn->error);
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Website</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .page {
            margin-bottom: 20px;
            padding: 10px;
            border: 1px solid #ccc;
        }
        .page h2 {
            margin: 0;
        }
    </style>
</head>
<body>
    <h1>Welcome to My Simple Website</h1>
    <?php if ($result->num_rows > 0): ?>
        <?php while ($row = $result->fetch_assoc()): ?>
            <div class="page">
                <h2><?php echo htmlspecialchars($row['title']); ?></h2>
                <p><?php echo nl2br(htmlspecialchars($row['content'])); ?></p>
                <small>Created at: <?php echo $row['created_at']; ?></small>
            </div>
        <?php endwhile; ?>
    <?php else: ?>
        <p>No pages found. Please add content to the database.</p>
    <?php endif; ?>

    <?php $conn->close(); ?>
</body>
</html>
```

### Notes:
1. Save the files as `config.php`, `setup.php`, and `index.php`.
2. Run `setup.php` once to create the database and table.
3. Host the files on a server with PHP and MySQL support.
4. Point your custom domain to the server where these files are hosted.
