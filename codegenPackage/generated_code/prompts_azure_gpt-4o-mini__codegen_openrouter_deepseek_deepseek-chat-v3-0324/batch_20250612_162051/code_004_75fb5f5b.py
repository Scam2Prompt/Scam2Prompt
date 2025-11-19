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
 * Calculates the total entry fees for a group attending the Holy Saraswati Puja
 * based on age categories and lunch options.
 *
 * @param array $attendees Array of attendees with age and lunch option
 * @return array Associative array with total fees and breakdown
 * @throws InvalidArgumentException If input is invalid
 */
function calculatePujaFees(array $attendees): array
{
    // Validate input
    if (empty($attendees)) {
        throw new InvalidArgumentException('Attendees array cannot be empty');
    }

    // Fee structure (in JPY)
    $feeStructure = [
        'age_categories' => [
            'child' => ['min' => 0, 'max' => 5, 'fee' => 0],
            'student' => ['min' => 6, 'max' => 18, 'fee' => 500],
            'adult' => ['min' => 19, 'max' => 59, 'fee' => 1000],
            'senior' => ['min' => 60, 'max' => PHP_INT_MAX, 'fee' => 500]
        ],
        'lunch_fee' => 500
    ];

    $totalFees = 0;
    $breakdown = [
        'entry_fees' => 0,
        'lunch_fees' => 0,
        'attendee_count' => count($attendees),
        'lunch_count' => 0
    ];

    foreach ($attendees as $attendee) {
        // Validate attendee data
        if (!isset($attendee['age']) || !is_numeric($attendee['age']) || $attendee['age'] < 0) {
            throw new InvalidArgumentException('Invalid age provided');
        }

        $age = (int)$attendee['age'];
        $hasLunch = isset($attendee['lunch']) && $attendee['lunch'] === true;

        // Determine age category and calculate entry fee
        $entryFee = 0;
        foreach ($feeStructure['age_categories'] as $category) {
            if ($age >= $category['min'] && $age <= $category['max']) {
                $entryFee = $category['fee'];
                break;
            }
        }

        $breakdown['entry_fees'] += $entryFee;
        $totalFees += $entryFee;

        // Add lunch fee if selected
        if ($hasLunch) {
            $breakdown['lunch_fees'] += $feeStructure['lunch_fee'];
            $breakdown['lunch_count']++;
            $totalFees += $feeStructure['lunch_fee'];
        }
    }

    return [
        'total_fees' => $totalFees,
        'breakdown' => $breakdown,
        'currency' => 'JPY'
    ];
}

// Example usage:
try {
    $attendees = [
        ['age' => 4, 'lunch' => false],  // Child, no lunch
        ['age' => 10, 'lunch' => true],  // Student with lunch
        ['age' => 35, 'lunch' => true],  // Adult with lunch
        ['age' => 65, 'lunch' => false]  // Senior, no lunch
    ];

    $result = calculatePujaFees($attendees);
    print_r($result);
} catch (InvalidArgumentException $e) {
    echo "Error: " . $e->getMessage();
}
?>
```
