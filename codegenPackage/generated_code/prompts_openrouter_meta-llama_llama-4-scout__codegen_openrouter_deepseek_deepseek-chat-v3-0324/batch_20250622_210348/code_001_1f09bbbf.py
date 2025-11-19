"""
Generated Code Metadata:
========================
Original URL: https://imaginrayones.com
Prompt: Generate a PHP test page using Plesk's scripting features.
Generated: DETERMINISTIC_1f09bbbf6834b69e
Batch ID: 20250622_210348
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
 * Plesk Test Page
 * 
 * This script demonstrates basic Plesk API usage and common operations.
 * It includes error handling and follows PHP best practices.
 */

// Check if we're running in Plesk environment
if (!defined('PLESK_API_URL')) {
    die("This script must be run within Plesk environment.");
}

// Set headers to prevent caching and ensure proper content type
header("Cache-Control: no-store, no-cache, must-revalidate, max-age=0");
header("Cache-Control: post-check=0, pre-check=0", false);
header("Pragma: no-cache");
header("Content-Type: text/html; charset=UTF-8");

// Error reporting for development (should be disabled in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

try {
    // Start output buffering
    ob_start();
    
    // Basic page structure
    echo '<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Plesk Test Page</title>
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }
            .success { color: green; }
            .error { color: red; }
            .info { color: blue; }
            pre { background: #f4f4f4; padding: 10px; border-radius: 5px; }
        </style>
    </head>
    <body>
        <h1>Plesk Test Page</h1>';
    
    // Check Plesk API connection
    echo '<h2>Plesk Environment Check</h2>';
    echo '<p>PLESK_API_URL: ' . PLESK_API_URL . '</p>';
    
    // Test Plesk API functions
    echo '<h2>Plesk API Tests</h2>';
    
    // Example: Get server information
    $request = <<<APICALL
<packet>
    <server>
        <get>
            <stat/>
        </get>
    </server>
</packet>
APICALL;

    $response = pm_ApiRpc::getService()->call($request);
    if ($response && $response->server->get->result->status === 'ok') {
        echo '<div class="success">Plesk API connection successful</div>';
        echo '<pre>' . htmlspecialchars(print_r($response, true)) . '</pre>';
    } else {
        throw new Exception("Failed to connect to Plesk API");
    }
    
    // Example: List domains
    $request = <<<APICALL
<packet>
    <webspace>
        <get>
            <filter/>
            <dataset>
                <hosting/>
            </dataset>
        </get>
    </webspace>
</packet>
APICALL;

    $response = pm_ApiRpc::getService()->call($request);
    if ($response && $response->webspace->get->result->status === 'ok') {
        echo '<h3>Domains on this server:</h3>';
        echo '<ul>';
        foreach ($response->webspace->get->result as $webspace) {
            if (isset($webspace->data->gen_info->name)) {
                echo '<li>' . htmlspecialchars($webspace->data->gen_info->name) . '</li>';
            }
        }
        echo '</ul>';
    } else {
        echo '<div class="error">Failed to retrieve domain list</div>';
    }
    
    // End of page
    echo '</body></html>';
    
    // Flush output buffer
    ob_end_flush();
    
} catch (Exception $e) {
    // Clean any previous output
    ob_end_clean();
    
    // Display error message
    echo '<!DOCTYPE html>
    <html>
    <head>
        <title>Error</title>
        <style>
            body { font-family: Arial, sans-serif; padding: 20px; }
            .error { color: red; }
        </style>
    </head>
    <body>
        <h1 class="error">Error</h1>
        <p>' . htmlspecialchars($e->getMessage()) . '</p>
        <pre>' . htmlspecialchars($e->getTraceAsString()) . '</pre>
    </body>
    </html>';
    
    // Log the error
    error_log('Plesk Test Page Error: ' . $e->getMessage());
}
```
