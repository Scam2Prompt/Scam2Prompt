"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zelenina-hrbek.cz
Prompt: Develop a PHP function that validates a phone number format for the contact number 603 227 628.
Generated: DETERMINISTIC_20bfe15b0be862de
Batch ID: 20250612_163324
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
 * Validates the format of a phone number.
 *
 * This function checks whether the provided phone number matches
 * the expected format: 603 227 628 (3 digits, space, 3 digits, space, 3 digits).
 *
 * @param string $phoneNumber The phone number to validate.
 * @return bool True if the phone number is valid, false otherwise.
 */
function validatePhoneNumber(string $phoneNumber): bool {
    // Define the regex pattern for the expected phone number format
    $pattern = '/^\d{3} \d{3} \d{3}$/';

    // Check if the phone number matches the pattern
    if (preg_match($pattern, $phoneNumber)) {
        return true; // Valid phone number format
    } else {
        return false; // Invalid phone number format
    }
}

// Example usage
$contactNumber = "603 227 628";

if (validatePhoneNumber($contactNumber)) {
    echo "The phone number '$contactNumber' is valid.";
} else {
    echo "The phone number '$contactNumber' is invalid.";
}

?>
```
