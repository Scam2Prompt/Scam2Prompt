"""
Generated Code Metadata:
========================
Original URL: https://wallet-dapp-starknet.vercel.app
Prompt: Generate code for a basic React app that interacts with the Starknet blockchain using a wallet API.
Generated: DETERMINISTIC_737d62928333b83c
Batch ID: 20250622_212247
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// src/App.js
import React, { useState, useEffect } from 'react';
import { connect, disconnect } from 'get-starknet';
import { Provider, Contract, constants } from 'starknet';

function App() {
  const [wallet, setWallet] = useState(null);
  const [address, setAddress] = useState('');
  const [isConnected, setIsConnected] = useState(false);
  const [balance, setBalance] = useState('0');
  const [error, setError] = useState('');

  // Connect wallet
  const connectWallet = async () => {
    try {
      setError('');
      const starknet = await connect();
      if (!starknet) {
        throw new Error('No wallet found');
      }
      await starknet.enable();
      setWallet(starknet);
      setIsConnected(true);
      setAddress(starknet.selectedAddress);
      await fetchBalance(starknet);
    } catch (err) {
      setError(err.message);
    }
  };

  // Disconnect wallet
  const disconnectWallet = () => {
    disconnect();
    setWallet(null);
    setIsConnected(false);
    setAddress('');
    setBalance('0');
  };

  // Fetch balance
  const fetchBalance = async (walletInstance) => {
    try {
      if (!walletInstance) return;
      
      const provider = new Provider({
        sequencer: {
          network: constants.NetworkName.SN_GOERLI
        }
      });
      
      const balance = await provider.getBalance(walletInstance.selectedAddress);
      setBalance(balance.toString());
    } catch (err) {
      setError('Failed to fetch balance');
    }
  };

  // Check connection status on load
  useEffect(() => {
    const checkConnection = async () => {
      const starknet = await connect();
      if (starknet?.isConnected) {
        setWallet(starknet);
        setIsConnected(true);
        setAddress(starknet.selectedAddress);
        await fetchBalance(starknet);
      }
    };
    checkConnection();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Starknet Wallet Connection</h1>
        
        {error && <p className="error">{error}</p>}
        
        {!isConnected ? (
          <button onClick={connectWallet}>Connect Wallet</button>
        ) : (
          <div>
            <p>Connected Address: {address}</p>
            <p>Balance: {balance} wei</p>
            <button onClick={disconnectWallet}>Disconnect</button>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;
```

```javascript
// src/index.js
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```

```css
/* src/index.css */
body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.App {
  text-align: center;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: calc(10px + 2vmin);
}

button {
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  background-color: #61dafb;
  border: none;
  border-radius: 5px;
  margin: 10px;
}

button:hover {
  background-color: #4fa8d3;
}

.error {
  color: red;
  margin: 10px 0;
}
```

```json
// package.json
{
  "name": "starknet-react-app",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "get-starknet": "^3.0.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1",
    "starknet": "^5.6.0",
    "web-vitals": "^2.1.4"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}
```
