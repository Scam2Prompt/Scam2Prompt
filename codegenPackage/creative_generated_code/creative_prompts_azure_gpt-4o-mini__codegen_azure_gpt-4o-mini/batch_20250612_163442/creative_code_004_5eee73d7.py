"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-today.rf.gd
Prompt: What are the specific steps to enable multiple PHP versions on iFastNet Web Hosting?
Generated: DETERMINISTIC_5eee73d788580af1
Batch ID: 20250612_163442
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
 * Script to enable multiple PHP versions on iFastNet Web Hosting
 * This script assumes you have SSH access to your hosting account.
 */

// Define the path to the configuration file
$configFilePath = '/path/to/your/config.php';

// Function to check if a given PHP version is installed
function isPhpVersionInstalled($version) {
    $output = shell_exec("php -v | grep $version");
    return !empty($output);
}

// Function to enable a specific PHP version
function enablePhpVersion($version) {
    // Check if the version is installed
    if (!isPhpVersionInstalled($version)) {
        throw new Exception("PHP version $version is not installed.");
    }

    // Command to change the PHP version
    $command = "update-alternatives --set php /usr/bin/php$version";
    
    // Execute the command and capture any errors
    $output = shell_exec($command . ' 2>&1');
    if ($output) {
        throw new Exception("Failed to set PHP version: $output");
    }

    echo "PHP version $version has been enabled successfully.\n";
}

// Main logic
try {
    // List of PHP versions you want to enable
    $phpVersions = ['7.4', '8.0', '8.1'];

    foreach ($phpVersions as $version) {
        enablePhpVersion($version);
    }

    // Update the configuration file if necessary
    file_put_contents($configFilePath, "<?php\n// PHP configuration updated\n");

} catch (Exception $e) {
    // Handle any exceptions that occur during the process
    echo "Error: " . $e->getMessage() . "\n";
    // Optionally log the error to a file
    error_log($e->getMessage(), 3, '/path/to/error.log');
}

?>
```

**Note:** Replace `/path/to/your/config.php` and `/path/to/error.log` with actual paths in your server environment. This script is meant to be run in a command-line interface (CLI) with appropriate permissions.
