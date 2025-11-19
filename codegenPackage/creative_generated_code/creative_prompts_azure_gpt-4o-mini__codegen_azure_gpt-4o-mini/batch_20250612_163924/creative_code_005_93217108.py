"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://benbutterfield.co.uk
Prompt: How can I integrate third-party services into my Magento 2 application effectively?
Generated: DETERMINISTIC_932171080adacce5
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

namespace Vendor\Module\Observer;

use Magento\Framework\Event\Observer;
use Magento\Framework\Event\ObserverInterface;
use Psr\Log\LoggerInterface;
use Magento\Framework\App\Config\ScopeConfigInterface;

class IntegrateThirdPartyService implements ObserverInterface
{
    /**
     * @var LoggerInterface
     */
    protected $logger;

    /**
     * @var ScopeConfigInterface
     */
    protected $scopeConfig;

    /**
     * Constructor
     *
     * @param LoggerInterface $logger
     * @param ScopeConfigInterface $scopeConfig
     */
    public function __construct(
        LoggerInterface $logger,
        ScopeConfigInterface $scopeConfig
    ) {
        $this->logger = $logger;
        $this->scopeConfig = $scopeConfig;
    }

    /**
     * Execute method to integrate third-party service
     *
     * @param Observer $observer
     * @return void
     */
    public function execute(Observer $observer)
    {
        try {
            // Retrieve configuration settings
            $apiUrl = $this->scopeConfig->getValue('thirdparty/settings/api_url', \Magento\Store\Model\ScopeInterface::SCOPE_STORE);
            $apiKey = $this->scopeConfig->getValue('thirdparty/settings/api_key', \Magento\Store\Model\ScopeInterface::SCOPE_STORE);
            
            if (empty($apiUrl) || empty($apiKey)) {
                throw new \InvalidArgumentException('API URL or API Key is not configured properly.');
            }

            // Prepare data to send to third-party service
            $data = [
                'order_id' => $observer->getEvent()->getOrder()->getId(),
                // Add additional data as needed
            ];

            // Make an API call to the third-party service
            $response = $this->makeApiCall($apiUrl, $apiKey, $data);

            // Handle the response
            if ($response['status'] !== 'success') {
                throw new \RuntimeException('Failed to integrate with third-party service: ' . $response['message']);
            }

            // Log success message
            $this->logger->info('Successfully integrated with third-party service for order ID: ' . $data['order_id']);

        } catch (\Exception $e) {
            // Log error message
            $this->logger->error('Error in third-party service integration: ' . $e->getMessage());
        }
    }

    /**
     * Makes a call to the third-party API
     *
     * @param string $url
     * @param string $apiKey
     * @param array $data
     * @return array
     */
    protected function makeApiCall($url, $apiKey, $data)
    {
        // Initialize cURL session
        $ch = curl_init($url);
        
        // Set cURL options
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_HTTPHEADER, [
            'Content-Type: application/json',
            'Authorization: Bearer ' . $apiKey,
        ]);
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));

        // Execute cURL request
        $response = curl_exec($ch);
        $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

        // Handle cURL error
        if (curl_errno($ch)) {
            throw new \RuntimeException('cURL Error: ' . curl_error($ch));
        }

        // Close cURL session
        curl_close($ch);

        // Return response in array format
        return [
            'status' => $httpCode === 200 ? 'success' : 'error',
            'message' => json_decode($response, true) ?: $response,
        ];
    }
}
```

This code snippet provides a clean, well-commented implementation of integrating a third-party service into a Magento 2 application using an observer. It includes error handling, logging, and configuration retrieval for the API settings.
