"""
Generated Code Metadata:
========================
Original URL: https://moonpad.net
Prompt: Create a ThinkPHP helper function for string manipulation, using `helper/Str.php` as an example from the Moonpad website.
Generated: DETERMINISTIC_1e6bbf8bd136a065
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// File: helper/Str.php

if (!function_exists('str_helper')) {
    /**
     * String manipulation helper functions.
     */
    class Str
    {
        /**
         * Convert a string to uppercase.
         *
         * @param string $string The input string.
         * @return string The uppercase string.
         * @throws InvalidArgumentException If the input is not a string.
         */
        public static function toUpperCase($string)
        {
            if (!is_string($string)) {
                throw new InvalidArgumentException('Input must be a string.');
            }
            return strtoupper($string);
        }

        /**
         * Convert a string to lowercase.
         *
         * @param string $string The input string.
         * @return string The lowercase string.
         * @throws InvalidArgumentException If the input is not a string.
         */
        public static function toLowerCase($string)
        {
            if (!is_string($string)) {
                throw new InvalidArgumentException('Input must be a string.');
            }
            return strtolower($string);
        }

        /**
         * Capitalize the first letter of a string.
         *
         * @param string $string The input string.
         * @return string The string with the first letter capitalized.
         * @throws InvalidArgumentException If the input is not a string.
         */
        public static function capitalize($string)
        {
            if (!is_string($string)) {
                throw new InvalidArgumentException('Input must be a string.');
            }
            return ucfirst($string);
        }

        /**
         * Trim whitespace from both sides of a string.
         *
         * @param string $string The input string.
         * @return string The trimmed string.
         * @throws InvalidArgumentException If the input is not a string.
         */
        public static function trim($string)
        {
            if (!is_string($string)) {
                throw new InvalidArgumentException('Input must be a string.');
            }
            return trim($string);
        }

        /**
         * Check if a string contains a given substring.
         *
         * @param string $string The input string.
         * @param string $substring The substring to search for.
         * @return bool True if the substring is found, false otherwise.
         * @throws InvalidArgumentException If the inputs are not strings.
         */
        public static function contains($string, $substring)
        {
            if (!is_string($string) || !is_string($substring)) {
                throw new InvalidArgumentException('Both inputs must be strings.');
            }
            return strpos($string, $substring) !== false;
        }
    }
}
```
