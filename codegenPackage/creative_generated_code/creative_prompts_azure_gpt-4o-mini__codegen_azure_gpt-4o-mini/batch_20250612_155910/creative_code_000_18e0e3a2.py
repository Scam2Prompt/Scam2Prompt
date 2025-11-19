"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ct.ws
Prompt: How can I create a free website using the ct.ws domain with InfinityFree, and what are the steps for setting up PHP and MySQL?
Generated: DETERMINISTIC_18e0e3a279821a61
Batch ID: 20250612_155910
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
 * This PHP script demonstrates a basic setup for connecting to a MySQL database
 * and displaying a welcome message on a website hosted with InfinityFree
 * using the ct.ws domain.
 */

// Database configuration
define('DB_HOST', 'sql213.epizy.com'); // Your database host
define('DB_USER', 'epiz_XXXXXX'); // Your database username
define('DB_PASS', 'your_password'); // Your database password
define('DB_NAME', 'epiz_XXXXXX_db'); // Your database name

/**
 * Create a connection to the MySQL database
 * 
 * @return mysqli $conn The connection object
 * @throws Exception If connection fails
 */
function connectDatabase() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check for connection errors
    if ($conn->connect_error) {
        throw new Exception('Database connection failed: ' . $conn->connect_error);
    }

    return $conn;
}

/**
 * Fetch welcome message from the database
 *
 * @param mysqli $conn The connection object
 * @return string Welcome message
 */
function fetchWelcomeMessage($conn) {
    $query = "SELECT message FROM welcome_messages LIMIT 1"; // Fetch one message
    $result = $conn->query($query);

    if ($result === false) {
        throw new Exception('Query error: ' . $conn->error);
    }

    $row = $result->fetch_assoc();
    return $row ? $row['message'] : 'Welcome to my website!';
}

/**
 * Main execution block
 */
try {
    // Establish database connection
    $connection = connectDatabase();

    // Fetch welcome message
    $welcomeMessage = fetchWelcomeMessage($connection);

    // Close the connection
    $connection->close();

} catch (Exception $e) {
    // Handle exceptions and display an error message
    $welcomeMessage = 'Error: ' . $e->getMessage();
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Free Website</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to CSS for styling -->
</head>
<body>
    <h1><?php echo htmlspecialchars($welcomeMessage); ?></h1> <!-- Display the welcome message -->
</body>
</html>
```
