"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.stellarviewrealty.com
Prompt: Create a PHP API that connects to StellarView Realty's database to fetch real estate listings in El Poblado, including details like price and number of bedrooms.
Generated: DETERMINISTIC_039925e9b6424109
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

// Enable error reporting for debugging (disable in production)
ini_set('display_errors', 1);
error_reporting(E_ALL);

// Define constants for database connection
define('DB_HOST', 'your-database-host'); // Replace with your database host
define('DB_NAME', 'stellarview_realty'); // Replace with your database name
define('DB_USER', 'your-database-username'); // Replace with your database username
define('DB_PASS', 'your-database-password'); // Replace with your database password

// Set the content type to JSON for API responses
header('Content-Type: application/json');

/**
 * Connect to the database.
 *
 * @return PDO Returns a PDO connection object.
 * @throws Exception Throws an exception if the connection fails.
 */
function connectToDatabase()
{
    try {
        $dsn = 'mysql:host=' . DB_HOST . ';dbname=' . DB_NAME . ';charset=utf8';
        $pdo = new PDO($dsn, DB_USER, DB_PASS);
        // Set PDO error mode to exception for better error handling
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (Exception $e) {
        // Return a JSON error response if the connection fails
        http_response_code(500);
        echo json_encode(['error' => 'Failed to connect to the database: ' . $e->getMessage()]);
        exit;
    }
}

/**
 * Fetch real estate listings in El Poblado.
 *
 * @param PDO $pdo The PDO database connection object.
 * @return array Returns an array of listings.
 */
function fetchRealEstateListings($pdo)
{
    try {
        // Prepare the SQL query to fetch real estate listings
        $sql = "SELECT id, title, price, bedrooms, description 
                FROM listings 
                WHERE location = :location";
        $stmt = $pdo->prepare($sql);
        // Bind the location parameter to the query
        $stmt->bindValue(':location', 'El Poblado', PDO::PARAM_STR);
        $stmt->execute();
        // Fetch all listings as an associative array
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (Exception $e) {
        // Return a JSON error response if the query fails
        http_response_code(500);
        echo json_encode(['error' => 'Failed to fetch listings: ' . $e->getMessage()]);
        exit;
    }
}

// Main API logic
try {
    // Connect to the database
    $pdo = connectToDatabase();
    // Fetch listings in El Poblado
    $listings = fetchRealEstateListings($pdo);
    // Return the listings as a JSON response
    echo json_encode(['success' => true, 'listings' => $listings]);
} catch (Exception $e) {
    // Catch any unexpected errors and return a JSON error response
    http_response_code(500);
    echo json_encode(['error' => 'An unexpected error occurred: ' . $e->getMessage()]);
}

?>
```
