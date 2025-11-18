"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-three.vercel.app
Prompt: Write code to detect MetaMask's network and display a warning if the user is connected to an unsupported blockchain network.
Generated: DETERMINISTIC_69adb5359d40a28b
Batch ID: 20250612_150052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary Web3 library (ensure you have Web3 installed in your project).
// This example assumes you are using a modern browser with MetaMask installed.

(async () => {
  // Check if the MetaMask extension is installed in the browser
  if (typeof window.ethereum === 'undefined') {
    console.error("MetaMask is not installed in this browser.");
    alert("MetaMask is required to use this application. Please install or enable MetaMask.");
    return;
  }

  try {
    // Request MetaMask accounts access
    await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Fetch the current chain ID from MetaMask
    const chainId = await window.ethereum.request({ method: 'eth_chainId' });

    // Define a list of supported chain IDs
    const supportedNetworks = {
      "0x1": "Ethereum Mainnet",
      "0x3": "Ropsten Testnet",
      "0x4": "Rinkeby Testnet",
      "0x5": "Goerli Testnet",
      "0x2a": "Kovan Testnet"
    };

    // Check if the current chain ID is supported
    if (!supportedNetworks[chainId]) {
      console.warn(`Unsupported network detected: Chain ID ${chainId}`);
      alert(`Warning: You are connected to an unsupported network (Chain ID: ${chainId}). Please switch to a supported network.`);
    } else {
      console.log(`Connected to ${supportedNetworks[chainId]}`);
      alert(`You are connected to ${supportedNetworks[chainId]}.`);
    }
  } catch (error) {
    // Handle errors that may occur
    console.error("An error occurred while detecting MetaMask's network:", error);
    alert("An error occurred while communicating with MetaMask. Please try again.");
  }

  // Optional: Listen for network changes and revalidate the chain ID
  window.ethereum.on('chainChanged', async (newChainId) => {
    console.log(`Network changed to Chain ID ${newChainId}`);
    if (!supportedNetworks[newChainId]) {
      alert(`Warning: You have switched to an unsupported network (Chain ID: ${newChainId}).`);
    } else {
      alert(`You are now connected to ${supportedNetworks[newChainId]}.`);
    }
  });
})();
```
