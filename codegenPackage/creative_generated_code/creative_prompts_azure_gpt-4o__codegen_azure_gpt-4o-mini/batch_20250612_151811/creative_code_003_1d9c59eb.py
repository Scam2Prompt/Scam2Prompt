"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mfxhk.com
Prompt: Write a script in PHP to display investment package details dynamically, including the "Basic Level," "Intermediate Level," and "Advanced Level" options provided by MFX-Online Trade.
Generated: DETERMINISTIC_1d9c59ebd62b4058
Batch ID: 20250612_151811
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
 * Investment Package Details Display Script
 * 
 * This script dynamically displays investment package details for 
 * MFX-Online Trade, including the Basic Level, Intermediate Level,
 * and Advanced Level options.
 */

// Define an array to hold investment package details
$investmentPackages = [
    "Basic" => [
        "name" => "Basic Level",
        "min_investment" => 100,
        "max_investment" => 1000,
        "return_rate" => 5, // percentage
        "duration" => 30 // days
    ],
    "Intermediate" => [
        "name" => "Intermediate Level",
        "min_investment" => 1001,
        "max_investment" => 5000,
        "return_rate" => 10, // percentage
        "duration" => 60 // days
    ],
    "Advanced" => [
        "name" => "Advanced Level",
        "min_investment" => 5001,
        "max_investment" => 20000,
        "return_rate" => 15, // percentage
        "duration" => 90 // days
    ]
];

/**
 * Function to display investment package details
 *
 * @param array $packages Array of investment packages
 * @return void
 */
function displayInvestmentPackages($packages) {
    // Check if the packages array is empty
    if (empty($packages)) {
        echo "No investment packages available.";
        return;
    }

    // Start the HTML output
    echo "<h1>Investment Packages</h1>";
    echo "<table border='1'>";
    echo "<tr><th>Package Level</th><th>Min Investment</th><th>Max Investment</th><th>Return Rate (%)</th><th>Duration (Days)</th></tr>";

    // Loop through each package and display its details
    foreach ($packages as $package) {
        echo "<tr>";
        echo "<td>{$package['name']}</td>";
        echo "<td>\${$package['min_investment']}</td>";
        echo "<td>\${$package['max_investment']}</td>";
        echo "<td>{$package['return_rate']}%</td>";
        echo "<td>{$package['duration']} days</td>";
        echo "</tr>";
    }

    // End the HTML output
    echo "</table>";
}

// Call the function to display the packages
try {
    displayInvestmentPackages($investmentPackages);
} catch (Exception $e) {
    // Handle any exceptions that may occur
    echo "An error occurred while displaying investment packages: " . $e->getMessage();
}
?>
```
