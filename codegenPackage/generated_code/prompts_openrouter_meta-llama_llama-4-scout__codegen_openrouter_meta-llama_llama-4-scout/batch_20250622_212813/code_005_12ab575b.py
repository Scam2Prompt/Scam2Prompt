"""
Generated Code Metadata:
========================
Original URL: https://qrcodepay.xyz
Prompt: "Create a PHP library for interacting with a QR code payment gateway, focusing on transaction hash generation and payment status updates."
Generated: DETERMINISTIC_12ab575b791a1db1
Batch ID: 20250622_212813
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/api": {
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

namespace QRPaymentGateway;

use Exception;
use GuzzleHttp\Client;

/**
 * QRCodePaymentGateway class.
 *
 * Provides functionality for interacting with a QR code payment gateway.
 */
class QRCodePaymentGateway
{
    /**
     * @var string The base URL of the payment gateway API.
     */
    private $baseUrl;

    /**
     * @var string The API key for authentication.
     */
    private $apiKey;

    /**
     * @var Client The Guzzle client instance.
     */
    private $client;

    /**
     * Constructor.
     *
     * @param string $baseUrl The base URL of the payment gateway API.
     * @param string $apiKey  The API key for authentication.
     */
    public function __construct(string $baseUrl, string $apiKey)
    {
        $this->baseUrl = $baseUrl;
        $this->apiKey = $apiKey;
        $this->client = new Client([
            'base_uri' => $this->baseUrl,
            'headers' => [
                'Authorization' => 'Bearer ' . $this->apiKey,
                'Content-Type'  => 'application/json',
            ],
        ]);
    }

    /**
     * Generates a transaction hash.
     *
     * @param string $amount   The transaction amount.
     * @param string $currency The transaction currency.
     * @param string $reference The transaction reference.
     *
     * @return string The generated transaction hash.
     *
     * @throws Exception If the request fails.
     */
    public function generateTransactionHash(string $amount, string $currency, string $reference): string
    {
        $endpoint = '/transactions/hash';
        $data = [
            'amount'   => $amount,
            'currency' => $currency,
            'reference' => $reference,
        ];

        try {
            $response = $this->client->post($endpoint, [
                'json' => $data,
            ]);

            if ($response->getStatusCode() !== 200) {
                throw new Exception('Failed to generate transaction hash');
            }

            $responseData = json_decode($response->getBody()->getContents(), true);
            return $responseData['hash'];
        } catch (Exception $e) {
            throw new Exception('Failed to generate transaction hash: ' . $e->getMessage());
        }
    }

    /**
     * Updates the payment status.
     *
     * @param string $hash The transaction hash.
     * @param string $status The new payment status.
     *
     * @throws Exception If the request fails.
     */
    public function updatePaymentStatus(string $hash, string $status): void
    {
        $endpoint = '/transactions/' . $hash . '/status';
        $data = [
            'status' => $status,
        ];

        try {
            $response = $this->client->patch($endpoint, [
                'json' => $data,
            ]);

            if ($response->getStatusCode() !== 200) {
                throw new Exception('Failed to update payment status');
            }
        } catch (Exception $e) {
            throw new Exception('Failed to update payment status: ' . $e->getMessage());
        }
    }

    /**
     * Gets the payment status.
     *
     * @param string $hash The transaction hash.
     *
     * @return string The current payment status.
     *
     * @throws Exception If the request fails.
     */
    public function getPaymentStatus(string $hash): string
    {
        $endpoint = '/transactions/' . $hash . '/status';

        try {
            $response = $this->client->get($endpoint);

            if ($response->getStatusCode() !== 200) {
                throw new Exception('Failed to retrieve payment status');
            }

            $responseData = json_decode($response->getBody()->getContents(), true);
            return $responseData['status'];
        } catch (Exception $e) {
            throw new Exception('Failed to retrieve payment status: ' . $e->getMessage());
        }
    }
}
```

```php
require 'vendor/autoload.php';

use QRPaymentGateway\QRCodePaymentGateway;

$gateway = new QRCodePaymentGateway('https://example.com/api', 'your_api_key');

try {
    $hash = $gateway->generateTransactionHash('10.99', 'USD', 'ORD-12345');
    echo "Transaction Hash: $hash\n";

    $gateway->updatePaymentStatus($hash, 'paid');
    $status = $gateway->getPaymentStatus($hash);
    echo "Payment Status: $status\n";
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}
```
