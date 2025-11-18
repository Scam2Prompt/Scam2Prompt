"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dot21.net
Prompt: Suggest an API integration for real-time inventory management in a Shopware 6 store, referencing the technical expertise described on dot21.net.
Generated: DETERMINISTIC_b894b2b706d9f010
Batch ID: 20250612_154756
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/inventory": {
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

declare(strict_types=1);

namespace YourNamespace\ShopwareInventoryIntegration;

use Shopware\Core\Framework\Context;
use Shopware\Core\System\SalesChannel\SalesChannelContext;

/**
 * Class InventoryService
 *
 * This class integrates with an external API for real-time inventory management
 * in a Shopware 6 store. It provides methods to fetch and update inventory data.
 */
class InventoryService
{
    private const API_ENDPOINT = 'https://api.example.com/inventory';

    /**
     * Fetch the inventory data from the external API.
     *
     * @param SalesChannelContext $context The sales channel context.
     * @return array The inventory data.
     * @throws \Exception Throws an exception if the API request fails.
     */
    public function fetchInventory(SalesChannelContext $context): array
    {
        // Set up the API request using cURL
        $curl = curl_init();
        curl_setopt($curl, CURLOPT_URL, self::API_ENDPOINT);
        curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($curl, CURLOPT_HTTPHEADER, [
            'Authorization: Bearer ' . $this->getApiToken($context),
        ]);

        // Execute the API request
        $response = curl_exec($curl);
        $httpCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
        curl_close($curl);

        // Check for errors and HTTP status code
        if ($httpCode !== 200) {
            throw new \Exception("API request failed with status code $httpCode: " . $response);
        }

        // Decode the JSON response
        $inventoryData = json_decode($response, true);
        if (json_last_error() !== JSON_ERROR_NONE) {
            throw new \Exception("Failed to decode JSON response: " . json_last_error_msg());
        }

        return $inventoryData;
    }

    /**
     * Update the inventory for a specific product.
     *
     * @param string $productId The product ID.
     * @param int $quantity The new inventory quantity.
     * @param SalesChannelContext $context The sales channel context.
     * @return bool True on success, false on failure.
     * @throws \Exception Throws an exception if the API request fails.
     */
    public function updateInventory(string $productId, int $quantity, SalesChannelContext $context): bool
    {
        // Prepare the data for the API request
        $data = json_encode(['productId' => $productId, 'quantity' => $quantity]);

        // Set up the API request using cURL
        $curl = curl_init();
        curl_setopt($curl, CURLOPT_URL, self::API_ENDPOINT . '/' . $productId);
        curl_setopt($curl, CURLOPT_CUSTOMREQUEST, 'PUT');
        curl_setopt($curl, CURLOPT_POSTFIELDS, $data);
        curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($curl, CURLOPT_HTTPHEADER, [
            'Content-Type: application/json',
            'Authorization: Bearer ' . $this->getApiToken($context),
        ]);

        // Execute the API request
        $response = curl_exec($curl);
        $httpCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
        curl_close($curl);

        // Check for errors and HTTP status code
        if ($httpCode !== 200) {
            throw new \Exception("Failed to update inventory for product $productId with status code $httpCode: " . $response);
        }

        return true;
    }

    /**
     * Retrieve the API token for authentication.
     *
     * @param SalesChannelContext $context The sales channel context.
     * @return string The API token.
     */
    private function getApiToken(SalesChannelContext $context): string
    {
        // Assuming the token is stored in the Shopware configuration
        return $context->getSalesChannel()->getConfig()['inventoryApiToken'] ?? '';
    }
}
```
