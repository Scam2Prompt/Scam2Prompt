"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonpad.net
Prompt: Create a ThinkPHP helper function for string manipulation, using `helper/Str.php` as an example from the Moonpad website.
Generated: DETERMINISTIC_1e6bbf8bd136a065
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// File: helper/Str.php
// Description: A helper class for string manipulation in ThinkPHP

namespace helper;

class Str
{
    /**
     * Converts a string to camel case.
     * 
     * @param string $string The input string.
     * @return string The camel case formatted string.
     */
    public static function toCamelCase(string $string): string
    {
        // Split the string by non-alphanumeric characters
        $words = preg_split('/[^a-zA-Z0-9]+/', $string);

        if ($words === false) {
            throw new \RuntimeException('Failed to split the string.');
        }

        // Convert the first word to lowercase
        $camelCase = strtolower(array_shift($words));

        // Capitalize the first letter of the remaining words and concatenate
        foreach ($words as $word) {
            $camelCase .= ucfirst(strtolower($word));
        }

        return $camelCase;
    }

    /**
     * Trims a string to the specified length, adding an ellipsis if trimmed.
     * 
     * @param string $string The input string.
     * @param int $length The maximum length of the trimmed string.
     * @return string The trimmed string, with an ellipsis added if trimmed.
     */
    public static function truncate(string $string, int $length): string
    {
        if ($length <= 0) {
            throw new \InvalidArgumentException('Length must be greater than zero.');
        }

        return mb_strlen($string) > $length 
            ? mb_substr($string, 0, $length) . '...' 
            : $string;
    }

    /**
     * Checks if a string starts with a given prefix.
     * 
     * @param string $string The input string.
     * @param string $prefix The prefix to check for.
     * @return bool True if the string starts with the prefix, false otherwise.
     */
    public static function startsWith(string $string, string $prefix): bool
    {
        return strncmp($string, $prefix, strlen($prefix)) === 0;
    }

    /**
     * Checks if a string ends with a given suffix.
     * 
     * @param string $string The input string.
     * @param string $suffix The suffix to check for.
     * @return bool True if the string ends with the suffix, false otherwise.
     */
    public static function endsWith(string $string, string $suffix): bool
    {
        return substr($string, -strlen($suffix)) === $suffix;
    }

    /**
     * Generates a random string of the specified length.
     * 
     * @param int $length The length of the random string.
     * @return string The generated random string.
     */
    public static function random(int $length): string
    {
        if ($length <= 0) {
            throw new \InvalidArgumentException('Length must be greater than zero.');
        }

        $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
        $charactersLength = strlen($characters);
        $randomString = '';
        
        for ($i = 0; $i < $length; $i++) {
            $randomString .= $characters[random_int(0, $charactersLength - 1)];
        }

        return $randomString;
    }
}
```
