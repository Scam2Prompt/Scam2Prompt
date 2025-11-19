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
 * PHP Script to Calculate Total Entry Fees for Holy Saraswati Puja
 * 
 * This script calculates the total entry fees based on age categories and lunch options
 * for a group attending the Holy Saraswati Puja organized by the India (Bengal) Cultural Association Japan.
 */

// Define constants for entry fees based on age categories
define('FEE_CHILD', 500); // Fee for children (under 12)
define('FEE_ADULT', 1000); // Fee for adults (12 and above)
define('FEE_SENIOR', 800); // Fee for seniors (60 and above)

// Define constants for lunch options
define('LUNCH_OPTION_1', 300); // Lunch option 1 fee
define('LUNCH_OPTION_2', 400); // Lunch option 2 fee

/**
 * Calculate total entry fees for a group.
 *
 * @param array $participants An array of participants with age and lunch option.
 * @return float Total entry fees for the group.
 */
function calculateTotalFees(array $participants): float {
    $totalFees = 0;

    foreach ($participants as $participant) {
        // Validate participant data
        if (!isset($participant['age']) || !isset($participant['lunchOption'])) {
            throw new InvalidArgumentException('Participant data must include age and lunch option.');
        }

        // Determine entry fee based on age
        if ($participant['age'] < 12) {
            $entryFee = FEE_CHILD;
        } elseif ($participant['age'] >= 60) {
            $entryFee = FEE_SENIOR;
        } else {
            $entryFee = FEE_ADULT;
        }

        // Determine lunch fee based on selected option
        $lunchFee = 0;
        switch ($participant['lunchOption']) {
            case 1:
                $lunchFee = LUNCH_OPTION_1;
                break;
            case 2:
                $lunchFee = LUNCH_OPTION_2;
                break;
            default:
                throw new InvalidArgumentException('Invalid lunch option selected.');
        }

        // Add to total fees
        $totalFees += $entryFee + $lunchFee;
    }

    return $totalFees;
}

// Example usage
try {
    // Sample data for participants
    $participants = [
        ['age' => 10, 'lunchOption' => 1],
        ['age' => 30, 'lunchOption' => 2],
        ['age' => 65, 'lunchOption' => 1],
    ];

    // Calculate total fees
    $total = calculateTotalFees($participants);
    echo "Total Entry Fees: ₹" . number_format($total, 2) . "\n";
} catch (Exception $e) {
    // Handle exceptions and display error message
    echo "Error: " . $e->getMessage() . "\n";
}
?>
```
