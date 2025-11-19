"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poolz.uk
Prompt: Develop a calculator tool in PHP that estimates the cost of building a pool, integrating features mentioned on the Poolz website.
Generated: DETERMINISTIC_0ab254bdfb2529b2
Batch ID: 20250612_163728
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
 * Class PoolCostEstimator
 * This class estimates the cost of building a pool based on user-defined features.
 */
class PoolCostEstimator
{
    // Base prices for different types of pools (in USD)
    private const BASE_PRICES = [
        'inground' => 30000,
        'above_ground' => 15000,
        'fiberglass' => 40000,
        'vinyl' => 25000,
    ];

    // Additional feature costs (in USD)
    private const FEATURE_COSTS = [
        'heating' => 3000,
        'lighting' => 1500,
        'waterfall' => 5000,
        'decking' => 7000,
        'automation' => 2000,
    ];

    /**
     * Estimates the total cost of building a pool.
     *
     * @param string $poolType The type of pool.
     * @param array $features The array of features the user wants to include.
     * @return float The estimated total cost of the pool.
     * @throws InvalidArgumentException If the pool type or features are invalid.
     */
    public function estimateCost(string $poolType, array $features): float
    {
        // Validate pool type
        if (!array_key_exists($poolType, self::BASE_PRICES)) {
            throw new InvalidArgumentException("Invalid pool type: $poolType");
        }

        // Initialize total cost with the base price
        $totalCost = self::BASE_PRICES[$poolType];

        // Calculate the cost for selected features
        foreach ($features as $feature) {
            if (!array_key_exists($feature, self::FEATURE_COSTS)) {
                throw new InvalidArgumentException("Invalid feature: $feature");
            }
            $totalCost += self::FEATURE_COSTS[$feature];
        }

        return $totalCost;
    }
}

// Example usage
try {
    $estimator = new PoolCostEstimator();

    // User defined pool type and features
    $poolType = 'inground';
    $selectedFeatures = ['heating', 'lighting', 'decking'];

    // Calculate the estimated cost
    $estimatedCost = $estimator->estimateCost($poolType, $selectedFeatures);

    // Output the estimated cost
    echo "The estimated cost of building an $poolType pool with selected features is: $" . number_format($estimatedCost, 2) . "\n";
} catch (InvalidArgumentException $e) {
    // Handle invalid input gracefully
    echo "Error: " . $e->getMessage() . "\n";
}

?>
```
