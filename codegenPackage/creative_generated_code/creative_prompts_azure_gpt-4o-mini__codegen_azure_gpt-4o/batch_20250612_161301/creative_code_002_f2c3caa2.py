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
 * Sends a print command to the Sam4s G-Cube 100 thermal receipt printer.
 * 
 * @param {string} printerIP - The IP address of the printer.
 * @param {number} printerPort - The port number of the printer (default: 9100).
 * @param {string} printData - The content to print (formatted as ESC/POS commands or plain text).
 * @returns {Promise<void>} Resolves when the print command is successfully sent.
 */
async function sendPrintCommand(printerIP, printerPort = 9100, printData) {
  const net = require("net");

  // Validate inputs
  if (!printerIP || typeof printerIP !== "string") {
    throw new Error("Invalid printer IP address.");
  }
  if (!Number.isInteger(printerPort) || printerPort <= 0) {
    throw new Error("Invalid printer port number.");
  }
  if (!printData || typeof printData !== "string") {
    throw new Error("Invalid print data. It must be a non-empty string.");
  }

  return new Promise((resolve, reject) => {
    // Create a socket connection to the printer
    const client = new net.Socket();

    // Set up error handling for the socket
    client.on("error", (error) => {
      reject(new Error(`Failed to connect to printer: ${error.message}`));
    });

    // Connect to the printer
    client.connect(printerPort, printerIP, () => {
      console.log(`Connected to Sam4s G-Cube 100 printer at ${printerIP}:${printerPort}`);

      // Send the print data to the printer
      client.write(printData, "utf8", () => {
        console.log("Print command sent successfully.");
        client.end(); // Close the connection
        resolve();
      });
    });

    // Handle connection closure
    client.on("close", () => {
      console.log("Connection to printer closed.");
    });
  });
}

// Example usage
(async () => {
  try {
    const printerIP = "192.168.1.100"; // Replace with the printer's IP address
    const printerPort = 9100; // Default port for most thermal printers
    const printData = "Hello, World!\n"; // ESC/POS formatted string or plain text

    await sendPrintCommand(printerIP, printerPort, printData);
    console.log("Print job completed.");
  } catch (error) {
    console.error(error.message);
  }
})();
```
