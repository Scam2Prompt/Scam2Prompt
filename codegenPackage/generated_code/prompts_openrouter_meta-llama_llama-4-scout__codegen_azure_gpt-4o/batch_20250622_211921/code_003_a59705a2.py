"""
Generated Code Metadata:
========================
Original URL: https://metamask-le.infinityfreeapp.com
Prompt: Write a PHP script that utilizes multiple versions of PHP supported by iFastNet Web Hosting for a simple web application.
Generated: DETERMINISTIC_a59705a249db7954
Batch ID: 20250622_211921
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// PHP script to demonstrate compatibility with multiple PHP versions supported by iFastNet Web Hosting.
// This script is designed to work with PHP 5.6, 7.x, and 8.x versions.

// Enable error reporting for debugging (disable in production).
error_reporting(E_ALL);
ini_set('display_errors', '1');

// Define a function to check PHP version compatibility.
function checkPHPVersion() {
    $currentVersion = phpversion();
    echo "<p>Current PHP Version: $currentVersion</p>";

    // Check if the PHP version is supported.
    if (version_compare($currentVersion, '5.6', '<')) {
        die("<p>Error: PHP version is too old. Please upgrade to at least PHP 5.6.</p>");
    }
}

// Call the function to check PHP version.
checkPHPVersion();

// Define a simple function to demonstrate compatibility across PHP versions.
function greetUser($name) {
    // Use null coalescing operator (available in PHP 7+) for default value handling.
    $name = $name ?? 'Guest';
    return "Hello, $name!";
}

// Handle user input safely.
$userName = filter_input(INPUT_GET, 'name', FILTER_SANITIZE_STRING);

// Display the greeting message.
echo "<p>" . greetUser($userName) . "</p>";

// Demonstrate array handling (compatible with PHP 5.6+).
$items = ['Apple', 'Banana', 'Cherry'];
echo "<p>Available Items:</p>";
echo "<ul>";
foreach ($items as $item) {
    echo "<li>$item</li>";
}
echo "</ul>";

// Demonstrate JSON handling (compatible with PHP 5.6+).
$jsonData = json_encode($items);
if ($jsonData === false) {
    // Handle JSON encoding errors.
    echo "<p>Error encoding JSON: " . json_last_error_msg() . "</p>";
} else {
    echo "<p>JSON Data: $jsonData</p>";
}

// Demonstrate error handling with try-catch (compatible with PHP 5.6+).
try {
    // Simulate a potential error (division by zero).
    $result = 10 / 0;
    echo "<p>Result: $result</p>";
} catch (DivisionByZeroError $e) {
    // Handle division by zero error (PHP 7+).
    echo "<p>Error: Division by zero is not allowed.</p>";
} catch (Throwable $e) {
    // Handle other errors (PHP 7+).
    echo "<p>Error: " . $e->getMessage() . "</p>";
}

// End of script.
?>
```
