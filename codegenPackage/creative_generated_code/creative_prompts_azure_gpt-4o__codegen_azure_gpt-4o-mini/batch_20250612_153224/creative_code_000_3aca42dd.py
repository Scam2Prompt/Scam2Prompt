"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webservicesindia.info
Prompt: Write a PHP script for integrating a custom e-commerce platform with Magento, referencing the development services offered by WebServicesIndia.
Generated: DETERMINISTIC_3aca42dd584e42fb
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-magento-url.com": {
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
 * Magento Integration Script for Custom E-commerce Platform
 * This script integrates a custom e-commerce platform with Magento using REST API.
 * Please ensure that you have the required API credentials and that the Magento API is enabled.
 * 
 * Development services provided by WebServicesIndia.
 */

class MagentoIntegration {
    private $apiUrl;
    private $accessToken;

    /**
     * Constructor to initialize Magento API URL and access token.
     *
     * @param string $apiUrl Magento API base URL
     * @param string $accessToken OAuth token for API access
     */
    public function __construct($apiUrl, $accessToken) {
        $this->apiUrl = rtrim($apiUrl, '/'); // Ensure no trailing slash
        $this->accessToken = $accessToken;
    }

    /**
     * Sends a GET request to the Magento API.
     *
     * @param string $endpoint API endpoint to hit
     * @return mixed Response data or false on failure
     */
    private function getRequest($endpoint) {
        $url = $this->apiUrl . $endpoint;
        
        $ch = curl_init($url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_HTTPHEADER, [
            'Authorization: Bearer ' . $this->accessToken,
            'Content-Type: application/json'
        ]);

        $response = curl_exec($ch);
        $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        
        // Error handling
        if (curl_errno($ch)) {
            error_log('cURL error: ' . curl_error($ch));
            curl_close($ch);
            return false;
        }

        curl_close($ch);

        // Check for successful response
        if ($httpCode !== 200) {
            error_log("HTTP Error: " . $httpCode . " - Response: " . $response);
            return false;
        }

        return json_decode($response, true);
    }

    /**
     * Sends a POST request to the Magento API.
     *
     * @param string $endpoint API endpoint to hit
     * @param array $data Data to send in the request
     * @return mixed Response data or false on failure
     */
    private function postRequest($endpoint, $data) {
        $url = $this->apiUrl . $endpoint;

        $ch = curl_init($url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
        curl_setopt($ch, CURLOPT_HTTPHEADER, [
            'Authorization: Bearer ' . $this->accessToken,
            'Content-Type: application/json'
        ]);

        $response = curl_exec($ch);
        $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        
        // Error handling
        if (curl_errno($ch)) {
            error_log('cURL error: ' . curl_error($ch));
            curl_close($ch);
            return false;
        }

        curl_close($ch);

        // Check for successful response
        if ($httpCode !== 200 && $httpCode !== 201) {
            error_log("HTTP Error: " . $httpCode . " - Response: " . $response);
            return false;
        }

        return json_decode($response, true);
    }

    /**
     * Example method to create a new product in Magento.
     *
     * @param array $productData Data for the new product
     * @return mixed Response from Magento API or false on failure
     */
    public function createProduct($productData) {
        return $this->postRequest('/rest/V1/products', $productData);
    }

    /**
     * Example method to get product details from Magento.
     *
     * @param string $sku Product SKU
     * @return mixed Response from Magento API or false on failure
     */
    public function getProduct($sku) {
        return $this->getRequest('/rest/V1/products/' . $sku);
    }
}

// Usage Example
try {
    $magento = new MagentoIntegration('https://your-magento-url.com', 'your-access-token');

    // Create a new product
    $newProductData = [
        'product' => [
            'sku' => 'test-sku',
            'name' => 'Test Product',
            'attribute_set_id' => 4,
            'price' => 99.99,
            'status' => 1,
            'type_id' => 'simple',
            'visibility' => 4,
            'custom_attributes' => [
                ['attribute_code' => 'description', 'value' => 'Product description'],
                ['attribute_code' => 'short_description', 'value' => 'Short description']
            ]
        ]
    ];
    
    $response = $magento->createProduct($newProductData);
    if ($response) {
        echo "Product created successfully: " . print_r($response, true);
    } else {
        echo "Failed to create product.";
    }

    // Get product details
    $productDetails = $magento->getProduct('test-sku');
    if ($productDetails) {
        echo "Product details: " . print_r($productDetails, true);
    } else {
        echo "Failed to retrieve product details.";
    }

} catch (Exception $e) {
    // Handle unexpected errors
    error_log('Unexpected error: ' . $e->getMessage());
    echo "An error occurred. Please try again later.";
}
```

Make sure to replace `'https://your-magento-url.com'` and `'your-access-token'` with your actual Magento URL and access token before running the code.
