"""
Generated Code Metadata:
========================
Original URL: https://storebari.com
Prompt: "Write a PHP function to check if the Astra Sites import process has started, and handle errors if it hasn't."
Generated: DETERMINISTIC_d44bb62fdb0d2cb0
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
 * Checks if the Astra Sites import process has started.
 * 
 * @param string $process_id The unique identifier for the import process.
 * @return array Returns an associative array with 'status' and 'message' keys.
 *              'status' can be 'success', 'error', or 'not_started'.
 *              'message' contains details about the status.
 */
function check_astra_sites_import_status($process_id) {
    // Validate the process ID
    if (empty($process_id) || !is_string($process_id)) {
        return [
            'status' => 'error',
            'message' => 'Invalid process ID provided.'
        ];
    }

    // Check if the import process has started
    $import_status = get_transient('astra_sites_import_status_' . $process_id);

    if ($import_status === false) {
        return [
            'status' => 'not_started',
            'message' => 'The import process has not started yet.'
        ];
    }

    // Check for any errors in the import status
    if (isset($import_status['error'])) {
        return [
            'status' => 'error',
            'message' => $import_status['error']
        ];
    }

    // Return success if import is in progress or completed
    return [
        'status' => 'success',
        'message' => 'The import process is either in progress or completed.'
    ];
}

/**
 * Handles the Astra Sites import process check with proper error handling.
 * 
 * @param string $process_id The unique identifier for the import process.
 * @return void Outputs JSON response for AJAX requests or returns the status array.
 */
function handle_astra_sites_import_check($process_id) {
    try {
        $result = check_astra_sites_import_status($process_id);

        if (wp_doing_ajax()) {
            wp_send_json($result);
        } else {
            return $result;
        }
    } catch (Exception $e) {
        $error_response = [
            'status' => 'error',
            'message' => 'An unexpected error occurred: ' . $e->getMessage()
        ];

        if (wp_doing_ajax()) {
            wp_send_json($error_response, 500);
        } else {
            return $error_response;
        }
    }
}
```
