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

namespace app\log\driver;

use think\contract\LogHandlerInterface;

class FileLogger implements LogHandlerInterface
{
    // Configuration settings for the file logger
    protected $config = [
        'path'     => '',       // Log storage path
        'level'    => [],       // Logging levels to handle
        'max_files' => 0,       // Maximum number of log files to retain
        'json'     => false,    // Whether to log in JSON format
    ];

    /**
     * Constructor to initialize the logger configuration.
     *
     * @param array $config Configuration settings for the logger.
     */
    public function __construct(array $config = [])
    {
        $this->config = array_merge($this->config, $config);

        // Ensure the log path exists
        if (!is_dir($this->config['path'])) {
            mkdir($this->config['path'], 0755, true);
        }
    }

    /**
     * Save logs to the file system.
     *
     * @param array $log Log data categorized by level.
     * @return void
     * @throws \Exception
     */
    public function save(array $log): void
    {
        try {
            // Generate a log file name based on current date
            $filename = $this->config['path'] . DIRECTORY_SEPARATOR . date('Y-m-d') . '.log';

            // Prepare the log content
            $logContent = '';
            foreach ($log as $level => $messages) {
                if (!empty($this->config['level']) && !in_array($level, $this->config['level'])) {
                    continue; // Skip levels not configured for logging
                }

                foreach ($messages as $message) {
                    $formattedMessage = $this->formatMessage($level, $message);
                    $logContent .= $formattedMessage . PHP_EOL;
                }
            }

            // Write the log content to the file
            file_put_contents($filename, $logContent, FILE_APPEND | LOCK_EX);

            // Handle log rotation if max_files is configured
            $this->handleLogRotation();
        } catch (\Exception $e) {
            throw new \Exception('Failed to save log: ' . $e->getMessage());
        }
    }

    /**
     * Format the individual log message.
     *
     * @param string $level Log level (e.g., error, info).
     * @param mixed $message Log message content.
     * @return string
     */
    protected function formatMessage(string $level, $message): string
    {
        // Format message to JSON if the JSON flag is enabled
        if ($this->config['json']) {
            $message = json_encode([
                'level'   => $level,
                'message' => $message,
                'time'    => date('Y-m-d H:i:s'),
            ]);
        } else {
            $message = sprintf(
                "[%s] %s: %s",
                date('Y-m-d H:i:s'),
                strtoupper($level),
                is_string($message) ? $message : var_export($message, true)
            );
        }

        return $message;
    }

    /**
     * Handle log file rotation based on the max_files configuration.
     *
     * @return void
     */
    protected function handleLogRotation(): void
    {
        if ($this->config['max_files'] > 0) {
            $files = glob($this->config['path'] . DIRECTORY_SEPARATOR . '*.log');
            if (count($files) > $this->config['max_files']) {
                // Sort files by last modified time
                usort($files, function ($a, $b) {
                    return filemtime($a) - filemtime($b);
                });

                // Remove oldest files to respect max_files limit
                while (count($files) > $this->config['max_files']) {
                    unlink(array_shift($files));
                }
            }
        }
    }
}

```
