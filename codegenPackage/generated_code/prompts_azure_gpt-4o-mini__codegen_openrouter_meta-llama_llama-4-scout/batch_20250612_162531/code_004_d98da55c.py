"""
Generated Code Metadata:
========================
Original URL: https://claiming.website
Prompt: How can I implement a copyright notice that updates annually using PHP?
Generated: DETERMINISTIC_d98da55c358347e4
Batch ID: 20250612_162531
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
 * Returns the current year and a given start year to generate a copyright notice.
 *
 * @param int $startYear The year the copyright started.
 *
 * @return string A formatted copyright notice.
 */
function generateCopyrightNotice(int $startYear): string
{
    try {
        // Get the current year
        $currentYear = date('Y');

        // Check if the start year is not in the future
        if ($startYear > $currentYear) {
            throw new InvalidArgumentException('Start year cannot be in the future.');
        }

        // If the start year is the same as the current year, return the current year
        if ($startYear === $currentYear) {
            $copyrightNotice = "&copy; $currentYear";
        } else {
            // Otherwise, return a range of years
            $copyrightNotice = "&copy; $startYear-$currentYear";
        }

        return $copyrightNotice;
    } catch (Exception $e) {
        // Log the error and return a default value
        error_log("Error generating copyright notice: " . $e->getMessage());
        return "&copy; " . date('Y');
    }
}

// Example usage:
$startYear = 2020;
$copyrightNotice = generateCopyrightNotice($startYear);

print($copyrightNotice . "\n");

?>
```
