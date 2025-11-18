"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://on-oeth.pages.dev
Prompt: Write a script in JavaScript using ethers.js to retrieve the current balances of stablecoins (DAI, USDC, USDT) backing OUSD from the Origin vault's smart contract.
Generated: DETERMINISTIC_07194f95fb2713c6
Batch ID: 20250612_150613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Script to retrieve the current balances of stablecoins (DAI, USDC, USDT) backing OUSD
 * from the Origin Vault's smart contract using ethers.js.
 * 
 * Requirements:
 * - Install ethers.js via `npm install ethers`
 * - Replace INFURA_PROJECT_ID, ETHEREUM_NETWORK, and VAULT_CONTRACT_ADDRESS with appropriate values
 */

const ethers = require('ethers');

// Configuration
const INFURA_PROJECT_ID = "your-infura-project-id"; // Replace with your Infura Project ID
const ETHEREUM_NETWORK = "mainnet"; // Use 'mainnet' or other networks as needed
const VAULT_CONTRACT_ADDRESS = "0x4fDd3F3e3d0C682cB6cC6D9baF8a69338D2820A0"; // Replace with Origin Vault contract address

// Stablecoin addresses (replace with actual contract addresses if necessary)
const STABLECOINS = {
  DAI: "0x6B175474E89094C44Da98b954EedeAC495271d0F",
  USDC: "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606EB48",
  USDT: "0xdAC17F958D2ee523a2206206994597C13D831ec7",
};

// ERC20 ABI (simplified for balanceOf method)
const ERC20_ABI = [
  "function balanceOf(address account) view returns (uint256)"
];

// Main function
async function getStablecoinBalances() {
  try {
    // Set up provider (Infura in this case)
    const provider = new ethers.providers.InfuraProvider(ETHEREUM_NETWORK, INFURA_PROJECT_ID);

    // Create contract instances for each stablecoin
    const stablecoinContracts = Object.entries(STABLECOINS).map(([name, address]) => ({
      name,
      contract: new ethers.Contract(address, ERC20_ABI, provider),
    }));

    console.log("Fetching balances from the Origin Vault contract...");

    // Retrieve and log balances
    for (const { name, contract } of stablecoinContracts) {
      const balance = await contract.balanceOf(VAULT_CONTRACT_ADDRESS);
      console.log(`${name} Balance: ${ethers.utils.formatUnits(balance, name === "USDC" || name === "USDT" ? 6 : 18)} ${name}`);
    }
  } catch (error) {
    console.error("Error fetching stablecoin balances:", error.message);
  }
}

// Execute the script
getStablecoinBalances();
```
