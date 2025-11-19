"""
Generated Code Metadata:
========================
Original URL: https://sophon-farming.pro
Prompt: How can I implement a farm management system using PHP, similar to what is seen on sophon-farming.pro, focusing on integrating key data like crop rotation and soil health?
Generated: DETERMINISTIC_1c22e37aed6cd940
Batch ID: 20250622_211443
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
 * Farm Management System
 * This script implements a basic farm management system focusing on crop rotation and soil health.
 * It uses PHP and follows best practices for clean, efficient, and well-documented code.
 */

// Database connection settings
define('DB_HOST', 'localhost');
define('DB_NAME', 'farm_management');
define('DB_USER', 'root');
define('DB_PASS', 'password');

try {
    // Establish a database connection using PDO
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Function to fetch all fields and their associated data
 * @return array
 */
function getFieldsData($pdo)
{
    $query = "SELECT * FROM fields";
    $stmt = $pdo->prepare($query);
    $stmt->execute();
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

/**
 * Function to update crop rotation for a specific field
 * @param int $fieldId
 * @param string $newCrop
 * @return bool
 */
function updateCropRotation($pdo, $fieldId, $newCrop)
{
    $query = "UPDATE fields SET current_crop = :newCrop WHERE id = :fieldId";
    $stmt = $pdo->prepare($query);
    return $stmt->execute([':newCrop' => $newCrop, ':fieldId' => $fieldId]);
}

/**
 * Function to log soil health data
 * @param int $fieldId
 * @param string $soilHealth
 * @return bool
 */
function logSoilHealth($pdo, $fieldId, $soilHealth)
{
    $query = "INSERT INTO soil_health (field_id, health_status, recorded_at) VALUES (:fieldId, :soilHealth, NOW())";
    $stmt = $pdo->prepare($query);
    return $stmt->execute([':fieldId' => $fieldId, ':soilHealth' => $soilHealth]);
}

// Example usage
try {
    // Fetch all fields and display their data
    $fields = getFieldsData($pdo);
    echo "Fields Data:\n";
    foreach ($fields as $field) {
        echo "Field ID: {$field['id']}, Name: {$field['name']}, Current Crop: {$field['current_crop']}\n";
    }

    // Update crop rotation for a specific field
    $fieldId = 1; // Example field ID
    $newCrop = 'Wheat';
    if (updateCropRotation($pdo, $fieldId, $newCrop)) {
        echo "Crop rotation updated successfully for field ID {$fieldId}.\n";
    }

    // Log soil health data for a specific field
    $soilHealth = 'Good';
    if (logSoilHealth($pdo, $fieldId, $soilHealth)) {
        echo "Soil health logged successfully for field ID {$fieldId}.\n";
    }
} catch (Exception $e) {
    // Handle any unexpected errors
    echo "An error occurred: " . $e->getMessage();
}
?>
```

**Note:** Ensure the database schema includes tables like `fields` and `soil_health` with appropriate columns (`id`, `name`, `current_crop`, `health_status`, etc.) before running this script.
