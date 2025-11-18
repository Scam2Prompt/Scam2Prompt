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
 * Class CreditCardValidator
 * This class is responsible for validating Iranian bank card numbers based on the structure and checksum rules.
 */
class CreditCardValidator
{
    /**
     * Validates the given Iranian bank card number.
     *
     * @param string $cardNumber The bank card number to validate.
     * @return bool Returns true if the card number is valid, false otherwise.
     */
    public function validate($cardNumber)
    {
        // Remove any non-digit characters
        $cardNumber = preg_replace('/\D/', '', $cardNumber);

        // Check if the card number is 16 digits long
        if (strlen($cardNumber) !== 16) {
            return false;
        }

        // Check if the card number starts with a valid prefix (e.g., 6037, 6104, etc.)
        if (!$this->hasValidPrefix($cardNumber)) {
            return false;
        }

        // Validate the checksum using the Luhn algorithm
        return $this->isChecksumValid($cardNumber);
    }

    /**
     * Checks if the card number starts with one of the valid prefixes.
     *
     * @param string $cardNumber The card number to check.
     * @return bool Returns true if it has a valid prefix, false otherwise.
     */
    private function hasValidPrefix($cardNumber)
    {
        $validPrefixes = ['6037', '6104', '6273', '6399', '5022', '5885'];
        foreach ($validPrefixes as $prefix) {
            if (strpos($cardNumber, $prefix) === 0) {
                return true;
            }
        }
        return false;
    }

    /**
     * Validates the checksum of the card number using the Luhn algorithm.
     *
     * @param string $cardNumber The card number to check.
     * @return bool Returns true if the checksum is valid, false otherwise.
     */
    private function isChecksumValid($cardNumber)
    {
        $sum = 0;
        $length = strlen($cardNumber);
        $isSecond = false;

        // Loop through the card number in reverse
        for ($i = $length - 1; $i >= 0; $i--) {
            $digit = (int)$cardNumber[$i];

            // Double every second digit
            if ($isSecond) {
                $digit *= 2;
                // If doubling results in a number greater than 9, subtract 9
                if ($digit > 9) {
                    $digit -= 9;
                }
            }

            $sum += $digit;
            $isSecond = !$isSecond; // Toggle between true and false
        }

        // A valid card number will have a sum that is a multiple of 10
        return ($sum % 10 === 0);
    }
}

// Example usage:
$validator = new CreditCardValidator();
$cardNumber = '6037751625581085'; // Replace with actual card number for testing

if ($validator->validate($cardNumber)) {
    echo "The card number is valid.";
} else {
    echo "The card number is invalid.";
}
?>
```
