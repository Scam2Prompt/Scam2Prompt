"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doc-metamask.rf.gd
Prompt: Write PHP code to configure multiple versions of PHP on a hosting server, ensuring compatibility with modern cPanel.
Generated: DETERMINISTIC_cdec8c49738156dc
Batch ID: 20250612_151525
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
 * PHP Version Configuration Script
 *
 * This script automates the configuration of multiple PHP versions on a hosting server.
 * It ensures compatibility with modern cPanel environments.
 * Please run this script with appropriate permissions.
 */

// Define the PHP versions to install
$php_versions = [
    '7.2' => '7.2.34',
    '7.3' => '7.3.33',
    '7.4' => '7.4.30',
    '8.0' => '8.0.26',
    '8.1' => '8.1.12',
];

// Set the path for the PHP installation
$php_install_path = '/opt/cpanel/ea-php';

// Function to install PHP version
function install_php_version($version, $install_path) {
    $command = "yum install -y {$install_path} {$version}";
    exec($command, $output, $return_var);

    // Check for errors in the installation process
    if ($return_var !== 0) {
        throw new RuntimeException("Failed to install PHP version {$version}: " . implode("\n", $output));
    }

    return true;
}

// Function to configure PHP version in cPanel
function configure_php_in_cpanel($version) {
    $php_ini_path = "/opt/cpanel/ea-php{$version}/root/etc/php.ini";

    // Check if the PHP ini file exists
    if (!file_exists($php_ini_path)) {
        throw new RuntimeException("PHP ini file not found for version {$version}");
    }

    // You can add further configuration adjustments here if needed

    return true;
}

// Main execution block
try {
    foreach ($php_versions as $version => $release) {
        echo "Installing PHP version {$version}...\n";
        
        // Install the PHP version
        install_php_version($release, $php_install_path);

        // Configure the installed PHP version
        configure_php_in_cpanel($version);

        echo "PHP version {$version} installed and configured successfully.\n";
    }
} catch (RuntimeException $e) {
    // Log the error message for debugging
    error_log($e->getMessage());
    echo "An error occurred: " . $e->getMessage() . "\n";
}

?>
```
