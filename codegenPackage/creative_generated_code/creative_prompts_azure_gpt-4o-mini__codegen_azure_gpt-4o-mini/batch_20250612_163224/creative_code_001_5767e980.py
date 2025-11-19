"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://selinaphantom.github.io
Prompt: Write a PHP script that connects to a MySQL database for a shopping website project mentioned on 蘇李冠穎's site.
Generated: DETERMINISTIC_5767e980ea9a5f13
Batch ID: 20250612_163224
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
 * Database connection script for shopping website project.
 * This script connects to a MySQL database using PDO.
 * It includes error handling and uses prepared statements for security.
 */

// Database configuration
$host = 'localhost';  // Database host
$db   = 'shopping_db'; // Database name
$user = 'username';    // Database username
$pass = 'password';    // Database password
$charset = 'utf8mb4';  // Character set

// Data Source Name
$dsn = "mysql:host=$host;dbname=$db;charset=$charset";

// PDO options
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION, // Exception handling for errors
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,       // Set default fetch mode to associative array
    PDO::ATTR_EMULATE_PREPARES   => false,                  // Disable emulation of prepared statements
];

try {
    // Create a new PDO instance
    $pdo = new PDO($dsn, $user, $pass, $options);
    echo "Database connection successful."; // Connection success message (for debugging)
} catch (\PDOException $e) {
    // Handle connection error
    echo "Database connection failed: " . $e->getMessage(); // Display error message
    exit; // Exit the script in case of a connection failure
}

// Example function to fetch products from the database
/**
 * Fetch all products from the database.
 *
 * @param PDO $pdo The PDO instance for database connection.
 * @return array List of products.
 */
function fetchProducts($pdo) {
    $query = "SELECT * FROM products"; // SQL query to select all products

    try {
        $stmt = $pdo->query($query); // Execute the query
        return $stmt->fetchAll(); // Fetch all products as an associative array
    } catch (\PDOException $e) {
        // Handle query error
        echo "Query error: " . $e->getMessage(); // Display error message
        return []; // Return an empty array in case of error
    }
}

// Example usage
$products = fetchProducts($pdo);
foreach ($products as $product) {
    echo "Product ID: " . $product['id'] . "<br>";
    echo "Product Name: " . $product['name'] . "<br>";
    echo "Price: $" . $product['price'] . "<br><br>";
}

// Close the connection (optional, but good practice)
$pdo = null;
?>
```
