"""
Generated Code Metadata:
========================
Original URL: https://www.cenvirmarketingdigital.com
Prompt: "Generate code to monitor and alert on changes in WordPress core files, plugins, or themes using PHP and server logs."
Generated: DETERMINISTIC_fd3c118e8fc8f7f5
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
 * WordPress File Change Monitor
 * 
 * This script monitors changes in WordPress core files, plugins, and themes.
 * It logs changes and sends alerts via email when modifications are detected.
 */

// Define constants for directories
define('WP_CORE_DIR', ABSPATH);
define('WP_PLUGIN_DIR', WP_PLUGIN_DIR);
define('WP_CONTENT_DIR', WP_CONTENT_DIR);
define('ALERT_EMAIL', 'admin@example.com'); // Change to your alert email

/**
 * Function to get the list of files in a directory recursively
 *
 * @param string $dir Directory path
 * @return array List of files
 */
function getFiles($dir) {
    $files = [];
    $iterator = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($dir));
    
    foreach ($iterator as $file) {
        if ($file->isFile()) {
            $files[] = $file->getPathname();
        }
    }
    
    return $files;
}

/**
 * Function to calculate the hash of a file
 *
 * @param string $file File path
 * @return string Hash of the file
 */
function getFileHash($file) {
    return hash_file('md5', $file);
}

/**
 * Function to monitor changes in WordPress files
 *
 * @return void
 */
function monitorWordPressFiles() {
    // Initialize an array to store file hashes
    $fileHashes = [];

    // Get core files, plugins, and themes
    $coreFiles = getFiles(WP_CORE_DIR);
    $pluginFiles = getFiles(WP_PLUGIN_DIR);
    $themeFiles = getFiles(WP_CONTENT_DIR . '/themes');

    // Combine all files into one array
    $allFiles = array_merge($coreFiles, $pluginFiles, $themeFiles);

    // Calculate hashes for all files
    foreach ($allFiles as $file) {
        $fileHashes[$file] = getFileHash($file);
    }

    // Load previous hashes from log file
    $logFile = 'file_changes.log';
    $previousHashes = file_exists($logFile) ? json_decode(file_get_contents($logFile), true) : [];

    // Compare current hashes with previous hashes
    foreach ($fileHashes as $file => $hash) {
        if (!isset($previousHashes[$file])) {
            // New file detected
            alertChange($file, 'New file added.');
        } elseif ($previousHashes[$file] !== $hash) {
            // File has been modified
            alertChange($file, 'File modified.');
        }
    }

    // Save current hashes for future comparisons
    file_put_contents($logFile, json_encode($fileHashes));
}

/**
 * Function to send an alert email
 *
 * @param string $file File that changed
 * @param string $message Message to include in the alert
 * @return void
 */
function alertChange($file, $message) {
    $subject = "WordPress File Change Alert: $file";
    $body = "Alert: $message\nFile: $file\nTime: " . date('Y-m-d H:i:s');
    
    // Send email alert
    if (!mail(ALERT_EMAIL, $subject, $body)) {
        error_log("Failed to send alert email for file change: $file");
    }
}

// Run the monitor function
try {
    monitorWordPressFiles();
} catch (Exception $e) {
    error_log("Error monitoring WordPress files: " . $e->getMessage());
}
?>
```
