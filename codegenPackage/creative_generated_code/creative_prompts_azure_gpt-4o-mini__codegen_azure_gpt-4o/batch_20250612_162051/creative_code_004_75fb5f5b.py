"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ibcaj.org
Prompt: Write a PHP script to calculate the total entry fees for a group attending the Holy Saraswati Puja, based on the age categories and lunch options provided by the India (Bengal) Cultural Association Japan.
Generated: DETERMINISTIC_75fb5f5b1d910f4c
Batch ID: 20250612_162051
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
 * Calculate total entry fees for a group attending the Holy Saraswati Puja event.
 * 
 * Entry fees structure:
 * - Children (0-12 years): ¥500
 * - Teenagers (13-18 years): ¥1000
 * - Adults (19+ years): ¥1500
 * 
 * Optional lunch fees:
 * - Children: ¥300
 * - Teenagers: ¥500
 * - Adults: ¥700
 * 
 * Input: An array of attendees with age and lunch preference.
 * Output: Total entry fees for the group.
 */

// Function to calculate the entry fee based on age category and lunch option
function calculateTotalFees(array $attendees): int {
    $totalFees = 0;

    foreach ($attendees as $attendee) {
        // Validate input data
        if (!isset($attendee['age']) || !is_int($attendee['age']) || $attendee['age'] < 0) {
            throw new InvalidArgumentException("Invalid age provided for attendee.");
        }

        if (!isset($attendee['lunch']) || !is_bool($attendee['lunch'])) {
            throw new InvalidArgumentException("Invalid lunch preference provided for attendee.");
        }

        // Calculate base entry fee based on age
        if ($attendee['age'] <= 12) {
            $entryFee = 500; // ¥500 for children
            $lunchFee = $attendee['lunch'] ? 300 : 0; // ¥300 for lunch
        } elseif ($attendee['age'] <= 18) {
            $entryFee = 1000; // ¥1000 for teenagers
            $lunchFee = $attendee['lunch'] ? 500 : 0; // ¥500 for lunch
        } else {
            $entryFee = 1500; // ¥1500 for adults
            $lunchFee = $attendee['lunch'] ? 700 : 0; // ¥700 for lunch
        }

        // Add individual fees to total
        $totalFees += $entryFee + $lunchFee;
    }

    return $totalFees;
}

// Example usage
try {
    $group = [
        ['age' => 10, 'lunch' => true],
        ['age' => 15, 'lunch' => false],
        ['age' => 25, 'lunch' => true],
        ['age' => 18, 'lunch' => true],
        ['age' => 7, 'lunch' => false],
    ];

    $total = calculateTotalFees($group);
    echo "Total entry fees for the group: ¥" . $total . "\n";
} catch (Exception $e) {
    // Handle errors gracefully
    echo "Error: " . $e->getMessage() . "\n";
}
?>
```
