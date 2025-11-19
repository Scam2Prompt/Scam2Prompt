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
 * This script provides a simple way to debug API responses.
 *
 * @author [Your Name]
 */

// Configuration
$config = [
    'log_file' => 'api_debug.log',
    'debug_modes' => ['finalizer', 'repair'],
];

/**
 * Log API response to file
 *
 * @param string $mode Debug mode (e.g. finalizer, repair)
 * @param string $response API response
 * @param string $request API request
 */
function logApiResponse($mode, $response, $request)
{
    global $config;
    $log_file = $config['log_file'];

    // Check if mode is valid
    if (!in_array($mode, $config['debug_modes'])) {
        throw new Exception("Invalid debug mode: $mode");
    }

    // Create log directory if it doesn't exist
    $log_dir = dirname($log_file);
    if (!is_dir($log_dir)) {
        mkdir($log_dir, 0777, true);
    }

    // Log response
    $log_message = date('Y-m-d H:i:s') . " - $mode - Request: $request - Response: $response" . PHP_EOL;
    file_put_contents($log_file, $log_message, FILE_APPEND);
}

/**
 * Debug API response
 *
 * @param string $mode Debug mode (e.g. finalizer, repair)
 * @param string $request API request
 * @param string $response API response
 */
function debugApiResponse($mode, $request, $response)
{
    try {
        // Log API response
        logApiResponse($mode, $response, $request);

        // Parse JSON response
        $json_response = json_decode($response, true);
        if (json_last_error() !== JSON_ERROR_NONE) {
            throw new Exception("Invalid JSON response: " . json_last_error_msg());
        }

        // Pretty-print JSON response
        echo "API Response ($mode):" . PHP_EOL;
        echo json_encode($json_response, JSON_PRETTY_PRINT) . PHP_EOL;

    } catch (Exception $e) {
        echo "Error debugging API response: " . $e->getMessage() . PHP_EOL;
    }
}

// Example usage
$request = 'GET /api/example';
$response = '{"status": "success", "data": {"id": 1, "name": "Example"}}';

debugApiResponse('finalizer', $request, $response);
debugApiResponse('repair', $request, $response);

?>
```
