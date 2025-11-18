"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://watpac.in
Prompt: Write a script in PHP to fetch product details from a database for Watpac Chemicals Pvt Ltd, filtering items by categories such as "Primers" and "Specialty Coatings."
Generated: DETERMINISTIC_75040a5337c95772
Batch ID: 20250612_153224
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
 * Script to fetch product details from a database for Watpac Chemicals Pvt Ltd,
 * filtering items by categories such as "Primers" and "Specialty Coatings".
 */

/**
 * Database Configuration
 */
define('DB_HOST', 'localhost'); // Replace with your database host
define('DB_NAME', 'watpac_db'); // Replace with your database name
define('DB_USER', 'root');      // Replace with your database username
define('DB_PASS', '');          // Replace with your database password

/**
 * Connect to the database using PDO
 */
try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // Enable exceptions for errors
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Fetch product details filtered by category
 *
 * @param PDO $pdo The database connection object
 * @param array $categories List of categories to filter products
 * @return array Filtered product details
 */
function fetchProductsByCategory(PDO $pdo, array $categories): array {
    try {
        // Prepare SQL query with placeholders for categories
        $placeholders = str_repeat('?,', count($categories) - 1) . '?';
        $sql = "SELECT id, name, description, category, price 
                FROM products 
                WHERE category IN ($placeholders)";
        
        // Prepare and execute the statement
        $stmt = $pdo->prepare($sql);
        $stmt->execute($categories);

        // Fetch results as an associative array
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        error_log("Failed to fetch products: " . $e->getMessage());
        return []; // Return an empty array in case of error
    }
}

// Categories to filter
$categoriesToFilter = ['Primers', 'Specialty Coatings'];

// Fetch products
$filteredProducts = fetchProductsByCategory($pdo, $categoriesToFilter);

/**
 * Output the fetched product details
 */
header('Content-Type: application/json'); // Set response type as JSON
echo json_encode($filteredProducts, JSON_PRETTY_PRINT);

?>
```
