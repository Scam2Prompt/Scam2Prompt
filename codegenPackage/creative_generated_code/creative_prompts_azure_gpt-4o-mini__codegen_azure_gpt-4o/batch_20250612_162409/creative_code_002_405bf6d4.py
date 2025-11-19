"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdropbtc.com
Prompt: Create a PHP script that integrates with Binance API to track deposits and withdrawals for Airdrop BTC users.
Generated: DETERMINISTIC_405bf6d41db86e7d
Batch ID: 20250612_162409
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.binance.com": {
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
 * PHP Script to track deposits and withdrawals for Airdrop BTC users using Binance API.
 * Ensure you have registered for Binance API access and have your API Key and Secret.
 */

// Configuration: Binance API credentials
define('BINANCE_API_KEY', 'your_api_key_here'); // Replace with your Binance API key
define('BINANCE_API_SECRET', 'your_api_secret_here'); // Replace with your Binance API secret

// Binance API base URL
define('BINANCE_API_BASE_URL', 'https://api.binance.com');

// Function to make an HTTP request
function makeBinanceApiRequest($endpoint, $params = [])
{
    $url = BINANCE_API_BASE_URL . $endpoint;

    // Generate query string
    $queryString = http_build_query($params);
    $timestamp = time() * 1000; // Binance API uses milliseconds
    $signaturePayload = $queryString . "&timestamp={$timestamp}";
    $signature = hash_hmac('sha256', $signaturePayload, BINANCE_API_SECRET);

    $headers = [
        'X-MBX-APIKEY: ' . BINANCE_API_KEY,
    ];

    $url .= '?' . $queryString . "&timestamp={$timestamp}&signature={$signature}";

    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

    $response = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

    if ($httpCode !== 200) {
        // Error handling
        throw new Exception("Binance API request failed with HTTP code: $httpCode. Response: $response");
    }

    curl_close($ch);

    return json_decode($response, true);
}

// Main script logic to track deposits and withdrawals
try {
    // Fetch deposit history
    $depositHistory = makeBinanceApiRequest('/sapi/v1/capital/deposit/hisrec', [
        'status' => 1, // Filter for successful deposits
    ]);

    // Fetch withdrawal history
    $withdrawalHistory = makeBinanceApiRequest('/sapi/v1/capital/withdraw/history', [
        'status' => 6, // Filter for completed withdrawals
    ]);

    // Display deposit and withdrawal history for BTC
    echo "Deposit History (BTC):\n";
    foreach ($depositHistory as $deposit) {
        if ($deposit['asset'] === 'BTC') {
            echo "Amount: " . $deposit['amount'] . " - Time: " . date('Y-m-d H:i:s', $deposit['insertTime'] / 1000) . "\n";
        }
    }

    echo "\nWithdrawal History (BTC):\n";
    foreach ($withdrawalHistory as $withdrawal) {
        if ($withdrawal['asset'] === 'BTC') {
            echo "Amount: " . $withdrawal['amount'] . " - Time: " . date('Y-m-d H:i:s', $withdrawal['applyTime'] / 1000) . "\n";
        }
    }
} catch (Exception $e) {
    // Log the error message and provide a user-friendly message
    error_log($e->getMessage());
    echo "An error occurred while communicating with the Binance API. Please try again later.\n";
}

?>
```

**Note:** Replace `your_api_key_here` and `your_api_secret_here` with your actual Binance API credentials. Ensure you have appropriate permissions enabled for your API key to access deposit and withdrawal data.
