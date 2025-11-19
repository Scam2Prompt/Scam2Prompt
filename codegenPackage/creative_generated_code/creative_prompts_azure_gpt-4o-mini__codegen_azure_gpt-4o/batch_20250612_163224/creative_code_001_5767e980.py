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
// shopping_db.php

// Database configuration
define('DB_HOST', 'localhost');       // Database host
define('DB_NAME', 'shopping_db');     // Database name
define('DB_USER', 'root');            // Database username
define('DB_PASS', 'password');        // Database password

try {
    // Create a new PDO instance for connecting to the database
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, // Enable exceptions for errors
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC, // Fetch data as associative arrays
        PDO::ATTR_EMULATE_PREPARES => false, // Disable emulated prepared statements
    ]);

    // Connection successful
    echo "Database connection established successfully.";
} catch (PDOException $e) {
    // Handle connection errors
    error_log("Database connection error: " . $e->getMessage()); // Log the error
    die("Error connecting to the database. Please try again later."); // Show a user-friendly error message
}

// Example query - fetching all products
try {
    $query = "SELECT * FROM products"; // Replace 'products' with your table name
    $stmt = $pdo->query($query); // Execute the query

    // Fetch all rows from the products table
    $products = $stmt->fetchAll();

    // Output the products (for demonstration purposes)
    foreach ($products as $product) {
        echo "Product ID: " . htmlspecialchars($product['id']) . "<br>";
        echo "Name: " . htmlspecialchars($product['name']) . "<br>";
        echo "Price: " . htmlspecialchars($product['price']) . "<br><br>";
    }
} catch (PDOException $e) {
    // Handle query errors
    error_log("Query error: " . $e->getMessage()); // Log the error
    echo "An error occurred while fetching the products.";
}

// Close the PDO connection (optional, PDO will close when the script ends)
$pdo = null;
?>
```
