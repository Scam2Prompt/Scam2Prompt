"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://therealrathore.in
Prompt: Write a PHP script to connect to a MySQL database for an e-commerce site, utilizing the technical skills highlighted in Ketan Rathod's portfolio.
Generated: DETERMINISTIC_457acbb3713a4867
Batch ID: 20250612_164151
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
$db_host = 'localhost'; // The hostname of the database server
$db_user = 'your_username'; // Database username
$db_password = 'your_password'; // Database password
$db_name = 'ecommerce_db'; // The name of the database to connect to

/**
 * Establishes a connection to the MySQL database.
 *
 * @return mysqli|null Returns a mysqli connection object on success, or null on failure.
 */
function connectToDatabase() {
    global $db_host, $db_user, $db_password, $db_name;

    // Create a connection
    $connection = new mysqli($db_host, $db_user, $db_password, $db_name);

    // Check for connection errors
    if ($connection->connect_error) {
        // Log the error and exit gracefully
        error_log('Database connection error: ' . $connection->connect_error);
        return null;
    }

    return $connection;
}

/**
 * Closes the database connection.
 *
 * @param mysqli $connection The mysqli connection object to be closed.
 */
function closeDatabaseConnection($connection) {
    if ($connection) {
        $connection->close();
    }
}

// Main execution
$connection = connectToDatabase();

if ($connection) {
    // Perform database operations here

    // Sample query to fetch products
    $query = "SELECT * FROM products";
    if ($result = $connection->query($query)) {
        while ($row = $result->fetch_assoc()) {
            // Output each product's details
            echo "Product ID: " . $row['id'] . " - Name: " . $row['name'] . " - Price: " . $row['price'] . "<br>";
        }
        // Free the result set
        $result->free();
    } else {
        error_log('Query error: ' . $connection->error);
    }

    // Close the database connection
    closeDatabaseConnection($connection);
} else {
    echo "Failed to connect to the database.";
}
?>
```
