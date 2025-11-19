"""
Generated Code Metadata:
========================
Original URL: https://ethereum-qr-code-generator.com
Prompt: Write code in PHP to generate an Ethereum QR code for cryptocurrency payments, ensuring compatibility with the features mentioned on the Ethereum QR Code Generator site.
Generated: DETERMINISTIC_d110cb5f9c27de60
Batch ID: 20250612_150329
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
 * Ethereum QR Code Generator
 * 
 * This script generates a QR code for Ethereum payments with support for various parameters
 * such as amount, gas limit, and custom data. The QR code follows the ERC-681 standard.
 */

require_once 'vendor/autoload.php'; // Include Composer autoloader

use Endroid\QrCode\Builder\Builder;
use Endroid\QrCode\Encoding\Encoding;
use Endiod\QrCode\ErrorCorrectionLevel\ErrorCorrectionLevelHigh;
use Endroid\QrCode\RoundBlockSizeMode\RoundBlockSizeModeMargin;
use Endroid\QrCode\Writer\PngWriter;

class EthereumQRCodeGenerator {
    /**
     * Generate Ethereum payment URI
     *
     * @param string $address Ethereum wallet address
     * @param float|null $amount Amount in ETH (optional)
     * @param int|null $gasLimit Gas limit in Gwei (optional)
     * @param string|null $data Additional data (optional)
     * @return string Ethereum payment URI
     */
    public static function generatePaymentURI(
        string $address,
        ?float $amount = null,
        ?int $gasLimit = null,
        ?string $data = null
    ): string {
        if (!self::isValidAddress($address)) {
            throw new InvalidArgumentException('Invalid Ethereum address');
        }

        $uri = "ethereum:{$address}";

        $params = [];
        if ($amount !== null) {
            $params['value'] = self::toWei($amount);
        }
        if ($gasLimit !== null) {
            $params['gas'] = $gasLimit;
        }
        if ($data !== null) {
            $params['data'] = $data;
        }

        if (!empty($params)) {
            $uri .= '?' . http_build_query($params);
        }

        return $uri;
    }

    /**
     * Generate QR code image from Ethereum payment URI
     *
     * @param string $uri Ethereum payment URI
     * @param int $size QR code size in pixels
     * @return string QR code image as binary data
     */
    public static function generateQRCode(string $uri, int $size = 300): string
    {
        return Builder::create()
            ->writer(new PngWriter())
            ->data($uri)
            ->encoding(new Encoding('UTF-8'))
            ->errorCorrectionLevel(new ErrorCorrectionLevelHigh())
            ->size($size)
            ->margin(10)
            ->roundBlockSizeMode(new RoundBlockSizeModeMargin())
            ->build()
            ->getString();
    }

    /**
     * Validate Ethereum address
     *
     * @param string $address Ethereum address
     * @return bool True if valid, false otherwise
     */
    private static function isValidAddress(string $address): bool
    {
        return preg_match('/^0x[a-fA-F0-9]{40}$/', $address) === 1;
    }

    /**
     * Convert ETH to Wei
     *
     * @param float $eth Amount in ETH
     * @return string Amount in Wei as string
     */
    private static function toWei(float $eth): string
    {
        return bcmul((string)$eth, '1000000000000000000', 0);
    }
}

// Example usage:
try {
    $address = '0x742d35Cc6634C0532925a3b844Bc454e4438f44e'; // Example address
    $amount = 0.5; // 0.5 ETH
    $gasLimit = 21000; // Standard gas limit
    
    $uri = EthereumQRCodeGenerator::generatePaymentURI($address, $amount, $gasLimit);
    $qrCode = EthereumQRCodeGenerator::generateQRCode($uri);
    
    // Output QR code to browser
    header('Content-Type: image/png');
    echo $qrCode;
    
} catch (Exception $e) {
    error_log('Error generating Ethereum QR code: ' . $e->getMessage());
    header('Content-Type: text/plain');
    echo 'Error: ' . $e->getMessage();
}
```
