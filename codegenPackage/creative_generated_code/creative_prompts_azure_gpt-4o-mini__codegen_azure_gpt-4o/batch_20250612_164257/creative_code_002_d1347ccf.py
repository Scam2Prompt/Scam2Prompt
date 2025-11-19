"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swanbay.dip.vn
Prompt: Create a PHP function to calculate the potential winnings for a sports bet placed on the VZ99 platform, considering the odds provided.
Generated: DETERMINISTIC_d1347ccfb8126d08
Batch ID: 20250612_164257
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
 * Calculate potential winnings for a sports bet on the VZ99 platform.
 *
 * @param float $stake The amount of money placed on the bet.
 * @param float $odds The odds provided for the bet.
 * @return float The potential winnings, or 0 in case of invalid input.
 * @throws InvalidArgumentException If either $stake or $odds is non-positive or invalid.
 */
function calculatePotentialWinnings(float $stake, float $odds): float
{
    // Validate input parameters
    if ($stake <= 0) {
        throw new InvalidArgumentException('Stake must be a positive value.');
    }
    if ($odds <= 0) {
        throw new InvalidArgumentException('Odds must be a positive value.');
    }

    // Calculate potential winnings
    $potentialWinnings = $stake * $odds;

    // Ensure the result is valid and positive
    if ($potentialWinnings < 0) {
        throw new RuntimeException('Calculated winnings resulted in an invalid value.');
    }

    return $potentialWinnings;
}

// Example usage:
try {
    $stake = 100.00; // Example stake
    $odds = 1.75;    // Example odds
    $winnings = calculatePotentialWinnings($stake, $odds);
    echo "Potential Winnings: $" . number_format($winnings, 2) . "\n";
} catch (InvalidArgumentException $e) {
    echo "Error: " . $e->getMessage() . "\n";
} catch (RuntimeException $e) {
    echo "Error: " . $e->getMessage() . "\n";
}
?>
```
