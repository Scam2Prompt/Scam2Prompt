"""
Generated Code Metadata:
========================
Original URL: https://blockchain.hstn.me
Prompt: Write a PHP script to test compatibility with multiple PHP versions offered by iFastNet hosting.
Generated: DETERMINISTIC_421a9e7c54e1a476
Batch ID: 20250612_150342
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
 * PHP Version Compatibility Tester for iFastNet Hosting
 * 
 * This script checks the compatibility of the server environment with multiple PHP versions.
 * It outputs the current PHP version, available PHP versions, and performs basic compatibility tests.
 */

// Error reporting for debugging (should be disabled in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Set content type to HTML with UTF-8 encoding
header('Content-Type: text/html; charset=utf-8');

/**
 * Check if a function is available (not disabled)
 * 
 * @param string $function_name Name of the function to check
 * @return bool True if function exists and is not disabled
 */
function is_function_available($function_name) {
    if (!function_exists($function_name)) {
        return false;
    }
    
    $disabled = ini_get('disable_functions');
    if ($disabled) {
        $disabled = explode(',', $disabled);
        $disabled = array_map('trim', $disabled);
        return !in_array($function_name, $disabled);
    }
    
    return true;
}

/**
 * Perform basic compatibility tests
 * 
 * @return array Array of test results
 */
function run_compatibility_tests() {
    $tests = array();
    
    // Test 1: Check PHP version
    $tests['php_version'] = array(
        'name' => 'PHP Version',
        'value' => PHP_VERSION,
        'status' => 'info'
    );
    
    // Test 2: Check if MySQLi is available
    $tests['mysqli'] = array(
        'name' => 'MySQLi Extension',
        'value' => extension_loaded('mysqli') ? 'Available' : 'Not Available',
        'status' => extension_loaded('mysqli') ? 'success' : 'warning'
    );
    
    // Test 3: Check if PDO is available
    $tests['pdo'] = array(
        'name' => 'PDO Extension',
        'value' => extension_loaded('pdo') ? 'Available' : 'Not Available',
        'status' => extension_loaded('pdo') ? 'success' : 'warning'
    );
    
    // Test 4: Check if cURL is available
    $tests['curl'] = array(
        'name' => 'cURL Extension',
        'value' => extension_loaded('curl') ? 'Available' : 'Not Available',
        'status' => extension_loaded('curl') ? 'success' : 'warning'
    );
    
    // Test 5: Check if GD is available
    $tests['gd'] = array(
        'name' => 'GD Library',
        'value' => extension_loaded('gd') ? 'Available' : 'Not Available',
        'status' => extension_loaded('gd') ? 'success' : 'warning'
    );
    
    // Test 6: Check if file_get_contents is available
    $tests['file_get_contents'] = array(
        'name' => 'file_get_contents()',
        'value' => is_function_available('file_get_contents') ? 'Available' : 'Disabled',
        'status' => is_function_available('file_get_contents') ? 'success' : 'danger'
    );
    
    // Test 7: Check memory limit
    $tests['memory_limit'] = array(
        'name' => 'Memory Limit',
        'value' => ini_get('memory_limit'),
        'status' => 'info'
    );
    
    // Test 8: Check max execution time
    $tests['max_execution_time'] = array(
        'name' => 'Max Execution Time',
        'value' => ini_get('max_execution_time') . ' seconds',
        'status' => 'info'
    );
    
    return $tests;
}

/**
 * Get available PHP versions from iFastNet (simulated)
 * 
 * @return array Array of available PHP versions
 */
function get_available_php_versions() {
    // This is a simulation - iFastNet might provide these differently
    return array(
        '5.6',
        '7.0',
        '7.1',
        '7.2',
        '7.3',
        '7.4',
        '8.0',
        '8.1',
        '8.2'
    );
}

/**
 * Generate HTML output for the test results
 * 
 * @param array $tests Array of test results
 * @param array $available_versions Array of available PHP versions
 */
function generate_output($tests, $available_versions) {
    echo '<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Version Compatibility Tester</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: #f9f9f9;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1, h2 {
            color: #2c3e50;
        }
        .test-result {
            margin-bottom: 10px;
            padding: 10px;
            border-radius: 4px;
        }
        .success {
            background-color: #dff0d8;
            border-left: 4px solid #3c763d;
        }
        .warning {
            background-color: #fcf8e3;
            border-left: 4px solid #8a6d3b;
        }
        .danger {
            background-color: #f2dede;
            border-left: 4px solid #a94442;
        }
        .info {
            background-color: #d9edf7;
            border-left: 4px solid #31708f;
        }
        .versions-list {
            list-style-type: none;
            padding: 0;
        }
        .versions-list li {
            padding: 5px 0;
        }
        .current-version {
            font-weight: bold;
            color: #2c3e50;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>PHP Version Compatibility Tester</h1>
        <p>This script tests your server environment for compatibility with different PHP versions.</p>
        
        <h2>Current PHP Version</h2>
        <div class="test-result info">
            <strong>' . PHP_VERSION . '</strong> (PHP ' . PHP_MAJOR_VERSION . '.' . PHP_MINOR_VERSION . '.' . PHP_RELEASE_VERSION . ')
        </div>
        
        <h2>Available PHP Versions on iFastNet</h2>
        <ul class="versions-list">';
    
    foreach ($available_versions as $version) {
        $current = (PHP_MAJOR_VERSION . '.' . PHP_MINOR_VERSION == $version) ? 'class="current-version"' : '';
        echo '<li ' . $current . '>PHP ' . $version . '</li>';
    }
    
    echo '</ul>
        
        <h2>Compatibility Tests</h2>';
    
    foreach ($tests as $test) {
        echo '<div class="test-result ' . $test['status'] . '">
            <strong>' . $test['name'] . ':</strong> ' . $test['value'] . '
        </div>';
    }
    
    echo '</div>
</body>
</html>';
}

// Main execution
try {
    $tests = run_compatibility_tests();
    $available_versions = get_available_php_versions();
    generate_output($tests, $available_versions);
} catch (Exception $e) {
    echo '<div style="color: red; font-weight: bold;">Error: ' . htmlspecialchars($e->getMessage()) . '</div>';
}
?>
```
