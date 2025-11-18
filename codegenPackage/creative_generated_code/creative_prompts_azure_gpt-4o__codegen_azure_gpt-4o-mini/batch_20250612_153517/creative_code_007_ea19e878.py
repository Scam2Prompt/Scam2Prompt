"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rainbowkit-example-git-daniel-metamask-rainbowdotme.vercel.app
Prompt: How can I use RainbowKit to connect a wallet in a React app, ensuring the button design matches the example on the RainbowKit demo page?
Generated: DETERMINISTIC_ea19e87854b5eea9
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useEffect } from 'react';
import { 
  getDefaultWallets, 
  RainbowKitProvider, 
  Chain, 
  walletConnect, 
  WalletConnectModal 
} from '@rainbow-me/rainbowkit';
import { ethers } from 'ethers';
import { configureChains, createClient, WagmiConfig } from 'wagmi';
import { mainnet, polygon, optimism, arbitrum } from 'wagmi/chains';

// Configure chains and wallets
const { chains, provider } = configureChains(
  [mainnet, polygon, optimism, arbitrum], 
  [walletConnect()]
);
const { connectors } = getDefaultWallets({
  appName: 'Your App Name',
  chains,
});

// Create a Wagmi client
const client = createClient({
  autoConnect: true,
  connectors: () => connectors,
  provider,
});

// Main App Component
const App = () => {
  // Effect to handle wallet connection status
  useEffect(() => {
    const checkWalletConnection = async () => {
      try {
        const accounts = await window.ethereum.request({ method: 'eth_accounts' });
        if (accounts.length > 0) {
          console.log('Wallet connected:', accounts[0]);
        } else {
          console.log('No wallet connected');
        }
      } catch (error) {
        console.error('Error checking wallet connection:', error);
      }
    };

    checkWalletConnection();
  }, []);

  // Function to handle wallet connection
  const connectWallet = async () => {
    try {
      await window.ethereum.request({ method: 'eth_requestAccounts' });
      console.log('Wallet connected successfully');
    } catch (error) {
      console.error('Error connecting wallet:', error);
    }
  };

  return (
    <WagmiConfig client={client}>
      <RainbowKitProvider chains={chains}>
        <div style={{ padding: '20px' }}>
          <h1>Connect Your Wallet</h1>
          <button 
            onClick={connectWallet}
            style={{
              backgroundColor: '#008CBA', // Match the RainbowKit demo button color
              color: 'white',
              padding: '15px 32px',
              textAlign: 'center',
              textDecoration: 'none',
              display: 'inline-block',
              fontSize: '16px',
              margin: '4px 2px',
              cursor: 'pointer',
              border: 'none',
              borderRadius: '4px',
            }}>
            Connect Wallet
          </button>
        </div>
      </RainbowKitProvider>
    </WagmiConfig>
  );
};

export default App;
```

Make sure to install the required packages with:

```bash
npm install @rainbow-me/rainbowkit wagmi ethers
``` 

This code sets up a simple React application using RainbowKit to connect a cryptocurrency wallet with proper error handling and styling.
