"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qqqqqqqtestu.web.app
Prompt: Implement a feature in a React app that connects to a Solana wallet and displays the user's rewards in $TNSR tokens, similar to Tensor's "Connect Wallet" functionality.
Generated: DETERMINISTIC_c56ccef952e05558
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and hooks from React and Solana wallet adapter
import React, { useEffect, useState } from 'react';
import {
  Connection,
  PublicKey,
} from '@solana/web3.js';
import {
  WalletProvider,
  useWallet,
} from '@solana/wallet-adapter-react';
import {
  WalletAdapterNetwork,
  getWalletAdapter
} from '@solana/wallet-adapter-base';
import {
  PhantomWalletAdapter
} from '@solana/wallet-adapter-phantom';

// Define the network and Solana token mint address for $TNSR
const network = WalletAdapterNetwork.Mainnet;
const TNSR_MINT_ADDRESS = 'YOUR_TNSR_MINT_ADDRESS_HERE';

// Main application component
const App = () => {
  const [rewards, setRewards] = useState(0); // State to store user's rewards
  const { wallet, connected } = useWallet(); // Access wallet connection status

  // Function to fetch user rewards from the blockchain
  const fetchRewards = async () => {
    if (!connected || !wallet) return; // Early exit if not connected

    try {
      // Establish connection to Solana network
      const connection = new Connection(network);

      // Fetch the user's token balance
      const tokenAccounts = await connection.getParsedTokenAccountsByOwner(wallet.publicKey, {
        mint: new PublicKey(TNSR_MINT_ADDRESS),
      });

      // Calculate the total rewards from the token accounts
      const totalRewards = tokenAccounts.value.reduce((acc, { account }) => {
        return acc + account.data.parsed.info.tokenAmount.uiAmount;
      }, 0);

      setRewards(totalRewards); // Update state with fetched rewards
    } catch (error) {
      console.error('Error fetching rewards:', error); // Log any errors
      alert('Failed to fetch rewards. Please try again later.'); // Notify the user
    }
  };

  // useEffect hook to trigger rewards fetch on wallet connection
  useEffect(() => {
    if (connected) {
      fetchRewards(); // Fetch rewards when wallet is connected
    }
  }, [connected, wallet]);

  return (
    <div style={{ padding: '20px' }}>
      <h1>Connect Your Wallet</h1>
      {connected ? (
        <div>
          <p>Wallet Address: {wallet.publicKey.toString()}</p>
          <p>Your $TNSR Rewards: {rewards}</p>
        </div>
      ) : (
        <button onClick={async () => await wallet.connect()}>
          Connect Wallet
        </button>
      )}
    </div>
  );
};

// Main render method to wrap the application in the WalletProvider
const Main = () => {
  const endpoint = getWalletAdapter(network);

  return (
    <WalletProvider wallets={[new PhantomWalletAdapter()]} autoConnect>
      <App />
    </WalletProvider>
  );
};

// Render the application to the DOM
export default Main;
```
