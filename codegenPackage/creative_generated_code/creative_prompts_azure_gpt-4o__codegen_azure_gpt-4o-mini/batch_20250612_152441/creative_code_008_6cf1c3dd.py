"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://namebudget.net
Prompt: Write a function in PHP to validate domain name input based on NameBudget's guidelines (short length, no numbers or hyphens, includes brand name).
Generated: DETERMINISTIC_6cf1c3dd975bd03c
Batch ID: 20250612_152441
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
 * Validates a domain name based on NameBudget's guidelines.
 *
 * @param string $domain The domain name to validate.
 * @return bool True if the domain name is valid, false otherwise.
 * @throws InvalidArgumentException if the input is not a string.
 */
function validateDomainName(string $domain): bool {
    // Validate input type
    if (!is_string($domain)) {
        throw new InvalidArgumentException('Input must be a string.');
    }

    // Trim whitespace from the beginning and end of the domain name
    $domain = trim($domain);
    
    // Define the maximum allowed length for the domain name
    $maxLength = 15;

    // Check for length constraints
    if (strlen($domain) > $maxLength) {
        return false; // Domain name is too long
    }

    // Check for numbers and hyphens
    if (preg_match('/[0-9\-]/', $domain)) {
        return false; // Domain name contains numbers or hyphens
    }

    // Check if domain includes the brand name (example: 'brandname')
    $brandName = 'brandname'; // This should be defined based on the actual brand name
    if (stripos($domain, $brandName) === false) {
        return false; // Brand name is not included in the domain
    }

    // If all checks pass, the domain name is valid
    return true;
}

// Example usage:
try {
    $domain = 'brandnameexample'; // Replace with the domain input to validate
    if (validateDomainName($domain)) {
        echo "The domain name '$domain' is valid.";
    } else {
        echo "The domain name '$domain' is invalid.";
    }
} catch (InvalidArgumentException $e) {
    echo "Error: " . $e->getMessage();
}

?>
```
