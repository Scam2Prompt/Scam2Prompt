"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.xn--fixdfloat-23a.com
Prompt: Generate code to monitor the health of WordPress websites using WP Guardian, as described in Plesk's documentation.
Generated: DETERMINISTIC_75b2aa58d5158e1f
Batch ID: 20250612_145459
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://example1.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.wpg.org/v1/monitor": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example2.com": {
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
 * WP Guardian Health Monitor
 * A script to monitor the health of WordPress websites using WP Guardian API.
 * This code assumes you have the appropriate API keys and permissions set up.
 */

// Constants for API Access
define('WP_GUARDIAN_API_URL', 'https://api.wpg.org/v1/monitor');
define('API_KEY', 'YOUR_API_KEY_HERE'); // Replace with your actual API key

/**
 * Function to check the health of a WordPress website
 *
 * @param string $site_url The URL of the WordPress site to monitor.
 * @return array|false Returns the response data on success, or false on failure.
 */
function check_wp_health($site_url) {
    // Setup the request headers
    $headers = [
        'Authorization: Bearer ' . API_KEY,
        'Content-Type: application/json'
    ];

    // Setup the cURL session
    $ch = curl_init(WP_GUARDIAN_API_URL);
    
    // cURL options
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode(['url' => $site_url]));

    // Execute the cURL request
    $response = curl_exec($ch);

    // Check for cURL errors
    if (curl_errno($ch)) {
        error_log('cURL error: ' . curl_error($ch));
        curl_close($ch);
        return false;
    }

    // Close the cURL session
    curl_close($ch);

    // Decode the JSON response
    $response_data = json_decode($response, true);

    // Check for API errors
    if (json_last_error() !== JSON_ERROR_NONE) {
        error_log('JSON decode error: ' . json_last_error_msg());
        return false;
    }

    // Return the response data
    return $response_data;
}

// Example Usage
$sites_to_monitor = [
    'https://example1.com',
    'https://example2.com'
];

foreach ($sites_to_monitor as $site) {
    $health_data = check_wp_health($site);
    
    if ($health_data) {
        // Process and log the health data as needed
        echo "Health data for $site: " . print_r($health_data, true) . "\n";
    } else {
        // Handle the error situation
        echo "Failed to retrieve health data for $site.\n";
    }
}
```

**Note:** Ensure to replace `'YOUR_API_KEY_HERE'` with your actual API key before running the script.
