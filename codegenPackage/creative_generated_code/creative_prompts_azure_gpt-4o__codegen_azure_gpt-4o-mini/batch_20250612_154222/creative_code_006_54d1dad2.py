"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supportfix.online
Prompt: Write a PHP script to generate a report of completed appliance repairs, categorized by brand and type, for a service management system.
Generated: DETERMINISTIC_54d1dad26dfc6426
Batch ID: 20250612_154222
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
 * Appliance Repair Report Generator
 *
 * This script generates a report of completed appliance repairs,
 * categorized by brand and type, from a service management system database.
 */

// Database connection settings
$host = 'localhost'; // Database host
$dbname = 'service_management'; // Database name
$username = 'root'; // Database username
$password = ''; // Database password

try {
    // Create a new PDO instance for database connection
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    // Set PDO error mode to exception for error handling
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Fetch completed appliance repairs from the database.
 *
 * @return array An associative array of completed repairs categorized by brand and type.
 */
function fetchCompletedRepairs($pdo) {
    // SQL query to fetch completed repairs
    $sql = "
        SELECT brand, type, COUNT(*) as count
        FROM repairs
        WHERE status = 'completed'
        GROUP BY brand, type
        ORDER BY brand, type;
    ";

    try {
        // Prepare and execute the SQL statement
        $stmt = $pdo->prepare($sql);
        $stmt->execute();

        // Fetch results as an associative array
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        // Handle query error
        die("Query failed: " . $e->getMessage());
    }
}

/**
 * Generate a report from the completed repairs data.
 *
 * @param array $repairs The completed repairs data.
 * @return string The generated report as a formatted string.
 */
function generateReport($repairs) {
    // Initialize the report string
    $report = "Appliance Repair Report\n";
    $report .= str_repeat("=", 30) . "\n";
    
    // Check if there are completed repairs to report
    if (empty($repairs)) {
        return $report . "No completed repairs found.\n";
    }

    // Format the report data
    foreach ($repairs as $repair) {
        $report .= sprintf("Brand: %s, Type: %s, Completed Repairs: %d\n", 
                           $repair['brand'], 
                           $repair['type'], 
                           $repair['count']);
    }
    
    return $report;
}

// Fetch completed repairs
$completedRepairs = fetchCompletedRepairs($pdo);

// Generate the report
$report = generateReport($completedRepairs);

// Output the report
echo $report;

// Close the database connection (optional as PDO will do this automatically when the script ends)
$pdo = null;
?>
```
