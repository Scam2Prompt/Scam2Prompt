"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pasionxlascasacas.com.uy
Prompt: Create a code snippet in PHP that connects to the Pasión X Las Casacas database to retrieve information about exclusive retro jerseys.
Generated: DETERMINISTIC_adaca34dc5036d1f
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

// Database connection parameters
$host = 'localhost';         // Database host
$dbName = 'pasion_x_casacas'; // Database name
$user = 'root';              // Database username
$password = '';              // Database password

try {
    // Create a PDO connection to the database
    $pdo = new PDO("mysql:host=$host;dbname=$dbName;charset=utf8", $user, $password);

    // Set error mode to exception to handle errors properly
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Prepare the SQL query to fetch exclusive retro jerseys information
    $query = "SELECT id, name, description, price, stock FROM retro_jerseys WHERE exclusive = 1";
    $stmt = $pdo->prepare($query);

    // Execute the query
    $stmt->execute();

    // Fetch all results as an associative array
    $results = $stmt->fetchAll(PDO::FETCH_ASSOC);

    // Check if results are found
    if (!empty($results)) {
        // Output data in a structured format (e.g., JSON)
        header('Content-Type: application/json');
        echo json_encode([
            'status' => 'success',
            'data' => $results
        ]);
    } else {
        // No results found
        echo json_encode([
            'status' => 'success',
            'message' => 'No exclusive retro jerseys found.'
        ]);
    }
} catch (PDOException $e) {
    // Handle database connection errors or query failures
    echo json_encode([
        'status' => 'error',
        'message' => 'Database error: ' . $e->getMessage()
    ]);
}

// Close the PDO connection (optional, as PHP will handle it automatically)
$pdo = null;

?>
```
