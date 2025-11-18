"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://example.walletconnect.org
Prompt: Implement a feature in React using WalletConnect v2.8.6 to select specific blockchain testnets for wallet connection.
Generated: DETERMINISTIC_d67a3ded8a5b5840
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules and dependencies
import React, { useState, useEffect } from 'react';
import { Web3Modal } from '@web3modal/react';
import { WalletConnectModalSign } from '@walletconnect/modal-sign';
import { Web3Provider } from '@walletconnect/web3-provider';

// Configure WalletConnect v2. Ensure you have installed walletconnect dependencies.
const projectId = 'YOUR_PROJECT_ID'; // Replace with your WalletConnect Project ID
const supportedChains = {
  polygonMumbai: 'Polygon Mumbai Testnet',
  optimismGoerli: 'Optimism Goerli Testnet',
  arbitrumGoerli: 'Arbitrum Goerli Testnet',
};

const walletConnectConfig = {
  projectId,
  chains: [80001, 420, 421613], // Corresponding chain IDs for testnets
  methods: ['eth_sendTransaction', 'eth_sign', 'personal_sign', 'eth_signTypedData'],
  events: ['accountsChanged', 'chainChanged'],
};

// React Component
const WalletConnectComponent = () => {
  const [selectedChain, setSelectedChain] = useState('');
  const [provider, setProvider] = useState(null);
  const [connectedAccount, setConnectedAccount] = useState('');

  useEffect(() => {
    // Cleanup provider on unmount
    return () => {
      if (provider) {
        provider.disconnect();
      }
    };
  }, [provider]);

  // Handle wallet connection
  const connectWallet = async () => {
    try {
      if (!selectedChain) {
        alert('Please select a blockchain testnet.');
        return;
      }

      const chainIdMapping = {
        polygonMumbai: 80001,
        optimismGoerli: 420,
        arbitrumGoerli: 421613,
      };

      const provider = new Web3Provider({
        projectId,
        rpc: {},
        // Specify the chain ID of the selected testnet
        chainId: chainIdMapping[selectedChain],
      });

      // Initialize and connect WalletConnect Modal
      const modal = new WalletConnectModalSign(walletConnectConfig);
      await modal.connect();
      setProvider(provider);

      // Retrieve the connected accounts
      const accounts = await provider.enable();
      setConnectedAccount(accounts[0] || '');
    } catch (error) {
      console.error('Error connecting wallet:', error);
      alert('Failed to connect wallet. Please try again.');
    }
  };

  // Render the component
  return (
    <div style={{ padding: '20px' }}>
      <h2>Connect Wallet via WalletConnect</h2>

      {/* Dropdown to select blockchain testnet */}
      <label htmlFor="blockchain-select">Select Blockchain Testnet: </label>
      <select
        id="blockchain-select"
        value={selectedChain}
        onChange={(e) => setSelectedChain(e.target.value)}
      >
        <option value="">-- Select Testnet --</option>
        {Object.entries(supportedChains).map(([key, name]) => (
          <option key={key} value={key}>
            {name}
          </option>
        ))}
      </select>

      {/* Button to connect wallet */}
      <button
        onClick={connectWallet}
        style={{ marginLeft: '10px', padding: '10px' }}
      >
        Connect Wallet
      </button>

      {/* Display connected account */}
      {connectedAccount && (
        <div style={{ marginTop: '20px' }}>
          <h3>Connected Account:</h3>
          <p>{connectedAccount}</p>
        </div>
      )}
    </div>
  );
};

export default WalletConnectComponent;
```
