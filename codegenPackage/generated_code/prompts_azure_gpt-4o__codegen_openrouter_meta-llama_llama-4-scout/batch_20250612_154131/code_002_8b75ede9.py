"""
Generated Code Metadata:
========================
Original URL: https://fastyield.app
Prompt: Generate code to detect and handle wallet connection events in a React-based dApp inspired by FastYield.
Generated: DETERMINISTIC_8b75ede9f27c0294
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// WalletConnectionHandler.js
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';

/**
 * Wallet connection event handler for React-based dApp.
 * 
 * @returns {Object} Wallet connection status and handlers.
 */
const useWalletConnection = () => {
  const [isConnected, setIsConnected] = useState(false);
  const [account, setAccount] = useState(null);
  const [web3, setWeb3] = useState(null);

  useEffect(() => {
    // Initialize Web3
    const initWeb3 = async () => {
      if (window.ethereum) {
        try {
          const web3Instance = new Web3(window.ethereum);
          setWeb3(web3Instance);
          // Request account access
          const accounts = await web3Instance.eth.getAccounts();
          if (accounts.length > 0) {
            setIsConnected(true);
            setAccount(accounts[0]);
          }
        } catch (error) {
          console.error('Error initializing Web3:', error);
        }
      } else {
        console.log('No Ethereum provider found.');
      }
    };
    initWeb3();
  }, []);

  // Handle wallet connection change
  useEffect(() => {
    const handleConnectionChange = async () => {
      if (web3) {
        try {
          const accounts = await web3.eth.getAccounts();
          if (accounts.length > 0 && accounts[0] !== account) {
            setAccount(accounts[0]);
            setIsConnected(true);
          } else if (accounts.length === 0) {
            setIsConnected(false);
            setAccount(null);
          }
        } catch (error) {
          console.error('Error handling connection change:', error);
        }
      }
    };
    window.ethereum?.on('accountsChanged', handleConnectionChange);
    window.ethereum?.on('disconnect', () => {
      setIsConnected(false);
      setAccount(null);
    });
    return () => {
      window.ethereum?.removeListener('accountsChanged', handleConnectionChange);
      window.ethereum?.removeListener('disconnect', () => { });
    };
  }, [web3, account]);

  // Connect wallet
  const connectWallet = async () => {
    if (window.ethereum) {
      try {
        await window.ethereum.request({ method: 'eth_requestAccounts' });
      } catch (error) {
        console.error('Error connecting wallet:', error);
      }
    } else {
      console.log('No Ethereum provider found.');
    }
  };

  // Disconnect wallet
  const disconnectWallet = async () => {
    if (window.ethereum) {
      try {
        await window.ethereum.request({ method: 'eth_disconnect' });
        setIsConnected(false);
        setAccount(null);
      } catch (error) {
        console.error('Error disconnecting wallet:', error);
      }
    }
  };

  return { isConnected, account, connectWallet, disconnectWallet };
};

export default useWalletConnection;
```

```javascript
// App.js
import React from 'react';
import useWalletConnection from './WalletConnectionHandler';

function App() {
  const { isConnected, account, connectWallet, disconnectWallet } = useWalletConnection();

  return (
    <div>
      {isConnected ? (
        <div>
          <p>Connected to {account}</p>
          <button onClick={disconnectWallet}>Disconnect Wallet</button>
        </div>
      ) : (
        <div>
          <p>Wallet not connected.</p>
          <button onClick={connectWallet}>Connect Wallet</button>
        </div>
      )}
    </div>
  );
}

export default App;
```

```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```
