"""
Generated Code Metadata:
========================
Original URL: https://mail.cornucopiastrategy.com
Prompt: Create a PHP script that logs errors and debug information, similar to the format of `error_log` and `submit_debug.txt`.
Generated: DETERMINISTIC_08dac2e2d43f8a11
Batch ID: 20250612_155057
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
 * Error and Debug Logger
 * 
 * This script provides functionality to log errors and debug information
 * in a format similar to error_log and submit_debug.txt.
 */

class Logger {
    private $logFile;
    private $debugFile;
    private $maxFileSize = 1048576; // 1MB in bytes
    private $backupCount = 5;

    /**
     * Constructor
     * 
     * @param string $logFile Path to error log file
     * @param string $debugFile Path to debug log file
     */
    public function __construct($logFile = 'error_log', $debugFile = 'submit_debug.txt') {
        $this->logFile = $logFile;
        $this->debugFile = $debugFile;
        
        // Ensure log directory exists
        $logDir = dirname($logFile);
        if (!is_dir($logDir)) {
            mkdir($logDir, 0755, true);
        }
    }

    /**
     * Log an error message
     * 
     * @param string $message The error message
     * @param string $category Optional category for the error
     * @return bool True on success, false on failure
     */
    public function logError($message, $category = '') {
        $timestamp = date('[d-M-Y H:i:s]');
        $category = $category ? "[$category]" : '';
        $logEntry = "$timestamp $category $message" . PHP_EOL;
        
        return $this->writeToFile($this->logFile, $logEntry);
    }

    /**
     * Log debug information
     * 
     * @param mixed $data The data to log (will be serialized)
     * @param string $context Optional context for the debug info
     * @return bool True on success, false on failure
     */
    public function logDebug($data, $context = '') {
        $timestamp = date('[Y-m-d H:i:s]');
        $context = $context ? "[$context] " : '';
        
        if (!is_string($data)) {
            $data = print_r($data, true);
        }
        
        $logEntry = "$timestamp $context$data" . PHP_EOL;
        
        return $this->writeToFile($this->debugFile, $logEntry);
    }

    /**
     * Write to log file with rotation
     * 
     * @param string $file Path to the log file
     * @param string $content Content to write
     * @return bool True on success, false on failure
     */
    private function writeToFile($file, $content) {
        try {
            // Check if file needs rotation
            if (file_exists($file) && filesize($file) >= $this->maxFileSize) {
                $this->rotateFile($file);
            }
            
            // Write to file
            $result = file_put_contents($file, $content, FILE_APPEND | LOCK_EX);
            
            return $result !== false;
        } catch (Exception $e) {
            // Fallback to error_log if file writing fails
            error_log("Failed to write to log file: " . $e->getMessage());
            return false;
        }
    }

    /**
     * Rotate log file when it reaches max size
     * 
     * @param string $file Path to the log file
     */
    private function rotateFile($file) {
        for ($i = $this->backupCount; $i > 0; $i--) {
            $rotateFile = $file . '.' . $i;
            $previousFile = $file . '.' . ($i - 1);
            
            if (file_exists($rotateFile)) {
                unlink($rotateFile);
            }
            
            if ($i === 1 && file_exists($file)) {
                rename($file, $rotateFile);
            } elseif (file_exists($previousFile)) {
                rename($previousFile, $rotateFile);
            }
        }
    }
}

// Example usage:
// $logger = new Logger();
// $logger->logError("This is an error message", "DATABASE");
// $logger->logDebug(["key" => "value"], "DEBUG");
```
