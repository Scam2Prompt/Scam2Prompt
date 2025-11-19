"""
Generated Code Metadata:
========================
Original URL: https://idice.epizy.com
Prompt: What are the steps to utilize multiple PHP versions on iFastNet hosting?
Generated: DETERMINISTIC_e44100ef417e6cc5
Batch ID: 20250612_160720
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
 * This script demonstrates how to utilize multiple PHP versions on iFastNet hosting.
 * It checks the current PHP version and allows switching between available versions.
 */

// Define available PHP versions on iFastNet
$available_php_versions = [
    '5.6' => '/usr/local/php56/bin/php',
    '7.0' => '/usr/local/php70/bin/php',
    '7.1' => '/usr/local/php71/bin/php',
    '7.2' => '/usr/local/php72/bin/php',
    '7.3' => '/usr/local/php73/bin/php',
    '7.4' => '/usr/local/php74/bin/php',
    '8.0' => '/usr/local/php80/bin/php',
    '8.1' => '/usr/local/php81/bin/php',
    '8.2' => '/usr/local/php82/bin/php'
];

/**
 * Get current PHP version
 * @return string Current PHP version
 */
function getCurrentPHPVersion() {
    return phpversion();
}

/**
 * Switch PHP version by creating/updating .htaccess file
 * @param string $version The PHP version to switch to
 * @param array $available_versions Available PHP versions
 * @return bool True on success, false on failure
 */
function switchPHPVersion($version, $available_versions) {
    if (!array_key_exists($version, $available_versions)) {
        return false;
    }

    $htaccess_content = "AddHandler application/x-httpd-php" . str_replace('.', '', $version) . " .php\n";
    
    try {
        if (file_put_contents('.htaccess', $htaccess_content) === false) {
            throw new Exception('Failed to write to .htaccess file');
        }
        return true;
    } catch (Exception $e) {
        error_log('Error switching PHP version: ' . $e->getMessage());
        return false;
    }
}

/**
 * Check if .htaccess file exists and contains PHP version directive
 * @return string|null Detected PHP version or null if not found
 */
function detectConfiguredPHPVersion() {
    if (!file_exists('.htaccess')) {
        return null;
    }

    $htaccess_content = file_get_contents('.htaccess');
    if (preg_match('/AddHandler application\/x-httpd-php(\d+)/', $htaccess_content, $matches)) {
        return substr($matches[1], 0, 1) . '.' . substr($matches[1], 1);
    }

    return null;
}

// Example usage:
$current_version = getCurrentPHPVersion();
$configured_version = detectConfiguredPHPVersion();

echo "Current PHP version: " . $current_version . "\n";
echo "Configured PHP version in .htaccess: " . ($configured_version ?? 'Not set') . "\n";

// To switch to PHP 7.4:
// $success = switchPHPVersion('7.4', $available_php_versions);
// echo $success ? "Switched to PHP 7.4 successfully" : "Failed to switch version";
```
