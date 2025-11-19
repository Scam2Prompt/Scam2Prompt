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
 * Generate a dynamic copyright notice that updates annually.
 * 
 * This script ensures the copyright year is always current and adjusts
 * automatically based on the current year.
 */

// Function to generate the copyright notice
function getCopyrightNotice($startYear, $ownerName) {
    // Validate input
    if (!is_int($startYear) || $startYear < 0) {
        throw new InvalidArgumentException("Start year must be a positive integer.");
    }
    if (empty($ownerName) || !is_string($ownerName)) {
        throw new InvalidArgumentException("Owner name must be a non-empty string.");
    }

    // Get the current year
    $currentYear = (int)date("Y");

    // Determine the year range for the copyright notice
    $yearRange = $startYear < $currentYear ? "$startYear-$currentYear" : $currentYear;

    // Return the formatted copyright notice
    return "© $yearRange $ownerName. All rights reserved.";
}

// Example usage
try {
    $startYear = 2020; // Replace with the year your copyright started
    $ownerName = "Your Company Name"; // Replace with your company or personal name
    echo getCopyrightNotice($startYear, $ownerName);
} catch (Exception $e) {
    // Handle errors gracefully
    error_log("Error generating copyright notice: " . $e->getMessage());
    echo "An error occurred while generating the copyright notice.";
}
?>
```
