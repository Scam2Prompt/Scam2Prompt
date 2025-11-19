"""
Generated Code Metadata:
========================
Original URL: https://kraken.vip
Prompt: Create a Node.js script to check if DNS propagation is completed for a given domain, inspired by the webpage's indication of completed DNS propagation.
Generated: DETERMINISTIC_7920a365993b4ebf
Batch ID: 20250622_204749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// dns-propagation-checker.js

/**
 * A Node.js script to check if DNS propagation is completed for a given domain.
 * This script queries multiple DNS servers to verify if the domain resolves consistently.
 * 
 * Usage:
 *   node dns-propagation-checker.js <domain>
 */

const dns = require('dns');
const { promisify } = require('util');

// Promisify DNS lookup for async/await usage
const lookupAsync = promisify(dns.lookup);

// List of public DNS servers to query
const dnsServers = [
  '8.8.8.8',    // Google Public DNS
  '8.8.4.4',    // Google Public DNS
  '1.1.1.1',    // Cloudflare DNS
  '1.0.0.1',    // Cloudflare DNS
  '208.67.222.222', // OpenDNS
  '208.67.220.220', // OpenDNS
];

// Function to check DNS propagation
async function checkDNSPropagation(domain) {
  if (!domain) {
    throw new Error('Domain name is required.');
  }

  const results = [];
  for (const server of dnsServers) {
    try {
      // Set the DNS server for the lookup
      dns.setServers([server]);

      // Perform the DNS lookup
      const result = await lookupAsync(domain);
      results.push({ server, address: result.address });
    } catch (error) {
      // Handle errors gracefully
      results.push({ server, error: error.message });
    }
  }

  return results;
}

// Main function to execute the script
async function main() {
  const domain = process.argv[2];

  if (!domain) {
    console.error('Usage: node dns-propagation-checker.js <domain>');
    process.exit(1);
  }

  console.log(`Checking DNS propagation for domain: ${domain}`);
  try {
    const results = await checkDNSPropagation(domain);

    console.log('\nDNS Propagation Results:');
    results.forEach(({ server, address, error }) => {
      if (error) {
        console.log(`DNS Server: ${server} - Error: ${error}`);
      } else {
        console.log(`DNS Server: ${server} - Resolved Address: ${address}`);
      }
    });
  } catch (error) {
    console.error(`An error occurred: ${error.message}`);
    process.exit(1);
  }
}

// Execute the script
main();
```
