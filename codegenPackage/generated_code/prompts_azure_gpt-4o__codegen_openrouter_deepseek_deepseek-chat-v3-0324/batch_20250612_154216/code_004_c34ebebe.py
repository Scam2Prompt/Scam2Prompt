"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-ju06cb1h2-dunghd.vercel.app
Prompt: Build a Next.js page with hot module replacement (HMR) enabled, allowing developers to test updates in real-time while integrating Web3 functionality.
Generated: DETERMINISTIC_c34ebebe6768036e
Batch ID: 20250612_154216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// pages/index.js
import { useState, useEffect } from 'react';
import { ethers } from 'ethers';

// Enable HMR (Hot Module Replacement) for this page
if (process.env.NODE_ENV === 'development') {
  if (module.hot) {
    module.hot.accept();
  }
}

export default function Web3IntegrationPage() {
  const [web3Provider, setWeb3Provider] = useState(null);
  const [account, setAccount] = useState('');
  const [network, setNetwork] = useState('');
  const [balance, setBalance] = useState('');
  const [error, setError] = useState('');

  // Initialize Web3 provider
  const initWeb3 = async () => {
    try {
      if (window.ethereum) {
        // Request account access
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        setWeb3Provider(provider);

        // Get network
        const network = await provider.getNetwork();
        setNetwork(network.name);

        // Get account and balance
        const signer = provider.getSigner();
        const address = await signer.getAddress();
        const balance = await provider.getBalance(address);

        setAccount(address);
        setBalance(ethers.utils.formatEther(balance));

        // Listen for account changes
        window.ethereum.on('accountsChanged', (accounts) => {
          setAccount(accounts[0] || '');
          window.location.reload();
        });

        // Listen for chain changes
        window.ethereum.on('chainChanged', () => {
          window.location.reload();
        });
      } else {
        setError('Please install MetaMask or another Web3 provider');
      }
    } catch (err) {
      setError(err.message);
    }
  };

  useEffect(() => {
    initWeb3();
    return () => {
      // Clean up event listeners
      if (window.ethereum) {
        window.ethereum.removeAllListeners();
      }
    };
  }, []);

  return (
    <div className="container">
      <h1>Web3 Integration with HMR</h1>
      
      {error && (
        <div className="error">
          <p>{error}</p>
        </div>
      )}

      {web3Provider ? (
        <div className="web3-info">
          <h2>Connected Account Information</h2>
          <p><strong>Network:</strong> {network}</p>
          <p><strong>Account:</strong> {account}</p>
          <p><strong>Balance:</strong> {balance} ETH</p>
        </div>
      ) : (
        <button onClick={initWeb3} className="connect-button">
          Connect Wallet
        </button>
      )}

      <style jsx>{`
        .container {
          max-width: 800px;
          margin: 0 auto;
          padding: 2rem;
          text-align: center;
        }
        .error {
          color: red;
          margin: 1rem 0;
        }
        .web3-info {
          margin: 2rem 0;
          padding: 1rem;
          border: 1px solid #ddd;
          border-radius: 8px;
          text-align: left;
        }
        .connect-button {
          padding: 0.5rem 1rem;
          background-color: #0070f3;
          color: white;
          border: none;
          border-radius: 4px;
          cursor: pointer;
          font-size: 1rem;
        }
        .connect-button:hover {
          background-color: #0061d5;
        }
      `}</style>
    </div>
  );
}
```
