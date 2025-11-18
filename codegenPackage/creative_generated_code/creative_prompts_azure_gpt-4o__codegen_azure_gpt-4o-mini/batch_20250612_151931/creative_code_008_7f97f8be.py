"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonpad.net
Prompt: Generate a ThinkPHP log driver for file-based logging, referencing `log/driver/File.php` from the Moonpad website.
Generated: DETERMINISTIC_7f97f8be2a2a7650
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
namespace think\log\driver;

use think\Log;

/**
 * File Log Driver for ThinkPHP
 * 
 * This class handles file-based logging for the ThinkPHP framework.
 * It allows for writing log messages to files in a specified directory.
 */
class File
{
    // Log directory path
    protected $logPath;

    // Log file name
    protected $logFileName;

    // Log file resource
    protected $logFile;

    /**
     * Constructor to initialize log file settings
     *
     * @param string $logPath Path where log files will be stored
     * @param string $logFileName Name of the log file
     */
    public function __construct($logPath, $logFileName = 'application.log')
    {
        // Set log path
        $this->logPath = rtrim($logPath, '/') . '/';
        
        // Set log file name
        $this->logFileName = $logFileName;

        // Ensure the log directory exists
        if (!is_dir($this->logPath)) {
            if (!mkdir($this->logPath, 0755, true)) {
                throw new \RuntimeException("Unable to create log directory: {$this->logPath}");
            }
        }

        // Open or create the log file
        $this->logFile = fopen($this->logPath . $this->logFileName, 'a');
        
        if ($this->logFile === false) {
            throw new \RuntimeException("Unable to open log file: {$this->logPath}{$this->logFileName}");
        }
    }

    /**
     * Write a log entry to the file
     *
     * @param string $level The severity level of the log (e.g., 'info', 'error', etc.)
     * @param string $message The log message
     * @param array $context Additional context to include in the log
     */
    public function log($level, $message, array $context = [])
    {
        $timestamp = date('Y-m-d H:i:s');
        
        // Format the log message
        $formattedMessage = sprintf("[%s] [%s] %s%s", 
            $timestamp, 
            strtoupper($level), 
            $this->interpolate($message, $context), 
            PHP_EOL
        );

        // Write to log file and handle errors
        if (fwrite($this->logFile, $formattedMessage) === false) {
            throw new \RuntimeException("Unable to write to log file: {$this->logPath}{$this->logFileName}");
        }
    }

    /**
     * Interpolates context variables into the log message
     *
     * @param string $message The log message
     * @param array $context The context array
     * @return string The interpolated message
     */
    protected function interpolate($message, array $context)
    {
        // Replace placeholders with actual context values
        return preg_replace_callback('/{([^}]+)}/', function ($matches) use ($context) {
            return $context[$matches[1]] ?? $matches[0];
        }, $message);
    }

    /**
     * Destructor to close the log file
     */
    public function __destruct()
    {
        if (is_resource($this->logFile)) {
            fclose($this->logFile);
        }
    }
}
```
