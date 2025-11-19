"""
Generated Code Metadata:
========================
Original URL: https://help-community.42web.io
Prompt: Write code to test the compatibility of multiple PHP versions on a hosting service like iFastNet, which supports various PHP versions.
Generated: DETERMINISTIC_00684224b762db00
Batch ID: 20250612_151513
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
 * PHP Version Compatibility Tester
 * 
 * This script tests the compatibility of the current PHP version with common features
 * and reports any deprecated or unsupported functions.
 */

// Define the minimum required PHP version
define('MIN_PHP_VERSION', '5.6.0');

// Define the recommended PHP version
define('RECOMMENDED_PHP_VERSION', '7.4.0');

// List of deprecated functions to check
$deprecated_functions = [
    'mysql_connect',
    'mysql_pconnect',
    'ereg',
    'split',
    'call_user_method',
    'mcrypt_generic_end'
];

// List of required extensions to check
$required_extensions = [
    'json',
    'pdo',
    'mbstring',
    'openssl'
];

/**
 * Check PHP version compatibility
 */
function check_php_version() {
    $current_version = phpversion();
    
    if (version_compare($current_version, MIN_PHP_VERSION, '<')) {
        return [
            'status' => 'error',
            'message' => "Your PHP version ($current_version) is below the minimum required version (" . MIN_PHP_VERSION . ")"
        ];
    }
    
    if (version_compare($current_version, RECOMMENDED_PHP_VERSION, '<')) {
        return [
            'status' => 'warning',
            'message' => "Your PHP version ($current_version) is below the recommended version (" . RECOMMENDED_PHP_VERSION . ")"
        ];
    }
    
    return [
        'status' => 'success',
        'message' => "Your PHP version ($current_version) meets the requirements"
    ];
}

/**
 * Check for deprecated functions
 */
function check_deprecated_functions($functions) {
    $results = [];
    
    foreach ($functions as $function) {
        if (function_exists($function)) {
            $results[] = [
                'function' => $function,
                'status' => 'deprecated',
                'message' => "This function is deprecated and should not be used"
            ];
        }
    }
    
    return $results;
}

/**
 * Check for required extensions
 */
function check_required_extensions($extensions) {
    $results = [];
    
    foreach ($extensions as $extension) {
        if (!extension_loaded($extension)) {
            $results[] = [
                'extension' => $extension,
                'status' => 'missing',
                'message' => "This extension is required but not installed"
            ];
        } else {
            $results[] = [
                'extension' => $extension,
                'status' => 'installed',
                'message' => "Extension is installed"
            ];
        }
    }
    
    return $results;
}

/**
 * Generate a compatibility report
 */
function generate_compatibility_report() {
    global $deprecated_functions, $required_extensions;
    
    $report = [
        'php_version' => check_php_version(),
        'deprecated_functions' => check_deprecated_functions($deprecated_functions),
        'required_extensions' => check_required_extensions($required_extensions)
    ];
    
    return $report;
}

/**
 * Format the report for display
 */
function format_report($report) {
    $output = "<h2>PHP Compatibility Report</h2>";
    
    // PHP Version
    $output .= "<h3>PHP Version Check</h3>";
    $output .= "<p class='{$report['php_version']['status']}'>";
    $output .= htmlspecialchars($report['php_version']['message']);
    $output .= "</p>";
    
    // Deprecated Functions
    $output .= "<h3>Deprecated Functions</h3>";
    if (empty($report['deprecated_functions'])) {
        $output .= "<p class='success'>No deprecated functions found</p>";
    } else {
        $output .= "<ul>";
        foreach ($report['deprecated_functions'] as $item) {
            $output .= "<li class='{$item['status']}'>";
            $output .= htmlspecialchars($item['function']) . ": " . htmlspecialchars($item['message']);
            $output .= "</li>";
        }
        $output .= "</ul>";
    }
    
    // Required Extensions
    $output .= "<h3>Required Extensions</h3>";
    $output .= "<ul>";
    foreach ($report['required_extensions'] as $item) {
        $output .= "<li class='{$item['status']}'>";
        $output .= htmlspecialchars($item['extension']) . ": " . htmlspecialchars($item['message']);
        $output .= "</li>";
    }
    $output .= "</ul>";
    
    return $output;
}

// Generate and display the report
$report = generate_compatibility_report();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Compatibility Tester</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }
        h2 { color: #333; }
        h3 { color: #444; margin-top: 20px; }
        .success { color: green; }
        .warning { color: orange; }
        .error { color: red; }
        .deprecated { color: #cc0000; }
        .missing { color: #ff6600; }
        .installed { color: #009900; }
        ul { list-style-type: none; padding-left: 0; }
        li { padding: 5px 0; }
    </style>
</head>
<body>
    <?php echo format_report($report); ?>
</body>
</html>
```
