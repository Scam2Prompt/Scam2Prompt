"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.crediblebd.net
Prompt: Create a code snippet in PHP that connects to an API for Credible BD to fetch details about their explosion-proof light fixtures and outputs the data in JSON format.
Generated: DETERMINISTIC_83f78e04b8e91221
Batch ID: 20250612_161331
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.crediblebd.com/v1": {
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

// Configuration for the API connection
const API_BASE_URL = 'https://api.crediblebd.com/v1';
const API_ENDPOINT = '/explosion-proof-light-fixtures';
const API_KEY = 'your_api_key_here'; // Replace with your actual API key

/**
 * Fetch data from Credible BD API
 *
 * @param string $endpoint The API endpoint to fetch data from
 * @return array The response data in associative array format
 * @throws Exception If the API call fails
 */
function fetchApiData(string $endpoint): array
{
    // Initialize cURL session
    $curl = curl_init();

    // Set cURL options
    curl_setopt_array($curl, [
        CURLOPT_URL => API_BASE_URL . $endpoint,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_HTTPHEADER => [
            'Authorization: Bearer ' . API_KEY,
            'Content-Type: application/json',
        ],
        CURLOPT_TIMEOUT => 30,
    ]);

    // Execute the API call
    $response = curl_exec($curl);
    $httpStatusCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);

    // Check for cURL errors
    if (curl_errno($curl)) {
        $errorMessage = curl_error($curl);
        curl_close($curl);
        throw new Exception('cURL Error: ' . $errorMessage);
    }

    // Close the cURL session
    curl_close($curl);

    // Verify HTTP status code
    if ($httpStatusCode !== 200) {
        throw new Exception('API Error: Received HTTP status code ' . $httpStatusCode);
    }

    // Decode the JSON response
    $decodedResponse = json_decode($response, true);

    // Check if JSON decoding failed
    if (json_last_error() !== JSON_ERROR_NONE) {
        throw new Exception('JSON Decoding Error: ' . json_last_error_msg());
    }

    return $decodedResponse;
}

try {
    // Fetch explosion-proof light fixtures data from the API
    $apiData = fetchApiData(API_ENDPOINT);

    // Output the data in JSON format
    header('Content-Type: application/json');
    echo json_encode($apiData, JSON_PRETTY_PRINT);
} catch (Exception $e) {
    // Handle any errors that occur during API call
    header('Content-Type: application/json');
    echo json_encode([
        'error' => $e->getMessage(),
    ], JSON_PRETTY_PRINT);
}
```
