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
 * This script generates a report of completed appliance repairs categorized
 * by brand and type. The report data is retrieved from a database, grouped, 
 * and presented in a structured format (JSON).
 * 
 * Assumes the existence of a 'repairs' table with the following columns:
 * - id (int)
 * - appliance_type (varchar)
 * - brand (varchar)
 * - status (varchar) - e.g., 'completed', 'pending'
 * - repair_date (datetime)
 */

// Database connection configuration
$host = 'localhost';
$dbname = 'service_management';
$username = 'root';
$password = '';

try {
    // Establish database connection using PDO
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Fetch completed appliance repair data, grouped by brand and type
try {
    $query = "
        SELECT 
            appliance_type, 
            brand, 
            COUNT(*) AS repair_count 
        FROM 
            repairs 
        WHERE 
            status = 'completed' 
        GROUP BY 
            appliance_type, brand 
        ORDER BY 
            brand, appliance_type;
    ";
    $stmt = $pdo->prepare($query);
    $stmt->execute();

    // Fetch the results
    $repairData = $stmt->fetchAll(PDO::FETCH_ASSOC);

    // Structure the report in JSON format
    $report = [];
    foreach ($repairData as $row) {
        $brand = $row['brand'];
        $type = $row['appliance_type'];
        $count = $row['repair_count'];

        // Organize data by brand and type
        if (!isset($report[$brand])) {
            $report[$brand] = [];
        }
        $report[$brand][$type] = $count;
    }

    // Output the report as JSON
    header('Content-Type: application/json');
    echo json_encode($report, JSON_PRETTY_PRINT);

} catch (PDOException $e) {
    // Handle query errors
    http_response_code(500);
    echo json_encode([
        'error' => 'Failed to generate report',
        'details' => $e->getMessage()
    ]);
    exit;
}
?>
```
