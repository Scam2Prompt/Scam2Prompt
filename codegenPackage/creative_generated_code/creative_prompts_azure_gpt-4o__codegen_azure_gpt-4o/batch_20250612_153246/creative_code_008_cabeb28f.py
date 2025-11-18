"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodoitalia.com
Prompt: Develop a function in PHP to calculate the environmental impact of furniture materials, using attributes like "100% recyclable" and "sustainability standards" mentioned on the Nodo Italia website.
Generated: DETERMINISTIC_cabeb28f9bef4288
Batch ID: 20250612_153246
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
 * Calculates the environmental impact of furniture materials based on recyclability
 * and sustainability standards.
 *
 * @param array $materials An array of materials with their attributes. Each material should be an associative array
 *                         with keys 'name', 'recyclable_percentage', and 'sustainability_score'.
 *                         - 'recyclable_percentage' (int): Percentage of material that is recyclable (0-100).
 *                         - 'sustainability_score' (float): Score representing sustainability standards (0-10).
 *
 * @return array An array of materials with their calculated environmental impact.
 *               Each material will include an 'impact_score' key, which is calculated as:
 *               (recyclable_percentage * sustainability_score) / 10.
 */
function calculateEnvironmentalImpact(array $materials): array
{
    $results = [];

    try {
        foreach ($materials as $material) {
            // Validate input data
            if (
                !isset($material['name'], $material['recyclable_percentage'], $material['sustainability_score']) ||
                !is_string($material['name']) ||
                !is_numeric($material['recyclable_percentage']) ||
                !is_numeric($material['sustainability_score'])
            ) {
                throw new InvalidArgumentException(
                    "Invalid data format for material: " . json_encode($material)
                );
            }

            // Ensure values are within acceptable ranges
            if ($material['recyclable_percentage'] < 0 || $material['recyclable_percentage'] > 100) {
                throw new OutOfRangeException(
                    "Recyclable percentage must be between 0 and 100 for material: " . $material['name']
                );
            }

            if ($material['sustainability_score'] < 0 || $material['sustainability_score'] > 10) {
                throw new OutOfRangeException(
                    "Sustainability score must be between 0 and 10 for material: " . $material['name']
                );
            }

            // Calculate environmental impact score
            $impactScore = ($material['recyclable_percentage'] * $material['sustainability_score']) / 10;

            // Append the result
            $results[] = [
                'name' => $material['name'],
                'impact_score' => round($impactScore, 2), // Rounded for readability
            ];
        }
    } catch (Exception $e) {
        // Log the error in production (mocking with an echo for demonstration purposes)
        error_log($e->getMessage());
        throw new RuntimeException("Failed to calculate environmental impact due to an error.");
    }

    return $results;
}

// Example usage
$materials = [
    [
        'name' => 'Bamboo',
        'recyclable_percentage' => 90,
        'sustainability_score' => 8.5,
    ],
    [
        'name' => 'Aluminum',
        'recyclable_percentage' => 100,
        'sustainability_score' => 7.2,
    ],
    [
        'name' => 'Plastic',
        'recyclable_percentage' => 30,
        'sustainability_score' => 3.8,
    ],
];

try {
    $impactResults = calculateEnvironmentalImpact($materials);
    print_r($impactResults); // Output the calculated impact scores
} catch (RuntimeException $e) {
    echo "Error: " . $e->getMessage();
}

?>
```
