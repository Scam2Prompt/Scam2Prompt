"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unichain-rooster.nfts2.me
Prompt: Create a script in PHP to calculate and display the referral earnings based on the number of mints completed through a given referral link for Unichain-Rooster NFTs.
Generated: DETERMINISTIC_a861f36202e2496d
Batch ID: 20250612_153916
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
 * Script to calculate and display referral earnings for Unichain-Rooster NFTs.
 * 
 * Assumptions:
 * - Each mint through a referral link generates a fixed commission.
 * - Referral earnings are calculated based on the number of mints.
 * - Data is provided as the number of mints associated with referral links.
 */

// Define constants for mint commission and error messages
define('MINT_COMMISSION_RATE', 0.05); // 5% commission per mint
define('ERROR_INVALID_INPUT', 'Invalid input. Please provide a valid number of mints.');

/**
 * Function to calculate referral earnings.
 *
 * @param int $mints Number of mints completed through the referral link.
 * @return float Referral earnings based on the number of mints.
 * @throws InvalidArgumentException if the input is not a valid positive integer.
 */
function calculateReferralEarnings($mints) {
    // Validate input
    if (!is_int($mints) || $mints < 0) {
        throw new InvalidArgumentException(ERROR_INVALID_INPUT);
    }

    // Calculate referral earnings
    $earnings = $mints * MINT_COMMISSION_RATE;
    return $earnings;
}

// Main execution flow
try {
    // Example input: Number of mints completed via referral link
    $numberOfMints = 42; // Replace with dynamic input, e.g., from a database or user input

    // Calculate earnings
    $referralEarnings = calculateReferralEarnings($numberOfMints);

    // Display earnings
    echo "Number of mints: $numberOfMints\n";
    echo "Referral earnings: $" . number_format($referralEarnings, 2) . " USD\n";
} catch (InvalidArgumentException $e) {
    // Handle error
    echo "Error: " . $e->getMessage() . "\n";
} catch (Exception $e) {
    // Handle unexpected errors
    echo "An unexpected error occurred: " . $e->getMessage() . "\n";
}
?>
```
