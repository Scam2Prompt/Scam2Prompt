"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect.com
Prompt: Write a code snippet that demonstrates how to implement WalletKit features for enhancing wallet user experience in a web3 application.
Generated: DETERMINISTIC_3aa36de39cf4b6a1
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary dependencies
import { Web3ReactProvider, useWeb3React } from '@web3-react/core';
import { InjectedConnector } from '@web3-react/injected-connector';
import { ethers } from 'ethers';

// Define an injected connector for wallet connection
const injectedConnector = new InjectedConnector({
  supportedChainIds: [1, 3, 4, 5, 42], // Ethereum Mainnet and Testnets
});

// WalletConnection Component
const WalletConnection = () => {
  const { activate, deactivate, active, account, library, error } = useWeb3React();

  // Connect wallet handler
  const connectWallet = async () => {
    try {
      await activate(injectedConnector);
      console.log('Wallet connected successfully');
    } catch (err) {
      console.error('Error connecting wallet:', err.message);
    }
  };

  // Disconnect wallet handler
  const disconnectWallet = () => {
    try {
      deactivate();
      console.log('Wallet disconnected successfully');
    } catch (err) {
      console.error('Error disconnecting wallet:', err.message);
    }
  };

  // Fetch wallet balance
  const fetchBalance = async () => {
    if (!library || !account) {
      console.error('Wallet not connected');
      return;
    }
    try {
      const balance = await library.getBalance(account);
      console.log('Wallet Balance:', ethers.utils.formatEther(balance));
    } catch (err) {
      console.error('Error fetching wallet balance:', err.message);
    }
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h2>WalletKit Example</h2>
      {active ? (
        <div>
          <p>Connected Account: <b>{account}</b></p>
          <button onClick={fetchBalance} style={{ margin: '10px' }}>
            Fetch Balance
          </button>
          <button onClick={disconnectWallet} style={{ margin: '10px' }}>
            Disconnect Wallet
          </button>
        </div>
      ) : (
        <button onClick={connectWallet} style={{ margin: '10px' }}>
          Connect Wallet
        </button>
      )}
      {/* Display potential error */}
      {error && <p style={{ color: 'red' }}>Error: {error.message}</p>}
    </div>
  );
};

// Create a Web3ReactProvider wrapper
const App = () => {
  return (
    <Web3ReactProvider getLibrary={(provider) => new ethers.providers.Web3Provider(provider)}>
      <WalletConnection />
    </Web3ReactProvider>
  );
};

// Export the main App component
export default App;
```
