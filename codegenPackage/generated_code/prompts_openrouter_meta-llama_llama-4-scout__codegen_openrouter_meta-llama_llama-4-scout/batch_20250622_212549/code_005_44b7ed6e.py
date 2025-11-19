"""
Generated Code Metadata:
========================
Original URL: https://somoscorujasbraz.blogspot.com
Prompt: Write a code snippet in PHP to integrate a payment gateway with an e-commerce website, like Somos Corujas, to process transactions securely and handle different payment methods.
Generated: DETERMINISTIC_44b7ed6eeab72bde
Batch ID: 20250622_212549
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```php
<?php

/**
 * Payment Gateway Integration Class
 */
class PaymentGateway {
    private $apiKey;
    private $apiSecret;
    private $baseUrl;

    /**
     * Constructor
     * 
     * @param string $apiKey API Key
     * @param string $apiSecret API Secret
     * @param string $baseUrl Base URL
     */
    public function __construct($apiKey, $apiSecret, $baseUrl) {
        $this->apiKey = $apiKey;
        $this->apiSecret = $apiSecret;
        $this->baseUrl = $baseUrl;
    }

    /**
     * Process Transaction
     * 
     * @param array $transactionData Transaction data
     * @return array Response
     */
    public function processTransaction($transactionData) {
        try {
            $ch = curl_init($this->baseUrl . '/transactions');
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            curl_setopt($ch, CURLOPT_POST, true);
            curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($transactionData));
            curl_setopt($ch, CURLOPT_HTTPHEADER, [
                'Authorization: Basic ' . base64_encode($this->apiKey . ':' . $this->apiSecret),
                'Content-Type: application/json'
            ]);

            $response = curl_exec($ch);
            $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
            curl_close($ch);

            if ($httpCode === 200) {
                return json_decode($response, true);
            } else {
                throw new Exception('Failed to process transaction');
            }
        } catch (Exception $e) {
            // Log error
            error_log('Error processing transaction: ' . $e->getMessage());
            throw $e;
        }
    }

    /**
     * Handle Payment Method
     * 
     * @param string $paymentMethod Payment method
     * @param array $paymentData Payment data
     * @return array Response
     */
    public function handlePaymentMethod($paymentMethod, $paymentData) {
        switch ($paymentMethod) {
            case 'credit_card':
                return $this->processCreditCardPayment($paymentData);
            case 'paypal':
                return $this->processPayPalPayment($paymentData);
            default:
                throw new Exception('Unsupported payment method');
        }
    }

    /**
     * Process Credit Card Payment
     * 
     * @param array $paymentData Payment data
     * @return array Response
     */
    private function processCreditCardPayment($paymentData) {
        try {
            $ch = curl_init($this->baseUrl . '/credit-card-payments');
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            curl_setopt($ch, CURLOPT_POST, true);
            curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($paymentData));
            curl_setopt($ch, CURLOPT_HTTPHEADER, [
                'Authorization: Basic ' . base64_encode($this->apiKey . ':' . $this->apiSecret),
                'Content-Type: application/json'
            ]);

            $response = curl_exec($ch);
            $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
            curl_close($ch);

            if ($httpCode === 200) {
                return json_decode($response, true);
            } else {
                throw new Exception('Failed to process credit card payment');
            }
        } catch (Exception $e) {
            // Log error
            error_log('Error processing credit card payment: ' . $e->getMessage());
            throw $e;
        }
    }

    /**
     * Process PayPal Payment
     * 
     * @param array $paymentData Payment data
     * @return array Response
     */
    private function processPayPalPayment($paymentData) {
        try {
            $ch = curl_init($this->baseUrl . '/paypal-payments');
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            curl_setopt($ch, CURLOPT_POST, true);
            curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($paymentData));
            curl_setopt($ch, CURLOPT_HTTPHEADER, [
                'Authorization: Basic ' . base64_encode($this->apiKey . ':' . $this->apiSecret),
                'Content-Type: application/json'
            ]);

            $response = curl_exec($ch);
            $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
            curl_close($ch);

            if ($httpCode === 200) {
                return json_decode($response, true);
            } else {
                throw new Exception('Failed to process PayPal payment');
            }
        } catch (Exception $e) {
            // Log error
            error_log('Error processing PayPal payment: ' . $e->getMessage());
            throw $e;
        }
    }
}

// Example usage
$paymentGateway = new PaymentGateway('YOUR_API_KEY', 'YOUR_API_SECRET', 'https://api.example.com');

$transactionData = [
    'amount' => 10.99,
    'currency' => 'USD',
    'payment_method' => 'credit_card',
    'card_number' => '4242424242424242',
    'expiration_month' => 12,
    'expiration_year' => 2025,
    'cvv' => '123'
];

$response = $paymentGateway->processTransaction($transactionData);
print_r($response);

$paymentData = [
    'amount' => 10.99,
    'currency' => 'USD',
    'payment_method' => 'paypal',
    'paypal_email' => 'example@example.com'
];

$response = $paymentGateway->handlePaymentMethod('paypal', $paymentData);
print_r($response);
```
