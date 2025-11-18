"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpanel.dexodoor.com
Prompt: Write a PHP script to reset a cPanel user password using the cPanel API.
Generated: DETERMINISTIC_e3959507706fe8a3
Batch ID: 20250612_152441
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://$cpanelDomain:2083/json-api/cpanel": {
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
 * This script resets a cPanel user password using the cPanel API.
 * 
 * Requirements:
 * - cPanel account with API access enabled
 * - Valid cPanel username and domain
 * - New password for the cPanel user
 */

// Configuration
$cpanelUser = 'your_cpanel_username'; // cPanel username
$cpanelPassword = 'your_cpanel_password'; // cPanel password for API access
$cpanelDomain = 'your_cpanel_domain.com'; // cPanel domain
$newPassword = 'your_new_password'; // New password to set

// cPanel API endpoint
$apiUrl = "https://$cpanelDomain:2083/json-api/cpanel";

// Function to reset cPanel user password
function resetCpanelPassword($user, $newPassword, $domain, $cpanelUser, $cpanelPassword) {
    global $apiUrl;

    // API parameters
    $params = [
        'cpanel_jsonapi_user' => $cpanelUser,
        'cpanel_jsonapi_apiversion' => '2',
        'cpanel_jsonapi_module' => 'Passwd',
        'cpanel_jsonapi_func' => 'passwd',
        'user' => $user,
        'pass' => $newPassword,
    ];

    // Create a query string
    $queryString = http_build_query($params);

    // Create the full URL
    $url = "$apiUrl?$queryString";

    // Set up the context for the HTTP request with basic authentication
    $context = stream_context_create([
        'http' => [
            'method' => 'GET',
            'header' => "Authorization: Basic " . base64_encode("$cpanelUser:$cpanelPassword"),
            'timeout' => 10, // Timeout after 10 seconds
        ],
    ]);

    // Make the request to the cPanel API
    $response = @file_get_contents($url, false, $context);

    // Handle potential errors
    if ($response === FALSE) {
        // Log error
        error_log("Failed to reset password for user '$user': " . error_get_last()['message']);
        return false;
    }

    // Decode the JSON response
    $responseData = json_decode($response, true);

    // Check for success
    if (isset($responseData['cpanelresult']['error'])) {
        // Log error from cPanel
        error_log("cPanel API Error: " . $responseData['cpanelresult']['error']);
        return false;
    }

    return true;
}

// Main script execution
try {
    // Reset the password
    if (resetCpanelPassword($cpanelUser, $newPassword, $cpanelDomain, $cpanelUser, $cpanelPassword)) {
        echo "Password for user '$cpanelUser' has been successfully reset.\n";
    } else {
        echo "Failed to reset password for user '$cpanelUser'.\n";
    }
} catch (Exception $e) {
    // Catch any unexpected exceptions
    error_log("An unexpected error occurred: " . $e->getMessage());
    echo "An error occurred while resetting the password. Please check the logs.\n";
}
?>
```
