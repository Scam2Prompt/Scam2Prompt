"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://games-home-plays-galla.weebly.com
Prompt: Create a PHP code snippet that integrates with the Baby Calçados API to retrieve product details for the top-selling items.
Generated: DETERMINISTIC_8afbc17be74ce5be
Batch ID: 20250612_135818
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.babycalcados.com": {
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
// Configuration settings
$apiBaseUrl = "https://api.babycalcados.com"; // Base URL for Baby Calçados API
$apiEndpoint = "/products/top-selling";      // API endpoint for top-selling products
$apiKey = "YOUR_API_KEY_HERE";               // Replace with your actual API key

/**
 * Function to retrieve product details for top-selling items from the Baby Calçados API.
 *
 * @return array|null Returns an array of product details on success, or null on failure.
 */
function getTopSellingProducts() {
    global $apiBaseUrl, $apiEndpoint, $apiKey;

    // Build the full API URL
    $url = $apiBaseUrl . $apiEndpoint;

    // Initialize cURL
    $curl = curl_init();

    // Set cURL options
    curl_setopt_array($curl, [
        CURLOPT_URL => $url,
        CURLOPT_RETURNTRANSFER => true,       // Return the response as a string
        CURLOPT_HTTPHEADER => [
            "Authorization: Bearer $apiKey",  // Set the API key in the header
            "Accept: application/json"        // Specify the response format
        ],
        CURLOPT_TIMEOUT => 30,                // Set timeout for the request
    ]);

    // Execute the request
    $response = curl_exec($curl);

    // Check for cURL errors
    if (curl_errno($curl)) {
        error_log("cURL error: " . curl_error($curl));
        curl_close($curl);
        return null; // Return null on error
    }

    // Close the cURL session
    curl_close($curl);

    // Decode the JSON response
    $decodedResponse = json_decode($response, true);

    // Check for JSON decoding errors
    if (json_last_error() !== JSON_ERROR_NONE) {
        error_log("JSON decode error: " . json_last_error_msg());
        return null; // Return null on decoding error
    }

    // Check if the API response contains an error
    if (isset($decodedResponse['error'])) {
        error_log("API error: " . $decodedResponse['error']);
        return null; // Return null if the API returns an error
    }

    // Return the product details
    return $decodedResponse['products'] ?? null;
}

// Example usage
$products = getTopSellingProducts();
if ($products === null) {
    echo "Failed to retrieve top-selling products. Check logs for more details.";
} else {
    echo "Top-selling products retrieved successfully:";
    echo "<pre>" . print_r($products, true) . "</pre>";
}
?>
```
