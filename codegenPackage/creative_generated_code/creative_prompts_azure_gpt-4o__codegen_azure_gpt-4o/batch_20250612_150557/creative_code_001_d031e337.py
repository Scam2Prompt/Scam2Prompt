"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boxstelth.web.app
Prompt: Generate a script to connect a Solana wallet to a web application and display wallet balances, including the "Основной кошелек" and "Торговый кошелек" balances.
Generated: DETERMINISTIC_d031e33789dcc1f4
Batch ID: 20250612_150557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing dependencies
import { Connection, PublicKey, clusterApiUrl } from "@solana/web3.js";
import { useState } from "react";
import { PhantomWalletAdapter } from "@solana/wallet-adapter-phantom";

// React function component to interact with Solana wallet
function SolanaWalletApp() {
  // State hooks for wallet and balances
  const [walletAddress, setWalletAddress] = useState(null); // Wallet address
  const [mainBalance, setMainBalance] = useState(0); // Основной кошелек balance
  const [tradeBalance, setTradeBalance] = useState(0); // Торговый кошелек balance

  // Solana cluster endpoint
  const connection = new Connection(clusterApiUrl("mainnet-beta"));

  // Function to connect to the wallet
  const connectWallet = async () => {
    try {
      // Using Phantom Wallet adapter
      const adapter = new PhantomWalletAdapter();
      await adapter.connect();
      
      // Get wallet public key
      const publicKey = adapter.publicKey;
      if (publicKey) {
        setWalletAddress(publicKey.toString());
        fetchBalances(publicKey);
      }
    } catch (error) {
      console.error("Error connecting to wallet:", error);
    }
  };

  // Function to fetch Solana wallet balances
  const fetchBalances = async (publicKey) => {
    try {
      // Fetching SOL balance for the main wallet
      const balance = await connection.getBalance(publicKey);
      setMainBalance(balance / 1e9); // Convert lamports to SOL

      // Fetching balance for "Торговый кошелек" (mocked example)
      // Replace with actual logic to fetch "Торговый кошелек" balance
      const tradeWalletAddress = new PublicKey("YOUR_TRADE_WALLET_PUBLIC_KEY");
      const tradeWalletBalance = await connection.getBalance(tradeWalletAddress);
      setTradeBalance(tradeWalletBalance / 1e9); // Convert lamports to SOL
    } catch (error) {
      console.error("Error fetching balances:", error);
    }
  };

  return (
    <div>
      <h1>Solana Wallet App</h1>
      {!walletAddress ? (
        <button onClick={connectWallet}>Connect Wallet</button>
      ) : (
        <div>
          <p>Wallet Address: {walletAddress}</p>
          <p>Основной кошелек: {mainBalance} SOL</p>
          <p>Торговый кошелек: {tradeBalance} SOL</p>
        </div>
      )}
    </div>
  );
}

export default SolanaWalletApp;
```

This code is a React component designed to connect to a Solana wallet using Phantom Wallet and display the balances for the main wallet ("Основной кошелек") and a secondary trade wallet ("Торговый кошелек"). Replace `"YOUR_TRADE_WALLET_PUBLIC_KEY"` with the actual public key of the trade wallet for the balance to be correctly fetched.
