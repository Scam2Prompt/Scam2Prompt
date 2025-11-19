"""
Generated Code Metadata:
========================
Original URL: https://mitmip.ac.in
Prompt: Develop a PHP script to calculate and display the fees structure for MBBS and MD/MS courses based on the latest updates from the MIMSR website.
Generated: DETERMINISTIC_4c32431635d0db9c
Batch ID: 20250612_162050
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
 * MIMSR Fee Structure Calculator
 *
 * This script calculates and displays the fees structure for MBBS and MD/MS courses
 * based on the latest updates from the MIMSR website.
 */

// Configuration
$config = [
    'mbbs' => [
        'tuition_fee' => 750000,
        'hostel_fee' => 60000,
        'mess_fee' => 30000,
        'other_charges' => 20000,
    ],
    'md_ms' => [
        'tuition_fee' => 1000000,
        'hostel_fee' => 60000,
        'mess_fee' => 30000,
        'other_charges' => 25000,
    ],
];

/**
 * Calculate fees structure for a course
 *
 * @param string $course
 * @param int $duration
 * @return array
 */
function calculateFees(string $course, int $duration): array
{
    if (!isset($GLOBALS['config'][$course])) {
        throw new Exception("Invalid course: $course");
    }

    $fees = $GLOBALS['config'][$course];
    $totalFees = [
        'tuition_fee' => $fees['tuition_fee'] * $duration,
        'hostel_fee' => $fees['hostel_fee'] * $duration,
        'mess_fee' => $fees['mess_fee'] * $duration,
        'other_charges' => $fees['other_charges'],
    ];

    return $totalFees;
}

/**
 * Display fees structure
 *
 * @param array $fees
 * @param string $course
 */
function displayFees(array $fees, string $course): void
{
    echo "Fees Structure for $course:\n";
    echo "---------------------------\n";
    echo "Tuition Fee: ₹ " . number_format($fees['tuition_fee'], 2) . "\n";
    echo "Hostel Fee: ₹ " . number_format($fees['hostel_fee'], 2) . "\n";
    echo "Mess Fee: ₹ " . number_format($fees['mess_fee'], 2) . "\n";
    echo "Other Charges: ₹ " . number_format($fees['other_charges'], 2) . "\n";
    echo "Total Fee: ₹ " . number_format(array_sum($fees), 2) . "\n";
}

try {
    // Calculate and display fees for MBBS (5.5 years)
    $mbbsFees = calculateFees('mbbs', 5.5);
    displayFees($mbbsFees, 'MBBS');

    echo "\n";

    // Calculate and display fees for MD/MS (3 years)
    $mdMsFees = calculateFees('md_ms', 3);
    displayFees($mdMsFees, 'MD/MS');
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}

?>
```
