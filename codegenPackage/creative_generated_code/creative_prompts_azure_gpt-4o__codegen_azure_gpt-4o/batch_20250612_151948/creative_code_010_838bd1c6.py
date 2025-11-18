"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dev--ethereumorg.netlify.app
Prompt: Write code to interact with Ethereum's decentralized DNS system using JavaScript, as described in Ethereum.org's documentation.
Generated: DETERMINISTIC_838bd1c688a11dd6
Batch ID: 20250612_151948
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Required libraries
const { ethers } = require("ethers");

// ENS domain to resolve
const ensDomain = "vitalik.eth";

// Ethereum provider - connecting to an Ethereum node
// You can replace with your own provider URL if needed
const provider = new ethers.providers.InfuraProvider("mainnet", "YOUR_INFURA_API_KEY");

// Function to resolve ENS domain to an Ethereum address
async function resolveEnsDomain(domain) {
  try {
    // Validate input
    if (!domain || typeof domain !== "string") {
      throw new Error("Invalid ENS domain.");
    }

    // Lookup the address associated with the ENS domain
    const address = await provider.resolveName(domain);

    // If no address is found, throw an error
    if (!address) {
      throw new Error(`No Ethereum address found for the ENS domain: ${domain}`);
    }

    return address;
  } catch (err) {
    // Handle errors gracefully
    console.error("Error resolving ENS domain:", err.message);
    throw err;
  }
}

// Function to reverse resolve Ethereum address to ENS domain
async function reverseResolveAddress(address) {
  try {
    // Validate input
    if (!ethers.utils.isAddress(address)) {
      throw new Error("Invalid Ethereum address.");
    }

    // Perform reverse lookup
    const domain = await provider.lookupAddress(address);

    // If no ENS domain is found, throw an error
    if (!domain) {
      throw new Error(`No ENS domain found for the Ethereum address: ${address}`);
    }

    return domain;
  } catch (err) {
    // Handle errors gracefully
    console.error("Error in reverse resolution:", err.message);
    throw err;
  }
}

// Example usage
(async () => {
  try {
    console.log(`Resolving ENS domain "${ensDomain}"...`);
    const resolvedAddress = await resolveEnsDomain(ensDomain);
    console.log(`Ethereum address for "${ensDomain}": ${resolvedAddress}`);

    console.log(`Reversing Ethereum address "${resolvedAddress}"...`);
    const reversedEnsDomain = await reverseResolveAddress(resolvedAddress);
    console.log(`ENS domain for "${resolvedAddress}": ${reversedEnsDomain}`);
  } catch (error) {
    console.error("An error occurred during ENS resolution:", error.message);
  }
})();
```

### Instructions:
1. Replace `"YOUR_INFURA_API_KEY"` with your Infura API key or use another Ethereum provider.
2. Install required dependencies with `npm install ethers`.
3. Run the script with `node script.js`.

This code demonstrates resolving an ENS domain to an Ethereum address and performing reverse resolution. It includes validation, error handling, and adheres to best practices.
