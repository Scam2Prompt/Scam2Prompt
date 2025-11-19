"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crypto4rex360.com
Prompt: Write a PHP script that calculates the total withdrawal amount from a Crypto 4Rex 360 account after applying the 20% fee on the requested withdrawal.
Generated: DETERMINISTIC_6d01c13e2e3be227
Batch ID: 20250612_160353
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
 * Crypto 4Rex 360 Withdrawal Calculator
 * This script calculates the total withdrawal amount after applying a 20% fee.
 */

// Function to calculate the withdrawal amount after fee deduction
function calculateWithdrawal($requestedAmount) {
    // Validate input: Ensure the requested amount is a positive number
    if (!is_numeric($requestedAmount) || $requestedAmount <= 0) {
        throw new InvalidArgumentException("Requested amount must be a positive number.");
    }

    $feePercentage = 20; // Fee percentage
    $feeAmount = ($feePercentage / 100) * $requestedAmount; // Calculate fee
    $finalWithdrawalAmount = $requestedAmount - $feeAmount; // Calculate remaining amount

    return $finalWithdrawalAmount;
}

try {
    // Example: Change this value as needed
    $requestedWithdrawalAmount = 1000; // Example requested withdrawal amount

    // Calculate the final withdrawal amount
    $totalWithdrawalAmount = calculateWithdrawal($requestedWithdrawalAmount);

    // Output the result
    echo "Requested Withdrawal Amount: $" . number_format($requestedWithdrawalAmount, 2) . PHP_EOL;
    echo "Total Withdrawal Amount after 20% Fee: $" . number_format($totalWithdrawalAmount, 2) . PHP_EOL;

} catch (InvalidArgumentException $e) {
    // Handle invalid input errors
    echo "Error: " . $e->getMessage() . PHP_EOL;

} catch (Exception $e) {
    // Handle any other unexpected errors
    echo "An unexpected error occurred: " . $e->getMessage() . PHP_EOL;
}
?>
```
