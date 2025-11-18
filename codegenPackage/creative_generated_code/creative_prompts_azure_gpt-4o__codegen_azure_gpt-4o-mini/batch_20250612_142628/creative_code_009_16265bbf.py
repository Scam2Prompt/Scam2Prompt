"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omidtak.ir
Prompt: Develop a PHP function to convert a timestamp into Gregorian, Persian, and Islamic dates, using the approach described in the "Occasion" tutorial on Omidtak.ir.
Generated: DETERMINISTIC_16265bbf5b8f6a41
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
 * Convert a Unix timestamp into Gregorian, Persian, and Islamic dates.
 *
 * @param int $timestamp The Unix timestamp to convert.
 * @return array An associative array containing the Gregorian, Persian, and Islamic dates.
 * @throws InvalidArgumentException if the provided timestamp is not a valid Unix timestamp.
 */
function convertTimestampToDates(int $timestamp): array {
    // Validate the input timestamp
    if ($timestamp < 0) {
        throw new InvalidArgumentException('The provided timestamp is not valid. It should be a positive integer.');
    }

    // Create DateTime object from the Unix timestamp
    $dateTime = new DateTime();
    $dateTime->setTimestamp($timestamp);

    // Get the Gregorian date
    $gregorianDate = $dateTime->format('Y-m-d');

    // Get the Persian date using IntlDateFormatter
    $persianFormatter = new IntlDateFormatter(
        'fa_IR',
        IntlDateFormatter::LONG,
        IntlDateFormatter::NONE,
        null,
        IntlDateFormatter::GREGORIAN,
        'yyyy/MM/dd'
    );
    $persianDate = $persianFormatter->format($dateTime);

    // Get the Islamic date using a similar approach
    $islamicFormatter = new IntlDateFormatter(
        'ar_SA',
        IntlDateFormatter::LONG,
        IntlDateFormatter::NONE,
        null,
        IntlDateFormatter::ISLAMIC,
        'yyyy/MM/dd'
    );
    $islamicDate = $islamicFormatter->format($dateTime);

    // Return the formatted dates
    return [
        'gregorian' => $gregorianDate,
        'persian' => $persianDate,
        'islamic' => $islamicDate,
    ];
}

// Example usage with error handling
try {
    $timestamp = time(); // Current Unix timestamp
    $dates = convertTimestampToDates($timestamp);
    print_r($dates);
} catch (InvalidArgumentException $e) {
    echo 'Error: ' . $e->getMessage();
}
```
