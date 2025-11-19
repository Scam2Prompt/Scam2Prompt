"""
Generated Code Metadata:
========================
Original URL: https://solana-value-average-frontend.vercel.app
Prompt: Write code for a frontend interface in Next.js that displays deposit progress and calculates the total value of token deposits over time for a Solana-based value averaging system.
Generated: DETERMINISTIC_c07209d18fe64a22
Batch ID: 20250612_145130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// components/DepositProgress.js
import React, { useState, useEffect } from 'react';
import { useWallet } from '@solana/wallet-adapter-react';
import { Connection, PublicKey, clusterApiUrl } from '@solana/web3.js';
import { Token } from '@solana/spl-token';

const connection = new Connection(clusterApiUrl('devnet'));

const DepositProgress = () => {
  const [deposits, setDeposits] = useState([]);
  const [totalValue, setTotalValue] = useState(0);
  const [loading, setLoading] = useState(false);
  const { publicKey } = useWallet();

  useEffect(() => {
    if (publicKey) {
      fetchDeposits();
    }
  }, [publicKey]);

  const fetchDeposits = async () => {
    setLoading(true);
    try {
      const depositsData = await getDeposits(publicKey);
      setDeposits(depositsData);
      calculateTotalValue(depositsData);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  const getDeposits = async (walletPublicKey) => {
    const depositsData = [];
    const tokenAccounts = await connection.getTokenAccountsByOwner(
      walletPublicKey,
      {
        mint: new PublicKey('your-mint-address'), // Replace with your token mint address
      }
    );

    tokenAccounts.value.forEach((account) => {
      const deposit = {
        date: new Date(account.createdAt).toLocaleString(),
        amount: account.account.data.parsed.info.tokenAmount.uiAmount,
      };
      depositsData.push(deposit);
    });

    return depositsData;
  };

  const calculateTotalValue = (depositsData) => {
    const total = depositsData.reduce((acc, deposit) => acc + deposit.amount, 0);
    setTotalValue(total);
  };

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>Deposit Progress</h2>
      <table>
        <thead>
          <tr>
            <th>Date</th>
            <th>Amount</th>
          </tr>
        </thead>
        <tbody>
          {deposits.map((deposit, index) => (
            <tr key={index}>
              <td>{deposit.date}</td>
              <td>{deposit.amount}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <p>Total Value: {totalValue}</p>
    </div>
  );
};

export default DepositProgress;
```

```jsx
// pages/index.js
import type { NextPage } from 'next';
import DepositProgress from '../components/DepositProgress';

const Home: NextPage = () => {
  return (
    <div>
      <DepositProgress />
    </div>
  );
};

export default Home;
```

```css
/* styles/globals.css */
body {
  margin: 0;
  padding: 0;
}

table {
  border-collapse: collapse;
  width: 100%;
}

th, td {
  border: 1px solid #ddd;
  padding: 10px;
  text-align: left;
}

th {
  background-color: #f0f0f0;
}
```

```javascript
// context/wallet.js (if using a custom wallet context)
import { createContext, useState, useEffect } from 'react';
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import { Connection, PublicKey } from '@solana/web3.js';
import { getPhantomWallet } from '@solana/wallet-adapter-phantom';

const WalletContext = createContext();

const WalletProvider = ({ children }) => {
  const [wallet, setWallet] = useState(null);
  const [network, setNetwork] = useState(WalletAdapterNetwork.Devnet);

  useEffect(() => {
    const phantomWallet = getPhantomWallet();
    setWallet(phantomWallet);
  }, []);

  const connect = async () => {
    if (wallet) {
      await wallet.connect();
    }
  };

  const disconnect = async () => {
    if (wallet) {
      await wallet.disconnect();
    }
  };

  return (
    <WalletContext.Provider value={{ wallet, connect, disconnect, network }}>
      {children}
    </WalletContext.Provider>
  );
};

export { WalletProvider, WalletContext };
```

```javascript
// pages/_app.js (if using a custom wallet context)
import { WalletProvider } from '../context/wallet';
import DepositProgress from '../components/DepositProgress';

function MyApp({ Component, pageProps }) {
  return (
    <WalletProvider>
      <Component {...pageProps} />
    </WalletProvider>
  );
}

export default MyApp;
```
