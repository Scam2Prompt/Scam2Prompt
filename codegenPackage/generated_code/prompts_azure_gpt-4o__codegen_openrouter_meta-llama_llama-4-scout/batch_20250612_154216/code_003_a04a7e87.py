"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-ju06cb1h2-dunghd.vercel.app
Prompt: Provide an example of using Web3 React to fetch and display the Chain ID and account balance of a connected wallet in a decentralized application.
Generated: DETERMINISTIC_a04a7e8734c3b3bf
Batch ID: 20250612_154216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// Web3ReactExample.js
import React, { useState, useEffect } from 'react';
import { useWeb3React } from '@web3-react/core';
import { Web3Provider } from '@ethersproject/providers';
import { InjectedConnector } from '@web3-react/injected-connector';

const connector = new InjectedConnector();

const Web3ReactExample = () => {
  const { 
    library, 
    chainId, 
    account, 
    activate, 
    deactivate, 
    error 
  } = useWeb3React<Web3Provider>();

  const [balance, setBalance] = useState(0);

  useEffect(() => {
    const fetchBalance = async () => {
      if (library && account) {
        try {
          const balance = await library.getBalance(account);
          setBalance(balance.toString());
        } catch (error) {
          console.error('Error fetching balance:', error);
        }
      }
    };
    fetchBalance();
  }, [library, account]);

  const handleConnect = () => {
    activate(connector)
      .then(() => console.log('Wallet connected'))
      .catch((error) => console.error('Error connecting wallet:', error));
  };

  const handleDisconnect = () => {
    deactivate();
    console.log('Wallet disconnected');
  };

  return (
    <div>
      <h1>Web3 React Example</h1>
      {chainId && <p>Chain ID: {chainId}</p>}
      {account && <p>Account: {account}</p>}
      {balance && <p>Balance: {balance}</p>}
      {error && <p style={{ color: 'red' }}>Error: {error.message}</p>}
      {!account && (
        <button onClick={handleConnect}>Connect Wallet</button>
      )}
      {account && (
        <button onClick={handleDisconnect}>Disconnect Wallet</button>
      )}
    </div>
  );
};

export default Web3ReactExample;
```

```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import { Web3ReactProvider } from '@web3-react/core';
import { Web3Provider } from '@ethersproject/providers';
import Web3ReactExample from './Web3ReactExample';

function getLibrary(provider) {
  return new Web3Provider(provider);
}

ReactDOM.render(
  <React.StrictMode>
    <Web3ReactProvider getLibrary={getLibrary}>
      <Web3ReactExample />
    </Web3ReactProvider>
  </React.StrictMode>,
  document.getElementById('root')
);
```

```bash
# package.json
{
  "name": "web3-react-example",
  "version": "0.1.0",
  "dependencies": {
    "@ethersproject/providers": "^5.4.1",
    "@web3-react/core": "^1.7.0",
    "@web3-react/injected-connector": "^1.4.0",
    "react": "^17.0.2",
    "react-dom": "^17.0.2"
  },
  "scripts": {
    "start": "react-scripts start"
  }
}
```
