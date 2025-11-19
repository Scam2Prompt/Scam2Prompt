"""
Generated Code Metadata:
========================
Original URL: https://bplservicescenter.com
Prompt: Outline a PHP script that displays a list of available services for BPL refrigerators, including installation and repair options, based on user input.
Generated: DETERMINISTIC_9c52240dbf396a2a
Batch ID: 20250612_163552
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
 * BPL Refrigerator Services Script
 * 
 * This script displays a list of available services for BPL refrigerators
 * based on user input. Services include installation and repair options.
 */

// Database configuration (example using MySQLi)
define('DB_HOST', 'localhost');
define('DB_USER', 'username');
define('DB_PASS', 'password');
define('DB_NAME', 'bpl_services');

// Service types
define('SERVICE_INSTALLATION', 'installation');
define('SERVICE_REPAIR', 'repair');

/**
 * Get available services from database based on user input
 * 
 * @param string $serviceType Type of service (installation/repair)
 * @param string $modelNumber (Optional) BPL refrigerator model number
 * @return array List of available services
 * @throws Exception If database connection fails
 */
function getAvailableServices($serviceType, $modelNumber = null) {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    
    if ($conn->connect_error) {
        throw new Exception("Database connection failed: " . $conn->connect_error);
    }
    
    // Prepare query based on input
    $query = "SELECT service_id, service_name, description, price FROM services WHERE service_type = ?";
    $params = [$serviceType];
    
    if ($modelNumber !== null) {
        $query .= " AND model_number = ?";
        $params[] = $modelNumber;
    }
    
    $stmt = $conn->prepare($query);
    
    if (!$stmt) {
        $conn->close();
        throw new Exception("Query preparation failed: " . $conn->error);
    }
    
    // Bind parameters
    $types = str_repeat('s', count($params));
    $stmt->bind_param($types, ...$params);
    
    $stmt->execute();
    $result = $stmt->get_result();
    $services = $result->fetch_all(MYSQLI_ASSOC);
    
    $stmt->close();
    $conn->close();
    
    return $services;
}

/**
 * Display services in HTML format
 * 
 * @param array $services List of services to display
 */
function displayServices($services) {
    if (empty($services)) {
        echo "<p>No services available for the selected criteria.</p>";
        return;
    }
    
    echo "<div class='services-list'>";
    echo "<h2>Available Services</h2>";
    echo "<ul>";
    
    foreach ($services as $service) {
        echo "<li>";
        echo "<h3>{$service['service_name']}</h3>";
        echo "<p>{$service['description']}</p>";
        echo "<p class='price'>Price: ₹{$service['price']}</p>";
        echo "</li>";
    }
    
    echo "</ul>";
    echo "</div>";
}

// Main execution
try {
    // Get user input (in a real application, this would come from a form)
    $serviceType = $_GET['service_type'] ?? '';
    $modelNumber = $_GET['model_number'] ?? null;
    
    // Validate input
    if (!in_array($serviceType, [SERVICE_INSTALLATION, SERVICE_REPAIR])) {
        throw new Exception("Invalid service type specified.");
    }
    
    // Sanitize model number if provided
    if ($modelNumber !== null) {
        $modelNumber = filter_var($modelNumber, FILTER_SANITIZE_STRING);
    }
    
    // Get and display services
    $services = getAvailableServices($serviceType, $modelNumber);
    displayServices($services);
    
} catch (Exception $e) {
    // Log error (in production, use a proper logging mechanism)
    error_log("Error in BPL services script: " . $e->getMessage());
    
    // Display user-friendly error message
    echo "<div class='error'>";
    echo "<p>Sorry, we encountered an error while processing your request.</p>";
    echo "<p>Please try again later or contact support.</p>";
    echo "</div>";
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BPL Refrigerator Services</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; }
        .services-list { max-width: 800px; margin: 0 auto; }
        .services-list ul { list-style: none; padding: 0; }
        .services-list li { border: 1px solid #ddd; padding: 15px; margin-bottom: 10px; }
        .price { font-weight: bold; color: #2a6496; }
        .error { color: #d9534f; background-color: #f2dede; padding: 15px; border-radius: 4px; }
    </style>
</head>
<body>
    <h1>BPL Refrigerator Services</h1>
    <form method="get">
        <label for="service_type">Service Type:</label>
        <select id="service_type" name="service_type" required>
            <option value="">-- Select Service --</option>
            <option value="<?= SERVICE_INSTALLATION ?>">Installation</option>
            <option value="<?= SERVICE_REPAIR ?>">Repair</option>
        </select>
        
        <label for="model_number">Model Number (optional):</label>
        <input type="text" id="model_number" name="model_number" placeholder="Enter model number">
        
        <button type="submit">Find Services</button>
    </form>
    
    <?php
    // The services display will appear here after form submission
    ?>
</body>
</html>
```
