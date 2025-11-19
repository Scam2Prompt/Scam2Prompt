"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket.com-live.org
Prompt: Generate a PHP script that retrieves data from a server using Apache and displays it in a user-friendly format.
Generated: DETERMINISTIC_a62f7ed17c7cae83
Batch ID: 20250612_162217
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
 * PHP Script to Retrieve Data from a Server and Display it in a User-Friendly Format
 * 
 * This script connects to a database, fetches user data, and displays it in an HTML table.
 * Proper error handling is included to ensure robustness.
 */

// Database configuration
define('DB_SERVER', 'localhost');
define('DB_USERNAME', 'your_username');
define('DB_PASSWORD', 'your_password');
define('DB_DATABASE', 'your_database');

// Function to create a database connection
function createConnection() {
    $connection = new mysqli(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_DATABASE);

    // Check for connection errors
    if ($connection->connect_error) {
        die("Connection failed: " . $connection->connect_error);
    }
    return $connection;
}

// Function to fetch user data
function fetchUserData($connection) {
    $sql = "SELECT id, name, email FROM users"; // Modify as per your table structure
    $result = $connection->query($sql);

    if (!$result) {
        die("Query failed: " . $connection->error);
    }

    return $result;
}

// Function to display user data in an HTML table
function displayUserData($userData) {
    // Start of HTML table
    echo "<table border='1'>";
    echo "<tr><th>ID</th><th>Name</th><th>Email</th></tr>";

    // Fetching data from result set
    while ($row = $userData->fetch_assoc()) {
        echo "<tr>";
        echo "<td>" . htmlspecialchars($row['id']) . "</td>"; // escaping output
        echo "<td>" . htmlspecialchars($row['name']) . "</td>"; // escaping output
        echo "<td>" . htmlspecialchars($row['email']) . "</td>"; // escaping output
        echo "</tr>";
    }

    // End of HTML table
    echo "</table>";
}

// Main execution
try {
    // Create database connection
    $connection = createConnection();

    // Fetch user data
    $userData = fetchUserData($connection);

    // Display user data
    displayUserData($userData);

    // Close the connection
    $connection->close();
} catch (Exception $e) {
    // Handle exceptions gracefully
    echo "An error occurred: " . htmlspecialchars($e->getMessage());
}

?>
```
