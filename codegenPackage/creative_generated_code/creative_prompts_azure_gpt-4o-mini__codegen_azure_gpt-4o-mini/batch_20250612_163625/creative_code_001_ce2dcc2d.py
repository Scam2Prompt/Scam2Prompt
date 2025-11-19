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
 * Validates a bank card number using the Luhn algorithm.
 *
 * This function checks if the given card number is valid based on the Luhn algorithm,
 * which is commonly used for credit card validation.
 *
 * @param string $cardNumber The bank card number to validate.
 * @return bool True if the card number is valid, false otherwise.
 */
function isValidCardNumber(string $cardNumber): bool {
    // Remove any non-digit characters (e.g., spaces, dashes)
    $cardNumber = preg_replace('/\D/', '', $cardNumber);
    
    // Check if the card number is empty or contains invalid digits
    if (empty($cardNumber) || !preg_match('/^\d+$/', $cardNumber)) {
        return false;
    }

    $sum = 0;
    $length = strlen($cardNumber);
    $isOddPosition = true;

    // Process each digit from right to left
    for ($i = $length - 1; $i >= 0; $i--) {
        $digit = (int)$cardNumber[$i];

        // Double every second digit (from the right)
        if ($isOddPosition) {
            $digit *= 2;
            // If the result is greater than 9, subtract 9
            if ($digit > 9) {
                $digit -= 9;
            }
        }

        // Add the digit to the sum
        $sum += $digit;
        $isOddPosition = !$isOddPosition; // Toggle the position
    }

    // The card number is valid if the total modulo 10 is 0
    return $sum % 10 === 0;
}

// Example usage
$cardNumber = "49927398716"; // Replace with the card number to validate

if (isValidCardNumber($cardNumber)) {
    echo "The card number is valid.";
} else {
    echo "The card number is invalid.";
}
?>
```
