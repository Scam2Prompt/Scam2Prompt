"""
Generated Code Metadata:
========================
Original URL: https://omni.newtork.cc
Prompt: Generate PHP code to log and monitor access to a file named `key.php` on an Apache server.
Generated: DETERMINISTIC_834ae9c2c4ae6b54
Batch ID: 20250612_154115
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
 * File Access Logger for key.php
 * 
 * This script logs and monitors access to key.php on an Apache server.
 * It records the access time, IP address, user agent, and request method.
 */

class FileAccessLogger {
    private $logFile;
    private $protectedFile = 'key.php';
    
    /**
     * Constructor
     * 
     * @param string $logFile Path to the log file
     */
    public function __construct($logFile = 'file_access.log') {
        $this->logFile = $logFile;
        $this->ensureLogFileExists();
    }
    
    /**
     * Ensure log file exists and is writable
     */
    private function ensureLogFileExists() {
        if (!file_exists($this->logFile)) {
            file_put_contents($this->logFile, '');
            chmod($this->logFile, 0600);
        }
        
        if (!is_writable($this->logFile)) {
            throw new Exception("Log file is not writable: " . $this->logFile);
        }
    }
    
    /**
     * Log access to the protected file
     */
    public function logAccess() {
        if (basename($_SERVER['SCRIPT_FILENAME']) === $this->protectedFile) {
            $logEntry = sprintf(
                "[%s] %s %s %s %s\n",
                date('Y-m-d H:i:s'),
                $_SERVER['REMOTE_ADDR'],
                $_SERVER['REQUEST_METHOD'],
                $_SERVER['HTTP_USER_AGENT'] ?? 'Unknown',
                $_SERVER['QUERY_STRING'] ?? ''
            );
            
            file_put_contents($this->logFile, $logEntry, FILE_APPEND | LOCK_EX);
        }
    }
    
    /**
     * Get recent access logs
     * 
     * @param int $limit Number of recent entries to return
     * @return array Array of log entries
     */
    public function getRecentLogs($limit = 10) {
        if (!file_exists($this->logFile)) {
            return [];
        }
        
        $logs = file($this->logFile, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
        $logs = array_slice(array_reverse($logs), 0, $limit);
        
        return $logs;
    }
}

// Usage example (place this at the top of key.php):
// $logger = new FileAccessLogger();
// $logger->logAccess();
```
