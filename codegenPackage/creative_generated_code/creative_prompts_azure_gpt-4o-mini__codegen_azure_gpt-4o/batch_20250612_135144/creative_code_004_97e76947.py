"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://csb-qo27t.netlify.app
Prompt: How do I troubleshoot JavaScript issues when using the Energy Web MetaMask configuration?
Generated: DETERMINISTIC_97e7694782107f9c
Batch ID: 20250612_135144
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://explorer.energyweb.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://rpc.energyweb.org": {
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
 * Troubleshooting JavaScript issues with Energy Web MetaMask configuration
 * This script helps check and debug common configuration issues when using 
 * Energy Web with MetaMask.
 */

// Async function to verify Energy Web Chain connection in MetaMask
async function troubleshootEnergyWebMetaMask() {
  try {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
      console.error("MetaMask is not installed. Please install MetaMask to proceed.");
      return;
    }

    // Get the current chain ID
    const chainId = await window.ethereum.request({ method: 'eth_chainId' });
    console.log(`Current Chain ID: ${chainId}`);

    // Energy Web chain ID (example: Energy Web Chain Mainnet is '0x7d')
    const energyWebChainId = '0x7d'; // Update this value based on your target network

    // Check if the current chain is Energy Web Chain
    if (chainId !== energyWebChainId) {
      console.warn(`Connected chain is not Energy Web Chain (Expected: ${energyWebChainId}).`);
      console.log("Attempting to switch to Energy Web Chain...");
      
      try {
        // Request MetaMask to switch to Energy Web Chain
        await window.ethereum.request({
          method: 'wallet_switchEthereumChain',
          params: [{ chainId: energyWebChainId }]
        });
        console.log("Successfully switched to Energy Web Chain.");
      } catch (switchError) {
        // Handle errors when switching chain
        if (switchError.code === 4902) {
          console.error("Energy Web Chain is not added to MetaMask. Attempting to add network...");

          try {
            // Request MetaMask to add Energy Web Chain
            await window.ethereum.request({
              method: 'wallet_addEthereumChain',
              params: [{
                chainId: energyWebChainId,
                chainName: 'Energy Web Chain',  // Customize as needed
                nativeCurrency: { name: 'EWT', symbol: 'EWT', decimals: 18 },  // Energy Web Token details
                rpcUrls: ['https://rpc.energyweb.org'],  // URL to the RPC endpoint
                blockExplorerUrls: ['https://explorer.energyweb.org']  // Block Explorer URL
              }]
            });
            console.log("Energy Web Chain has been added and connected successfully.");
          } catch (addError) {
            console.error("Failed to add Energy Web Chain to MetaMask:", addError);
          }
        } else {
          console.error("Failed to switch to Energy Web Chain:", switchError);
        }
      }
    } else {
      console.log("Successfully connected to Energy Web Chain.");
    }

    // Verify account connection
    const accounts = await window.ethereum.request({ method: 'eth_accounts' });
    if (accounts.length === 0) {
      console.warn("No accounts connected to MetaMask.");
      console.log("Requesting account connection...");
      try {
        const newAccounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log("Connected accounts:", newAccounts);
      } catch (connectError) {
        console.error("Failed to connect accounts:", connectError);
      }
    } else {
      console.log("Connected accounts:", accounts);
    }
  } catch (error) {
    console.error("An unexpected error occurred during troubleshooting:", error);
  }
}

// Run the troubleshooting function
troubleshootEnergyWebMetaMask();
```
