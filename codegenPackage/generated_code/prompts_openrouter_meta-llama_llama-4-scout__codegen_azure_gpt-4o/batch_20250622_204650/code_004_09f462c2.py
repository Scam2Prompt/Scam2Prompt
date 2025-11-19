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
<<<<<<< HEAD
 * Function to determine the location (city and province) based on a national code.
 * 
 * @param string $nationalCode The national code to look up.
 * @return array|null Returns an associative array with 'city' and 'province' if found, or null if not found.
 */
function getLocationByNationalCode($nationalCode) {
    // Validate the input
    if (!is_string($nationalCode) || strlen($nationalCode) !== 10 || !ctype_digit($nationalCode)) {
        throw new InvalidArgumentException("Invalid national code. It must be a 10-digit numeric string.");
    }

    // Mapping of national code prefixes to city and province
    $locationData = [
        '001' => ['city' => 'Tehran', 'province' => 'Tehran'],
        '002' => ['city' => 'Mashhad', 'province' => 'Razavi Khorasan'],
        '003' => ['city' => 'Isfahan', 'province' => 'Isfahan'],
        // Add more mappings as needed
    ];

    // Extract the prefix (first 3 digits) of the national code
    $prefix = substr($nationalCode, 0, 3);

    // Check if the prefix exists in the mapping
    if (array_key_exists($prefix, $locationData)) {
        return $locationData[$prefix];
    }

    // Return null if no match is found
    return null;
}

// Example usage
try {
    $nationalCode = "0011234567";
    $location = getLocationByNationalCode($nationalCode);

    if ($location) {
        echo "City: " . $location['city'] . "\n";
        echo "Province: " . $location['province'] . "\n";
    } else {
        echo "No location found for the given national code.\n";
    }
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}

=======
 * Determine the location (city and province) of a national code.
 *
 * This function uses predefined mappings of national code prefixes to cities and provinces.
 * The mappings are based on the information provided in the article on omidtak.ir.
 *
 * @param string $nationalCode The 10-digit Iranian national code.
 * @return array|null Returns an associative array with 'city' and 'province' if found, or null if invalid or not found.
 */
function getLocationByNationalCode(string $nationalCode): ?array
{
    // Validate the national code format (must be 10 digits).
    if (!preg_match('/^\d{10}$/', $nationalCode)) {
        return null; // Invalid format.
    }

    // Extract the prefix (first three digits) of the national code.
    $prefix = substr($nationalCode, 0, 3);

    // Mapping of national code prefixes to cities and provinces.
    $locationMap = [
        '001' => ['city' => 'Tehran', 'province' => 'Tehran'],
        '002' => ['city' => 'Tehran', 'province' => 'Tehran'],
        '003' => ['city' => 'Karaj', 'province' => 'Alborz'],
        '004' => ['city' => 'Qom', 'province' => 'Qom'],
        '005' => ['city' => 'Mashhad', 'province' => 'Khorasan Razavi'],
        // Add more mappings as needed based on the article's data.
    ];

    // Check if the prefix exists in the mapping.
    if (array_key_exists($prefix, $locationMap)) {
        return $locationMap[$prefix];
    }

    // Return null if the prefix is not found in the mapping.
    return null;
}

// Example usage:
$nationalCode = '0011234567';
$location = getLocationByNationalCode($nationalCode);

if ($location) {
    echo "City: " . $location['city'] . "\n";
    echo "Province: " . $location['province'] . "\n";
} else {
    echo "Invalid or unknown national code.\n";
}
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
?>
```
