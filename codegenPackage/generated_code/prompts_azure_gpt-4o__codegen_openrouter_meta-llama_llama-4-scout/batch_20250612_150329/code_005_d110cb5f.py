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
 * Generates an Ethereum QR code for cryptocurrency payments.
 *
 * @param string $address Ethereum address to encode in the QR code.
 * @param float $amount Amount of Ether to send (optional).
 * @param string $label Label for the payment (optional).
 * @param string $message Message to include with the payment (optional).
 *
 * @return string The Ethereum QR code data as a string.
 */
function generateEthereumQrCode(string $address, float $amount = null, string $label = null, string $message = null): string
{
    // Ethereum QR code prefix
    $prefix = "ethereum:";

    // Initialize the payload with the address
    $payload = $prefix . $address;

    // Add the amount if provided
    if ($amount !== null) {
        $payload .= "?value=" . $amount;
    }

    // Add the label if provided
    if ($label !== null) {
        if (strpos($payload, "?") === false) {
            $payload .= "?label=" . $label;
        } else {
            $payload .= "&label=" . $label;
        }
    }

    // Add the message if provided
    if ($message !== null) {
        if (strpos($payload, "?") === false) {
            $payload .= "?message=" . $message;
        } else {
            $payload .= "&message=" . $message;
        }
    }

    return $payload;
}

/**
 * Generates a QR code image from the provided data.
 *
 * @param string $data Data to encode in the QR code.
 * @param int $size Size of the QR code image (in pixels).
 *
 * @return string The QR code image as a base64-encoded string.
 */
function generateQrCodeImage(string $data, int $size = 200): string
{
    // Use the endroid/qr-code library to generate the QR code image
    require_once __DIR__ . "/vendor/autoload.php";

    $qrCode = new \Endroid\QrCode\QrCode();
    $qrCode->setText($data);
    $qrCode->setSize($size);

    $writer = new \Endroid\QrCode\Writer\PngWriter();
    $result = $writer->write($qrCode);

    $image = $result->getImage();

    // Return the QR code image as a base64-encoded string
    ob_start();
    imagepng($image);
    $imageData = base64_encode(ob_get_clean());

    return "data:image/png;base64," . $imageData;
}

// Example usage:
$address = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"; // Replace with the Ethereum address
$amount = 1.0; // Optional
$label = "Payment Label"; // Optional
$message = "Payment Message"; // Optional

$qrCodeData = generateEthereumQrCode($address, $amount, $label, $message);
$qrCodeImage = generateQrCodeImage($qrCodeData);

print("<img src=\"$qrCodeImage\" alt=\"Ethereum QR Code\">");

?>
```
