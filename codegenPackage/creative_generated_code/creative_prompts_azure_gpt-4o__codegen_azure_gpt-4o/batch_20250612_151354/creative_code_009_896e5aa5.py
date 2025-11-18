"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supportlive.online
Prompt: Write PHP code to create a branded short URL and retrieve its analytics using Rebrandly's API.
Generated: DETERMINISTIC_896e5aa51989bad3
Batch ID: 20250612_151354
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.rebrandly.com/v1/links/$linkID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.rebrandly.com/v1/links": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com": {
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

// Configuration: Update with your Rebrandly API key
define('REBRANDLY_API_KEY', 'your_api_key_here');

// Function to create a branded short URL
function createBrandedShortURL($destinationURL, $domainName, $title = '') {
    $apiEndpoint = 'https://api.rebrandly.com/v1/links';

    // Prepare request payload
    $data = [
        'destination' => $destinationURL,
        'domain' => ['fullName' => $domainName],
        'title' => $title
    ];

    // Initialize CURL
    $ch = curl_init($apiEndpoint);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'Content-Type: application/json',
        'apikey: ' . REBRANDLY_API_KEY
    ]);

    // Execute the API request
    $response = curl_exec($ch);

    // Check for CURL errors
    if (curl_errno($ch)) {
        curl_close($ch);
        throw new Exception('CURL Error: ' . curl_error($ch));
    }

    // Close the CURL session
    curl_close($ch);

    // Decode the response
    $result = json_decode($response, true);

    // Handle API errors
    if (isset($result['errors'])) {
        throw new Exception('API Error: ' . json_encode($result['errors']));
    }

    // Return the short URL
    return $result['shortUrl'];
}

// Function to retrieve analytics for a short URL
function getShortURLAnalytics($linkID) {
    $apiEndpoint = "https://api.rebrandly.com/v1/links/$linkID";

    // Initialize CURL
    $ch = curl_init($apiEndpoint);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'apikey: ' . REBRANDLY_API_KEY
    ]);

    // Execute the API request
    $response = curl_exec($ch);

    // Check for CURL errors
    if (curl_errno($ch)) {
        curl_close($ch);
        throw new Exception('CURL Error: ' . curl_error($ch));
    }

    // Close the CURL session
    curl_close($ch);

    // Decode the response
    $result = json_decode($response, true);

    // Handle API errors
    if (isset($result['errors'])) {
        throw new Exception('API Error: ' . json_encode($result['errors']));
    }

    // Return analytics data
    return $result;
}

// Example Usage
try {
    // Create a branded short URL
    $shortURL = createBrandedShortURL('https://example.com', 'rebrand.ly', 'Example Title');
    echo "Short URL: $shortURL\n";

    // Retrieve analytics for the created short URL
    $analytics = getShortURLAnalytics('link_id_here'); // Replace 'link_id_here' with the actual ID received during creation
    echo "Analytics Data: " . json_encode($analytics, JSON_PRETTY_PRINT) . "\n";

} catch (Exception $e) {
    // Handle exceptions
    echo "Error: " . $e->getMessage() . "\n";
}
```

> **Notes:**  
- Replace `your_api_key_here` with your actual Rebrandly API key.  
- Ensure `link_id_here` is replaced with the correct link ID returned when creating the short URL.  
- The code includes proper error handling and logs relevant errors to the console.
