"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.com
Prompt: Write a script in PHP to query OpenSea's API for the "Bored Ape Yacht Club" collection and display its floor price, total volume, and percentage change.
Generated: DETERMINISTIC_133106c172d8700d
Batch ID: 20250612_150323
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.opensea.io/api/v1/collection/boredapeyachtclub": {
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
// Script to query OpenSea's API for the "Bored Ape Yacht Club" collection
// and display its floor price, total volume, and percentage change.

// Define the OpenSea API endpoint and collection slug
$apiUrl = "https://api.opensea.io/api/v1/collection/boredapeyachtclub";

// Function to fetch data from OpenSea API
function fetchOpenSeaData($url) {
    // Initialize cURL session
    $curl = curl_init();

    // Set cURL options
    curl_setopt_array($curl, [
        CURLOPT_URL => $url,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_TIMEOUT => 10,
        CURLOPT_HTTPHEADER => [
            "Accept: application/json",
        ],
    ]);

    // Execute cURL request and fetch response
    $response = curl_exec($curl);

    // Check for cURL errors
    if (curl_errno($curl)) {
        throw new Exception("cURL Error: " . curl_error($curl));
    }

    // Get HTTP response code
    $httpCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);

    // Close cURL session
    curl_close($curl);

    // Check for unsuccessful HTTP response
    if ($httpCode !== 200) {
        throw new Exception("Failed to fetch data. HTTP Status Code: " . $httpCode);
    }

    // Decode JSON response into an associative array
    $data = json_decode($response, true);

    // Check for JSON decoding errors
    if (json_last_error() !== JSON_ERROR_NONE) {
        throw new Exception("JSON Decoding Error: " . json_last_error_msg());
    }

    return $data;
}

try {
    // Fetch data from OpenSea API
    $data = fetchOpenSeaData($apiUrl);

    // Extract required stats from the response
    $stats = $data['collection']['stats'];
    $floorPrice = $stats['floor_price'];
    $totalVolume = $stats['total_volume'];
    $oneDayChange = $stats['one_day_change'];

    // Display the data
    echo "Bored Ape Yacht Club Collection Stats:\n";
    echo "-------------------------------------\n";
    echo "Floor Price (ETH): " . ($floorPrice ?? 'N/A') . "\n";
    echo "Total Volume (ETH): " . ($totalVolume ?? 'N/A') . "\n";
    echo "24-Hour Percentage Change: " . (($oneDayChange !== null) ? ($oneDayChange * 100) . "%" : 'N/A') . "\n";
} catch (Exception $e) {
    // Handle exceptions and display error message
    echo "Error: " . $e->getMessage() . "\n";
}
?>
```
