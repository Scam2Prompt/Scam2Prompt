"""
Generated Code Metadata:
========================
Original URL: https://starknet-dapp.vercel.app
Prompt: Generate code to enable wallet connection in a StarkNet dApp, ensuring compatibility with popular wallets like Argent.
Generated: DETERMINISTIC_b2aed707b767cbe8
Batch ID: 20250612_151932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import { StarknetProvider } from 'starknet-react';
import { useEffect, useState } from 'react';

// Main App component
const App = () => {
  // State to manage wallet connection status
  const [isConnected, setIsConnected] = useState(false);
  const [walletAddress, setWalletAddress] = useState('');

  // Function to connect to the wallet
  const connectWallet = async () => {
    try {
      // Request wallet connection
      const provider = new StarknetProvider();
      const accounts = await provider.enable();
      
      // Set the wallet address and connection status
      setWalletAddress(accounts[0]);
      setIsConnected(true);
    } catch (error) {
      console.error('Failed to connect to wallet:', error);
      alert('Error connecting to wallet. Please try again.');
    }
  };

  // Function to disconnect the wallet
  const disconnectWallet = () => {
    setWalletAddress('');
    setIsConnected(false);
  };

  // Effect to handle wallet connection status
  useEffect(() => {
    // Check if wallet is already connected on component mount
    const checkConnection = async () => {
      try {
        const provider = new StarknetProvider();
        const accounts = await provider.getAccounts();
        if (accounts.length > 0) {
          setWalletAddress(accounts[0]);
          setIsConnected(true);
        }
      } catch (error) {
        console.error('Error checking wallet connection:', error);
      }
    };

    checkConnection();
  }, []);

  return (
    <div>
      <h1>StarkNet dApp Wallet Connection</h1>
      {isConnected ? (
        <div>
          <p>Connected Wallet: {walletAddress}</p>
          <button onClick={disconnectWallet}>Disconnect</button>
        </div>
      ) : (
        <button onClick={connectWallet}>Connect Wallet</button>
      )}
    </div>
  );
};

// Export the App component as default
export default App;
```
