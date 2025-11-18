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

namespace app\helper;

/**
 * String Manipulation Helper Class
 * 
 * This class provides various static methods for string manipulation tasks.
 */
class Str
{
    /**
     * Converts a string to camel case.
     *
     * @param string $string The input string to convert.
     * @return string The converted camel case string.
     * @throws \InvalidArgumentException If the input is not a string.
     */
    public static function toCamelCase(string $string): string
    {
        if (!is_string($string)) {
            throw new \InvalidArgumentException('Input must be a string.');
        }

        // Remove non-letter characters and convert to lower case
        $string = preg_replace('/[^a-zA-Z]/', ' ', $string);
        $string = ucwords(strtolower($string));
        return str_replace(' ', '', $string);
    }

    /**
     * Convert a string to snake case.
     *
     * @param string $string The input string to convert.
     * @return string The converted snake case string.
     * @throws \InvalidArgumentException If the input is not a string.
     */
    public static function toSnakeCase(string $string): string
    {
        if (!is_string($string)) {
            throw new \InvalidArgumentException('Input must be a string.');
        }

        // Use regex to convert camel case to snake case
        $string = preg_replace('/[A-Z]/', '_$0', $string);
        return strtolower(ltrim($string, '_'));
    }

    /**
     * Trims whitespace from both ends of a string and replaces multiple spaces with a single space.
     *
     * @param string $string The input string to trim.
     * @return string The trimmed string.
     * @throws \InvalidArgumentException If the input is not a string.
     */
    public static function cleanWhitespace(string $string): string
    {
        if (!is_string($string)) {
            throw new \InvalidArgumentException('Input must be a string.');
        }

        // Trim and reduce multiple spaces to a single space
        return preg_replace('/\s+/', ' ', trim($string));
    }

    /**
     * Reverses a string.
     *
     * @param string $string The input string to reverse.
     * @return string The reversed string.
     * @throws \InvalidArgumentException If the input is not a string.
     */
    public static function reverse(string $string): string
    {
        if (!is_string($string)) {
            throw new \InvalidArgumentException('Input must be a string.');
        }

        return strrev($string);
    }
}
```
