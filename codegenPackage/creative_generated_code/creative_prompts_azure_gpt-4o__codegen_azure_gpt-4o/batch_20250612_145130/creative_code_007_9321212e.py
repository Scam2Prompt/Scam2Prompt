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
  "https://api.inmotionhosting.com": {
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
 * Script to notify users when their WordPress Playground environment becomes inactive.
 * Utilizes InMotion Central's API for environment status checks.
 * 
 * Requirements:
 * - PHP 7.4 or later
 * - InMotion Central API credentials (API Key)
 */

// Configuration
define('IMC_API_BASE_URL', 'https://api.inmotionhosting.com'); // InMotion Central API base URL
define('IMC_API_KEY', 'your_api_key_here'); // Replace with your API key
define('EMAIL_FROM', 'no-reply@yourdomain.com'); // Sender email address
define('ADMIN_EMAIL', 'admin@yourdomain.com'); // Admin email address for fallback

/**
 * Sends an email notification to the user about the inactive environment.
 * 
 * @param string $email Recipient email address.
 * @param string $environmentName Environment name.
 * @return bool True if email sent successfully, false otherwise.
 */
function notifyUser($email, $environmentName)
{
    $subject = "Your WordPress Playground Environment is Inactive";
    $message = "Hello,\n\nYour WordPress Playground environment '{$environmentName}' has become inactive.\n\nPlease visit your InMotion Central dashboard to reactivate it.\n\nRegards,\nYour Team";
    
    $headers = "From: " . EMAIL_FROM;
    
    return mail($email, $subject, $message, $headers);
}

/**
 * Fetches the list of environments and their statuses from InMotion Central.
 * 
 * @return array|null Array of environments with statuses, or null on failure.
 */
function fetchEnvironments()
{
    $url = IMC_API_BASE_URL . '/v1/environments'; // API endpoint for fetching environments
    
    $options = [
        'http' => [
            'header' => "Authorization: Bearer " . IMC_API_KEY,
            'method' => 'GET'
        ]
    ];
    
    $context = stream_context_create($options);
    $response = file_get_contents($url, false, $context);
    
    if ($response === false) {
        error_log("Failed to fetch environments from InMotion Central API.");
        return null;
    }
    
    $data = json_decode($response, true);
    if (!is_array($data)) {
        error_log("Invalid response format received from InMotion Central API.");
        return null;
    }
    
    return $data;
}

/**
 * Main function to check environments and notify users if inactive.
 */
function checkAndNotifyInactiveEnvironments()
{
    $environments = fetchEnvironments();
    
    if ($environments === null) {
        error_log("Unable to retrieve environments. Exiting.");
        return;
    }
    
    foreach ($environments as $environment) {
        // Validate required keys
        if (!isset($environment['name'], $environment['status'], $environment['owner_email'])) {
            error_log("Environment data is incomplete: " . json_encode($environment));
            continue;
        }
        
        // Check if the environment is inactive
        if ($environment['status'] === 'inactive') {
            $emailSent = notifyUser($environment['owner_email'], $environment['name']);
            
            if (!$emailSent) {
                error_log("Failed to send email notification to {$environment['owner_email']} for environment '{$environment['name']}'.");
            }
        }
    }
}

// Execute the script
checkAndNotifyInactiveEnvironments();
```
