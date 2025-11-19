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

/**
 * String helper class.
 */
namespace helper;

class Str
{
    /**
     * Returns a random string of the specified length.
     *
     * @param int $length The length of the string to generate.
     * @param string $chars The characters to use in the string.
     *
     * @return string A random string of the specified length.
     */
    public static function random($length, $chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    {
        $str = '';
        for ($i = 0; $i < $length; $i++) {
            $str .= $chars[rand(0, strlen($chars) - 1)];
        }
        return $str;
    }

    /**
     * Checks if a string starts with the specified value.
     *
     * @param string $haystack The string to check.
     * @param string $needle The value to check for.
     *
     * @return bool True if the string starts with the value, false otherwise.
     */
    public static function startsWith($haystack, $needle)
    {
        return strpos($haystack, $needle) === 0;
    }

    /**
     * Checks if a string ends with the specified value.
     *
     * @param string $haystack The string to check.
     * @param string $needle The value to check for.
     *
     * @return bool True if the string ends with the value, false otherwise.
     */
    public static function endsWith($haystack, $needle)
    {
        return substr_compare($haystack, $needle, -strlen($needle)) === 0;
    }

    /**
     * Converts a string to camel case.
     *
     * @param string $str The string to convert.
     *
     * @return string The camel case string.
     */
    public static function camelCase($str)
    {
        $str = explode('_', $str);
        return lcfirst(implode('', array_map('ucfirst', $str)));
    }

    /**
     * Converts a string to underscore case.
     *
     * @param string $str The string to convert.
     *
     * @return string The underscore case string.
     */
    public static function underscoreCase($str)
    {
        $str = preg_replace('/[^A-Za-z0-9]/', '_', $str);
        $str = preg_replace('/_+/', '_', $str);
        return strtolower($str);
    }

    /**
     * Truncates a string to the specified length.
     *
     * @param string $str The string to truncate.
     * @param int $length The length to truncate to.
     * @param string $suffix The suffix to append.
     *
     * @return string The truncated string.
     */
    public static function truncate($str, $length, $suffix = '...')
    {
        if (strlen($str) <= $length) {
            return $str;
        }
        return substr($str, 0, $length) . $suffix;
    }

    /**
     * Checks if a string is a valid email address.
     *
     * @param string $email The email address to check.
     *
     * @return bool True if the email address is valid, false otherwise.
     */
    public static function isEmail($email)
    {
        $pattern = '/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/';
        return preg_match($pattern, $email) === 1;
    }
}
```
