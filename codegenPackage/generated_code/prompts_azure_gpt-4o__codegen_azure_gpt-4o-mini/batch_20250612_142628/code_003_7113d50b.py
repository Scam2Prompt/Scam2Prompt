"""
Generated Code Metadata:
========================
Original URL: https://omidtak.ir
Prompt: Develop a PHP function to display occasions (Gregorian, Persian, and Islamic dates) for a given timestamp, based on the tutorial provided on Omidtak.ir.
Generated: DETERMINISTIC_7113d50bb068016e
Batch ID: 20250612_142628
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
 * Class DateConverter
 * A class to convert a given timestamp into Gregorian, Persian, and Islamic dates.
 */
class DateConverter
{
    /**
     * Converts a timestamp to various date formats.
     *
     * @param int $timestamp Unix timestamp to convert.
     * @return array An associative array containing Gregorian, Persian, and Islamic dates.
     * @throws InvalidArgumentException If the timestamp is not a valid integer.
     */
    public function convertTimestamp($timestamp)
    {
        // Validate the input timestamp
        if (!is_int($timestamp) || $timestamp < 0) {
            throw new InvalidArgumentException('Invalid timestamp provided. It must be a non-negative integer.');
        }

        // Convert timestamp to Gregorian date
        $gregorianDate = date('Y-m-d', $timestamp);

        // Convert timestamp to Persian date using IntlDateFormatter
        $persianDate = $this->convertToPersianDate($timestamp);

        // Convert timestamp to Islamic date using IntlDateFormatter
        $islamicDate = $this->convertToIslamicDate($timestamp);

        // Return the dates in an associative array
        return [
            'gregorian' => $gregorianDate,
            'persian' => $persianDate,
            'islamic' => $islamicDate,
        ];
    }

    /**
     * Converts a timestamp to Persian date format.
     *
     * @param int $timestamp Unix timestamp to convert.
     * @return string Persian date in 'Y/m/d' format.
     */
    private function convertToPersianDate($timestamp)
    {
        $formatter = new IntlDateFormatter(
            'fa_IR',
            IntlDateFormatter::LONG,
            IntlDateFormatter::NONE,
            null,
            IntlDateFormatter::GREGORIAN,
            'yyyy/MM/dd'
        );

        return $formatter->format($timestamp);
    }

    /**
     * Converts a timestamp to Islamic date format.
     *
     * @param int $timestamp Unix timestamp to convert.
     * @return string Islamic date in 'Y/m/d' format.
     */
    private function convertToIslamicDate($timestamp)
    {
        $formatter = new IntlDateFormatter(
            'ar_SA',
            IntlDateFormatter::LONG,
            IntlDateFormatter::NONE,
            null,
            IntlDateFormatter::TRADITIONAL,
            'yyyy/MM/dd'
        );

        return $formatter->format($timestamp);
    }
}

// Example usage
try {
    $dateConverter = new DateConverter();
    $timestamp = time(); // Current timestamp
    $dates = $dateConverter->convertTimestamp($timestamp);
    
    // Display the results
    echo "Gregorian Date: " . $dates['gregorian'] . PHP_EOL;
    echo "Persian Date: " . $dates['persian'] . PHP_EOL;
    echo "Islamic Date: " . $dates['islamic'] . PHP_EOL;
} catch (Exception $e) {
    // Handle any exceptions that may occur
    echo 'Error: ' . $e->getMessage() . PHP_EOL;
}
?>
```
