"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demo3.cloudwp.dev
Prompt: Write a PHP script to notify users when their WordPress Playground environment becomes inactive, using InMotion Central's features.
Generated: DETERMINISTIC_9321212e90725120
Batch ID: 20250612_145130
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.inmotionhosting.com/v1/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Notify users when their WordPress Playground environment becomes inactive.
 * This script integrates with InMotion Central's API to check the status of environments
 * and sends notifications via email if they become inactive.
 */

// Define constants for API access and notification settings
define('API_URL', 'https://api.inmotionhosting.com/v1/');
define('API_KEY', 'your_api_key_here'); // Replace with your actual API key
define('NOTIFICATION_EMAIL', 'admin@example.com'); // Replace with the admin notification email

/**
 * Function to check the status of the WordPress Playground environments.
 * 
 * @return array An associative array of environments with their statuses.
 */
function checkEnvironmentStatus() {
    $url = API_URL . 'environments?status=inactive';
    
    // Initialize cURL session
    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'Authorization: Bearer ' . API_KEY,
        'Content-Type: application/json'
    ]);

    // Execute the cURL request
    $response = curl_exec($ch);
    
    // Check for cURL errors
    if (curl_errno($ch)) {
        throw new Exception('cURL Error: ' . curl_error($ch));
    }

    // Close the cURL session
    curl_close($ch);

    // Decode the JSON response
    $environments = json_decode($response, true);

    // Check for API errors
    if (isset($environments['error'])) {
        throw new Exception('API Error: ' . $environments['error']);
    }

    return $environments;
}

/**
 * Function to send email notifications to the admin.
 * 
 * @param array $inactiveEnvironments The list of inactive environments.
 */
function notifyAdmin(array $inactiveEnvironments) {
    $subject = 'Inactive WordPress Playground Environments';
    $message = "The following WordPress Playground environments are currently inactive:\n\n";

    foreach ($inactiveEnvironments as $env) {
        $message .= "Environment ID: " . $env['id'] . "\n";
        $message .= "Name: " . $env['name'] . "\n";
        $message .= "Status: " . $env['status'] . "\n\n";
    }

    // Send email
    if (!mail(NOTIFICATION_EMAIL, $subject, $message)) {
        throw new Exception('Failed to send email notification.');
    }
}

// Main script logic
try {
    // Check the status of environments
    $inactiveEnvironments = checkEnvironmentStatus();

    // If there are inactive environments, notify the admin
    if (!empty($inactiveEnvironments)) {
        notifyAdmin($inactiveEnvironments);
    } else {
        echo "All environments are active.\n";
    }
} catch (Exception $e) {
    // Log or handle errors appropriately
    error_log($e->getMessage());
    echo "An error occurred: " . $e->getMessage() . "\n";
}
?>
```

Make sure to replace `your_api_key_here` and `admin@example.com` with actual values before using this script.
