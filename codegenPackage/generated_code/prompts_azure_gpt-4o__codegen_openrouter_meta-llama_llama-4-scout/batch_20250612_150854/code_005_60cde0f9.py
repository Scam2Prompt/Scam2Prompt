"""
Generated Code Metadata:
========================
Original URL: https://immediategpt.nl
Prompt: Write code in PHP to display a disclaimer message to users based on their country, similar to the "Forbidden - Visitors from your country are not permitted to browse this site" functionality on Immediate GPT.
Generated: DETERMINISTIC_60cde0f968b60604
Batch ID: 20250612_150854
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://ip-api.com/json/$ipAddress": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```php
<?php

/**
 * Country Disclaimer Checker
 *
 * This script checks the user's country based on their IP address and displays a disclaimer message if their country is not permitted.
 */

// Configuration
$permittedCountries = array('US', 'CA', 'GB'); // List of permitted countries
$disclaimerMessage = 'Forbidden - Visitors from your country are not permitted to browse this site';

/**
 * Get the user's country based on their IP address
 *
 * @param string $ipAddress
 * @return string|null
 */
function getCountryFromIp($ipAddress)
{
    try {
        $response = file_get_contents("http://ip-api.com/json/$ipAddress");
        if ($response !== false) {
            $data = json_decode($response, true);
            return $data['countryCode'];
        } else {
            // Handle API request failure
            error_log('Failed to retrieve country data from ip-api.com');
            return null;
        }
    } catch (Exception $e) {
        // Handle exception
        error_log('Error retrieving country data: ' . $e->getMessage());
        return null;
    }
}

/**
 * Check if the user's country is permitted
 *
 * @param string $countryCode
 * @return bool
 */
function isCountryPermitted($countryCode, $permittedCountries)
{
    return in_array($countryCode, $permittedCountries);
}

// Get the user's IP address
$userIpAddress = $_SERVER['REMOTE_ADDR'];

// Get the user's country
$userCountry = getCountryFromIp($userIpAddress);

// Check if the user's country is permitted
if ($userCountry !== null && !isCountryPermitted($userCountry, $permittedCountries)) {
    // Display disclaimer message
    http_response_code(403);
    echo $disclaimerMessage;
    exit;
}

// If the user's country is permitted, continue to the rest of the site
// You can add your site's content here

?>
```
