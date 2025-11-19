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
 * Converts a timestamp to different calendar dates.
 */
class DateConverter
{
    const GREGORIAN_CALENDAR = 'gregorian';
    const PERSIAN_CALENDAR = 'persian';
    const ISLAMIC_CALENDAR = 'islamic';

    /**
     * @param int $timestamp Unix timestamp
     * @return array
     */
    public function convert($timestamp)
    {
        if (!is_int($timestamp)) {
            throw new InvalidArgumentException('Timestamp must be an integer.');
        }

        $dates = [];

        // Gregorian date
        $dates[self::GREGORIAN_CALENDAR] = $this->getGregorianDate($timestamp);

        // Persian date
        $dates[self::PERSIAN_CALENDAR] = $this->getPersianDate($timestamp);

        // Islamic date
        $dates[self::ISLAMIC_CALENDAR] = $this->getIslamicDate($timestamp);

        return $dates;
    }

    /**
     * @param int $timestamp Unix timestamp
     * @return string
     */
    private function getGregorianDate($timestamp)
    {
        $date = new DateTime("@$timestamp");
        return $date->format('Y-m-d');
    }

    /**
     * @param int $timestamp Unix timestamp
     * @return string
     */
    private function getPersianDate($timestamp)
    {
        $date = new DateTime("@$timestamp");
        $date->setTimezone(new DateTimeZone('Asia/Tehran'));
        $persianDate = $date->format('Y-m-d');
        list($year, $month, $day) = explode('-', $persianDate);
        $persianMonth = $this->getPersianMonth($date->format('n'));
        return $this->jalaliDate($year, $date->format('n'), $date->format('j'));
    }

    /**
     * @param int $month
     * @return string
     */
    private function getPersianMonth($month)
    {
        $months = [
            1 => 'فروردین',
            2 => 'اردیبهشت',
            3 => 'خرداد',
            4 => 'تیر',
            5 => 'مرداد',
            6 => 'شهریور',
            7 => 'مهر',
            8 => 'آبان',
            9 => 'آذر',
            10 => 'دی',
            11 => 'بهمن',
            12 => 'اسفند',
        ];

        return $months[$month];
    }

    /**
     * @param int $year
     * @param int $month
     * @param int $day
     * @return string
     */
    private function jalaliDate($year, $month, $day)
    {
        $jalaliMonths = [31, 30, 31, 31, 30, 31, 30, 31, 31, 30, 30, 29];

        if ($month < 1 || $month > 12) {
            throw new Exception('Invalid month');
        }

        if ($day < 1 || $day > $jalaliMonths[$month - 1]) {
            throw new Exception('Invalid day');
        }

        $persianMonths = [
            1 => 'فروردین',
            2 => 'اردیبهشت',
            3 => 'خرداد',
            4 => 'تیر',
            5 => 'مرداد',
            6 => 'شهریور',
            7 => 'مهر',
            8 => 'آبان',
            9 => 'آذر',
            10 => 'دی',
            11 => 'بهمن',
            12 => 'اسفند',
        ];

        return $this->padZero($year) . '-' . $this->padZero($month) . '-' . $this->padZero($day);
    }

    /**
     * @param int $num
     * @return string
     */
    private function padZero($num)
    {
        return str_pad($num, 2, '0', STR_PAD_LEFT);
    }

    /**
     * @param int $timestamp Unix timestamp
     * @return string
     */
    private function getIslamicDate($timestamp)
    {
        $date = new DateTime("@$timestamp");
        $date->setTimezone(new DateTimeZone('Asia/Tehran'));
        $day = $date->format('j');
        $month = $date->format('n');
        $year = $date->format('Y');

        // Calculate Islamic date
        $HijriYear = $year - 622;
        $HijriMonth = $month;
        $HijriDay = $day;

        // Calculate the number of days in the months of the previous Hijri year
        $daysInPrevMonths = 0;
        for ($i = 1; $i < $HijriMonth; $i++) {
            if (in_array($i, [1, 3, 5, 7, 8, 10, 12])) {
                $daysInPrevMonths += 31;
            } elseif (in_array($i, [4, 6, 8, 11, 13])) {
                $daysInPrevMonths += 30;
            } else {
                $daysInPrevMonths += 29;
            }
        }

        // Check for leap year
        if (($HijriYear % 4 == 0 && $HijriYear % 100 != 0) || $HijriYear % 400 == 0) {
            $daysInPrevMonths += 1;
        }

        $HijriDate = $HijriYear . '-' . $this->padZero($HijriMonth) . '-' . $this->padZero($HijriDay);

        return $HijriDate;
    }
}

function main()
{
    $converter = new DateConverter();
    $timestamp = strtotime('2022-01-01');
    try {
        $dates = $converter->convert($timestamp);
        print_r($dates);
    } catch (Exception $e) {
        echo 'Caught exception: ',  $e->getMessage(), "\n";
    }
}

main();

?>
```
