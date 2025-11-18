"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sunnyhurghada.com
Prompt: Create a PHP function to calculate the total number of properties available for sale and rent in Hurghada, categorized by type (e.g., apartment, shop, villa).
Generated: DETERMINISTIC_b2de29b1709bfa6a
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
 * Function to calculate the total number of properties available for sale and rent in Hurghada,
 * categorized by type (e.g., apartment, shop, villa).
 *
 * @param PDO $dbConnection A PDO database connection object.
 * @return array An associative array with the count of properties categorized by type for sale and rent.
 * [
 *   'sale' => ['apartment' => X, 'shop' => Y, 'villa' => Z],
 *   'rent' => ['apartment' => A, 'shop' => B, 'villa' => C]
 * ]
 * @throws Exception if there is an error fetching data from the database.
 */
function getPropertyCounts(PDO $dbConnection): array
{
    try {
        // Query to count properties for sale categorized by type
        $saleQuery = "SELECT type, COUNT(*) AS count 
                      FROM properties 
                      WHERE location = 'Hurghada' AND availability = 'sale' 
                      GROUP BY type";
        
        // Query to count properties for rent categorized by type
        $rentQuery = "SELECT type, COUNT(*) AS count 
                      FROM properties 
                      WHERE location = 'Hurghada' AND availability = 'rent' 
                      GROUP BY type";

        // Initialize result array
        $result = [
            'sale' => [],
            'rent' => []
        ];

        // Execute sale query and populate result array
        $saleStmt = $dbConnection->prepare($saleQuery);
        $saleStmt->execute();
        while ($row = $saleStmt->fetch(PDO::FETCH_ASSOC)) {
            $result['sale'][$row['type']] = (int)$row['count'];
        }

        // Execute rent query and populate result array
        $rentStmt = $dbConnection->prepare($rentQuery);
        $rentStmt->execute();
        while ($row = $rentStmt->fetch(PDO::FETCH_ASSOC)) {
            $result['rent'][$row['type']] = (int)$row['count'];
        }

        return $result;

    } catch (PDOException $e) {
        // Handle database errors
        throw new Exception("Database error: " . $e->getMessage());
    } catch (Exception $e) {
        // Handle general errors
        throw new Exception("Error: " . $e->getMessage());
    }
}

// Example Usage:
// Assuming $pdo is a valid PDO instance connected to the database
/*
try {
    $propertyCounts = getPropertyCounts($pdo);
    print_r($propertyCounts);
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
*/
```
