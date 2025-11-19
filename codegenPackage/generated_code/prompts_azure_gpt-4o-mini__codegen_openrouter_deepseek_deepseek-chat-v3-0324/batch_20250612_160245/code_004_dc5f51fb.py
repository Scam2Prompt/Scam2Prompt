"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-g3by6mqqf-dung-huynh-duc-kakas-projects.vercel.app
Prompt: How do I edit the pages/index.tsx file to test hot module replacement (HMR) updates in a DApp project as outlined in the Dapp Starter content?
Generated: DETERMINISTIC_dc5f51fb6f9f7765
Batch ID: 20250612_160245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// pages/index.tsx
import { useState, useEffect } from 'react';
import { useWeb3React } from '@web3-react/core';
import { Web3Provider } from '@ethersproject/providers';
import { formatEther } from '@ethersproject/units';
import { injected } from '../components/wallet/connectors';

// Test component to demonstrate HMR
const HMRTest = () => {
  const [count, setCount] = useState(0);
  return (
    <div style={{ margin: '20px 0', padding: '20px', border: '1px solid #ddd' }}>
      <h3>HMR Test Component</h3>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      <p>Edit this component and save to test HMR</p>
    </div>
  );
};

export default function Home() {
  const { active, account, library, activate, deactivate } = useWeb3React<Web3Provider>();
  const [balance, setBalance] = useState<string | null>(null);

  useEffect(() => {
    if (account && library) {
      library.getBalance(account).then((result) => {
        setBalance(formatEther(result));
      });
    }
  }, [account, library]);

  const connect = async () => {
    try {
      await activate(injected);
    } catch (ex) {
      console.error(ex);
    }
  };

  const disconnect = async () => {
    try {
      deactivate();
    } catch (ex) {
      console.error(ex);
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>DApp Starter</h1>
      
      {/* HMR Test Component */}
      <HMRTest />

      {active ? (
        <div>
          <p>Connected with: {account}</p>
          <p>Balance: {balance} ETH</p>
          <button onClick={disconnect}>Disconnect</button>
        </div>
      ) : (
        <button onClick={connect}>Connect to MetaMask</button>
      )}
    </div>
  );
}

// Enable HMR for this module
if (module.hot) {
  module.hot.accept();
}
```
