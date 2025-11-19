"""
Generated Code Metadata:
========================
Original URL: https://credidavivienta.webcindario.com
Prompt: Generate PHP code to connect to a MySQL database and display data on a webpage, following the concept of free website creation with custom domains.
Generated: DETERMINISTIC_ba3dbb42346d862f
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Database connection and data display script for a free website creation service.
 * 
 * This script connects to a MySQL database, fetches website data, and displays it on a webpage.
 * It includes error handling and follows security best practices.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'username');
define('DB_PASS', 'password');
define('DB_NAME', 'website_creator');
define('DB_PORT', 3306);

// Error reporting for development (should be disabled in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Start session for user authentication if needed
session_start();

/**
 * Establishes a connection to the MySQL database.
 * 
 * @return PDO Returns a PDO database connection object
 * @throws PDOException If connection fails
 */
function connectToDatabase() {
    try {
        $dsn = "mysql:host=" . DB_HOST . ";port=" . DB_PORT . ";dbname=" . DB_NAME . ";charset=utf8mb4";
        $options = [
            PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            PDO::ATTR_EMULATE_PREPARES   => false,
        ];
        
        return new PDO($dsn, DB_USER, DB_PASS, $options);
    } catch (PDOException $e) {
        // Log the error and display a user-friendly message
        error_log("Database connection failed: " . $e->getMessage());
        die("We're experiencing technical difficulties. Please try again later.");
    }
}

/**
 * Fetches website data from the database.
 * 
 * @param PDO $pdo Database connection object
 * @return array Array of website data
 */
function fetchWebsiteData(PDO $pdo) {
    try {
        $stmt = $pdo->prepare("SELECT id, domain_name, owner_email, creation_date, status FROM websites ORDER BY creation_date DESC");
        $stmt->execute();
        return $stmt->fetchAll();
    } catch (PDOException $e) {
        error_log("Error fetching website data: " . $e->getMessage());
        return [];
    }
}

/**
 * Sanitizes output to prevent XSS attacks.
 * 
 * @param string $data The data to be sanitized
 * @return string Sanitized data
 */
function sanitizeOutput($data) {
    return htmlspecialchars($data, ENT_QUOTES, 'UTF-8');
}

// Main execution
try {
    $pdo = connectToDatabase();
    $websites = fetchWebsiteData($pdo);
} catch (Exception $e) {
    // Handle any unexpected errors
    error_log("Unexpected error: " . $e->getMessage());
    die("An unexpected error occurred. Our team has been notified.");
}

// HTML output
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Free Website Creator - Custom Domains</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        h1 {
            color: #2c3e50;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        th {
            background-color: #f2f2f2;
        }
        tr:hover {
            background-color: #f5f5f5;
        }
        .status-active {
            color: green;
        }
        .status-inactive {
            color: red;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Free Website Creator - Custom Domains</h1>
        
        <?php if (!empty($websites)): ?>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Domain Name</th>
                        <th>Owner Email</th>
                        <th>Creation Date</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    <?php foreach ($websites as $website): ?>
                        <tr>
                            <td><?php echo sanitizeOutput($website['id']); ?></td>
                            <td><?php echo sanitizeOutput($website['domain_name']); ?></td>
                            <td><?php echo sanitizeOutput($website['owner_email']); ?></td>
                            <td><?php echo sanitizeOutput($website['creation_date']); ?></td>
                            <td class="status-<?php echo strtolower(sanitizeOutput($website['status'])); ?>">
                                <?php echo sanitizeOutput($website['status']); ?>
                            </td>
                        </tr>
                    <?php endforeach; ?>
                </tbody>
            </table>
        <?php else: ?>
            <p>No websites found in the database.</p>
        <?php endif; ?>
    </div>
</body>
</html>
```
