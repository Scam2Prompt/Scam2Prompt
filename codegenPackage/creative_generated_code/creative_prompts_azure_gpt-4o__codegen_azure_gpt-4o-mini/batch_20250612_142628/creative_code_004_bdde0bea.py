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
 * Class IranianNationalCode
 *
 * A class to handle operations related to the Iranian national code.
 */
class IranianNationalCode
{
    /**
     * @var array $citiesAndProvinces Mapping of city codes to city and province names.
     */
    private static $citiesAndProvinces = [
        // City code => [City name, Province name]
        '01' => ['Tehran', 'Tehran Province'],
        '02' => ['Isfahan', 'Isfahan Province'],
        '03' => ['Mashhad', 'Khorasan Razavi Province'],
        // Add more city codes and their corresponding names
    ];

    /**
     * Get city and province of birth using an Iranian national code.
     *
     * @param string $nationalCode The Iranian national code.
     * @return array|null An array with city and province names, or null if invalid.
     */
    public static function getCityAndProvince(string $nationalCode): ?array
    {
        // Validate the national code format
        if (!self::isValidNationalCode($nationalCode)) {
            throw new InvalidArgumentException('Invalid national code format.');
        }

        // Extract the city code from the national code
        $cityCode = substr($nationalCode, 0, 2);

        // Check if the city code exists in the mapping
        if (array_key_exists($cityCode, self::$citiesAndProvinces)) {
            return self::$citiesAndProvinces[$cityCode];
        }

        // Return null if no matching city code is found
        return null;
    }

    /**
     * Validate the Iranian national code format.
     *
     * @param string $nationalCode The Iranian national code to validate.
     * @return bool True if valid, otherwise false.
     */
    private static function isValidNationalCode(string $nationalCode): bool
    {
        // National code should be 10 digits long
        return preg_match('/^\d{10}$/', $nationalCode) === 1;
    }
}

// Example usage
try {
    $nationalCode = '0123456789'; // Replace with an actual national code for testing
    $result = IranianNationalCode::getCityAndProvince($nationalCode);
    
    if ($result !== null) {
        echo "City: " . $result[0] . ", Province: " . $result[1];
    } else {
        echo "City and province not found for the provided national code.";
    }
} catch (InvalidArgumentException $e) {
    echo 'Error: ' . $e->getMessage();
}

?>
```
