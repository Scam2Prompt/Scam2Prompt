"""
Generated Code Metadata:
========================
Original URL: https://metamask-version5.42web.io
Prompt: Generate a PHP script to test multiple PHP versions on iFastNet hosting, as highlighted in the website's features.
Generated: DETERMINISTIC_b9a24a00a1b27915
Batch ID: 20250612_154222
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
 * This script tests the compatibility of different PHP versions available on iFastNet hosting.
 * It checks the active PHP version and lists available versions for testing.
 */

// Prevent direct access to this script
if (!isset($_SERVER['HTTP_HOST'])) {
    die('This script can only be accessed via HTTP.');
}

// Set error reporting
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Define available PHP versions to test (based on iFastNet's offerings)
$availableVersions = [
    '5.6',
    '7.0',
    '7.1',
    '7.2',
    '7.3',
    '7.4',
    '8.0',
    '8.1',
    '8.2'
];

// Get current PHP version
$currentVersion = phpversion();

// Function to test PHP version features
function testPhpVersion($version) {
    $features = [];
    
    // Basic version check
    $features['version_check'] = version_compare(PHP_VERSION, $version, '>=');
    
    // Test common extensions
    $features['json_support'] = extension_loaded('json');
    $features['mysqli_support'] = extension_loaded('mysqli');
    $features['pdo_support'] = extension_loaded('pdo');
    $features['openssl_support'] = extension_loaded('openssl');
    $features['gd_support'] = extension_loaded('gd');
    
    // Test PHP 7+ features if version >= 7.0
    if (version_compare($version, '7.0', '>=')) {
        $features['scalar_type_hints'] = true;
        $features['return_type_declarations'] = true;
        $features['spaceship_operator'] = true;
    }
    
    // Test PHP 7.1+ features
    if (version_compare($version, '7.1', '>=')) {
        $features['nullable_types'] = true;
        $features['void_return_type'] = true;
    }
    
    // Test PHP 8.0+ features
    if (version_compare($version, '8.0', '>=')) {
        $features['named_arguments'] = true;
        $features['attributes'] = true;
        $features['union_types'] = true;
    }
    
    return $features;
}

// Test current version
$currentFeatures = testPhpVersion($currentVersion);

// HTML output
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Version Tester for iFastNet</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }
        h1, h2 { color: #333; }
        table { border-collapse: collapse; width: 100%; margin-bottom: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        .success { color: green; }
        .warning { color: orange; }
        .error { color: red; }
        .info { color: blue; }
    </style>
</head>
<body>
    <h1>PHP Version Compatibility Tester</h1>
    <p>This script tests the compatibility of different PHP versions available on iFastNet hosting.</p>
    
    <h2>Current PHP Version: <?php echo $currentVersion; ?></h2>
    
    <h3>Available PHP Versions on iFastNet</h3>
    <ul>
        <?php foreach ($availableVersions as $version): ?>
            <li><?php echo $version; ?></li>
        <?php endforeach; ?>
    </ul>
    
    <h2>Current Version Features</h2>
    <table>
        <tr>
            <th>Feature</th>
            <th>Status</th>
        </tr>
        <?php foreach ($currentFeatures as $feature => $status): ?>
            <tr>
                <td><?php echo str_replace('_', ' ', $feature); ?></td>
                <td class="<?php echo $status ? 'success' : 'error'; ?>">
                    <?php echo $status ? 'Supported' : 'Not Supported'; ?>
                </td>
            </tr>
        <?php endforeach; ?>
    </table>
    
    <h2>How to Change PHP Version on iFastNet</h2>
    <ol>
        <li>Log in to your iFastNet control panel</li>
        <li>Navigate to the "PHP Version" section</li>
        <li>Select your desired PHP version from the dropdown</li>
        <li>Save changes</li>
        <li>Refresh this page to see changes</li>
    </ol>
    
    <footer>
        <p class="info">Note: Some features may not be available depending on server configuration.</p>
    </footer>
</body>
</html>
```
