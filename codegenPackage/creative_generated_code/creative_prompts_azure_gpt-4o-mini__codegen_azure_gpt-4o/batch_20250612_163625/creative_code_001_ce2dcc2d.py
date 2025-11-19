"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omidtak.ir
Prompt: Generate a PHP script that validates a bank card number using the algorithm outlined in the bank card check section of Omidtak's content.
Generated: DETERMINISTIC_ce2dcc2dc07cf7c0
Batch ID: 20250612_163625
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
 * Bank Card Validation Script
 *
 * This script validates a bank card number using the Luhn algorithm.
 * The Luhn algorithm is commonly used for validating credit card numbers.
 * 
 * @param string $cardNumber The bank card number to validate.
 * @return bool Returns true if the card number is valid, false otherwise.
 */

function validateCardNumber(string $cardNumber): bool
{
    // Remove any non-numeric characters (e.g., spaces, dashes).
    $cardNumber = preg_replace('/\D/', '', $cardNumber);

    // Ensure the card number contains only digits and is not empty.
    if (empty($cardNumber) || !ctype_digit($cardNumber)) {
        return false;
    }

    // Initialize variables for the Luhn algorithm.
    $sum = 0;
    $reverseDigits = str_split(strrev($cardNumber));

    // Loop through digits in reverse order.
    foreach ($reverseDigits as $index => $digit) {
        $digit = (int) $digit;

        // Double every second digit (even index in reverse order).
        if ($index % 2 === 1) {
            $digit *= 2;

            // If doubling results in a two-digit number, subtract 9.
            if ($digit > 9) {
                $digit -= 9;
            }
        }

        // Add the processed digit to the sum.
        $sum += $digit;
    }

    // The card number is valid if the sum is divisible by 10.
    return $sum % 10 === 0;
}

// Example usage:
$cardNumber = "1234 5678 9012 3456"; // Replace with the card number to validate.
if (validateCardNumber($cardNumber)) {
    echo "The card number is valid.";
} else {
    echo "The card number is invalid.";
}
?>
```
