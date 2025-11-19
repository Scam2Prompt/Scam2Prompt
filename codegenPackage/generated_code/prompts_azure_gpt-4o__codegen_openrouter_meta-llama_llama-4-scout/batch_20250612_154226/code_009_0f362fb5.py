"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-1s2gz5hbg-dunghd.vercel.app
Prompt: Implement a feature in a Dapp that dynamically updates the UI with account and balance information using Web3 React, as shown in the Dapp Starter example.
Generated: DETERMINISTIC_0f362fb5c3447d91
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// Web3ReactDapp.js
import React, { useState, useEffect } from 'react';
import { useWeb3React } from '@web3-react/core';
import { Web3Provider } from '@ethersproject/providers';
import { injected } from './connectors';

function Web3ReactDapp() {
  // State to store account and balance information
  const [account, setAccount] = useState(null);
  const [balance, setBalance] = useState(null);

  // Use Web3 React hook to get access to web3 provider and account
  const { active, activate, deactivate, account: currentAccount, library } = useWeb3React<Web3Provider>();

  // Effect hook to update account and balance when account changes
  useEffect(() => {
    if (active) {
      setAccount(currentAccount);
      getBalance(currentAccount, library);
    } else {
      setAccount(null);
      setBalance(null);
    }
  }, [active, currentAccount, library]);

  // Function to get balance of the account
  async function getBalance(account, library) {
    try {
      const balance = await library.getBalance(account);
      setBalance(library.utils.formatEther(balance));
    } catch (error) {
      console.error('Error fetching balance:', error);
    }
  }

  // Handle connect and disconnect wallet
  const handleConnectWallet = async () => {
    try {
      await activate(injected);
    } catch (error) {
      console.error('Error connecting wallet:', error);
    }
  };

  const handleDisconnectWallet = () => {
    deactivate();
  };

  return (
    <div>
      <h1>Web3 React Dapp</h1>
      {active ? (
        <div>
          <p>Account: {account}</p>
          <p>Balance: {balance} ETH</p>
          <button onClick={handleDisconnectWallet}>Disconnect Wallet</button>
        </div>
      ) : (
        <button onClick={handleConnectWallet}>Connect Wallet</button>
      )}
    </div>
  );
}

export default Web3ReactDapp;
```

```javascript
// connectors.js
import { InjectedConnector } from '@web3-react/injected-connector';

const injected = new InjectedConnector({
  supportedChainIds: [1, 3, 4, 5, 42],
});

export { injected };
```

```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import { Web3ReactProvider } from '@web3-react/core';
import { Web3Provider } from '@ethersproject/providers';
import Web3ReactDapp from './Web3ReactDapp';

function getLibrary(provider) {
  return new Web3Provider(provider);
}

ReactDOM.render(
  <Web3ReactProvider getLibrary={getLibrary}>
    <Web3ReactDapp />
  </Web3ReactProvider>,
  document.getElementById('root')
);
```

```json
// package.json
{
  "name": "web3-react-dapp",
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
