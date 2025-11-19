"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-pay3wfto1-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Write code to fetch and display the Chain ID and account information of a connected wallet using Web3 React, as implemented in the Dapp Starter template.
Generated: DETERMINISTIC_4e8d2e4c283b7b75
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// Web3ReactConfig.js
import { Web3ReactProvider } from '@web3-react/core';
import { Web3Provider } from '@ethersproject/providers';

function getLibrary(provider) {
  const library = new Web3Provider(provider);
  library.pollingInterval = 8000;
  return library;
}

export const Web3React = { Web3ReactProvider, getLibrary };
```

```jsx
// useChainId.js
import { useWeb3React } from '@web3-react/core';

const useChainId = () => {
  const { chainId, error } = useWeb3React();

  if (error) {
    console.error('Error fetching chainId:', error);
  }

  return chainId;
};

export default useChainId;
```

```jsx
// useAccount.js
import { useWeb3React } from '@web3-react/core';

const useAccount = () => {
  const { account, error } = useWeb3React();

  if (error) {
    console.error('Error fetching account:', error);
  }

  return account;
};

export default useAccount;
```

```jsx
// WalletInfo.js
import React from 'react';
import useChainId from './useChainId';
import useAccount from './useAccount';

const WalletInfo = () => {
  const chainId = useChainId();
  const account = useAccount();

  if (!chainId || !account) {
    return <div>Please connect your wallet</div>;
  }

  return (
    <div>
      <h2>Wallet Information</h2>
      <p>Chain ID: {chainId}</p>
      <p>Account: {account}</p>
    </div>
  );
};

export default WalletInfo;
```

```jsx
// App.js
import React from 'react';
import { Web3ReactProvider, Web3React } from './Web3ReactConfig';
import WalletInfo from './WalletInfo';

function App() {
  return (
    <Web3ReactProvider getLibrary={Web3React.getLibrary}>
      <WalletInfo />
    </Web3ReactProvider>
  );
}

export default App;
```

```jsx
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
