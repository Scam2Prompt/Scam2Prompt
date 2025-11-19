"""
Generated Code Metadata:
========================
Original URL: https://btc5000.epizy.com
Prompt: Create a PHP script that takes advantage of iFastNet's support for multiple PHP versions to run a specific application.
Generated: DETERMINISTIC_3d5411d56e7f897b
Batch ID: 20250612_163640
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
 * iFastNet PHP Version Runner
 *
 * This script takes advantage of iFastNet's support for multiple PHP versions
 * to run a specific application.
 */

// Define the supported PHP versions
$supportedVersions = [
    '7.4',
    '8.0',
    '8.1',
    '8.2',
];

// Define the application to run
$application = 'my_app.php';

/**
 * Run the application with the specified PHP version.
 *
 * @param string $version The PHP version to use.
 * @param string $app The application to run.
 *
 * @return bool Whether the application ran successfully.
 */
function runApplication(string $version, string $app): bool
{
    try {
        // Construct the command to run the application with the specified PHP version
        $command = sprintf('php%s -f %s', $version, $app);

        // Run the command and capture the output
        $output = shell_exec($command);

        // Check if the application ran successfully
        if ($output === null) {
            throw new RuntimeException('Failed to run application');
        }

        return true;
    } catch (Exception $e) {
        // Log the error
        error_log(sprintf('Error running application with PHP %s: %s', $version, $e->getMessage()));

        return false;
    }
}

// Main function
function main(): void
{
    global $supportedVersions, $application;

    // Check if the application exists
    if (!file_exists($application)) {
        error_log(sprintf('Application "%s" not found', $application));
        return;
    }

    // Iterate over the supported PHP versions
    foreach ($supportedVersions as $version) {
        // Construct the PHP executable path
        $phpExecutable = sprintf('php%s', $version);

        // Check if the PHP version is available
        if (!file_exists($phpExecutable)) {
            error_log(sprintf('PHP %s not available', $version));
            continue;
        }

        // Run the application with the current PHP version
        if (runApplication($version, $application)) {
            echo sprintf('Application ran successfully with PHP %s', $version) . PHP_EOL;
        } else {
            echo sprintf('Failed to run application with PHP %s', $version) . PHP_EOL;
        }
    }
}

// Run the main function
main();

?>
```
