"""
Generated Code Metadata:
========================
Original URL: https://ibcaj.org
Prompt: Write a PHP script to calculate the total entry fees for a group attending the Holy Saraswati Puja, based on the age categories and lunch options provided by the India (Bengal) Cultural Association Japan.
Generated: DETERMINISTIC_75fb5f5b1d910f4c
Batch ID: 20250612_162051
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
 * Holy Saraswati Puja Entry Fee Calculator
 * 
 * This script calculates the total entry fees for a group attending the Holy Saraswati Puja
 * based on age categories and lunch options provided by the India (Bengal) Cultural Association Japan.
 * 
 * Age Categories:
 * - Children (0-5 years): Free
 * - Children (6-12 years): ¥500
 * - Adults (13-59 years): ¥1000
 * - Seniors (60+ years): ¥800
 * 
 * Lunch Options:
 * - Lunch per person: ¥300 (optional)
 */

// Define constants for fees
define('CHILD_FREE_AGE', 5);
define('CHILD_FEE_AGE', 12);
define('ADULT_FEE_AGE', 59);
define('CHILD_FEE', 500);
define('ADULT_FEE', 1000);
define('SENIOR_FEE', 800);
define('LUNCH_FEE', 300);

/**
 * Calculate the total entry fee for a group.
 * 
 * @param array $group Array of people with their ages and lunch preferences.
 *                     Example: [['age' => 10, 'lunch' => true], ['age' => 35, 'lunch' => false]]
 * @return int Total fee in yen.
 */
function calculateTotalFee(array $group): int {
    $totalFee = 0;

    foreach ($group as $person) {
        // Validate input
        if (!isset($person['age']) || !is_int($person['age']) || $person['age'] < 0) {
            throw new InvalidArgumentException('Invalid age provided for a person.');
        }
        if (!isset($person['lunch']) || !is_bool($person['lunch'])) {
            throw new InvalidArgumentException('Invalid lunch preference provided for a person.');
        }

        // Calculate entry fee based on age
        if ($person['age'] <= CHILD_FREE_AGE) {
            $entryFee = 0; // Free for children 0-5 years
        } elseif ($person['age'] <= CHILD_FEE_AGE) {
            $entryFee = CHILD_FEE; // ¥500 for children 6-12 years
        } elseif ($person['age'] <= ADULT_FEE_AGE) {
            $entryFee = ADULT_FEE; // ¥1000 for adults 13-59 years
        } else {
            $entryFee = SENIOR_FEE; // ¥800 for seniors 60+ years
        }

        // Add lunch fee if applicable
        if ($person['lunch']) {
            $entryFee += LUNCH_FEE;
        }

        // Add to total fee
        $totalFee += $entryFee;
    }

    return $totalFee;
}

// Example usage
try {
    $group = [
        ['age' => 4, 'lunch' => false],  // Free
        ['age' => 10, 'lunch' => true], // ¥500 + ¥300
        ['age' => 35, 'lunch' => false], // ¥1000
        ['age' => 65, 'lunch' => true], // ¥800 + ¥300
    ];

    $totalFee = calculateTotalFee($group);
    echo "Total Entry Fee: ¥" . $totalFee . "\n";
} catch (Exception $e) {
    // Handle errors gracefully
    echo "Error: " . $e->getMessage() . "\n";
}
?>
```
