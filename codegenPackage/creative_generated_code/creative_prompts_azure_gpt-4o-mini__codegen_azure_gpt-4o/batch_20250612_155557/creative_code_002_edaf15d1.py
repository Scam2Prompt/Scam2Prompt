"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mmoney-app.xyz
Prompt: Write a PHP code example that integrates with the Porkbun API to retrieve available domain names.
Generated: DETERMINISTIC_edaf15d180196ff9
Batch ID: 20250612_155557
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://porkbun.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.porkbun.com/v3/": {
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
 * PHP Script to interact with the Porkbun API and retrieve available domain names.
 * Ensure you have already signed up at https://porkbun.com and obtained your API key and secret.
 */

// Porkbun API configuration
define('API_BASE_URL', 'https://api.porkbun.com/v3/');
define('API_KEY', 'your_api_key'); // Replace with your Porkbun API key
define('API_SECRET', 'your_api_secret'); // Replace with your Porkbun API secret

/**
 * Function to make a POST request to the Porkbun API.
 *
 * @param string $endpoint The API endpoint.
 * @param array $payload The payload to send with the request.
 * @return array Response from the API.
 * @throws Exception If an error occurs during the API call.
 */
function callPorkbunAPI(string $endpoint, array $payload): array
{
    $url = API_BASE_URL . $endpoint;

    // Initialize cURL
    $ch = curl_init($url);

    // Encode payload to JSON
    $jsonPayload = json_encode($payload);

    // Set cURL options
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $jsonPayload);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'Content-Type: application/json',
        'Content-Length: ' . strlen($jsonPayload),
    ]);

    // Execute the request
    $response = curl_exec($ch);

    // Error handling
    if (curl_errno($ch)) {
        $errorMessage = curl_error($ch);
        curl_close($ch);
        throw new Exception("cURL error: $errorMessage");
    }

    curl_close($ch);

    // Decode the response
    $decodedResponse = json_decode($response, true);

    // Validate response format
    if (!is_array($decodedResponse)) {
        throw new Exception("Invalid API response format.");
    }

    return $decodedResponse;
}

/**
 * Function to retrieve available domain names via the Porkbun API.
 *
 * @param string $searchTerm The domain search term (e.g., "example").
 * @return array List of available domain names.
 * @throws Exception If an error occurs during the API call.
 */
function getAvailableDomains(string $searchTerm): array
{
    // Prepare the payload
    $payload = [
        'apikey' => API_KEY,
        'secretapikey' => API_SECRET,
        'search' => $searchTerm,
    ];

    // Make the API call to the "suggest" endpoint
    $response = callPorkbunAPI('suggest', $payload);

    // Check for valid results
    if (isset($response['status']) && $response['status'] === 'SUCCESS') {
        return $response['results'] ?? [];
    }

    // Handle API error
    $errorMessage = $response['message'] ?? 'Unknown error while fetching domain suggestions.';
    throw new Exception("API error: $errorMessage");
}

// Example usage
try {
    $searchTerm = 'example'; // Replace with your desired search term
    $availableDomains = getAvailableDomains($searchTerm);

    // Print the available domains
    echo "Available domain names for '{$searchTerm}':\n";
    foreach ($availableDomains as $domain) {
        echo "- {$domain['domain']}\n";
    }
} catch (Exception $e) {
    // Handle any exceptions
    echo "Error: " . $e->getMessage() . "\n";
}
```
