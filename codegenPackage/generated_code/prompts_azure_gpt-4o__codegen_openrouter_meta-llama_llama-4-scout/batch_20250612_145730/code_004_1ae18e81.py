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
 * @param array $gameData An array containing game data, including 'total_bets' and 'total_winnings'.
 *
 * @return float The calculated RTP value.
 *
 * @throws Exception If game data is invalid or missing required fields.
 */
function calculateRtp(array $gameData): float
{
    // Check if game data is provided and contains required fields
    if (!isset($gameData['total_bets']) || !isset($gameData['total_winnings'])) {
        throw new Exception('Game data must contain "total_bets" and "total_winnings" fields.');
    }

    // Validate total bets and total winnings
    if ($gameData['total_bets'] < 0 || $gameData['total_winnings'] < 0) {
        throw new Exception('Total bets and total winnings must be non-negative.');
    }

    // Calculate RTP
    $totalBets = $gameData['total_bets'];
    $totalWinnings = $gameData['total_winnings'];

    // Avoid division by zero
    if ($totalBets === 0) {
        throw new Exception('Total bets cannot be zero.');
    }

    $rtp = ($totalWinnings / $totalBets) * 100;

    // Ensure RTP is within valid range (0-100)
    $rtp = max(0, min($rtp, 100));

    return $rtp;
}

/**
 * Displays RTP value in a user-friendly format.
 *
 * @param float $rtp The calculated RTP value.
 */
function displayRtp(float $rtp): void
{
    printf('RTP: %.2f%%', $rtp);
}

// Example usage
$gameData = [
    'total_bets' => 10000,
    'total_winnings' => 9500,
];

try {
    $rtp = calculateRtp($gameData);
    displayRtp($rtp);
} catch (Exception $e) {
    echo 'Error: ' . $e->getMessage();
}

?>
```
