"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana-value-average-frontend.vercel.app
Prompt: Write a Next.js frontend component for a Solana-based application that allows users to connect their wallet and specify input and output tokens for value averaging deposits. Include functionality for scheduling start date and time.
Generated: DETERMINISTIC_5b5be3ba8c0253aa
Batch ID: 20250612_145130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// components/ValueAveragingDeposit.js

import { useState } from 'react';
import dynamic from 'next/dynamic';
import { WalletProvider } from '@solana/wallet-adapter-react';
import { ConnectionProvider } from '@solana/wallet-adapter-react';
import { clusterApiUrl } from '@solana/web3.js';
import {
  PhantomWalletAdapter,
  SolflareWalletAdapter,
} from '@solana/wallet-adapter-wallets';
import { WalletModalProvider } from '@solana/wallet-adapter-react-ui';

// Dynamically import the wallet adapter UI styles
const WalletConnect = dynamic(() => import('@solana/wallet-adapter-react-ui'), {
  ssr: false,
});

// Main Component
const ValueAveragingDeposit = () => {
  // State for wallet connection
  const [wallet, setWallet] = useState(null);

  // State for form inputs
  const [inputToken, setInputToken] = useState('');
  const [outputToken, setOutputToken] = useState('');
  const [startDateTime, setStartDateTime] = useState('');

  // Initialize Solana wallets
  const wallets = [new PhantomWalletAdapter(), new SolflareWalletAdapter()];

  // Handle wallet selection
  const onWalletConnect = (wallet) => {
    setWallet(wallet);
  };

  // Handle form submission
  const handleSubmit = async (event) => {
    event.preventDefault();

    if (!wallet) {
      alert('Please connect your wallet first!');
      return;
    }

    try {
      // Validation
      if (!inputToken || !outputToken || !startDateTime) {
        alert('Please fill in all fields.');
        return;
      }

      // Normally, you'd send this data to your backend or Solana program
      console.log({
        inputToken,
        outputToken,
        startDateTime,
      });

      alert('Value averaging deposit scheduled successfully!');
    } catch (error) {
      console.error('Error scheduling deposit:', error);
      alert('Failed to schedule the deposit. Please try again.');
    }
  };

  return (
    <ConnectionProvider endpoint={clusterApiUrl('mainnet-beta')}>
      <WalletProvider wallets={wallets} autoConnect>
        <WalletModalProvider>
          <div style={{ padding: '2rem', maxWidth: '600px', margin: 'auto' }}>
            <h1>Value Averaging Deposit</h1>
            <WalletConnect>
              {/* Wallet connection button */}
              <WalletConnect.WalletConnectButton />
            </WalletConnect>
            <form onSubmit={handleSubmit} style={{ marginTop: '1rem' }}>
              {/* Input Token */}
              <label>
                Input Token:
                <input
                  type="text"
                  value={inputToken}
                  onChange={(e) => setInputToken(e.target.value)}
                  placeholder="Enter input token (e.g., SOL)"
                  required
                />
              </label>
              <br />
              {/* Output Token */}
              <label>
                Output Token:
                <input
                  type="text"
                  value={outputToken}
                  onChange={(e) => setOutputToken(e.target.value)}
                  placeholder="Enter output token (e.g., USDT)"
                  required
                />
              </label>
              <br />
              {/* Start Date and Time */}
              <label>
                Start Date & Time:
                <input
                  type="datetime-local"
                  value={startDateTime}
                  onChange={(e) => setStartDateTime(e.target.value)}
                  required
                />
              </label>
              <br />
              {/* Submit Button */}
              <button type="submit">Schedule Deposit</button>
            </form>
          </div>
        </WalletModalProvider>
      </WalletProvider>
    </ConnectionProvider>
  );
};

export default ValueAveragingDeposit;
```
