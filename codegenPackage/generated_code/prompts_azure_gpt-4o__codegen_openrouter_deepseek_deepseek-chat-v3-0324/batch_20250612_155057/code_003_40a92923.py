"""
Generated Code Metadata:
========================
Original URL: https://mail.cornucopiastrategy.com
Prompt: Write a PHP script to debug API responses, inspired by the techniques used in `finalizer_debug.txt` and `repair_debug.txt`.
Generated: DETERMINISTIC_40a92923726d8d33
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
 * API Response Debugger
 * 
 * This script helps debug API responses by logging detailed information,
 * handling errors, and providing a structured output for analysis.
 */

class ApiDebugger {
    private $logFile;
    private $verbose;
    private $maxLogSize = 1048576; // 1MB in bytes

    /**
     * Constructor
     * 
     * @param string $logFile Path to log file
     * @param bool $verbose Enable verbose logging
     */
    public function __construct($logFile = 'api_debug.log', $verbose = false) {
        $this->logFile = $logFile;
        $this->verbose = $verbose;
        $this->initializeLog();
    }

    /**
     * Initialize log file with headers
     */
    private function initializeLog() {
        if (!file_exists($this->logFile)) {
            file_put_contents($this->logFile, "=== API Debug Log ===\n", FILE_APPEND);
        } else {
            // Rotate log if it exceeds max size
            if (filesize($this->logFile) > $this->maxLogSize) {
                $backupFile = $this->logFile . '.' . date('YmdHis');
                rename($this->logFile, $backupFile);
                file_put_contents($this->logFile, "=== API Debug Log (Rotated) ===\n");
            }
        }
    }

    /**
     * Log a debug message
     * 
     * @param string $message Message to log
     * @param mixed $data Additional data to log
     */
    public function log($message, $data = null) {
        $timestamp = date('Y-m-d H:i:s');
        $logEntry = "[$timestamp] $message\n";

        if ($this->verbose && $data !== null) {
            $logEntry .= $this->formatData($data) . "\n";
        }

        file_put_contents($this->logFile, $logEntry, FILE_APPEND);
    }

    /**
     * Format data for logging
     * 
     * @param mixed $data Data to format
     * @return string Formatted data
     */
    private function formatData($data) {
        if (is_string($data)) {
            return $data;
        }

        if (is_resource($data)) {
            return '[Resource]';
        }

        return print_r($data, true);
    }

    /**
     * Debug an API response
     * 
     * @param mixed $response API response to debug
     * @param array $context Additional context information
     */
    public function debugResponse($response, $context = []) {
        $this->log("=== API Response Debug ===");
        
        // Log context if provided
        if (!empty($context)) {
            $this->log("Context:", $context);
        }

        // Check if response is valid
        if ($response === null) {
            $this->log("Error: Response is NULL");
            return;
        }

        // Handle different response types
        if (is_string($response)) {
            $this->debugStringResponse($response);
        } elseif (is_array($response) || is_object($response)) {
            $this->debugStructuredResponse($response);
        } else {
            $this->log("Unknown response type: " . gettype($response));
        }

        $this->log("=== End Debug ===");
    }

    /**
     * Debug a string response
     * 
     * @param string $response API response as string
     */
    private function debugStringResponse($response) {
        $this->log("Raw Response:", $response);

        // Try to decode JSON
        $decoded = json_decode($response, true);
        if (json_last_error() === JSON_ERROR_NONE) {
            $this->log("Decoded JSON:", $decoded);
        } else {
            $this->log("Response is not JSON (Error: " . json_last_error_msg() . ")");
        }

        // Check for common error patterns
        $this->checkForErrors($response);
    }

    /**
     * Debug a structured response (array/object)
     * 
     * @param mixed $response Structured API response
     */
    private function debugStructuredResponse($response) {
        $this->log("Structured Response:", $response);

        // Check for common error fields
        if (is_array($response) || is_object($response)) {
            $this->checkErrorFields($response);
        }
    }

    /**
     * Check string response for common error patterns
     * 
     * @param string $response API response
     */
    private function checkForErrors($response) {
        $errorPatterns = [
            '/error/i',
            '/exception/i',
            '/failed/i',
            '/not found/i',
            '/unauthorized/i',
            '/forbidden/i',
            '/timeout/i',
            '/server error/i'
        ];

        foreach ($errorPatterns as $pattern) {
            if (preg_match($pattern, $response)) {
                $this->log("Potential error detected in response (pattern: $pattern)");
            }
        }
    }

    /**
     * Check structured response for common error fields
     * 
     * @param array|object $response API response
     */
    private function checkErrorFields($response) {
        $errorFields = ['error', 'errors', 'message', 'status', 'code'];
        
        foreach ($errorFields as $field) {
            if (is_array($response) && isset($response[$field])) {
                $this->log("Error field detected: $field = " . $this->formatData($response[$field]));
            } elseif (is_object($response) && property_exists($response, $field)) {
                $this->log("Error field detected: $field = " . $this->formatData($response->$field));
            }
        }
    }

    /**
     * Get the log contents
     * 
     * @return string Log contents
     */
    public function getLog() {
        return file_get_contents($this->logFile);
    }

    /**
     * Clear the log file
     */
    public function clearLog() {
        file_put_contents($this->logFile, "=== API Debug Log (Cleared) ===\n");
    }
}

// Example usage:
// $debugger = new ApiDebugger('custom_debug.log', true);
// $debugger->debugResponse($apiResponse, ['endpoint' => '/users', 'method' => 'GET']);
// echo $debugger->getLog();
?>
```
