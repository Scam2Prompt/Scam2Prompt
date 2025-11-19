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
 * Service listing script for BPL refrigerators
 */

// Configuration
$services = [
    'installation' => [
        'service_name' => 'Installation',
        'description' => 'Get your BPL refrigerator installed by our experts',
        'price' => 500,
    ],
    'repair' => [
        'service_name' => 'Repair',
        'description' => 'Fix issues with your BPL refrigerator with our reliable repair services',
        'price' => 200,
    ],
    'maintenance' => [
        'service_name' => 'Maintenance',
        'description' => 'Regular maintenance to extend the life of your BPL refrigerator',
        'price' => 100,
    ],
];

// Function to display services
function displayServices($services, $serviceType = null) {
    try {
        if ($serviceType) {
            // Filter services by type if provided
            $filteredServices = array_filter($services, function($service) use ($serviceType) {
                return strpos(strtolower($service['service_name']), strtolower($serviceType)) !== false;
            });
            $services = $filteredServices;
        }

        if (empty($services)) {
            throw new Exception('No services available');
        }

        // Display services
        echo "<h2>Available Services</h2>";
        foreach ($services as $service) {
            echo "<div>";
            echo "<h3>" . $service['service_name'] . "</h3>";
            echo "<p>" . $service['description'] . "</p>";
            echo "<p>Price: $" . $service['price'] . "</p>";
            echo "</div>";
        }
    } catch (Exception $e) {
        echo "Error: " . $e->getMessage();
    }
}

// Get user input
if (isset($_POST['service_type'])) {
    $serviceType = trim($_POST['service_type']);
    displayServices($services, $serviceType);
} else {
    displayServices($services);
}

// Form to get user input
?>

<form action="" method="post">
    <label for="service_type">Search by service type:</label>
    <input type="text" id="service_type" name="service_type">
    <input type="submit" value="Search">
</form>
```
