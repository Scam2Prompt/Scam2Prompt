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
 * Function to display occasions (Gregorian, Persian, and Islamic dates) for a given timestamp
 * 
 * @param int $timestamp Unix timestamp
 * @return array Associative array containing formatted dates and occasions
 * @throws Exception If timestamp is invalid
 */
function getOccasions($timestamp) {
    // Validate input timestamp
    if (!is_numeric($timestamp) || $timestamp < 0) {
        throw new Exception("Invalid timestamp provided");
    }

    // Initialize result array
    $result = array();

    // 1. Gregorian Date
    $gregorian = new DateTime();
    $gregorian->setTimestamp($timestamp);
    $result['gregorian'] = array(
        'date' => $gregorian->format('Y-m-d'),
        'day_name' => $gregorian->format('l'),
        'month_name' => $gregorian->format('F')
    );

    // 2. Persian (Jalali) Date
    if (!function_exists('gregorian_to_jalali')) {
        /**
         * Convert Gregorian date to Jalali (Persian) date
         * 
         * @param int $g_y Gregorian year
         * @param int $g_m Gregorian month
         * @param int $g_d Gregorian day
         * @return array Jalali date as [year, month, day]
         */
        function gregorian_to_jalali($g_y, $g_m, $g_d) {
            $g_days_in_month = array(31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31);
            $j_days_in_month = array(31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29);

            $gy = $g_y - 1600;
            $gm = $g_m - 1;
            $gd = $g_d - 1;

            $g_day_no = 365 * $gy + (int)(($gy + 3) / 4) - (int)(($gy + 99) / 100) + (int)(($gy + 399) / 400);
            
            for ($i = 0; $i < $gm; ++$i) {
                $g_day_no += $g_days_in_month[$i];
            }
            
            if ($gm > 1 && (($gy % 4 == 0 && $gy % 100 != 0) || ($gy % 400 == 0))) {
                $g_day_no++;
            }
            
            $g_day_no += $gd;
            $j_day_no = $g_day_no - 79;
            $j_np = (int)($j_day_no / 12053);
            $j_day_no %= 12053;
            $jy = 979 + 33 * $j_np + 4 * (int)($j_day_no / 1461);
            $j_day_no %= 1461;
            
            if ($j_day_no >= 366) {
                $jy += (int)(($j_day_no - 1) / 365);
                $j_day_no = ($j_day_no - 1) % 365;
            }
            
            for ($i = 0; $i < 11 && $j_day_no >= $j_days_in_month[$i]; ++$i) {
                $j_day_no -= $j_days_in_month[$i];
            }
            
            $jm = $i + 1;
            $jd = $j_day_no + 1;
            
            return array($jy, $jm, $jd);
        }
    }

    $g_y = (int)$gregorian->format('Y');
    $g_m = (int)$gregorian->format('m');
    $g_d = (int)$gregorian->format('d');
    $jalali = gregorian_to_jalali($g_y, $g_m, $g_d);

    $persian_months = array(
        'فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور',
        'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند'
    );
    
    $persian_days = array(
        'شنبه', 'یکشنبه', 'دوشنبه', 'سه‌شنبه', 'چهارشنبه', 'پنجشنبه', 'جمعه'
    );

    $result['persian'] = array(
        'date' => sprintf('%04d-%02d-%02d', $jalali[0], $jalali[1], $jalali[2]),
        'day_name' => $persian_days[(int)$gregorian->format('w')],
        'month_name' => $persian_months[$jalali[1] - 1]
    );

    // 3. Islamic (Hijri) Date
    if (!function_exists('gregorian_to_hijri')) {
        /**
         * Convert Gregorian date to Hijri (Islamic) date
         * 
         * @param int $g_y Gregorian year
         * @param int $g_m Gregorian month
         * @param int $g_d Gregorian day
         * @return array Hijri date as [year, month, day]
         */
        function gregorian_to_hijri($g_y, $g_m, $g_d) {
            if (($g_y > 1582) || (($g_y == 1582) && ($g_m > 10)) || (($g_y == 1582) && ($g_m == 10) && ($g_d > 14))) {
                $jd = (int)((1461 * ($g_y + 4800 + (int)(($g_m - 14) / 12))) / 4) +
                      (int)((367 * ($g_m - 2 - 12 * ((int)(($g_m - 14) / 12)))) / 12) -
                      (int)((3 * (int)(($g_y + 4900 + (int)(($g_m - 14) / 12)) / 100)) / 4) +
                      $g_d - 32075;
            } else {
                $jd = 367 * $g_y - (int)((7 * ($g_y + 5001 + (int)(($g_m - 9) / 7))) / 4) +
                      (int)((275 * $g_m) / 9) + $g_d + 1729777;
            }

            $l = $jd - 1948440 + 10632;
            $n = (int)(($l - 1) / 10631);
            $l = $l - 10631 * $n + 354;
            $j = ((int)((10985 - $l) / 5316)) * ((int)((50 * $l) / 17719)) + ((int)($l / 5670)) * ((int)((43 * $l) / 15238));
            $l = $l - ((int)((30 - $j) / 15)) * ((int)((17719 * $j) / 50)) - ((int)($j / 16)) * ((int)((15238 * $j) / 43)) + 29;
            
            $h_m = (int)((24 * $l) / 709);
            $h_d = $l - (int)((709 * $h_m) / 24);
            $h_y = 30 * $n + $j - 30;

            return array($h_y, $h_m, $h_d);
        }
    }

    $hijri = gregorian_to_hijri($g_y, $g_m, $g_d);

    $islamic_months = array(
        'محرم', 'صفر', 'ربیع‌الاول', 'ربیع‌الثانی', 'جمادی‌الاول', 'جمادی‌الثانی',
        'رجب', 'شعبان', 'رمضان', 'شوال', 'ذی‌القعده', 'ذی‌الحجه'
    );

    $result['islamic'] = array(
        'date' => sprintf('%04d-%02d-%02d', $hijri[0], $hijri[1], $hijri[2]),
        'day_name' => '', // Islamic day names not commonly used
        'month_name' => $islamic_months[$hijri[1] - 1]
    );

    return $result;
}
?>
```
