"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hodlit.rf.gd
Prompt: Generate PHP code to check and switch between multiple PHP versions on a hosting service, referencing the iFastNet hosting platform.
Generated: DETERMINISTIC_66ad6a665de36984
Batch ID: 20250612_151504
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.ifastnet.com/api/switchPhpVersion": {
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
 * Switch PHP version on iFastNet hosting platform.
 *
 * This script checks the current PHP version and allows the user to switch
 * to a specified version if it is supported by the hosting service.
 *
 * Usage: 
 * 1. Set the desired PHP version by modifying the `$desiredPhpVersion` variable.
 * 2. Run the script to check and switch PHP versions.
 */

// List of supported PHP versions on iFastNet
$supportedPhpVersions = ['7.4', '8.0', '8.1', '8.2'];

// Desired PHP version to switch to
$desiredPhpVersion = '8.1'; // Change this to the desired version

// Function to check if the desired PHP version is supported
function isPhpVersionSupported($version, $supportedVersions) {
    return in_array($version, $supportedVersions);
}

// Function to switch PHP version
function switchPhpVersion($version) {
    // Assuming iFastNet's API or control panel allows switching PHP versions via a specific endpoint
    $apiUrl = "https://example.ifastnet.com/api/switchPhpVersion"; // Replace with actual API URL
    $apiKey = "your_api_key"; // Replace with your actual API key

    // Prepare the data to send in the API request
    $data = [
        'version' => $version,
        'apiKey' => $apiKey
    ];

    // Use cURL to make the API request
    $ch = curl_init($apiUrl);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));

    // Execute the request
    $response = curl_exec($ch);
    
    // Check for cURL errors
    if (curl_errno($ch)) {
        error_log('cURL error: ' . curl_error($ch));
        throw new Exception('Could not switch PHP version due to cURL error.');
    }

    // Close the cURL session
    curl_close($ch);

    // Decode the response
    $result = json_decode($response, true);

    // Check for errors in the response
    if (!isset($result['success']) || !$result['success']) {
        throw new Exception('Error switching PHP version: ' . $result['message']);
    }

    return true;
}

// Main execution logic
try {
    // Check if the desired PHP version is supported
    if (!isPhpVersionSupported($desiredPhpVersion, $supportedPhpVersions)) {
        throw new Exception('The specified PHP version is not supported.');
    }

    // Get the current PHP version
    $currentPhpVersion = phpversion();

    // Output current PHP version
    echo "Current PHP version: " . $currentPhpVersion . PHP_EOL;

    // Check if a switch is necessary
    if ($currentPhpVersion !== $desiredPhpVersion) {
        // Attempt to switch to the desired PHP version
        switchPhpVersion($desiredPhpVersion);
        echo "Successfully switched to PHP version: " . $desiredPhpVersion . PHP_EOL;
    } else {
        echo "You are already using the desired PHP version: " . $desiredPhpVersion . PHP_EOL;
    }

} catch (Exception $e) {
    // Handle any exceptions and log the error message
    error_log($e->getMessage());
    echo "An error occurred: " . $e->getMessage() . PHP_EOL;
}
?>
```
