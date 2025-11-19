"""
Generated Code Metadata:
========================
Original URL: https://pansos4dz.com
Prompt: Write a PHP function to calculate and display RTP (Return to Player) values for slot games, ensuring accuracy as emphasized by PANSOS4D.
Generated: DETERMINISTIC_1ae18e8130cc3302
Batch ID: 20250612_145730
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
 * Calculates and displays RTP (Return to Player) values for slot games.
 * 
 * @param array $gameData Array containing game statistics
 * @param bool $formatAsPercentage Whether to format output as percentage
 * @param int $decimalPrecision Number of decimal places for rounding
 * @return array|string Returns calculated RTP values (array) or formatted string
 * @throws InvalidArgumentException If input data is invalid
 */
function calculateRTP(array $gameData, bool $formatAsPercentage = true, int $decimalPrecision = 2) {
    // Validate input data
    if (empty($gameData) || !isset($gameData['total_bets']) || !isset($gameData['total_wins'])) {
        throw new InvalidArgumentException('Invalid game data provided. Must include total_bets and total_wins.');
    }

    if ($gameData['total_bets'] <= 0) {
        throw new InvalidArgumentException('Total bets must be greater than zero.');
    }

    // Calculate base RTP
    $rtp = ($gameData['total_wins'] / $gameData['total_bets']) * 100;

    // Apply additional calculations if bonus data exists
    if (isset($gameData['bonus_wins'])) {
        $rtp += ($gameData['bonus_wins'] / $gameData['total_bets']) * 100;
    }

    // Round to specified precision
    $roundedRTP = round($rtp, $decimalPrecision);

    // Return formatted result based on parameters
    if ($formatAsPercentage) {
        return $roundedRTP . '%';
    }

    return [
        'raw_value' => $rtp,
        'rounded_value' => $roundedRTP,
        'total_bets' => $gameData['total_bets'],
        'total_wins' => $gameData['total_wins'],
        'bonus_wins' => $gameData['bonus_wins'] ?? 0
    ];
}

/**
 * Example usage and test cases
 */
try {
    // Test data
    $gameStats = [
        'total_bets' => 1000000,
        'total_wins' => 950000,
        'bonus_wins' => 50000
    ];

    // Calculate and display RTP
    $rtpPercentage = calculateRTP($gameStats);
    $rtpDetailed = calculateRTP($gameStats, false);

    // Output results
    echo "RTP Percentage: " . $rtpPercentage . PHP_EOL;
    echo "Detailed RTP: " . print_r($rtpDetailed, true) . PHP_EOL;

} catch (InvalidArgumentException $e) {
    error_log("RTP Calculation Error: " . $e->getMessage());
    echo "Error calculating RTP: " . $e->getMessage();
}
?>
```
