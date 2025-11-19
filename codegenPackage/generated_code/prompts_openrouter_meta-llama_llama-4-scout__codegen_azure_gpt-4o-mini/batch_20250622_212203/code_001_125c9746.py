"""
Generated Code Metadata:
========================
Original URL: https://magentobuldozer.com
Prompt: "How to integrate a third-party API for payment gateway in Magento?"
Generated: DETERMINISTIC_125c9746a958658f
Batch ID: 20250622_212203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Magento 2 Payment Gateway Integration
 *
 * This module integrates a third-party payment gateway into Magento 2.
 * It includes necessary configurations, API calls, and error handling.
 */

namespace Vendor\PaymentGateway\Model;

use Magento\Payment\Model\Method\AbstractMethod;
use Magento\Framework\Exception\LocalizedException;
use Magento\Framework\HTTP\Client\Curl;
use Magento\Framework\App\Config\ScopeConfigInterface;

class PaymentGateway extends AbstractMethod
{
    const CODE = 'payment_gateway';

    protected $_code = self::CODE;

    /**
     * @var Curl
     */
    protected $curl;

    /**
     * @var ScopeConfigInterface
     */
    protected $scopeConfig;

    /**
     * Constructor
     *
     * @param Curl $curl
     * @param ScopeConfigInterface $scopeConfig
     */
    public function __construct(
        Curl $curl,
        ScopeConfigInterface $scopeConfig
    ) {
        $this->curl = $curl;
        $this->scopeConfig = $scopeConfig;
    }

    /**
     * Process payment
     *
     * @param array $paymentData
     * @return array
     * @throws LocalizedException
     */
    public function processPayment(array $paymentData)
    {
        // Prepare API request
        $apiUrl = $this->scopeConfig->getValue('payment/payment_gateway/api_url');
        $apiKey = $this->scopeConfig->getValue('payment/payment_gateway/api_key');

        // Validate required fields
        if (empty($apiUrl) || empty($apiKey)) {
            throw new LocalizedException(__('API URL or API Key is not configured.'));
        }

        // Set up CURL request
        $this->curl->setOption(CURLOPT_URL, $apiUrl);
        $this->curl->setOption(CURLOPT_RETURNTRANSFER, true);
        $this->curl->setOption(CURLOPT_POST, true);
        $this->curl->setOption(CURLOPT_POSTFIELDS, json_encode($paymentData));
        $this->curl->setOption(CURLOPT_HTTPHEADER, [
            'Content-Type: application/json',
            'Authorization: Bearer ' . $apiKey
        ]);

        // Execute CURL request and handle response
        try {
            $response = $this->curl->get();
            $responseData = json_decode($response, true);

            if (isset($responseData['error'])) {
                throw new LocalizedException(__('Payment processing error: %1', $responseData['error']));
            }

            return $responseData; // Return successful response data
        } catch (\Exception $e) {
            throw new LocalizedException(__('An error occurred while processing the payment: %1', $e->getMessage()));
        }
    }
}
```

This code snippet provides a basic structure for integrating a third-party payment gateway in Magento 2, including error handling and configuration management. Make sure to replace `Vendor\PaymentGateway` with your actual vendor and module name.
