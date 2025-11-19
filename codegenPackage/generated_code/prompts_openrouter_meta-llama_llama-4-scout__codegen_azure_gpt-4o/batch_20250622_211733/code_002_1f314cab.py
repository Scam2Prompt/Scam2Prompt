"""
Generated Code Metadata:
========================
Original URL: https://minipepe.digital
Prompt: Explain the difference between IPv4 and IPv6, and write a code snippet in Node.js to check if a server supports IPv4 or IPv6 using the `net` module.
Generated: DETERMINISTIC_1f314cabf5a2360f
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import the 'net' module from Node.js
const net = require('net');

/**
 * Function to check if a server supports IPv4 or IPv6.
 * @param {string} host - The hostname or IP address of the server.
 * @param {number} port - The port number to connect to.
 * @returns {Promise<string>} - Resolves with 'IPv4', 'IPv6', or 'Neither'.
 */
async function checkIPSupport(host, port) {
  return new Promise((resolve) => {
    let ipv4Supported = false;
    let ipv6Supported = false;

    // Create an IPv4 socket
    const ipv4Socket = net.createConnection({ host, port, family: 4 }, () => {
      ipv4Supported = true;
      ipv4Socket.end(); // Close the connection
    });

    // Handle IPv4 connection errors
    ipv4Socket.on('error', () => {
      ipv4Socket.destroy(); // Ensure the socket is closed
    });

    // Create an IPv6 socket
    const ipv6Socket = net.createConnection({ host, port, family: 6 }, () => {
      ipv6Supported = true;
      ipv6Socket.end(); // Close the connection
    });

    // Handle IPv6 connection errors
    ipv6Socket.on('error', () => {
      ipv6Socket.destroy(); // Ensure the socket is closed
    });

    // Wait for both sockets to finish
    ipv4Socket.on('close', () => {
      if (!ipv6Socket.destroyed) return; // Wait for IPv6 to finish
      resolveResult();
    });

    ipv6Socket.on('close', () => {
      if (!ipv4Socket.destroyed) return; // Wait for IPv4 to finish
      resolveResult();
    });

    // Resolve the result based on the support flags
    function resolveResult() {
      if (ipv4Supported && ipv6Supported) {
        resolve('Both IPv4 and IPv6 are supported');
      } else if (ipv4Supported) {
        resolve('IPv4 is supported');
      } else if (ipv6Supported) {
        resolve('IPv6 is supported');
      } else {
        resolve('Neither IPv4 nor IPv6 is supported');
      }
    }
  });
}

// Example usage
(async () => {
  const host = 'example.com'; // Replace with the target hostname or IP
  const port = 80; // Replace with the target port
  try {
    const result = await checkIPSupport(host, port);
    console.log(`Result: ${result}`);
  } catch (error) {
    console.error('Error:', error.message);
  }
})();
```
