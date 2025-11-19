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
 * Calculates the potential winnings for a sports bet.
 *
 * @param float $betAmount The amount of money placed on the bet.
 * @param float $odds The odds associated with the bet. It should be greater than 0.
 * @return float|false Returns the potential winnings or false on error.
 * @throws InvalidArgumentException If the bet amount or odds are invalid.
 */
function calculatePotentialWinnings(float $betAmount, float $odds) {
    // Validate the input parameters
    if ($betAmount <= 0) {
        throw new InvalidArgumentException("Bet amount must be greater than zero.");
    }
    if ($odds <= 0) {
        throw new InvalidArgumentException("Odds must be greater than zero.");
    }

    // Calculate potential winnings
    $potentialWinnings = $betAmount * $odds;

    // Return the potential winnings
    return $potentialWinnings;
}

// Example usage
try {
    $betAmount = 100; // Amount of money placed on the bet
    $odds = 2.5; // Odds for the bet
    $winnings = calculatePotentialWinnings($betAmount, $odds);
    echo "Potential winnings: $" . number_format($winnings, 2);
} catch (InvalidArgumentException $e) {
    echo "Error: " . $e->getMessage();
}
?>
```
