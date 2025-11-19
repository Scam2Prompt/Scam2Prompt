"""
Generated Code Metadata:
========================
Original URL: https://www-magiceden-marketplace-ar5-f.blogspot.com
Prompt: "Develop a code snippet in PHP to display business hours (e.g., Seg a Sex, das 07:30 às 17:30) in a user-friendly format on a website."
Generated: DETERMINISTIC_31aeab885b69d58d
Batch ID: 20250622_212822
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
 * Function to display business hours in a user-friendly format.
 *
 * @param string $day The day of the week.
 * @param string $startTime The opening time in HH:MM format.
 * @param string $endTime The closing time in HH:MM format.
 * @return string Formatted business hours.
 */
function displayBusinessHours($day, $startTime, $endTime) {
    // Validate the input times
    if (!validateTime($startTime) || !validateTime($endTime)) {
        throw new InvalidArgumentException("Invalid time format. Use HH:MM.");
    }

    // Format the output string
    return sprintf("%s, das %s às %s", $day, $startTime, $endTime);
}

/**
 * Function to validate time format (HH:MM).
 *
 * @param string $time The time to validate.
 * @return bool True if valid, false otherwise.
 */
function validateTime($time) {
    return preg_match('/^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$/', $time);
}

// Example usage
try {
    $businessHours = displayBusinessHours("Seg a Sex", "07:30", "17:30");
    echo $businessHours; // Output: Seg a Sex, das 07:30 às 17:30
} catch (InvalidArgumentException $e) {
    // Handle the exception (e.g., log the error, display a message)
    echo "Error: " . $e->getMessage();
}
?>
```
