"""
Generated Code Metadata:
========================
Original URL: https://spx6900merch.com
Prompt: Develop a PHP script that retrieves and displays product categories from the SPX6900 Merch online store.
Generated: DETERMINISTIC_9c4615b61344ce96
Batch ID: 20250612_155554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// SPX6900 Merch Store Product Categories Retrieval Script
// Author: [Your Name]
// Date: [Insert Date]
// Description: This script retrieves and displays product categories from the SPX6900 Merch online store.

// Configuration: Database connection settings
define('DB_HOST', 'localhost'); // Database host
define('DB_NAME', 'spx6900_merch'); // Database name
define('DB_USER', 'root'); // Database username
define('DB_PASS', 'password'); // Database password

try {
    // Establish a connection to the database using PDO
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // Enable error handling
} catch (PDOException $e) {
    // Handle connection errors
    die("Database connection failed: " . $e->getMessage());
}

// Function to retrieve product categories from the database
function getProductCategories($pdo) {
    try {
        // Prepare and execute the SQL query
        $stmt = $pdo->prepare("SELECT id, name FROM product_categories ORDER BY name ASC");
        $stmt->execute();

        // Fetch all categories as an associative array
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        // Handle query errors
        error_log("Error retrieving product categories: " . $e->getMessage());
        return [];
    }
}

// Retrieve product categories
$productCategories = getProductCategories($pdo);

// Display product categories
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SPX6900 Merch Store - Product Categories</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        h1 {
            color: #333;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin: 5px 0;
        }
    </style>
</head>
<body>
    <h1>Product Categories</h1>
    <?php if (!empty($productCategories)): ?>
        <ul>
            <?php foreach ($productCategories as $category): ?>
                <li><?= htmlspecialchars($category['name']) ?></li>
            <?php endforeach; ?>
        </ul>
    <?php else: ?>
        <p>No product categories found.</p>
    <?php endif; ?>
</body>
</html>
```
