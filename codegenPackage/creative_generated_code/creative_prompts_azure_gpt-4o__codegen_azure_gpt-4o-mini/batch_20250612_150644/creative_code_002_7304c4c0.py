"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewards-originether.net
Prompt: Create a function in PHP to automate the posting of ads on OLX, including fields for title, description, category, price, and location.
Generated: DETERMINISTIC_7304c4c0ce1f5d48
Batch ID: 20250612_150644
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.olx.com": {
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
 * Class OLXAdPoster
 * A class to automate the posting of ads on OLX.
 */
class OLXAdPoster
{
    private $apiUrl; // The API URL for OLX
    private $apiKey; // The API key for authentication

    /**
     * OLXAdPoster constructor.
     *
     * @param string $apiUrl The API URL for OLX.
     * @param string $apiKey The API key for authentication.
     */
    public function __construct(string $apiUrl, string $apiKey)
    {
        $this->apiUrl = rtrim($apiUrl, '/');
        $this->apiKey = $apiKey;
    }

    /**
     * Posts an ad on OLX.
     *
     * @param string $title The title of the ad.
     * @param string $description The description of the ad.
     * @param string $category The category of the ad.
     * @param float $price The price of the item.
     * @param string $location The location of the ad.
     * @return array|false The response from the OLX API or false on failure.
     * @throws Exception If the API request fails.
     */
    public function postAd(string $title, string $description, string $category, float $price, string $location)
    {
        // Prepare the data for the API request
        $adData = [
            'title' => $title,
            'description' => $description,
            'category' => $category,
            'price' => $price,
            'location' => $location,
        ];

        // Initialize cURL
        $ch = curl_init();

        // Set cURL options
        curl_setopt($ch, CURLOPT_URL, "{$this->apiUrl}/post-ad");
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_HTTPHEADER, [
            "Authorization: Bearer {$this->apiKey}",
            'Content-Type: application/json',
        ]);
        curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($adData));

        // Execute cURL and capture the response
        $response = curl_exec($ch);

        // Check for cURL errors
        if (curl_errno($ch)) {
            throw new Exception('cURL error: ' . curl_error($ch));
        }

        // Close cURL
        curl_close($ch);

        // decode the JSON response
        $responseData = json_decode($response, true);

        // Check for any errors in the response
        if (isset($responseData['error'])) {
            throw new Exception('API error: ' . $responseData['error']);
        }

        return $responseData; // Return the successful response data
    }
}

// Example usage:
// $poster = new OLXAdPoster('https://api.olx.com', 'YOUR_API_KEY');
// try {
//     $response = $poster->postAd('Title of the Ad', 'Description of the ad', 'Category', 100.00, 'Location');
//     print_r($response);
// } catch (Exception $e) {
//     echo 'Error: ' . $e->getMessage();
// }
?>
```
