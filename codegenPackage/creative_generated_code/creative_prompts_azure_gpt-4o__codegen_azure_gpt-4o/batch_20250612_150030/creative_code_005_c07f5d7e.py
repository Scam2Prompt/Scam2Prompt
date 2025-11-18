"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-dapp.vercel.app
Prompt: Show how to set up Web3Modal with custom themes and styles in a blockchain application.
Generated: DETERMINISTIC_c07f5d7ef2183423
Batch ID: 20250612_150030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary dependencies
import React, { useEffect } from 'react';
import { Web3Modal } from '@web3modal/react'; // Web3Modal package
import { providers } from 'ethers'; // Ethers.js for blockchain interactions
import './App.css'; // Import custom styles for the app

// Define constants for your Web3Modal setup
const projectId = 'YOUR_INFURA_PROJECT_ID_OR_WALLETCONNECT_PROJECT_ID'; // Replace with your actual project ID

function App() {
  // Function to handle wallet connection
  const connectWallet = async () => {
    try {
      // Initialize Web3Modal with custom configuration
      const web3Modal = new Web3Modal({
        cacheProvider: true, // Enables automatic reconnection if a wallet was previously connected
        theme: {
          background: 'rgb(39, 49, 56)', // Custom background color
          main: 'rgb(255, 255, 255)', // Custom main text color
          secondary: 'rgb(136, 136, 136)', // Custom secondary text color
          border: 'rgba(196, 196, 196, 0.14)', // Custom border color
          hover: 'rgba(16, 26, 32, 0.16)', // Custom hover color
        },
        network: 'mainnet', // Default network
        providerOptions: {
          walletconnect: {
            package: require('@walletconnect/web3-provider'), // WalletConnect package
            options: {
              infuraId: projectId, // Infura project ID
            },
          },
          // Add support for other providers as needed
        },
      });

      // Open the modal and let the user select a provider
      const provider = await web3Modal.connect();

      // Wrap the provider with ethers.js
      const web3Provider = new providers.Web3Provider(provider);

      // Get the user's account information
      const signer = web3Provider.getSigner();
      const userAddress = await signer.getAddress();

      console.log('Connected wallet address:', userAddress);
    } catch (error) {
      console.error('Error connecting wallet:', error);
    }
  };

  // Automatically clean up resources on unmount
  useEffect(() => {
    return () => {
      // Perform any cleanup operations if needed
    };
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Blockchain Application</h1>
        <button className="connect-button" onClick={connectWallet}>
          Connect Wallet
        </button>
      </header>
    </div>
  );
}

export default App;
```

**Additional Notes:**
- Replace `'YOUR_INFURA_PROJECT_ID_OR_WALLETCONNECT_PROJECT_ID'` with your actual project ID from Infura or WalletConnect.
- Create a CSS file (`App.css`) for your custom styles, such as `.connect-button`.
- Ensure dependencies (`@web3modal/react`, `ethers`, `@walletconnect/web3-provider`) are installed using `npm install`.
