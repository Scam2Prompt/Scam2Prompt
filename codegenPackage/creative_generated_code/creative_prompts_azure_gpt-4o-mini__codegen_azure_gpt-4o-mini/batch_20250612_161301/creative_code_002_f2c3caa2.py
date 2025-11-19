"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://manaftech.com
Prompt: Write a function in JavaScript that sends print commands to a Sam4s G-Cube 100 thermal receipt printer.
Generated: DETERMINISTIC_f2c3caa2b6a56168
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Prints a receipt using the Sam4s G-Cube 100 thermal printer.
 * 
 * @param {string} printerIp - The IP address of the printer.
 * @param {string} receiptContent - The content to be printed on the receipt.
 * @returns {Promise<void>} - A promise that resolves when the print command has been sent.
 * @throws {Error} - Throws an error if the printer cannot be reached or if printing fails.
 */
async function printReceipt(printerIp, receiptContent) {
    try {
        // Validate input parameters
        if (!isValidIp(printerIp)) {
            throw new Error("Invalid printer IP address.");
        }
        if (typeof receiptContent !== 'string' || receiptContent.trim() === '') {
            throw new Error("Receipt content must be a non-empty string.");
        }

        // Create a socket connection to the printer
        const net = require('net');
        const client = new net.Socket();

        return new Promise((resolve, reject) => {
            client.connect(9100, printerIp, () => {
                console.log('Connected to printer.');

                // Send print commands in ESC/POS format
                const printCommand = Buffer.from(receiptContent + '\n\n\n' + '\x1D\x61\x01' + '\x1D\x56\x00');
                client.write(printCommand, (err) => {
                    if (err) {
                        reject(new Error("Failed to send data to printer: " + err.message));
                    } else {
                        console.log('Print command sent.');
                        client.end(); // Close the connection
                        resolve();
                    }
                });
            });

            // Handle errors during connection
            client.on('error', (err) => {
                reject(new Error('Connection error: ' + err.message));
            });
            
            // Handle connection timeout
            client.setTimeout(5000); // Set timeout to 5 seconds
            client.on('timeout', () => {
                client.destroy(); // Close the connection on timeout
                reject(new Error('Connection timed out.'));
            });
        });
    } catch (error) {
        console.error('Error occurred while printing:', error);
        throw error; // Rethrow the error after logging it
    }
}

/**
 * Validates the IP address format.
 * 
 * @param {string} ip - The IP address to validate.
 * @returns {boolean} - True if the IP is valid, otherwise false.
 */
function isValidIp(ip) {
    const ipPattern = /^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(
        25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(
        25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(
        25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;
    return ipPattern.test(ip);
}

// Example usage
// printReceipt('192.168.1.100', 'Hello, World!').catch(err => console.error(err));
```
