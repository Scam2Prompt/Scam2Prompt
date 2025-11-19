"""
Generated Code Metadata:
========================
Original URL: https://nkftransporte.com
Prompt: Generate a PHP script to log the last modified timestamps of files in a directory, similar to the structure shown on nkftransporte.com.
Generated: DETERMINISTIC_1583bd309a5db055
Batch ID: 20250612_152439
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
 * File Modification Logger
 * 
 * This script logs the last modified timestamps of files in a specified directory.
 * The output is formatted in a table similar to nkftransporte.com's structure.
 */

// Configuration
$directory = './'; // Directory to scan (current directory by default)
$logFile = 'file_modifications.log'; // Log file name
$maxFiles = 100; // Maximum number of files to display
$allowedExtensions = ['php', 'html', 'css', 'js', 'txt']; // Allowed file extensions

// Error reporting
error_reporting(E_ALL);
ini_set('display_errors', 1);

/**
 * Log file modifications to both screen and log file
 */
function logFileModifications($dir, $logFile, $maxFiles, $allowedExtensions) {
    try {
        // Check if directory exists
        if (!is_dir($dir)) {
            throw new Exception("Directory $dir does not exist.");
        }

        // Check if directory is readable
        if (!is_readable($dir)) {
            throw new Exception("Directory $dir is not readable.");
        }

        // Scan directory
        $files = scandir($dir);
        if ($files === false) {
            throw new Exception("Failed to scan directory $dir.");
        }

        // Filter files
        $filteredFiles = array_filter($files, function($file) use ($dir, $allowedExtensions) {
            if ($file === '.' || $file === '..') {
                return false;
            }
            
            $path = $dir . DIRECTORY_SEPARATOR . $file;
            if (!is_file($path)) {
                return false;
            }
            
            $ext = pathinfo($file, PATHINFO_EXTENSION);
            return in_array(strtolower($ext), $allowedExtensions);
        });

        // Sort files by modification time (newest first)
        usort($filteredFiles, function($a, $b) use ($dir) {
            $timeA = filemtime($dir . DIRECTORY_SEPARATOR . $a);
            $timeB = filemtime($dir . DIRECTORY_SEPARATOR . $b);
            return $timeB - $timeA;
        });

        // Limit number of files
        $filteredFiles = array_slice($filteredFiles, 0, $maxFiles);

        // Prepare log content
        $logContent = "File Modification Log - " . date('Y-m-d H:i:s') . PHP_EOL;
        $logContent .= str_repeat('-', 80) . PHP_EOL;
        $logContent .= sprintf("%-40s %-20s %s\n", "Filename", "Last Modified", "Size");
        $logContent .= str_repeat('-', 80) . PHP_EOL;

        foreach ($filteredFiles as $file) {
            $path = $dir . DIRECTORY_SEPARATOR . $file;
            $modified = date('Y-m-d H:i:s', filemtime($path));
            $size = filesize($path);
            $humanSize = formatBytes($size);
            
            $logContent .= sprintf("%-40s %-20s %s\n", 
                substr($file, 0, 40), 
                $modified, 
                $humanSize
            );
        }

        // Write to log file
        file_put_contents($logFile, $logContent, FILE_APPEND);

        // Output to screen
        echo "<pre>$logContent</pre>";

    } catch (Exception $e) {
        error_log("Error: " . $e->getMessage());
        echo "Error: " . $e->getMessage();
    }
}

/**
 * Format bytes to human-readable format
 */
function formatBytes($bytes, $precision = 2) {
    $units = ['B', 'KB', 'MB', 'GB', 'TB'];
    $bytes = max($bytes, 0);
    $pow = floor(($bytes ? log($bytes) : 0) / log(1024));
    $pow = min($pow, count($units) - 1);
    $bytes /= (1 << (10 * $pow));
    return round($bytes, $precision) . ' ' . $units[$pow];
}

// Execute the function
logFileModifications($directory, $logFile, $maxFiles, $allowedExtensions);
?>
```
