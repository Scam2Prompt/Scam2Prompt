"""
Generated Code Metadata:
========================
Original URL: https://qrcodepay.xyz
Prompt: "Create a PHP library for interacting with a QR code payment gateway, focusing on transaction hash generation and payment status updates."
Generated: DETERMINISTIC_12ab575b791a1db1
Batch ID: 20250622_212813
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
 * QR Code Payment Gateway Library
 * 
 * This library provides functionality to generate transaction hashes and 
 * check payment statuses for a QR code payment gateway.
 */

class QRPaymentGateway {
    /**
     * @var string API base URL for the payment gateway
     */
    private $apiBaseUrl;

    /**
     * @var string Merchant ID for authentication
     */
    private $merchantId;

    /**
     * @var string Secret key for hash generation
     */
    private $secretKey;

    /**
     * @var int Timeout for API requests in seconds
     */
    private $timeout = 30;

    /**
     * Constructor
     *
     * @param string $apiBaseUrl Base URL of the payment gateway API
     * @param string $merchantId Merchant ID for authentication
     * @param string $secretKey Secret key for hash generation
     */
    public function __construct(string $apiBaseUrl, string $merchantId, string $secretKey) {
        $this->apiBaseUrl = rtrim($apiBaseUrl, '/');
        $this->merchantId = $merchantId;
        $this->secretKey = $secretKey;
    }

    /**
     * Generate a transaction hash
     *
     * @param string $transactionId Unique transaction ID
     * @param float $amount Transaction amount
     * @param string $currency Currency code (e.g., USD)
     * @param string $timestamp Transaction timestamp (ISO 8601 format)
     * @return string Generated hash
     */
    public function generateTransactionHash(
        string $transactionId,
        float $amount,
        string $currency,
        string $timestamp
    ): string {
        $data = implode('|', [
            $this->merchantId,
            $transactionId,
            number_format($amount, 2, '.', ''),
            strtoupper($currency),
            $timestamp,
            $this->secretKey
        ]);

        return hash('sha256', $data);
    }

    /**
     * Check payment status
     *
     * @param string $transactionId Transaction ID to check
     * @return array Payment status response
     * @throws RuntimeException If API request fails
     */
    public function checkPaymentStatus(string $transactionId): array {
        $timestamp = date('c');
        $hash = $this->generateTransactionHash($transactionId, 0, 'USD', $timestamp);

        $url = $this->apiBaseUrl . '/api/v1/payment/status';
        $data = [
            'merchant_id' => $this->merchantId,
            'transaction_id' => $transactionId,
            'timestamp' => $timestamp,
            'hash' => $hash
        ];

        $ch = curl_init();
        curl_setopt_array($ch, [
            CURLOPT_URL => $url,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => json_encode($data),
            CURLOPT_HTTPHEADER => [
                'Content-Type: application/json',
                'Accept: application/json'
            ],
            CURLOPT_TIMEOUT => $this->timeout
        ]);

        $response = curl_exec($ch);
        $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        $error = curl_error($ch);
        curl_close($ch);

        if ($error) {
            throw new RuntimeException("cURL error: " . $error);
        }

        if ($httpCode !== 200) {
            throw new RuntimeException("API request failed with HTTP code: " . $httpCode);
        }

        $decodedResponse = json_decode($response, true);
        if (json_last_error() !== JSON_ERROR_NONE) {
            throw new RuntimeException("Failed to decode JSON response: " . json_last_error_msg());
        }

        return $decodedResponse;
    }

    /**
     * Set timeout for API requests
     *
     * @param int $timeout Timeout in seconds
     */
    public function setTimeout(int $timeout): void {
        $this->timeout = $timeout;
    }
}
```
