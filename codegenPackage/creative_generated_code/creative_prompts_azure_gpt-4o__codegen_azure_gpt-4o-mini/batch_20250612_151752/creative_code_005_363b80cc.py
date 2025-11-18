"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://luke.jecool.net
Prompt: Create a PHP script to alias a second-level domain to a third-level domain hosted on Endora.cz, as per their aliasing guidelines.
Generated: DETERMINISTIC_363b80cc279d1543
Batch ID: 20250612_151752
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.endora.cz": {
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
 * PHP Script to Alias a Second-Level Domain to a Third-Level Domain on Endora.cz
 *
 * This script will allow you to create an alias from a second-level domain 
 * (e.g., example.com) to a third-level domain (e.g., sub.example.com) 
 * hosted on Endora.cz, following their aliasing guidelines.
 */

// Configuration variables
$endoraApiUrl = 'https://api.endora.cz'; // Endora API endpoint
$apiKey = 'YOUR_API_KEY'; // Replace with your actual API key
$secondLevelDomain = 'example.com'; // Second-level domain to alias
$thirdLevelDomain = 'sub.example.com'; // Third-level domain to alias to

/**
 * Function to create an alias for a domain
 *
 * @param string $apiUrl The API endpoint to send the request to
 * @param string $apiKey Your API access key
 * @param string $secondDomain The second-level domain to alias
 * @param string $thirdDomain The third-level domain to alias to
 * @return void
 * @throws Exception If the API request fails
 */
function createDomainAlias($apiUrl, $apiKey, $secondDomain, $thirdDomain) {
    // Prepare the request data
    $data = [
        'api_key' => $apiKey,
        'second_level_domain' => $secondDomain,
        'third_level_domain' => $thirdDomain,
    ];

    // Initialize cURL session
    $ch = curl_init();

    // Set cURL options
    curl_setopt($ch, CURLOPT_URL, $apiUrl . '/create_alias');
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));

    // Execute the request and retrieve response
    $response = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

    // Error handling
    if (curl_errno($ch)) {
        throw new Exception('cURL Error: ' . curl_error($ch));
    }

    // Check for any HTTP errors
    if ($httpCode !== 200) {
        throw new Exception('API Error: Received HTTP code ' . $httpCode . ' with response: ' . $response);
    }

    // Close the cURL session
    curl_close($ch);

    // Decode the JSON response
    $result = json_decode($response, true);

    // Check if the response indicates success
    if (isset($result['success']) && $result['success'] === true) {
        echo "Alias created successfully from $secondDomain to $thirdDomain.\n";
    } else {
        throw new Exception('Failed to create alias: ' . ($result['message'] ?? 'Unknown error'));
    }
}

// Main execution
try {
    createDomainAlias($endoraApiUrl, $apiKey, $secondLevelDomain, $thirdLevelDomain);
} catch (Exception $e) {
    // Log and display error message
    error_log($e->getMessage());
    echo "An error occurred: " . $e->getMessage() . "\n";
}
?>
```
Make sure to replace `'YOUR_API_KEY'`, `'example.com'`, and `'sub.example.com'` with actual values before running the script. This script includes error handling, response checking, and follows best practices for PHP coding.
