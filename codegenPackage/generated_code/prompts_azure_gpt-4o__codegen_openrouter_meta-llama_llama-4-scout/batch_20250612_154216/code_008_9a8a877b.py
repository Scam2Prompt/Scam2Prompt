"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-ju06cb1h2-dunghd.vercel.app
Prompt: Write code to fetch and display the balance of a connected wallet using Web3 React and display it in a daisyUI-styled component.
Generated: DETERMINISTIC_9a8a877b36c5bab2
Batch ID: 20250612_154216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// WalletBalance.js
import React, { useState, useEffect } from 'react';
import { useWeb3 } from '@web3-react/core';
import { Button, Card } from 'daisyui';

const WalletBalance = () => {
  const { account, library } = useWeb3();
  const [balance, setBalance] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchBalance = async () => {
      if (library && account) {
        try {
          const balance = await library.getBalance(account);
          setBalance(balance);
          setError(null);
        } catch (error) {
          setError(error.message);
          setBalance(null);
        }
      }
    };
    fetchBalance();
  }, [library, account]);

  const balanceInEther = balance ? balance / 1e18 : 0;

  return (
    <Card className="shadow-lg bg-base-100">
      <Card.Header>
        <h2 className="card-title">Wallet Balance</h2>
      </Card.Header>
      <Card.Body>
        {error ? (
          <p className="text-error">{error}</p>
        ) : (
          <p className="text-lg">
            {balanceInEther.toFixed(4)} ETH
          </p>
        )}
        <Button className="btn-primary" disabled={!account}>
          {account ? `Connected to ${account}` : 'Connect Wallet'}
        </Button>
      </Card.Body>
    </Card>
  );
};

export default WalletBalance;
```

```jsx
// App.js
import React from 'react';
import { Web3ReactProvider } from '@web3-react/core';
import { Web3Provider } from '@ethersproject/providers';
import WalletBalance from './WalletBalance';

function getLibrary(provider) {
  return new Web3Provider(provider);
}

function App() {
  return (
    <Web3ReactProvider getLibrary={getLibrary}>
      <div className="container mx-auto p-4 pt-6 md:p-6 lg:p-12 xl:p-24">
        <WalletBalance />
      </div>
    </Web3ReactProvider>
  );
}

export default App;
```

```css
/* globals.css */
@import 'daisyui/dist/full.css';
@import 'tailwindcss/base';
@import 'tailwindcss/components';
@import 'tailwindcss/utilities';
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
