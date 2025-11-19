"""
Generated Code Metadata:
========================
Original URL: https://illuviumprotocol.net
Prompt: Provide an example of using the PHP command line for executing scripts, incorporating details from the PHP documentation on command line usage.
Generated: DETERMINISTIC_4f3912e266e49545
Batch ID: 20250612_155936
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
 * Command Line Script Example
 * 
 * Demonstrates basic command line usage in PHP, including argument parsing and output.
 * 
 * Usage: php script.php [options] [arguments]
 * Options:
 *   -h, --help     Show this help message
 *   -v, --verbose  Enable verbose output
 * Arguments:
 *   name           Your name (optional)
 */

// Check if running from command line
if (php_sapi_name() !== 'cli') {
    die("This script must be run from the command line.\n");
}

// Initialize variables
$verbose = false;
$name = '';

// Parse command line arguments
$options = getopt('hv', ['help', 'verbose']);
$args = array_slice($argv, 1);

// Process options
if (isset($options['h']) || isset($options['help'])) {
    echo "Usage: php " . basename(__FILE__) . " [options] [arguments]\n";
    echo "Options:\n";
    echo "  -h, --help     Show this help message\n";
    echo "  -v, --verbose  Enable verbose output\n";
    echo "Arguments:\n";
    echo "  name           Your name (optional)\n";
    exit(0);
}

if (isset($options['v']) || isset($options['verbose'])) {
    $verbose = true;
}

// Process arguments
foreach ($args as $arg) {
    if (substr($arg, 0, 1) !== '-') {
        $name = $arg;
        break;
    }
}

// Main script logic
if ($verbose) {
    echo "Verbose mode enabled.\n";
}

if (!empty($name)) {
    echo "Hello, " . htmlspecialchars($name) . "!\n";
} else {
    echo "Hello, World!\n";
}

if ($verbose) {
    echo "Script completed successfully.\n";
}

exit(0);
?>
```
