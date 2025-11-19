"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mmetadaflkugigns.webflow.io
Prompt: Generate code snippets to interact with the Ethereum Mainnet using the MetaMask wallet, highlighting the supported networks.
Generated: DETERMINISTIC_ee2d8a1cdd799102
Batch ID: 20250612_155344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Example code for interacting with the Ethereum Mainnet using MetaMask
 * and checking supported networks.
 */

// Importing ethers.js for working with Ethereum
import { ethers } from 'ethers';

/**
 * Initialize connection to MetaMask and Ethereum Mainnet.
 */
async function connectToMetaMask() {
  try {
    // Check if the browser has MetaMask installed
    if (typeof window.ethereum === 'undefined') {
      console.error('MetaMask is not installed!');
      alert('Please install MetaMask to continue.');
      return;
    }

    // Request account access from MetaMask
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Initialize ethers provider using MetaMask's injected provider
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    console.log('Connected account:', accounts[0]);
    console.log('Provider connected:', provider);
    return { accounts, provider };
  } catch (error) {
    console.error('Error connecting to MetaMask:', error);
    alert('Failed to connect to MetaMask. Please try again.');
  }
}

/**
 * Check the currently selected network in MetaMask.
 */
async function checkNetwork(provider) {
  try {
    // Fetch the network details
    const network = await provider.getNetwork();

    // Supported networks by MetaMask
    const supportedNetworks = {
      1: 'Ethereum Mainnet',
      3: 'Ropsten Test Network',
      4: 'Rinkeby Test Network',
      5: 'Goerli Test Network',
      42: 'Kovan Test Network'
    };

    const networkName = supportedNetworks[network.chainId] || 'Unknown Network';
    console.log(`Connected to: ${networkName} (Chain ID: ${network.chainId})`);
    return networkName;
  } catch (error) {
    console.error('Error checking network:', error);
    alert('Failed to fetch network details. Please try again.');
  }
}

/**
 * Entry point function to connect to MetaMask
 * and check network information.
 */
async function main() {
  try {
    const { accounts, provider } = await connectToMetaMask();

    if (provider) {
      const networkName = await checkNetwork(provider);

      console.log(`Account: ${accounts[0]}`);
      console.log(`Network: ${networkName}`);
    }
  } catch (error) {
    console.error('Error in main function:', error);
  }
}

// Run the main function when the script loads
main();
```
