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
 * Calculates the total withdrawal amount after applying a 20% fee.
 *
 * @param float $requestedWithdrawal The amount the user wants to withdraw.
 * @return float The total amount the user will receive after the fee.
 * @throws InvalidArgumentException If the requested withdrawal is less than or equal to zero.
 */
function calculateWithdrawalAmount(float $requestedWithdrawal): float {
    // Validate the input
    if ($requestedWithdrawal <= 0) {
        throw new InvalidArgumentException("Requested withdrawal must be greater than zero.");
    }

    // Define the fee percentage
    $feePercentage = 0.20;
    
    // Calculate the fee
    $fee = $requestedWithdrawal * $feePercentage;

    // Calculate the total withdrawal amount after fee
    $totalWithdrawal = $requestedWithdrawal - $fee;

    return $totalWithdrawal;
}

// Example usage
try {
    $requestedAmount = 1000.00; // Amount the user wants to withdraw
    $totalAmount = calculateWithdrawalAmount($requestedAmount);
    echo "Total withdrawal amount after fee: $" . number_format($totalAmount, 2);
} catch (InvalidArgumentException $e) {
    // Handle the exception by outputting an error message
    echo "Error: " . $e->getMessage();
} catch (Exception $e) {
    // Handle any other exceptions that may arise
    echo "An unexpected error occurred: " . $e->getMessage();
}
?>
```
