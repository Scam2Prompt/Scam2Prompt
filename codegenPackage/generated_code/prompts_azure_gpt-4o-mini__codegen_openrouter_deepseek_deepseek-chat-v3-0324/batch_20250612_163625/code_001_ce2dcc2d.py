"""
Generated Code Metadata:
========================
Original URL: https://omidtak.ir
Prompt: Generate a PHP script that validates a bank card number using the algorithm outlined in the bank card check section of Omidtak's content.
Generated: DETERMINISTIC_ce2dcc2dc07cf7c0
Batch ID: 20250612_163625
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
 * Validates a bank card number using the Luhn algorithm.
 *
 * @param string $cardNumber The card number to validate (digits only, no spaces/hyphens)
 * @return bool True if the card number is valid, false otherwise
 * @throws InvalidArgumentException If the input is not a string of digits
 */
function isValidCardNumber(string $cardNumber): bool
{
    // Remove any non-digit characters
    $cleanedNumber = preg_replace('/\D/', '', $cardNumber);

    // Check if the cleaned number is empty
    if (empty($cleanedNumber)) {
        throw new InvalidArgumentException('Card number must contain at least one digit');
    }

    $sum = 0;
    $length = strlen($cleanedNumber);

    // Iterate through each digit from right to left
    for ($i = 0; $i < $length; $i++) {
        $digit = (int)$cleanedNumber[$length - 1 - $i];

        // Double every second digit
        if ($i % 2 === 1) {
            $digit *= 2;
            // If the result is greater than 9, add the digits
            if ($digit > 9) {
                $digit = ($digit % 10) + 1;
            }
        }

        $sum += $digit;
    }

    // The card is valid if the sum is a multiple of 10
    return ($sum % 10 === 0);
}

// Example usage:
try {
    $cardNumber = '4111111111111111'; // Test Visa card number
    if (isValidCardNumber($cardNumber)) {
        echo "Card number {$cardNumber} is valid.";
    } else {
        echo "Card number {$cardNumber} is invalid.";
    }
} catch (InvalidArgumentException $e) {
    echo "Error: " . $e->getMessage();
}

?>
```
