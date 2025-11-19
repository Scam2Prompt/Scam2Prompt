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
 * @param string $cardNumber The bank card number to validate.
 * @return bool Returns true if the card number is valid, false otherwise.
 */
function validateCardNumber(string $cardNumber): bool {
    // Remove any non-digit characters from the card number
    $cardNumber = preg_replace('/\D/', '', $cardNumber);

    // Check if the card number is empty or not numeric
    if (empty($cardNumber) || !is_numeric($cardNumber)) {
        throw new InvalidArgumentException('Invalid card number provided.');
    }

    $sum = 0;
    $length = strlen($cardNumber);
    $isEvenPosition = false;

    // Loop through the card number from right to left
    for ($i = $length - 1; $i >= 0; $i--) {
        $digit = (int)$cardNumber[$i];

        // Double every second digit
        if ($isEvenPosition) {
            $digit *= 2;
            // If doubling results in a number greater than 9, subtract 9
            if ($digit > 9) {
                $digit -= 9;
            }
        }

        // Add the digit to the sum
        $sum += $digit;
        // Toggle the position for the next iteration
        $isEvenPosition = !$isEvenPosition;
    }

    // A valid card number will have a sum that is a multiple of 10
    return $sum % 10 === 0;
}

// Example usage
try {
    $cardNumber = '4539 1488 0343 6467'; // Example card number
    if (validateCardNumber($cardNumber)) {
        echo "The card number is valid.";
    } else {
        echo "The card number is invalid.";
    }
} catch (InvalidArgumentException $e) {
    echo "Error: " . $e->getMessage();
}
?>
```
