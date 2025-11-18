"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton.me
Prompt: Provide a step-by-step guide and code example for integrating TON DNS into a decentralized application.
Generated: DETERMINISTIC_b6623063a2de71b3
Batch ID: 20250612_153915
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://testnet.toncenter.com/api/v2/jsonRPC": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Step-by-Step Guide and Code Example for Integrating TON DNS into a Decentralized Application
 *
 * Prerequisites:
 * - Install `tonweb` library using npm: `npm install tonweb`
 * - Ensure you have access to the TON DNS smart contract and a TON wallet.
 * - Acquire TON DNS names through TON's official platforms.
 */

const TonWeb = require('tonweb'); // Import TON SDK
const { Cell } = TonWeb.boc; // Used for working with BOC (Bag of Cells) format

// TON DNS smart contract address (update this address with the actual deployed DNS contract)
const DNS_SMART_CONTRACT_ADDRESS = 'EQC...'; // Replace with actual contract address

// Your TON provider endpoint (replace with real endpoint)
const TON_PROVIDER_ENDPOINT = 'https://testnet.toncenter.com/api/v2/jsonRPC';

// TON API key for accessing the provider (if applicable, replace with your actual API key)
const TON_API_KEY = 'your_api_key_here';

// Initialize TonWeb with the provider
const tonweb = new TonWeb(new TonWeb.HttpProvider(TON_PROVIDER_ENDPOINT, { apiKey: TON_API_KEY }));

/**
 * Resolves a TON DNS name to its corresponding wallet address or smart contract address.
 * @param {string} dnsName - The TON DNS name to resolve.
 * @returns {Promise<string>} - The resolved address in hexadecimal format.
 */
async function resolveTONDNS(dnsName) {
  try {
    // Validate DNS name format
    if (!dnsName || typeof dnsName !== 'string') {
      throw new Error('Invalid DNS name provided.');
    }

    // The DNS query is a simple text query in BOC format
    const queryCell = new Cell();
    queryCell.bits.writeUint(0, 32); // Query ID (0 for DNS resolution)
    queryCell.bits.writeString(dnsName); // Write the DNS name to query

    // Resolve the DNS using the contract
    const result = await tonweb.callGetMethod(
      DNS_SMART_CONTRACT_ADDRESS, // Smart contract address
      'dnsResolve', // Smart contract method name
      [queryCell.toBoc().toString('base64')] // BOC query in base64 format
    );

    // Parse the result and extract the address
    if (result && result.stack && result.stack[0] && result.stack[0][1]) {
      const resolvedAddress = result.stack[0][1].toString();
      return resolvedAddress; // Return the resolved address
    } else {
      throw new Error('Failed to resolve TON DNS name.');
    }
  } catch (error) {
    // Handle errors gracefully
    console.error('Error resolving TON DNS:', error.message);
    throw error; // Re-throw error for higher-level handling
  }
}

/**
 * Example Usage: Resolve a DNS name
 */
(async () => {
  const dnsName = 'example.ton'; // Replace with actual TON DNS name
  try {
    const resolvedAddress = await resolveTONDNS(dnsName);
    console.log(`Resolved Address for "${dnsName}": ${resolvedAddress}`);
  } catch (error) {
    console.error('Failed to resolve DNS name:', error.message);
  }
})();
```
