"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-version5.42web.io
Prompt: Generate a PHP script to test multiple PHP versions on iFastNet hosting, as highlighted in the website's features.
Generated: DETERMINISTIC_b9a24a00a1b27915
Batch ID: 20250612_154222
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
 * PHP Version Tester Script
 * This script tests the current PHP version on iFastNet hosting
 * and allows the user to switch between multiple PHP versions.
 */

// Define the available PHP versions for testing
$availableVersions = [
    '7.2',
    '7.3',
    '7.4',
    '8.0',
    '8.1',
    '8.2'
];

// Function to get the current PHP version
function getCurrentPHPVersion() {
    return phpversion();
}

// Function to generate the HTML form for version selection
function generateVersionSelectionForm($versions) {
    echo "<form method='POST' action=''>";
    echo "<label for='version'>Select PHP Version:</label>";
    echo "<select name='version' id='version'>";

    foreach ($versions as $version) {
        echo "<option value='{$version}'>{$version}</option>";
    }

    echo "</select>";
    echo "<input type='submit' value='Switch PHP Version'>";
    echo "</form>";
}

// Function to switch PHP version (simulated for this example)
function switchPHPVersion($version) {
    // Normally, this would involve server configuration changes
    // Here, we mock the behavior by returning a success message
    return "Switched to PHP version {$version}. Please refresh the page.";
}

// Check if a version has been submitted for switching
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['version'])) {
    $selectedVersion = $_POST['version'];

    // Validate the selected version
    if (in_array($selectedVersion, $availableVersions)) {
        $message = switchPHPVersion($selectedVersion);
    } else {
        $message = "Error: Invalid PHP version selected.";
    }
}

// Display the current PHP version
$currentVersion = getCurrentPHPVersion();
echo "<h1>Current PHP Version: {$currentVersion}</h1>";

// Display any messages (success or error)
if (isset($message)) {
    echo "<p>{$message}</p>";
}

// Generate the version selection form
generateVersionSelectionForm($availableVersions);
?>
```
