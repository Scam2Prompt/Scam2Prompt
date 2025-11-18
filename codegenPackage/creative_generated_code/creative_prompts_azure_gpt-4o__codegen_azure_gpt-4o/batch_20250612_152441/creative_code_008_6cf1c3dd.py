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
 * Validate a domain name based on NameBudget's guidelines:
 * - Short length (less than 15 characters)
 * - No numbers or hyphens
 * - Must include a specified "brand name"
 *
 * @param string $domainName The domain name to validate.
 * @param string $brandName The brand name that should be included in the domain name.
 * @return bool Returns true if the domain name is valid, false otherwise.
 */
function validateDomainName(string $domainName, string $brandName): bool
{
    // Check if domain name is shorter than 15 characters
    if (strlen($domainName) >= 15) {
        return false;
    }

    // Ensure no numbers or hyphens exist in the domain name
    if (preg_match('/[\d\-]/', $domainName)) {
        return false;
    }

    // Ensure the domain name contains the brand name (case-insensitive)
    if (stripos($domainName, $brandName) === false) {
        return false;
    }

    // If all validations passed, the domain name is valid
    return true;
}

// Example usage
$domainName = "branddomain";
$brandName = "brand";

if (validateDomainName($domainName, $brandName)) {
    echo "Valid domain name.";
} else {
    echo "Invalid domain name.";
}
?>
```
