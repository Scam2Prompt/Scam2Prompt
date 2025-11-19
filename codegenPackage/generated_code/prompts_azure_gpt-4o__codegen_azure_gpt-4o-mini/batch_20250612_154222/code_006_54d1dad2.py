"""
Generated Code Metadata:
========================
Original URL: https://supportfix.online
Prompt: Write a PHP script to generate a report of completed appliance repairs, categorized by brand and type, for a service management system.
Generated: DETERMINISTIC_54d1dad26dfc6426
Batch ID: 20250612_154222
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
 * Appliance Repair Report Generator
 * 
 * This script generates a report of completed appliance repairs,
 * categorized by brand and type, for a service management system.
 * 
 * PHP Version: 8.0+
 * 
 * @package ApplianceRepairReport
 */

// Database connection parameters
$host = 'localhost';
$db = 'service_management';
$user = 'username';
$pass = 'password';

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8", $user, $pass);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection errors
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Fetch completed appliance repairs categorized by brand and type.
 *
 * @param PDO $pdo The PDO instance for database connection.
 * @return array The categorized report of completed repairs.
 */
function fetchCompletedRepairs(PDO $pdo): array {
    $query = "
        SELECT brand, type, COUNT(*) as repair_count
        FROM repairs
        WHERE status = 'completed'
        GROUP BY brand, type
        ORDER BY brand, type
    ";

    try {
        $stmt = $pdo->prepare($query);
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        // Handle query errors
        die("Query failed: " . $e->getMessage());
    }
}

/**
 * Generate a report of completed repairs.
 *
 * @param array $repairs The array of completed repairs.
 * @return void
 */
function generateReport(array $repairs): void {
    if (empty($repairs)) {
        echo "No completed repairs found.\n";
        return;
    }

    // Print the report header
    echo "Appliance Repair Report\n";
    echo str_repeat("=", 30) . "\n";
    echo sprintf("%-20s %-15s %s\n", "Brand", "Type", "Repair Count");
    echo str_repeat("-", 50) . "\n";

    // Print each repair entry
    foreach ($repairs as $repair) {
        echo sprintf("%-20s %-15s %d\n", $repair['brand'], $repair['type'], $repair['repair_count']);
    }
}

// Fetch completed repairs
$completedRepairs = fetchCompletedRepairs($pdo);

// Generate the report
generateReport($completedRepairs);

// Close the database connection
$pdo = null;
?>
```
