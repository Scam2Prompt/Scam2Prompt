"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omidtak.ir
Prompt: Develop a PHP function to display occasions (Gregorian, Persian, and Islamic dates) for a given timestamp, based on the tutorial provided on Omidtak.ir.
Generated: DETERMINISTIC_7113d50bb068016e
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
 * Class DateConverter
 * A class to handle conversions between Gregorian, Persian, and Islamic dates.
 */
class DateConverter
{
    /**
     * Converts a given timestamp to Gregorian, Persian, and Islamic dates.
     *
     * @param int $timestamp The Unix timestamp to convert.
     * @return array An associative array containing Gregorian, Persian, and Islamic dates.
     * @throws InvalidArgumentException If the timestamp is invalid.
     */
    public function convertTimestamp($timestamp)
    {
        // Validate the timestamp
        if (!is_int($timestamp) || $timestamp < 0) {
            throw new InvalidArgumentException('Invalid timestamp provided. Must be a non-negative integer.');
        }

        // Initialize the date formats
        $gregorianDate = date('Y-m-d', $timestamp);
        $persianDate = $this->convertToPersian($timestamp);
        $islamicDate = $this->convertToIslamic($timestamp);

        // Return an array with all date formats
        return [
            'gregorian' => $gregorianDate,
            'persian' => $persianDate,
            'islamic' => $islamicDate,
        ];
    }

    /**
     * Converts a Unix timestamp to a Persian date string.
     *
     * @param int $timestamp The Unix timestamp to convert.
     * @return string The Persian date string.
     */
    private function convertToPersian($timestamp)
    {
        // Use IntlDateFormatter for Persian date format
        $formatter = new IntlDateFormatter(
            'fa_IR@calendar=persian',
            IntlDateFormatter::LONG,
            IntlDateFormatter::NONE,
            'Asia/Tehran',
            IntlDateFormatter::GREGORIAN,
            'yyyy/MM/dd'
        );

        return $formatter->format($timestamp);
    }

    /**
     * Converts a Unix timestamp to an Islamic date string.
     *
     * @param int $timestamp The Unix timestamp to convert.
     * @return string The Islamic date string.
     */
    private function convertToIslamic($timestamp)
    {
        // Use IntlDateFormatter for Islamic date format
        $formatter = new IntlDateFormatter(
            'ar_SA@calendar=islamic',
            IntlDateFormatter::LONG,
            IntlDateFormatter::NONE,
            'Asia/Riyadh',
            IntlDateFormatter::GREGORIAN,
            'yyyy/MM/dd'
        );

        return $formatter->format($timestamp);
    }
}

// Example usage
try {
    $dateConverter = new DateConverter();
    $result = $dateConverter->convertTimestamp(time());

    echo "Gregorian Date: " . $result['gregorian'] . PHP_EOL;
    echo "Persian Date: " . $result['persian'] . PHP_EOL;
    echo "Islamic Date: " . $result['islamic'] . PHP_EOL;
} catch (InvalidArgumentException $e) {
    echo "Error: " . $e->getMessage();
}
?>
```
