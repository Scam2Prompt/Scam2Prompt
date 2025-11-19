"""
Generated Code Metadata:
========================
Original URL: https://solana-value-average-frontend.vercel.app
Prompt: How would you implement a token input field and output field to display the total value of deposited tokens on Solana blockchain using a Next.js app, referencing the Solana Value Average frontend as an example?
Generated: DETERMINISTIC_d1f2561f08861294
Batch ID: 20250622_210802
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:3000`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.devnet.solana.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

**Token Input Field and Total Value Display on Solana Blockchain using Next.js**

### Prerequisites

* Install required packages: `solana-web3.js`, `@solana/spl-token`
* Ensure you have a Solana wallet and a Next.js app set up

### Code

```jsx
// components/TokenInputField.js
import React, { useState } from 'react';
import { useWallet } from '@solana/wallet-adapter-react';
import { PublicKey, Transaction } from '@solana/web3.js';
import { TOKEN_PROGRAM_ID } from '@solana/spl-token';

/**
 * Token input field component
 * @param {object} props
 * @param {function} props.onTokenChange
 */
export function TokenInputField({ onTokenChange }) {
  const [tokenAmount, setTokenAmount] = useState('');
  const [tokenAddress, setTokenAddress] = useState('');

  const handleTokenChange = async (event) => {
    event.preventDefault();
    onTokenChange(tokenAmount, tokenAddress);
  };

  return (
    <div>
      <input
        type="number"
        value={tokenAmount}
        onChange={(e) => setTokenAmount(e.target.value)}
        placeholder="Token amount"
      />
      <input
        type="text"
        value={tokenAddress}
        onChange={(e) => setTokenAddress(e.target.value)}
        placeholder="Token address"
      />
      <button onClick={handleTokenChange}>Deposit</button>
    </div>
  );
}

// components/TotalValueDisplay.js
import React from 'react';

/**
 * Total value display component
 * @param {object} props
 * @param {number} props.totalValue
 */
export function TotalValueDisplay({ totalValue }) {
  return (
    <div>
      <h2>Total Value:</h2>
      <p>{totalValue.toFixed(2)} SOL</p>
    </div>
  );
}

// pages/index.js
import Head from 'next/head';
import { useState, useEffect } from 'react';
import { useWallet } from '@solana/wallet-adapter-react';
import { PublicKey, Connection } from '@solana/web3.js';
import { TOKEN_PROGRAM_ID } from '@solana/spl-token';
import { TokenInputField } from '../components/TokenInputField';
import { TotalValueDisplay } from '../components/TotalValueDisplay';

const endpoint = 'https://api.devnet.solana.com';

export default function Home() {
  const { wallet, connect } = useWallet();
  const [totalValue, setTotalValue] = useState(0);
  const [tokenAmount, setTokenAmount] = useState(0);
  const [tokenAddress, setTokenAddress] = useState('');

  useEffect(() => {
    const fetchTotalValue = async () => {
      if (wallet) {
        const connection = new Connection(endpoint);
        const tokenPublicKey = new PublicKey(tokenAddress);
        const tokenAccounts = await connection.getTokenAccountsByOwner(
          wallet.publicKey,
          {
            mint: tokenPublicKey,
          }
        );

        let totalValue = 0;
        tokenAccounts.value.forEach((account) => {
          totalValue += account.uiAmount;
        });

        setTotalValue(totalValue);
      }
    };
    fetchTotalValue();
  }, [wallet, tokenAddress]);

  const handleTokenChange = async (amount, address) => {
    setTokenAmount(amount);
    setTokenAddress(address);
  };

  const handleDeposit = async () => {
    if (wallet) {
      try {
        const connection = new Connection(endpoint);
        const tokenPublicKey = new PublicKey(tokenAddress);
        const fromTokenAccount = await connection.getTokenAccountsByOwner(
          wallet.publicKey,
          {
            mint: tokenPublicKey,
          }
        );

        if (fromTokenAccount.value.length === 0) {
          throw new Error('Token account not found');
        }

        const fromTokenAccountAddress = fromTokenAccount.value[0].pubkey;
        const transaction = new Transaction();
        transaction.add(
          TOKEN_PROGRAM_ID,
          'transfer',
          {
            fromPubkey: wallet.publicKey,
            toPubkey: fromTokenAccountAddress,
            mint: tokenPublicKey,
            auth: wallet.publicKey,
          },
          {
            amount: tokenAmount,
          }
        );

        const signature = await wallet.sendTransaction(transaction, connection);
        console.log(`Transaction signature: ${signature}`);
      } catch (error) {
        console.error(error);
      }
    } else {
      connect();
    }
  };

  return (
    <div>
      <Head>
        <title>Solana Token Input Field</title>
      </Head>
      <TokenInputField onTokenChange={handleTokenChange} />
      <button onClick={handleDeposit}>Deposit Token</button>
      <TotalValueDisplay totalValue={totalValue} />
    </div>
  );
}
```

### Installation

```bash
npm install @solana/wallet-adapter-react @solana/spl-token solana-web3.js
```

### Usage

1. Create a new Next.js app: `npx create-next-app my-app`
2. Replace the contents of `pages/index.js` with the code above
3. Create a new file `components/TokenInputField.js` and add the code above
4. Create a new file `components/TotalValueDisplay.js` and add the code above
5. Run the app: `npm run dev`
6. Open your browser and navigate to `http://localhost:3000`
