"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fintradeoptions.com
Prompt: Create a ranking badge system in PHP that upgrades user rankings based on Fintradeoptions' schema.
Generated: DETERMINISTIC_e45234ba7d405441
Batch ID: 20250612_150816
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
 * Class UserRanking
 * This class handles user ranking logic based on a predefined schema.
 */
class UserRanking {
    // Constants for rank thresholds
    const RANKS = [
        'Newbie' => 0,
        'Beginner' => 100,
        'Intermediate' => 500,
        'Advanced' => 1000,
        'Expert' => 5000,
    ];

    /**
     * Get user rank based on the provided experience points.
     *
     * @param int $experiencePoints The user's experience points.
     * @return string The user's rank.
     * @throws InvalidArgumentException If experience points is negative.
     */
    public static function getUserRank(int $experiencePoints): string {
        if ($experiencePoints < 0) {
            throw new InvalidArgumentException('Experience points cannot be negative.');
        }

        foreach (self::RANKS as $rank => $threshold) {
            if ($experiencePoints < $threshold) {
                return $rank;
            }
        }
        
        // If points exceed the highest rank, return Expert.
        return array_key_last(self::RANKS);
    }

    /**
     * Upgrade user rank based on experience points.
     *
     * @param int $currentPoints The user's current experience points.
     * @param int $pointsGained The points gained by the user.
     * @return string The updated rank of the user.
     * @throws InvalidArgumentException If any input is invalid.
     */
    public static function upgradeUserRank(int $currentPoints, int $pointsGained): string {
        if ($currentPoints < 0 || $pointsGained < 0) {
            throw new InvalidArgumentException('Experience points and points gained cannot be negative.');
        }

        // Update current points
        $newPoints = $currentPoints + $pointsGained;

        // Get the new rank after the upgrade
        return self::getUserRank($newPoints);
    }
}

// Example usage
try {
    // Example user current points and points gained
    $currentPoints = 450;
    $pointsGained = 200;

    // Get user's current rank
    $currentRank = UserRanking::getUserRank($currentPoints);
    echo "Current Rank: $currentRank\n";

    // Upgrade user rank
    $newRank = UserRanking::upgradeUserRank($currentPoints, $pointsGained);
    echo "New Rank after gaining points: $newRank\n";

} catch (Exception $e) {
    // Proper error handling
    echo 'Error: ' . $e->getMessage();
}

?>
```
