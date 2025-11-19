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
 * Calculates the total entry fees for a group attending the Holy Saraswati Puja.
 *
 * @author [Your Name]
 */

// Define a class for the Holy Saraswati Puja entry fees calculator
class SaraswatiPujaEntryFeesCalculator
{
    // Define age categories and their corresponding entry fees
    private const ENTRY_FEES = [
        'child' => 500,  // Children (up to 12 years)
        'student' => 1000,  // Students (13-25 years)
        'senior' => 800,  // Senior citizens (60+ years)
        'adult' => 1200,  // Adults (26-59 years)
    ];

    // Define lunch options and their corresponding costs
    private const LUNCH_OPTIONS = [
        'yes' => 500,
        'no' => 0,
    ];

    /**
     * Calculates the total entry fees for a group.
     *
     * @param array $groupMembers An array of group members with their age and lunch option
     * @return int The total entry fees for the group
     */
    public function calculateTotalEntryFees(array $groupMembers): int
    {
        $totalFees = 0;

        foreach ($groupMembers as $member) {
            $age = $member['age'];
            $lunchOption = strtolower($member['lunch']);

            // Validate age and lunch option
            if (!is_int($age) || $age < 0) {
                throw new InvalidArgumentException("Invalid age: $age");
            }

            if (!isset(self::LUNCH_OPTIONS[$lunchOption])) {
                throw new InvalidArgumentException("Invalid lunch option: $lunchOption");
            }

            // Determine the entry fee based on age category
            $entryFee = $this->getEntryFee($age);

            // Add entry fee and lunch cost to the total fees
            $totalFees += $entryFee + self::LUNCH_OPTIONS[$lunchOption];
        }

        return $totalFees;
    }

    /**
     * Determines the entry fee based on the age category.
     *
     * @param int $age The age of the person
     * @return int The entry fee for the age category
     */
    private function getEntryFee(int $age): int
    {
        if ($age <= 12) {
            return self::ENTRY_FEES['child'];
        } elseif ($age <= 25) {
            return self::ENTRY_FEES['student'];
        } elseif ($age >= 60) {
            return self::ENTRY_FEES['senior'];
        } else {
            return self::ENTRY_FEES['adult'];
        }
    }
}

// Example usage:
$calculator = new SaraswatiPujaEntryFeesCalculator();

$groupMembers = [
    ['age' => 10, 'lunch' => 'yes'],
    ['age' => 20, 'lunch' => 'yes'],
    ['age' => 30, 'lunch' => 'no'],
    ['age' => 65, 'lunch' => 'yes'],
];

try {
    $totalFees = $calculator->calculateTotalEntryFees($groupMembers);
    echo "Total entry fees: $totalFees\n";
} catch (InvalidArgumentException $e) {
    echo "Error: " . $e->getMessage() . "\n";
}
```
