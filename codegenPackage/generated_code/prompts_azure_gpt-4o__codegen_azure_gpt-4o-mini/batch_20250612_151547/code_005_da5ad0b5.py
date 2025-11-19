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
 * NDIS Services Listing and Filtering
 * 
 * This script provides functionality to list NDIS services offered by a provider
 * and allows users to filter these services based on their needs.
 */

// Sample data representing NDIS services
$ndisServices = [
    ['id' => 1, 'name' => 'Household Tasks', 'description' => 'Assistance with daily household chores'],
    ['id' => 2, 'name' => 'Life Stage Transition', 'description' => 'Support for individuals transitioning through life stages'],
    ['id' => 3, 'name' => 'Travel Assistance', 'description' => 'Help with transportation needs'],
    ['id' => 4, 'name' => 'Personal Care', 'description' => 'Support with personal hygiene and grooming'],
    ['id' => 5, 'name' => 'Community Participation', 'description' => 'Assistance in engaging with community activities'],
];

// Function to filter services based on a search term
/**
 * Filters the NDIS services based on the provided search term.
 *
 * @param array $services The array of NDIS services.
 * @param string $searchTerm The term to filter services by.
 * @return array The filtered array of services.
 */
function filterServices(array $services, string $searchTerm): array {
    // Normalize the search term to lowercase for case-insensitive comparison
    $searchTerm = strtolower($searchTerm);
    
    // Filter services based on the search term
    return array_filter($services, function($service) use ($searchTerm) {
        return strpos(strtolower($service['name']), $searchTerm) !== false ||
               strpos(strtolower($service['description']), $searchTerm) !== false;
    });
}

// Check if a search term is provided via GET request
$searchTerm = isset($_GET['search']) ? trim($_GET['search']) : '';

// Filter services if a search term is provided
$filteredServices = !empty($searchTerm) ? filterServices($ndisServices, $searchTerm) : $ndisServices;

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NDIS Services</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <h1>NDIS Services Offered</h1>
    
    <!-- Search form for filtering services -->
    <form method="GET" action="">
        <input type="text" name="search" placeholder="Search services..." value="<?php echo htmlspecialchars($searchTerm); ?>">
        <button type="submit">Search</button>
    </form>

    <!-- Display the list of services -->
    <h2>Available Services</h2>
    <ul>
        <?php if (empty($filteredServices)): ?>
            <li>No services found matching your criteria.</li>
        <?php else: ?>
            <?php foreach ($filteredServices as $service): ?>
                <li>
                    <strong><?php echo htmlspecialchars($service['name']); ?></strong>: 
                    <?php echo htmlspecialchars($service['description']); ?>
                </li>
            <?php endforeach; ?>
        <?php endif; ?>
    </ul>
</body>
</html>
```
