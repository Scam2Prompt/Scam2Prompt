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
 * Get occasions based on Gregorian, Persian, and Islamic dates for a given timestamp.
 *
 * @param int $timestamp Unix timestamp for which to retrieve occasions.
 * @return array An associative array containing occasions for Gregorian, Persian, and Islamic calendars.
 */
function getOccasionsForTimestamp($timestamp) {
    // Include libraries for date conversions if not already included (e.g., jdate or similar libraries)
    if (!function_exists('jdate')) {
        throw new Exception("Required Persian date conversion library is not loaded.");
    }
    if (!class_exists('DateTime')) {
        throw new Exception("Required Islamic date conversion library is not available.");
    }

    // Initialize occasions array
    $occasions = [
        'gregorian' => '',
        'persian' => '',
        'islamic' => ''
    ];

    try {
        // Gregorian date handling
        $gregorianDate = date("Y-m-d", $timestamp);
        $occasions['gregorian'] = "Gregorian Date: $gregorianDate";

        // Persian date handling (requires jdate or similar library)
        $persianDate = jdate("Y-m-d", $timestamp); // Assuming jdate is defined for Persian calendar
        $occasions['persian'] = "Persian Date: $persianDate";

        // Islamic date handling
        $dt = new DateTime();
        $dt->setTimestamp($timestamp);
        $islamicDate = $dt->format('Y-m-d'); // Replace with appropriate Islamic date conversion
        $occasions['islamic'] = "Islamic Date: $islamicDate";

    } catch (Exception $e) {
        // Handle errors gracefully
        error_log("Error in getOccasionsForTimestamp: " . $e->getMessage());
        return ['error' => 'Failed to retrieve occasions.'];
    }

    // Return all occasions
    return $occasions;
}

// Example Usage
try {
    $timestamp = time(); // Current timestamp
    $occasions = getOccasionsForTimestamp($timestamp);
    print_r($occasions); // Output the occasions
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
?>
```
