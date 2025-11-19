"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qrcodepay.xyz
Prompt: Create a JavaScript example that displays a QR code for a payment of 1500 USDT using QRCodePay's secure payment features.
Generated: DETERMINISTIC_b44a76b1046647fa
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the QRCode library (ensure you have `qrcode` installed in your project via npm)
const QRCode = require('qrcode');

// Function to generate and display the QR Code for a payment
async function generatePaymentQRCode(amount, currency) {
    try {
        // 1. Define the payment details
        const paymentDetails = {
            amount: amount, // The payment amount
            currency: currency, // The currency type
            description: "Secure payment using QRCodePay", // Description of the transaction
            timestamp: Date.now(), // Current timestamp for security
        };

        // 2. Convert payment details to a JSON string
        const paymentData = JSON.stringify(paymentDetails);

        // 3. Generate the QR Code
        const qrCodeDataURL = await QRCode.toDataURL(paymentData);

        // 4. Display the generated QR Code
        console.log("Generated QR Code for payment:");
        console.log(qrCodeDataURL);

        // If using in a web app, you could return the QR Code as an `<img>` source
        // Example: document.querySelector('#qrCodeImage').src = qrCodeDataURL;

    } catch (error) {
        // Handle errors during QR Code generation
        console.error("Error generating QR Code:", error.message);
    }
}

// Call the function to generate a QR Code for 1500 USDT payment
generatePaymentQRCode(1500, "USDT");
```

### Notes:
1. Install the `qrcode` package by running: `npm install qrcode`.
2. This code generates a QR Code that encodes the payment details in JSON format.
3. Replace `console.log` with appropriate rendering in a web or mobile application if needed.
