"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moraragora.com.br
Prompt: Create a code snippet in PHP that connects to a real estate database and retrieves information about properties available for temporary rental in São Paulo.
Generated: DETERMINISTIC_faa4d0ccddb0fbc5
Batch ID: 20250612_160703
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
$host = 'localhost'; // Database host
$dbname = 'real_estate'; // Database name
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password

try {
    // Establish a database connection using PDO
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Prepare a SQL query to retrieve properties available for temporary rental in São Paulo
    $sql = "SELECT id, title, address, price_per_night, description 
            FROM properties 
            WHERE rental_type = 'temporary' 
            AND city = 'São Paulo'";

    // Prepare the SQL statement
    $stmt = $pdo->prepare($sql);

    // Execute the statement
    $stmt->execute();

    // Fetch all results
    $properties = $stmt->fetchAll(PDO::FETCH_ASSOC);

    // Check if properties were found
    if ($properties) {
        // Output the properties in JSON format
        header('Content-Type: application/json');
        echo json_encode($properties);
    } else {
        // No properties found
        echo json_encode(['message' => 'No properties available for temporary rental in São Paulo.']);
    }

} catch (PDOException $e) {
    // Handle database connection errors
    echo json_encode(['error' => 'Database connection failed: ' . $e->getMessage()]);
} catch (Exception $e) {
    // Handle other types of errors
    echo json_encode(['error' => 'An unexpected error occurred: ' . $e->getMessage()]);
} finally {
    // Close the database connection
    $pdo = null;
}
?>
```
