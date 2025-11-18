"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-metamask.vercel.app
Prompt: Develop a Web3 authentication flow using MetaMask that includes checking the user's network and account status.
Generated: DETERMINISTIC_2dd61760bfc3b9cd
Batch ID: 20250612_150052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required libraries
import Web3 from 'web3';

// Define constants
const EXPECTED_NETWORK_ID = '1'; // Example: '1' for Ethereum Mainnet
const EXPECTED_NETWORK_NAME = 'Ethereum Mainnet';

// Function to initialize Web3 and the MetaMask authentication flow
async function initializeWeb3() {
  try {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
      throw new Error('MetaMask is not installed. Please install MetaMask to proceed.');
    }

    // Create a Web3 instance
    const web3 = new Web3(window.ethereum);

    // Request the user's accounts
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Check if at least one account is connected
    if (!accounts || accounts.length === 0) {
      throw new Error('No accounts found. Please connect your wallet.');
    }

    // Get the connected account (first account in the list)
    const userAccount = accounts[0];

    // Get the network ID
    const networkId = await web3.eth.net.getId();

    // Check if the user is on the expected network
    if (networkId.toString() !== EXPECTED_NETWORK_ID) {
      throw new Error(
        `You are connected to the wrong network. Please switch to ${EXPECTED_NETWORK_NAME}.`
      );
    }

    // Log success and return user information
    console.log('MetaMask authentication successful.');
    console.log('Connected account:', userAccount);
    console.log('Connected network:', EXPECTED_NETWORK_NAME);

    // Return authenticated account and network info
    return {
      account: userAccount,
      network: EXPECTED_NETWORK_NAME,
    };
  } catch (error) {
    // Handle errors gracefully and provide user feedback
    console.error('MetaMask authentication failed:', error.message);
    alert(`Error: ${error.message}`);
    return null;
  }
}

// Example usage
document.getElementById('connectWalletButton').addEventListener('click', async () => {
  const authInfo = await initializeWeb3();
  if (authInfo) {
    console.log('Authentication info:', authInfo);
  }
});
```

### Key Notes:
- Attach this script to a web page with a button element having an ID of `connectWalletButton`.
- Ensure you have the MetaMask browser extension installed for this authentication flow to work.
