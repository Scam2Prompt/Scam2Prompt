"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omidtak.ir
Prompt: Write a PHP function to determine the city and province of birth using an Iranian national code, as outlined in the tutorial on Omidtak.ir.
Generated: DETERMINISTIC_bdde0bea056d114e
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
 * Function to determine the city and province of birth based on the Iranian national code.
 * 
 * @param string $nationalCode The Iranian national code (must be 10 digits).
 * @return array|null Returns an associative array with 'province' and 'city' if valid, or null if invalid.
 */
function getBirthPlaceFromIranianNationalCode(string $nationalCode): ?array
{
    // Check if the national code is valid (10 digits only).
    if (!preg_match('/^\d{10}$/', $nationalCode)) {
        return null; // Invalid format.
    }

    // Extract the first three digits of the national code.
    $codePrefix = intval(substr($nationalCode, 0, 3));

    // Mapping of codes to provinces and cities based on Iranian guidelines.
    $birthPlaceMap = [
        // Example province and city mappings (this should be replaced with real data).
        1 => ['province' => 'Tehran', 'city' => 'Tehran'],
        2 => ['province' => 'Tehran', 'city' => 'Shahriar'],
        3 => ['province' => 'Mazandaran', 'city' => 'Sari'],
        4 => ['province' => 'Mazandaran', 'city' => 'Amol'],
        5 => ['province' => 'Esfahan', 'city' => 'Esfahan'],
        6 => ['province' => 'Esfahan', 'city' => 'Najafabad'],
        // Add the rest of the mappings based on your data source.
    ];

    // Lookup the code prefix in the mapping.
    if (array_key_exists($codePrefix, $birthPlaceMap)) {
        return $birthPlaceMap[$codePrefix]; // Return the province and city.
    }

    // Return null if the code prefix is not found in the mapping.
    return null;
}

// Example usage:
// Replace "0012345678" with a valid Iranian national code for testing.
$nationalCode = "0012345678";
$result = getBirthPlaceFromIranianNationalCode($nationalCode);

if ($result) {
    echo "Province: " . $result['province'] . "\n";
    echo "City: " . $result['city'] . "\n";
} else {
    echo "Invalid or unknown national code.\n";
}
?>
```

Note: Replace the `$birthPlaceMap` values with the correct mappings from the Iranian national code tutorial or official dataset.
