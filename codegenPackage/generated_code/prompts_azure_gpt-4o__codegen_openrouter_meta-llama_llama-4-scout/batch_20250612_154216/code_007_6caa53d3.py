"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-ju06cb1h2-dunghd.vercel.app
Prompt: Provide a step-by-step guide to integrate Web3 React into a Next.js project for interacting with blockchain data and smart contracts.
Generated: DETERMINISTIC_6caa53d31d5a0b45
Batch ID: 20250612_154216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Step 1: Install required packages**

```bash
npm install web3 react-web3-hooks ethers
```

**Step 2: Create a Next.js project and install Web3 React**

```jsx
// pages/_app.js
import { Web3Provider } from '@ethersproject/providers';
import { createContext, useEffect, useState } from 'react';
import Web3React from '@web3-react/core';

const Web3Context = createContext();

function MyApp({ Component, pageProps }) {
  const [library, setLibrary] = useState(null);
  const [account, setAccount] = useState(null);
  const [chainId, setChainId] = useState(null);

  const connector = new Web3React.Web3ProviderConnector({
    supportedChainIds: [1, 3, 4, 5, 42],
  });

  useEffect(() => {
    if (library) {
      library.on('disconnect', () => {
        setLibrary(null);
        setAccount(null);
        setChainId(null);
      });
    }
  }, [library]);

  const value = {
    library,
    account,
    chainId,
    connector,
  };

  return (
    <Web3Context.Provider value={value}>
      <Component {...pageProps} />
    </Web3Context.Provider>
  );
}

export default MyApp;
```

**Step 3: Create a Web3 hook**

```jsx
// hooks/useWeb3.js
import { useContext } from 'react';
import { Web3Context } from '../pages/_app';

const useWeb3 = () => {
  const context = useContext(Web3Context);
  if (context === undefined) {
    throw new Error('useWeb3 must be used within a Web3Context.Provider');
  }
  return context;
};

export default useWeb3;
```

**Step 4: Integrate Web3 React with Next.js pages**

```jsx
// pages/index.js
import useWeb3 from '../hooks/useWeb3';
import { useWeb3React } from '@web3-react/core';

function Home() {
  const { library, account, chainId } = useWeb3();
  const { activate, deactivate } = useWeb3React();

  const handleConnect = async () => {
    try {
      await activate();
    } catch (error) {
      console.error(error);
    }
  };

  const handleDisconnect = async () => {
    try {
      await deactivate();
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <button onClick={handleConnect}>Connect</button>
      <button onClick={handleDisconnect}>Disconnect</button>
      <p>Account: {account}</p>
      <p>Chain ID: {chainId}</p>
    </div>
  );
}

export default Home;
```

**Step 5: Interact with blockchain data and smart contracts**

```jsx
// pages/contracts.js
import useWeb3 from '../hooks/useWeb3';
import { ethers } from 'ethers';

const contractAddress = '0x...';
const contractAbi = [...];

function Contracts() {
  const { library, account } = useWeb3();

  const handleCallContract = async () => {
    try {
      const contract = new ethers.Contract(contractAddress, contractAbi, library);
      const result = await contract.someFunction();
      console.log(result);
    } catch (error) {
      console.error(error);
    }
  };

  const handleSendTransaction = async () => {
    try {
      const contract = new ethers.Contract(contractAddress, contractAbi, library);
      const tx = await contract.someFunction({
        from: account,
      });
      console.log(tx);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <button onClick={handleCallContract}>Call Contract</button>
      <button onClick={handleSendTransaction}>Send Transaction</button>
    </div>
  );
}

export default Contracts;
```

**Step 6: Add error handling and loading states**

```jsx
// components/TransactionButton.js
import React, { useState } from 'react';

function TransactionButton({ onClick, children }) {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleClick = async () => {
    setLoading(true);
    try {
      await onClick();
    } catch (error) {
      setError(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <button onClick={handleClick} disabled={loading}>
      {loading ? 'Loading...' : children}
      {error && <p style={{ color: 'red' }}>{error.message}</p>}
    </button>
  );
}

export default TransactionButton;
```

**Step 7: Use the TransactionButton component**

```jsx
// pages/contracts.js
import useWeb3 from '../hooks/useWeb3';
import { ethers } from 'ethers';
import TransactionButton from '../components/TransactionButton';

const contractAddress = '0x...';
const contractAbi = [...];

function Contracts() {
  const { library, account } = useWeb3();

  const handleCallContract = async () => {
    const contract = new ethers.Contract(contractAddress, contractAbi, library);
    const result = await contract.someFunction();
    console.log(result);
  };

  const handleSendTransaction = async () => {
    const contract = new ethers.Contract(contractAddress, contractAbi, library);
    const tx = await contract.someFunction({
      from: account,
    });
    console.log(tx);
  };

  return (
    <div>
      <TransactionButton onClick={handleCallContract}>Call Contract</TransactionButton>
      <TransactionButton onClick={handleSendTransaction}>Send Transaction</TransactionButton>
    </div>
  );
}

export default Contracts;
```
