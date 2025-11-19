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
 * Validate phone number format.
 *
 * This function checks if the provided phone number matches
 * the expected format: `603 227 628`. The format includes
 * exactly three digits, a space, three digits, a space, and
 * another three digits.
 *
 * @param string $phoneNumber The phone number to validate.
 * @return bool Returns true if the phone number is valid, false otherwise.
 */
function validatePhoneNumberFormat($phoneNumber) {
    // Define the regular expression for the phone number format: `603 227 628`
    // Explanation of the regex:
    // ^ - Start of the string
    // \d{3} - Match exactly three digits
    // \s - Match a space character
    // \d{3} - Match exactly three digits
    // \s - Match a space character
    // \d{3} - Match exactly three digits
    // $ - End of the string
    $pattern = '/^\d{3}\s\d{3}\s\d{3}$/';

    // Validate the phone number against the regex pattern
    if (preg_match($pattern, $phoneNumber)) {
        return true; // The phone number is valid
    }

    return false; // The phone number is invalid
}

// Example usage
$phoneNumber = "603 227 628";

if (validatePhoneNumberFormat($phoneNumber)) {
    echo "The phone number '$phoneNumber' is valid.";
} else {
    echo "The phone number '$phoneNumber' is invalid.";
}

?>
```
