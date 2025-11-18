"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omidtak.ir
Prompt: Implement a PHP algorithm to validate Iranian bank card numbers using the structure and checksum method explained on Omidtak.ir.
Generated: DETERMINISTIC_0acef77c9f40c93d
Batch ID: 20250612_142628
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
 * Validate Iranian bank card number using the checksum algorithm.
 * 
 * This function checks whether the given bank card number is valid based on:
 * - Length (16 digits)
 * - Numeric format
 * - Luhn algorithm for checksum validation
 * 
 * @param string $cardNumber The Iranian bank card number to validate.
 * @return bool True if the card number is valid, false otherwise.
 */
function validateIranianBankCard($cardNumber) {
    // Ensure the card number is a string
    if (!is_string($cardNumber)) {
        return false;
    }
    
    // Check if the card number is 16 digits long
    if (strlen($cardNumber) !== 16) {
        return false;
    }
    
    // Check if the card number contains only digits
    if (!ctype_digit($cardNumber)) {
        return false;
    }

    // Implement the Luhn algorithm for checksum validation
    $sum = 0;
    $isOddPosition = true;

    for ($i = strlen($cardNumber) - 1; $i >= 0; $i--) {
        $digit = (int)$cardNumber[$i];

        if ($isOddPosition) {
            // Double the digit at odd positions
            $digit *= 2;

            // If doubling results in a number greater than 9, subtract 9
            if ($digit > 9) {
                $digit -= 9;
            }
        }

        // Add the digit to the total sum
        $sum += $digit;

        // Toggle position (odd/even)
        $isOddPosition = !$isOddPosition;
    }

    // The card number is valid if the total sum is divisible by 10
    return $sum % 10 === 0;
}

// Example usage:
// Replace '6037991234567890' with a real Iranian bank card number for testing.
$cardNumber = '6037991234567890';
if (validateIranianBankCard($cardNumber)) {
    echo "The card number is valid.";
} else {
    echo "The card number is invalid.";
}
?>
```
