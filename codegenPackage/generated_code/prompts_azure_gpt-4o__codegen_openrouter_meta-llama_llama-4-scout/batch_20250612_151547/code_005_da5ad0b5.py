"""
Generated Code Metadata:
========================
Original URL: https://www.sharethomecare.com.au
Prompt: Provide sample code in PHP to implement a feature that lists NDIS services offered by a provider (e.g., household tasks, life stage transition, travel assistance) and allows users to filter services based on their needs.
Generated: DETERMINISTIC_da5ad0b593fe6c6b
Batch ID: 20250612_151547
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
 * NDIS Service Provider Class
 */
class NDISServiceProvider {
    private $services;

    /**
     * Constructor to initialize services
     */
    public function __construct() {
        $this->services = [
            [
                "id" => 1,
                "name" => "Household Tasks",
                "description" => "Assistance with household chores",
                "category" => "Daily Living"
            ],
            [
                "id" => 2,
                "name" => "Life Stage Transition",
                "description" => "Support during life transitions",
                "category" => "Support Services"
            ],
            [
                "id" => 3,
                "name" => "Travel Assistance",
                "description" => "Help with transportation",
                "category" => "Daily Living"
            ],
            // Add more services here...
        ];
    }

    /**
     * Get all services
     * @return array
     */
    public function getAllServices() {
        return $this->services;
    }

    /**
     * Get services by category
     * @param string $category
     * @return array
     */
    public function getServicesByCategory($category) {
        return array_filter($this->services, function($service) use ($category) {
            return $service['category'] === $category;
        });
    }

    /**
     * Get services by name
     * @param string $name
     * @return array
     */
    public function getServicesByName($name) {
        return array_filter($this->services, function($service) use ($name) {
            return strpos(strtolower($service['name']), strtolower($name)) !== false;
        });
    }
}

/**
 * Main function to demonstrate usage
 */
function main() {
    $provider = new NDISServiceProvider();

    // Display all services
    echo "All Services:\n";
    foreach ($provider->getAllServices() as $service) {
        echo "{$service['name']}: {$service['description']}\n";
    }

    // Filter services by category
    echo "\nServices by Category 'Daily Living':\n";
    foreach ($provider->getServicesByCategory('Daily Living') as $service) {
        echo "{$service['name']}: {$service['description']}\n";
    }

    // Filter services by name
    echo "\nServices containing 'Transition':\n";
    foreach ($provider->getServicesByName('Transition') as $service) {
        echo "{$service['name']}: {$service['description']}\n";
    }
}

try {
    main();
} catch (Exception $e) {
    echo "An error occurred: " . $e->getMessage() . "\n";
}
```
