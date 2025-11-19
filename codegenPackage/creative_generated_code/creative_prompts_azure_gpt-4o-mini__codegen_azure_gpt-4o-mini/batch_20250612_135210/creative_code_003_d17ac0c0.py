"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zksync-starter.vercel.app
Prompt: Create a React component that connects to a wallet using wagmi and displays the user's balance on zkSync.
Generated: DETERMINISTIC_d17ac0c0438f1375
Batch ID: 20250612_135210
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://zksync2-mainnet.zksync.io": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and hooks from React and wagmi
import React, { useEffect, useState } from 'react';
import { useAccount, useBalance, chain, WagmiConfig, createClient } from 'wagmi';
import { zkSync } from '@wagmi/chains';

// Create a Wagmi client
const client = createClient({
  autoConnect: true,
  provider: ({ chain }) => {
    if (chain.id === zkSync.id) {
      return new ethers.providers.JsonRpcProvider('https://zksync2-mainnet.zksync.io');
    }
  },
});

// WalletBalance component definition
const WalletBalance = () => {
  const { isConnected } = useAccount();
  const [{ data: balanceData, error: balanceError, isLoading: isBalanceLoading }] = useBalance({
    address: isConnected ? useAccount().address : undefined,
    chainId: zkSync.id,
  });

  // Error handling for balance fetch
  if (balanceError) {
    console.error('Error fetching balance:', balanceError);
  }

  return (
    <div>
      {isBalanceLoading ? (
        <p>Loading balance...</p>
      ) : isConnected ? (
        <p>Your balance on zkSync: {balanceData ? balanceData.formatted : '0'} {balanceData?.symbol}</p>
      ) : (
        <p>Please connect your wallet.</p>
      )}
    </div>
  );
};

// Main App component
const App = () => {
  return (
    <WagmiConfig client={client}>
      <div style={{ padding: '20px' }}>
        <h1>zkSync Wallet Balance</h1>
        <WalletBalance />
      </div>
    </WagmiConfig>
  );
};

// Export the App component
export default App;
```
