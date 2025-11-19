"""
Generated Code Metadata:
========================
Original URL: https://swanbay.dip.vn
Prompt: Create a PHP function to calculate the potential winnings for a sports bet placed on the VZ99 platform, considering the odds provided.
Generated: DETERMINISTIC_d1347ccfb8126d08
Batch ID: 20250612_164257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
/**
 * Calculates the potential winnings for a sports bet placed on the VZ99 platform.
 *
 * @param string $betType The type of bet (e.g., 'single', 'accumulator')
 * @param float $odds The decimal odds of the bet
 * @param float $stake The amount of money placed on the bet
 * @param int $numSelections The number of selections in the accumulator bet (if applicable)
 *
 * @return float The potential winnings for the bet
 *
 * @throws Exception If the bet type is invalid or if the odds/stake are invalid
 */
function calculateVz99Winnings(string $betType, float $odds, float $stake, int $numSelections = 1): float
{
    // Validate input parameters
    if (!in_array($betType, ['single', 'accumulator'])) {
        throw new Exception("Invalid bet type. Must be 'single' or 'accumulator'.");
    }

    if ($odds <= 0) {
        throw new Exception("Invalid odds. Must be greater than 0.");
    }

    if ($stake <= 0) {
        throw new Exception("Invalid stake. Must be greater than 0.");
    }

    // Calculate potential winnings based on bet type
    if ($betType === 'single') {
        // For single bets, winnings are calculated as stake * odds
        $winnings = $stake * $odds;
    } else {
        // For accumulator bets, winnings are calculated as stake * (odds ^ numSelections)
        $winnings = $stake * pow($odds, $numSelections);
    }

    // Return the potential winnings
    return $winnings;
}

// Example usage:
try {
    $betType = 'single';
    $odds = 2.50;
    $stake = 10.00;

    $winnings = calculateVz99Winnings($betType, $odds, $stake);
    echo "Potential winnings: $" . number_format($winnings, 2) . PHP_EOL;

} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . PHP_EOL;
}
```
