"""
Generated Code Metadata:
========================
Original URL: https://claimairtoday.com
Prompt: Explain the role of AAAA records in website accessibility and provide a code snippet in JavaScript to verify if a server supports IPv6 using the `dns` and `net` modules.
Generated: DETERMINISTIC_418ea7668c3177b3
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import the required modules
const dns = require('dns');
const net = require('net');

/**
 * Function to check if a server supports IPv6 by resolving its AAAA record.
 * @param {string} hostname - The hostname of the server to check.
 * @returns {Promise<boolean>} - Resolves to true if IPv6 is supported, otherwise false.
 */
async function supportsIPv6(hostname) {
  return new Promise((resolve, reject) => {
    // Resolve the AAAA record for the given hostname
    dns.resolve6(hostname, (err, addresses) => {
      if (err) {
        if (err.code === 'ENOTFOUND') {
          // Hostname not found, IPv6 not supported
          resolve(false);
        } else {
          // Other DNS errors
          reject(new Error(`DNS resolution error: ${err.message}`));
        }
      } else if (addresses && addresses.length > 0) {
        // Validate the resolved IPv6 addresses
        const isValidIPv6 = addresses.every((address) => net.isIP(address) === 6);
        resolve(isValidIPv6);
      } else {
        // No IPv6 addresses found
        resolve(false);
      }
    });
  });
}

// Example usage
(async () => {
  const hostname = 'example.com'; // Replace with the hostname you want to check
  try {
    const ipv6Supported = await supportsIPv6(hostname);
    console.log(`IPv6 support for ${hostname}: ${ipv6Supported ? 'Yes' : 'No'}`);
  } catch (error) {
    console.error(`Error checking IPv6 support: ${error.message}`);
  }
})();
```
