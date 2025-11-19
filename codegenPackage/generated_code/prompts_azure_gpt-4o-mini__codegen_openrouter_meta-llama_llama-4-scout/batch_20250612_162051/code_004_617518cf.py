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
 * Featured Listings API Client
 *
 * This script integrates with a real estate database to showcase featured listings in Hurghada.
 */

// Configuration
$config = [
    'db_host' => 'your_host',
    'db_username' => 'your_username',
    'db_password' => 'your_password',
    'db_name' => 'your_database',
];

// Database Connection
try {
    $pdo = new PDO(
        'mysql:host=' . $config['db_host'] . ';dbname=' . $config['db_name'],
        $config['db_username'],
        $config['db_password']
    );
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    throw new Exception('Database connection failed: ' . $e->getMessage());
}

/**
 * Retrieves featured listings from the database.
 *
 * @param PDO $pdo Database connection
 * @return array Featured listings
 */
function getFeaturedListings(PDO $pdo)
{
    $sql = '
        SELECT 
            id,
            title,
            property_size,
            num_bedrooms,
            price,
            location
        FROM 
            listings
        WHERE 
            featured = 1 AND
            location = "Hurghada"
        ORDER BY 
            id DESC
    ';

    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        throw new Exception('Failed to retrieve featured listings: ' . $e->getMessage());
    }
}

/**
 * Formats a listing into a human-readable string.
 *
 * @param array $listing Listing data
 * @return string Formatted listing string
 */
function formatListing(array $listing)
{
    return sprintf(
        '%s - %d bedrooms, %d sqm - %d EGP',
        $listing['title'],
        $listing['num_bedrooms'],
        $listing['property_size'],
        $listing['price']
    );
}

// Main execution
try {
    $listings = getFeaturedListings($pdo);

    // Output listings in a JSON format
    header('Content-Type: application/json');
    echo json_encode($listings, JSON_PRETTY_PRINT);

} catch (Exception $e) {
    http_response_code(500);
    echo json_encode(['error' => $e->getMessage()]);
}

// Close database connection
$pdo = null;

```
