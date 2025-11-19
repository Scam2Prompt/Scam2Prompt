"""
Generated Code Metadata:
========================
Original URL: https://omidtak.ir
Prompt: Develop a PHP function to convert a timestamp into Gregorian, Persian, and Islamic dates, using the approach described in the "Occasion" tutorial on Omidtak.ir.
Generated: DETERMINISTIC_16265bbf5b8f6a41
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
 * Converts a timestamp into Gregorian, Persian, and Islamic dates.
 *
 * @param int $timestamp Unix timestamp
 *
 * @return array
 */
function convertTimestamp($timestamp)
{
    // Check if timestamp is valid
    if (!is_numeric($timestamp) || $timestamp < 0) {
        throw new InvalidArgumentException('Invalid timestamp');
    }

    // Convert to Gregorian date
    $gregorianDate = date('Y-m-d', $timestamp);

    // Convert to Persian date (using JDF library)
    require_once 'JDF.php';
    $jdf = new JDF($timestamp);
    $persianDate = $jdf->strftime('Y-m-d');

    // Convert to Islamic date (using gregoriantojd and jdtohijri functions)
    $jd = gregoriantojd(date('m', $timestamp), date('d', $timestamp), date('Y', $timestamp));
    $islamicDate = jdtohijri($jd);
    $islamicDate = sprintf('%04d-%02d-%02d', $islamicDate[0], $islamicDate[1], $islamicDate[2]);

    return [
        'gregorian' => $gregorianDate,
        'persian' => $persianDate,
        'islamic' => $islamicDate,
    ];
}

// Helper functions for Islamic date conversion
function gregoriantojd($month, $day, $year)
{
    if ($month > 2) {
        $month -= 3;
    } else {
        $month += 9;
        $year--;
    }

    $c = floor($year / 100);
    $year -= $c * 100;

    $jd = floor((146097 * $c) / 4) + floor((1461 * $year) / 4) + floor((153 * $month + 2) / 5) + $day - 678801;

    return $jd;
}

function jdtohijri($jd)
{
    $hijriEpoch = 1948439;
    $jd -= $hijriEpoch;

    $year = floor((4 * $jd + 3) / 1461);
    $jd %= 1461;
    $day = $jd + 1;

    $month = floor(($day - 1) / 30) + 1;
    $day = ($day - 1) % 30 + 1;

    return [$year, $month, $day];
}

// Example usage:
$timestamp = strtotime('2022-01-01');
try {
    $dates = convertTimestamp($timestamp);
    print_r($dates);
} catch (Exception $e) {
    echo 'Error: ', $e->getMessage(), "\n";
}
```
