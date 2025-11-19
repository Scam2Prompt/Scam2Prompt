"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-realio.network
Prompt: Can you provide an example of using the MetaMask API to create a walletless dapp?
Generated: DETERMINISTIC_5d715358897f5b18
Batch ID: 20250612_163051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary packages
import detectEthereumProvider from '@metamask/detect-provider';

// Function to initialize the dApp
async function initializeDApp() {
  // Detect the MetaMask provider
  const provider = await detectEthereumProvider();

  if (!provider) {
    console.error('MetaMask is not installed. Please install MetaMask to use this application.');
    return;
  }

  console.log('MetaMask detected.');

  // Check if the user is connected to the dApp
  try {
    const accounts = await provider.request({ method: 'eth_accounts' });

    if (accounts.length > 0) {
      console.log('User is already connected:', accounts);
    } else {
      console.log('User is not connected.');
    }
  } catch (error) {
    console.error('Error checking connection status:', error);
  }

  // Listen for account changes
  provider.on('accountsChanged', (accounts) => {
    if (accounts.length === 0) {
      console.log('User disconnected from MetaMask.');
    } else {
      console.log('User switched accounts:', accounts);
    }
  });

  // Listen for network changes
  provider.on('chainChanged', (chainId) => {
    console.log('Network changed to:', chainId);
  });

  // Create button for enabling MetaMask connection
  createConnectButton(provider);
}

// Function to create a "Connect Wallet" button
function createConnectButton(provider) {
  const button = document.createElement('button');
  button.innerText = 'Connect to MetaMask';
  button.style.padding = '10px 20px';
  button.style.margin = '20px';
  button.style.fontSize = '16px';

  // Attach click event to initiate MetaMask connection
  button.onclick = async () => {
    try {
      const accounts = await provider.request({ method: 'eth_requestAccounts' });
      console.log('Connected accounts:', accounts);
    } catch (error) {
      if (error.code === 4001) {
        console.error('User rejected connection request.');
      } else {
        console.error('Failed to connect to MetaMask:', error);
      }
    }
  };

  // Append button to the DOM
  document.body.appendChild(button);
}

// Initialize the dApp on page load
window.onload = () => {
  initializeDApp();
};
```

**Note**: This code is built using the MetaMask API and the `@metamask/detect-provider` package. It creates a walletless dApp and dynamically generates a "Connect to MetaMask" button. Make sure to install the required package (`npm install @metamask/detect-provider`) and serve the code in a browser environment.
