"""
Generated Code Metadata:
========================
Original URL: https://sunnyhurghada.com
Prompt: Write a PHP script that integrates with a real estate database to showcase featured listings in Hurghada, including details like property size and number of bedrooms, as described on Sunny Hurghada's webpage.
Generated: DETERMINISTIC_617518cfb1ef2d4c
Batch ID: 20250612_162051
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
 * Featured Listings for Hurghada
 * 
 * This script retrieves and displays featured real estate listings from a database,
 * showcasing properties in Hurghada with details like property size and bedrooms.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'username');
define('DB_PASS', 'password');
define('DB_NAME', 'real_estate_db');

/**
 * Establishes a database connection
 * 
 * @return PDO|false Returns PDO connection object or false on failure
 */
function connectToDatabase() {
    try {
        $dsn = "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME . ";charset=utf8mb4";
        $options = [
            PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            PDO::ATTR_EMULATE_PREPARES   => false,
        ];
        return new PDO($dsn, DB_USER, DB_PASS, $options);
    } catch (PDOException $e) {
        error_log("Database connection failed: " . $e->getMessage());
        return false;
    }
}

/**
 * Retrieves featured listings from the database
 * 
 * @param PDO $pdo Database connection object
 * @return array Array of featured listings or empty array on failure
 */
function getFeaturedListings(PDO $pdo) {
    try {
        $stmt = $pdo->prepare("
            SELECT 
                id, title, description, price, size_sqm, bedrooms, 
                bathrooms, location, featured_image, date_added
            FROM properties
            WHERE 
                location = 'Hurghada' 
                AND is_featured = 1
                AND is_active = 1
            ORDER BY date_added DESC
            LIMIT 10
        ");
        $stmt->execute();
        return $stmt->fetchAll();
    } catch (PDOException $e) {
        error_log("Error fetching featured listings: " . $e->getMessage());
        return [];
    }
}

/**
 * Displays the featured listings in HTML format
 * 
 * @param array $listings Array of property listings
 */
function displayFeaturedListings(array $listings) {
    if (empty($listings)) {
        echo '<div class="alert alert-info">No featured listings available at the moment.</div>';
        return;
    }

    foreach ($listings as $listing) {
        echo '<div class="property-listing">';
        echo '<h3>' . htmlspecialchars($listing['title']) . '</h3>';
        
        if (!empty($listing['featured_image'])) {
            echo '<img src="' . htmlspecialchars($listing['featured_image']) . '" alt="' . htmlspecialchars($listing['title']) . '" class="property-image">';
        }
        
        echo '<div class="property-details">';
        echo '<p><strong>Location:</strong> ' . htmlspecialchars($listing['location']) . '</p>';
        echo '<p><strong>Price:</strong> $' . number_format($listing['price'], 2) . '</p>';
        echo '<p><strong>Size:</strong> ' . htmlspecialchars($listing['size_sqm']) . ' sqm</p>';
        echo '<p><strong>Bedrooms:</strong> ' . htmlspecialchars($listing['bedrooms']) . '</p>';
        echo '<p><strong>Bathrooms:</strong> ' . htmlspecialchars($listing['bathrooms']) . '</p>';
        echo '<p>' . htmlspecialchars($listing['description']) . '</p>';
        echo '</div>';
        echo '</div>';
    }
}

// Main execution
$pdo = connectToDatabase();
if ($pdo === false) {
    die("We're experiencing technical difficulties. Please try again later.");
}

$featuredListings = getFeaturedListings($pdo);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Featured Properties in Hurghada</title>
    <style>
        .property-listing {
            border: 1px solid #ddd;
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 5px;
        }
        .property-image {
            max-width: 100%;
            height: auto;
            margin-bottom: 10px;
        }
        .property-details {
            margin-top: 10px;
        }
        .alert {
            padding: 15px;
            background-color: #f8f9fa;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <h1>Featured Properties in Hurghada</h1>
    <?php displayFeaturedListings($featuredListings); ?>
</body>
</html>
```
