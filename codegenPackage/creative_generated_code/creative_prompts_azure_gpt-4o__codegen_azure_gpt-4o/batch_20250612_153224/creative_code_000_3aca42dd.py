"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webservicesindia.info
Prompt: Write a PHP script for integrating a custom e-commerce platform with Magento, referencing the development services offered by WebServicesIndia.
Generated: DETERMINISTIC_3aca42dd584e42fb
Batch ID: 20250612_153224
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://your-magento-site.com/rest/V1/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://your-custom-platform.com/api/": {
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
 * Magento Integration Script
 * This script integrates a custom e-commerce platform with Magento.
 * Developed in reference to the development services offered by WebServicesIndia.
 * 
 * @author WebServicesIndia
 * @date YYYY-MM-DD
 */

// Configuration for Magento API
define('MAGENTO_API_URL', 'https://your-magento-site.com/rest/V1/');
define('MAGENTO_API_TOKEN', 'your-magento-api-token'); // Replace with your Magento API token

// Configuration for custom e-commerce platform API
define('CUSTOM_PLATFORM_API_URL', 'https://your-custom-platform.com/api/');
define('CUSTOM_PLATFORM_API_KEY', 'your-custom-platform-api-key'); // Replace with your custom platform API key

/**
 * Function to send HTTP requests
 * 
 * @param string $url The URL to send the request to
 * @param string $method The HTTP method (GET, POST, PUT, DELETE)
 * @param array|null $data The data to send in the request body
 * @param array $headers Additional headers for the request
 * 
 * @return array|false The response data (decoded JSON), or false if the request fails
 */
function sendHttpRequest($url, $method, $data = null, $headers = [])
{
    $curl = curl_init();
    
    curl_setopt($curl, CURLOPT_URL, $url);
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($curl, CURLOPT_CUSTOMREQUEST, $method);
    
    if ($data) {
        curl_setopt($curl, CURLOPT_POSTFIELDS, json_encode($data));
        $headers[] = 'Content-Type: application/json';
    }
    
    if (!empty($headers)) {
        curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);
    }
    
    $response = curl_exec($curl);
    $httpCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
    
    curl_close($curl);
    
    // Error handling
    if ($httpCode >= 200 && $httpCode < 300) {
        return json_decode($response, true);
    } else {
        error_log("HTTP Request failed with status code: $httpCode");
        return false;
    }
}

/**
 * Function to fetch products from the custom e-commerce platform
 * 
 * @return array|false The list of products, or false if the request fails
 */
function fetchCustomPlatformProducts()
{
    $url = CUSTOM_PLATFORM_API_URL . 'products';
    $headers = ['Authorization: Bearer ' . CUSTOM_PLATFORM_API_KEY];
    return sendHttpRequest($url, 'GET', null, $headers);
}

/**
 * Function to create a product in Magento
 * 
 * @param array $productData The product data to create
 * 
 * @return array|false The Magento API response, or false if the request fails
 */
function createMagentoProduct($productData)
{
    $url = MAGENTO_API_URL . 'products';
    $headers = ['Authorization: Bearer ' . MAGENTO_API_TOKEN];
    return sendHttpRequest($url, 'POST', $productData, $headers);
}

/**
 * Main script logic
 * Fetch products from the custom e-commerce platform and create them in Magento.
 */
function integrateProducts()
{
    // Fetch products from custom platform
    $products = fetchCustomPlatformProducts();
    
    if ($products === false) {
        echo "Failed to fetch products from custom platform.\n";
        return;
    }
    
    foreach ($products as $product) {
        // Prepare product data for Magento
        $magentoProductData = [
            'sku' => $product['sku'],
            'name' => $product['name'],
            'price' => $product['price'],
            'status' => 1, // Enabled
            'visibility' => 4, // Catalog and Search
            'type_id' => 'simple', // Assuming 'simple' products
            'attribute_set_id' => 4, // Default attribute set ID
            'extension_attributes' => [
                'stock_item' => [
                    'qty' => $product['quantity'],
                    'is_in_stock' => $product['quantity'] > 0
                ]
            ]
        ];
        
        // Create product in Magento
        $result = createMagentoProduct($magentoProductData);
        
        if ($result === false) {
            echo "Failed to create product in Magento: " . $product['name'] . "\n";
        } else {
            echo "Successfully created product in Magento: " . $product['name'] . "\n";
        }
    }
}

// Run the integration
integrateProducts();

?>
```
