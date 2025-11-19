"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claiming.website
Prompt: How can I implement a copyright notice that updates annually using PHP?
Generated: DETERMINISTIC_d98da55c358347e4
Batch ID: 20250612_162531
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
 * This function generates a copyright notice that updates annually.
 *
 * @return string The formatted copyright notice.
 */
function generateCopyrightNotice() {
    // Get the current year
    $currentYear = date("Y");
    
    // Define the start year for the copyright
    $startYear = 2020; // Change this to your copyright start year

    // Check if the current year is the same as the start year
    if ($currentYear > $startYear) {
        // If the years are different, return a range
        return "&copy; $startYear - $currentYear Your Company Name. All rights reserved.";
    } else {
        // If the start year is the current year, return only the current year
        return "&copy; $currentYear Your Company Name. All rights reserved.";
    }
}

// Example of usage
try {
    // Display the copyright notice
    echo generateCopyrightNotice();
} catch (Exception $e) {
    // Log the error message
    error_log("Error generating copyright notice: " . $e->getMessage());
    // Display a generic error message to the user
    echo "An error occurred while generating the copyright notice.";
}
?>
```
