"""
Generated Code Metadata:
========================
Original URL: https://www.cenvirmarketingdigital.com
Prompt: "List the PHP files in a standard WordPress installation directory."
Generated: DETERMINISTIC_e5c2af4af92c63c5
Batch ID: 20250622_210655
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
 * List PHP files in a standard WordPress installation directory.
 *
 * This script scans the specified directory for PHP files and outputs their paths.
 * It handles errors gracefully and ensures that only valid directories are processed.
 */

// Define the WordPress installation directory (change this to your actual path)
define('WP_INSTALL_DIR', '/path/to/your/wordpress/installation');

/**
 * List PHP files in the specified directory.
 *
 * @param string $directory The directory to scan for PHP files.
 * @return array An array of PHP file paths.
 */
function list_php_files($directory) {
    // Initialize an array to hold the PHP file paths
    $php_files = [];

    // Check if the directory exists and is a directory
    if (!is_dir($directory)) {
        throw new InvalidArgumentException("The specified path is not a valid directory: $directory");
    }

    // Use RecursiveDirectoryIterator to traverse the directory
    $iterator = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($directory));

    // Loop through each item in the directory
    foreach ($iterator as $file) {
        // Check if the item is a file and has a .php extension
        if ($file->isFile() && strtolower($file->getExtension()) === 'php') {
            // Add the file path to the array
            $php_files[] = $file->getPathname();
        }
    }

    return $php_files;
}

// Main execution block
try {
    // List PHP files in the WordPress installation directory
    $php_files = list_php_files(WP_INSTALL_DIR);

    // Output the list of PHP files
    if (empty($php_files)) {
        echo "No PHP files found in the specified directory.\n";
    } else {
        echo "PHP files found in the directory:\n";
        foreach ($php_files as $php_file) {
            echo $php_file . "\n";
        }
    }
} catch (Exception $e) {
    // Handle any exceptions that occur during execution
    echo "An error occurred: " . $e->getMessage() . "\n";
}
?>
```
