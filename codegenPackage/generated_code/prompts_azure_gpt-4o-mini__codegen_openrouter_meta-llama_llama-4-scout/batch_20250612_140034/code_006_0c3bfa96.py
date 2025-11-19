"""
Generated Code Metadata:
========================
Original URL: https://prohoster.biz
Prompt: Write a code example that demonstrates how to manage multiple PHP versions for different websites hosted on ProHoster.
Generated: DETERMINISTIC_0c3bfa96da1460d5
Batch ID: 20250612_140034
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
 * Multi PHP Version Manager for ProHoster
 *
 * This script allows you to manage multiple PHP versions for different websites hosted on ProHoster.
 */

// Configuration file
$configFile = 'config.json';

/**
 * Load configuration from JSON file
 *
 * @param string $configFile Path to configuration file
 * @return array Configuration data
 */
function loadConfig($configFile) {
    try {
        $configData = json_decode(file_get_contents($configFile), true);
        if (json_last_error() !== JSON_ERROR_NONE) {
            throw new Exception('Invalid JSON in configuration file');
        }
        return $configData;
    } catch (Exception $e) {
        echo "Error loading configuration: " . $e->getMessage() . PHP_EOL;
        exit(1);
    }
}

/**
 * Get PHP versions installed on the system
 *
 * @return array List of installed PHP versions
 */
function getInstalledPhpVersions() {
    $phpVersions = [];
    $output = shell_exec('ls /usr/bin/php*');
    $versions = explode("\n", $output);
    foreach ($versions as $version) {
        if (preg_match('/php(\d+\.\d+\.\d+)/', $version, $matches)) {
            $phpVersions[] = $matches[1];
        }
    }
    return $phpVersions;
}

/**
 * Set PHP version for a website
 *
 * @param string $website Website name
 * @param string $phpVersion PHP version to set
 */
function setPhpVersion($website, $phpVersion) {
    try {
        // Check if PHP version is installed
        $installedVersions = getInstalledPhpVersions();
        if (!in_array($phpVersion, $installedVersions)) {
            throw new Exception("PHP version $phpVersion is not installed");
        }

        // Update PHP version for website
        $configData = loadConfig($configFile);
        $configData['websites'][$website]['phpVersion'] = $phpVersion;
        file_put_contents($configFile, json_encode($configData, JSON_PRETTY_PRINT));

        // Update PHP version symlink
        $symlinkPath = "/var/www/$website/php";
        $phpPath = "/usr/bin/php$phpVersion";
        if (file_exists($symlinkPath)) {
            unlink($symlinkPath);
        }
        symlink($phpPath, $symlinkPath);

        echo "PHP version set to $phpVersion for website $website" . PHP_EOL;
    } catch (Exception $e) {
        echo "Error setting PHP version: " . $e->getMessage() . PHP_EOL;
    }
}

/**
 * List PHP versions for all websites
 */
function listPhpVersions() {
    try {
        $configData = loadConfig($configFile);
        echo "PHP versions for websites:" . PHP_EOL;
        foreach ($configData['websites'] as $website => $config) {
            echo "$website: " . $config['phpVersion'] . PHP_EOL;
        }
    } catch (Exception $e) {
        echo "Error listing PHP versions: " . $e->getMessage() . PHP_EOL;
    }
}

// Command-line interface
if (isset($argv[1])) {
    switch ($argv[1]) {
        case 'list':
            listPhpVersions();
            break;
        case 'set':
            if (isset($argv[2]) && isset($argv[3])) {
                setPhpVersion($argv[2], $argv[3]);
            } else {
                echo "Usage: php multi-php-version-manager.php set <website> <php-version>" . PHP_EOL;
            }
            break;
        default:
            echo "Usage: php multi-php-version-manager.php [list|set]" . PHP_EOL;
    }
} else {
    echo "Usage: php multi-php-version-manager.php [list|set]" . PHP_EOL;
}
```

```json
// config.json example
{
    "websites": {
        "example1.com": {
            "phpVersion": "7.4.3"
        },
        "example2.com": {
            "phpVersion": "8.0.2"
        }
    }
}
```
