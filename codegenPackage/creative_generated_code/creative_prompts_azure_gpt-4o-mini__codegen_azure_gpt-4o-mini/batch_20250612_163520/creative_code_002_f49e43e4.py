"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://armaghanenajaf.org
Prompt: Create a PHP code snippet that displays the latest reports from Armaghan-e-Najaf's media department on a webpage.
Generated: DETERMINISTIC_f49e43e4d4cbf3e1
Batch ID: 20250612_163520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Enable error reporting for development (remove in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Database configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'armaghan_db');
define('DB_USER', 'username'); // Update with your database username
define('DB_PASS', 'password'); // Update with your database password

/**
 * Establish a connection to the database.
 * 
 * @return PDO|null Returns the PDO object or null on failure.
 */
function getDatabaseConnection() {
    try {
        $dsn = "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME . ";charset=utf8mb4";
        $options = [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            PDO::ATTR_EMULATE_PREPARES => false,
        ];
        return new PDO($dsn, DB_USER, DB_PASS, $options);
    } catch (PDOException $e) {
        // Handle connection error
        error_log('Database connection error: ' . $e->getMessage());
        return null;
    }
}

/**
 * Fetch the latest reports from the media department.
 * 
 * @param PDO $pdo The database connection object.
 * @return array Returns an array of latest reports.
 */
function fetchLatestReports($pdo) {
    $sql = "SELECT title, content, created_at FROM reports ORDER BY created_at DESC LIMIT 5";
    try {
        $stmt = $pdo->query($sql);
        return $stmt->fetchAll();
    } catch (PDOException $e) {
        // Handle query error
        error_log('Query error: ' . $e->getMessage());
        return [];
    }
}

// Main execution
$pdo = getDatabaseConnection();
$reports = [];

if ($pdo) {
    $reports = fetchLatestReports($pdo);
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Latest Reports - Armaghan-e-Najaf</title>
    <link rel="stylesheet" href="styles.css"> <!-- Optional CSS file -->
</head>
<body>
    <h1>Latest Reports from Armaghan-e-Najaf Media Department</h1>
    <?php if (!empty($reports)): ?>
        <ul>
            <?php foreach ($reports as $report): ?>
                <li>
                    <h2><?php echo htmlspecialchars($report['title']); ?></h2>
                    <p><?php echo nl2br(htmlspecialchars($report['content'])); ?></p>
                    <small>Published on: <?php echo htmlspecialchars($report['created_at']); ?></small>
                </li>
            <?php endforeach; ?>
        </ul>
    <?php else: ?>
        <p>No reports available at the moment.</p>
    <?php endif; ?>
</body>
</html>
```

Make sure to update the database credentials and adjust the SQL query according to your actual database schema. This code provides a basic structure for fetching and displaying reports while handling potential errors.
