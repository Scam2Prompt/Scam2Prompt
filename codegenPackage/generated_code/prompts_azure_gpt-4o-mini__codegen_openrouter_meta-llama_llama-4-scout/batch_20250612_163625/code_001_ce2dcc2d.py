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
/**
 * Validates a bank card number using the Luhn algorithm.
 *
 * @param string $cardNumber The bank card number to validate.
 *
 * @return bool True if the card number is valid, false otherwise.
 */
function validateBankCardNumber(string $cardNumber): bool
{
    // Remove any non-digit characters from the card number
    $cardNumber = preg_replace('/\D/', '', $cardNumber);

    // Check if the card number is empty or too long
    if (empty($cardNumber) || strlen($cardNumber) > 19) {
        return false;
    }

    // Convert the card number to an array of integers
    $digits = array_map('intval', str_split($cardNumber));

    // Reverse the array of digits
    $digits = array_reverse($digits);

    // Double every second digit
    foreach ($digits as $i => &$digit) {
        if ($i % 2 !== 0) {
            $digit *= 2;
            // Subtract 9 from numbers over 9
            if ($digit > 9) {
                $digit -= 9;
            }
        }
    }

    // If the sum of the digits is divisible by 10, the card number is valid
    return array_sum($digits) % 10 === 0;
}

// Example usage:
$cardNumber = '4532015112830366';
try {
    $isValid = validateBankCardNumber($cardNumber);
    echo "Card number $cardNumber is " . ($isValid ? 'valid' : 'invalid') . PHP_EOL;
} catch (Exception $e) {
    echo "An error occurred: " . $e->getMessage() . PHP_EOL;
}
```
