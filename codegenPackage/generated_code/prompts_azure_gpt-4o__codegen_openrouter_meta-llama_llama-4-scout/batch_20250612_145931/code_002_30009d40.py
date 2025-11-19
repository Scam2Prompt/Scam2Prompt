"""
Generated Code Metadata:
========================
Original URL: https://walletsignpage.rf.gd
Prompt: Generate a PHP script that utilizes multiple versions of PHP for compatibility testing on a hosting platform like iFastNet.
Generated: DETERMINISTIC_30009d405f58f6b5
Batch ID: 20250612_145931
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
 * PHP Compatibility Tester
 *
 * This script tests compatibility of a PHP application across multiple PHP versions.
 */

// Configuration
$config = [
    'php_versions' => [
        '7.4' => '/usr/bin/php7.4',
        '7.3' => '/usr/bin/php7.3',
        '7.2' => '/usr/bin/php7.2',
        '7.1' => '/usr/bin/php7.1',
        '7.0' => '/usr/bin/php7.0',
    ],
    'test_script' => 'test.php',
];

/**
 * Execute a PHP script using a specific PHP version.
 *
 * @param string $phpVersion
 * @param string $script
 * @return string
 */
function executePhpScript(string $phpVersion, string $script): string
{
    $phpPath = $GLOBALS['config']['php_versions'][$phpVersion];
    if (!$phpPath) {
        throw new Exception("PHP $phpVersion not found");
    }

    $output = [];
    $returnCode = null;
    exec("$phpPath $script 2>&1", $output, $returnCode);

    if ($returnCode !== 0) {
        throw new Exception("PHP $phpVersion execution failed with code $returnCode");
    }

    return implode("\n", $output);
}

/**
 * Test compatibility across multiple PHP versions.
 *
 * @param array $config
 * @return array
 */
function testCompatibility(array $config): array
{
    $results = [];

    foreach ($config['php_versions'] as $version => $phpPath) {
        try {
            $output = executePhpScript($version, $config['test_script']);
            $results[$version] = [
                'success' => true,
                'output' => $output,
            ];
        } catch (Exception $e) {
            $results[$version] = [
                'success' => false,
                'error' => $e->getMessage(),
            ];
        }
    }

    return $results;
}

// Run compatibility test
try {
    $results = testCompatibility($config);

    // Print results
    foreach ($results as $version => $result) {
        echo "PHP $version:\n";
        if ($result['success']) {
            echo "  Success\n";
            echo "  Output:\n" . $result['output'] . "\n";
        } else {
            echo "  Error: " . $result['error'] . "\n";
        }
    }
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}

?>
```
