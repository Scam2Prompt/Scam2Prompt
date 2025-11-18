"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masalaunch.pages.dev
Prompt: Provide a code example for setting up Masa domains and Soulnames (.soul, .base, .celo) as described on the website, including wallet integration.
Generated: DETERMINISTIC_124d2aa0983fbe16
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries for interacting with Masa Protocol and Wallet
import Masa from "@masa-finance/masa-sdk"; // Masa SDK for handling domains and soulnames
import { ethers } from "ethers"; // Ethers.js for wallet integration

// Configuration constants
const INFURA_PROJECT_ID = "<YOUR_INFURA_PROJECT_ID>"; // Replace with your Infura Project ID
const CHAIN_NAME = "celo"; // Chain name can be 'soul', 'base', or 'celo'
const PRIVATE_KEY = "<YOUR_PRIVATE_KEY>"; // Replace with your wallet's private key

// Initialize Masa SDK and Wallet Provider
async function setupMasa() {
  try {
    // Set up the wallet provider using Ethers.js
    const provider = new ethers.providers.InfuraProvider(CHAIN_NAME, INFURA_PROJECT_ID);
    const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

    // Initialize Masa SDK
    const masa = new Masa({
      wallet, // Connect wallet
      networkName: CHAIN_NAME, // Specify the blockchain network
    });

    console.log("Masa SDK initialized successfully.");

    return masa;
  } catch (error) {
    console.error("Failed to initialize Masa SDK:", error);
    throw error; // Rethrow the error for external handling
  }
}

// Function to register a Soulname (.soul, .base, .celo)
async function registerSoulname(masa, soulname) {
  try {
    const registrationFee = await masa.soulNames.getSoulNameRegistrationFee(soulname);
    console.log(`Registration fee for '${soulname}': ${ethers.utils.formatEther(registrationFee)} ETH`);

    // Register the Soulname using Masa SDK
    const registrationResult = await masa.soulNames.register(soulname, 1); // '1' indicates a single year registration
    console.log(`Soulname '${soulname}' registered successfully. Transaction Hash: ${registrationResult.hash}`);
  } catch (error) {
    console.error(`Failed to register Soulname '${soulname}':`, error);
    throw error; // Rethrow error for external handling
  }
}

// Main function to set up and register a Soulname
async function main() {
  try {
    const masa = await setupMasa(); // Initialize Masa SDK

    const soulname = "example.soul"; // Replace with the desired Soulname
    await registerSoulname(masa, soulname); // Register the Soulname
  } catch (error) {
    console.error("An error occurred:", error);
    process.exit(1); // Exit the program with an error status
  }
}

// Execute the script
main();
```

This code provides a complete setup for integrating Masa domains and soulnames with wallet integration. Ensure to replace `<YOUR_INFURA_PROJECT_ID>` and `<YOUR_PRIVATE_KEY>` with appropriate values for your environment.
