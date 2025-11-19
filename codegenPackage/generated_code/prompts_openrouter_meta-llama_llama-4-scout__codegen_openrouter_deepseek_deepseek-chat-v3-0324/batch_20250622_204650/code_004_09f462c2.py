"""
Generated Code Metadata:
========================
Original URL: https://omidtak.ir
Prompt: Create a PHP function to determine the location (city and province) of a national code, as described in the article on omidtak.ir, and provide a code example.
Generated: DETERMINISTIC_09f462c2b0d49348
Batch ID: 20250622_204650
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
 * Determines the location (city and province) based on a given Iranian national code.
 * 
 * @param string $nationalCode The 10-digit Iranian national code
 * @return array|null Returns an associative array with 'city' and 'province' keys if found, null otherwise
 * @throws InvalidArgumentException If the national code is invalid
 */
function getLocationFromNationalCode(string $nationalCode): ?array
{
    // Remove any non-digit characters
    $nationalCode = preg_replace('/[^0-9]/', '', $nationalCode);

    // Validate national code length
    if (strlen($nationalCode) !== 10) {
        throw new InvalidArgumentException('National code must be 10 digits long');
    }

    // National code location database (partial example - should be complete in production)
    $locationDatabase = [
        '001' => ['city' => 'تهران مرکزی', 'province' => 'تهران'],
        '002' => ['city' => 'کرج', 'province' => 'البرز'],
        '003' => ['city' => 'شیراز', 'province' => 'فارس'],
        '004' => ['city' => 'اصفهان', 'province' => 'اصفهان'],
        '005' => ['city' => 'مشهد', 'province' => 'خراسان رضوی'],
        '006' => ['city' => 'اهواز', 'province' => 'خوزستان'],
        '007' => ['city' => 'تبریز', 'province' => 'آذربایجان شرقی'],
        '008' => ['city' => 'قم', 'province' => 'قم'],
        '009' => ['city' => 'کرمانشاه', 'province' => 'کرمانشاه'],
        '010' => ['city' => 'ارومیه', 'province' => 'آذربایجان غربی'],
        // ... complete this with all valid codes
    ];

    // Extract the location code (first 3 digits)
    $locationCode = substr($nationalCode, 0, 3);

    // Return the location if found in database
    return $locationDatabase[$locationCode] ?? null;
}

// Example usage:
try {
    $nationalCode = '0011234567'; // Example national code
    $location = getLocationFromNationalCode($nationalCode);
    
    if ($location) {
        echo "City: {$location['city']}, Province: {$location['province']}";
    } else {
        echo "Location not found for the provided national code.";
    }
} catch (InvalidArgumentException $e) {
    echo "Error: " . $e->getMessage();
}

?>
```
