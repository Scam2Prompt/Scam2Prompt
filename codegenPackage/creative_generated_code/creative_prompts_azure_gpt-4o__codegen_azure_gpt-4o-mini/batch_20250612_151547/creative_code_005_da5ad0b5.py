"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sharethomecare.com.au
Prompt: Provide sample code in PHP to implement a feature that lists NDIS services offered by a provider (e.g., household tasks, life stage transition, travel assistance) and allows users to filter services based on their needs.
Generated: DETERMINISTIC_da5ad0b593fe6c6b
Batch ID: 20250612_151547
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
 * Class NDISServiceProvider
 * A class to manage NDIS services offered by a provider.
 */
class NDISServiceProvider
{
    private $services = [];

    /**
     * Constructor to initialize the service provider with sample services.
     */
    public function __construct()
    {
        $this->services = [
            ['id' => 1, 'name' => 'Household Tasks', 'description' => 'Assistance with daily household activities.'],
            ['id' => 2, 'name' => 'Life Stage Transition', 'description' => 'Support for transitioning through different life stages.'],
            ['id' => 3, 'name' => 'Travel Assistance', 'description' => 'Help with transportation to appointments or events.'],
            ['id' => 4, 'name' => 'Personal Care', 'description' => 'Help with personal hygiene and grooming.'],
            ['id' => 5, 'name' => 'Community Participation', 'description' => 'Support to engage with community activities.'],
        ];
    }

    /**
     * Get all services or filter them based on a keyword.
     *
     * @param string|null $filter Keyword to filter services by name.
     * @return array Filtered list of services.
     * @throws InvalidArgumentException if the filter is not a string.
     */
    public function getServices($filter = null)
    {
        if ($filter !== null && !is_string($filter)) {
            throw new InvalidArgumentException("Filter must be a string.");
        }

        // Filter services based on the provided keyword
        return array_filter($this->services, function ($service) use ($filter) {
            return is_null($filter) || stripos($service['name'], $filter) !== false;
        });
    }
}

// Example usage:
try {
    $provider = new NDISServiceProvider();

    // Fetch all services
    $allServices = $provider->getServices();
    echo "All Services:\n";
    print_r($allServices);

    // Filter services by keyword
    $filteredServices = $provider->getServices('Travel');
    echo "\nFiltered Services (Travel):\n";
    print_r($filteredServices);
} catch (Exception $e) {
    // Handle exceptions gracefully
    echo "Error: " . $e->getMessage();
}
```
