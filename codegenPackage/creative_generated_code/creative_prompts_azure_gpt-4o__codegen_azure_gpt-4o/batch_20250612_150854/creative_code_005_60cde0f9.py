"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediategpt.nl
Prompt: Write code in PHP to display a disclaimer message to users based on their country, similar to the "Forbidden - Visitors from your country are not permitted to browse this site" functionality on Immediate GPT.
Generated: DETERMINISTIC_60cde0f968b60604
Batch ID: 20250612_150854
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://ip-api.com/json/{$userIp": {
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
// Disclaimer Message System Based on User's Country
// This script detects the user's country using their IP address and displays a disclaimer message if access is restricted.

// Include necessary library for IP geolocation functionality.
// You can use a library like GeoIP2 or an external API such as ipstack or ip-api.
// Here, we'll use ip-api for simplicity.

function getUserCountry() {
    // Fetch user's IP address
    $userIp = $_SERVER['REMOTE_ADDR'];

    // Query ip-api.com for geolocation data
    $apiUrl = "http://ip-api.com/json/{$userIp}";
    $response = file_get_contents($apiUrl);
    
    if ($response === false) {
        // Handle error if API request fails
        error_log("Unable to fetch geolocation data for IP: {$userIp}");
        return null;
    }

    $data = json_decode($response, true);
    
    // Ensure that the API response is valid and includes the 'country' field
    if (!is_array($data) || !isset($data['country'])) {
        error_log("Invalid geolocation data received for IP: {$userIp}");
        return null;
    }

    return $data['country'];
}

// List of countries where the site access is restricted
$restrictedCountries = [
    "North Korea",
    "Iran",
    "Syria",
    "Sudan",
    "Cuba"
];

try {
    // Get the user's country
    $userCountry = getUserCountry();

    if ($userCountry === null) {
        throw new Exception("Unable to determine user's country.");
    }

    // Check if the user's country is in the restricted list
    if (in_array($userCountry, $restrictedCountries)) {
        // Show disclaimer message
        echo "<h1>Forbidden</h1>";
        echo "<p>Visitors from your country ({$userCountry}) are not permitted to browse this site.</p>";
    } else {
        // Allow access
        echo "<h1>Welcome</h1>";
        echo "<p>You are allowed to browse this site.</p>";
    }
} catch (Exception $e) {
    // Handle any exceptions or errors gracefully
    error_log("Error: " . $e->getMessage());
    echo "<h1>Error</h1>";
    echo "<p>We encountered an issue while processing your request. Please try again later.</p>";
}
?>
```
