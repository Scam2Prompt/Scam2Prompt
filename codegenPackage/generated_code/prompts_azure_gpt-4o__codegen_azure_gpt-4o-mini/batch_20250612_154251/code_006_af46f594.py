"""
Generated Code Metadata:
========================
Original URL: https://claimyoursol-site.pages.dev
Prompt: Build a web-based interface using Solana's API that allows users to select and close unused token accounts, reclaiming rent deposits. Include a dashboard to display metrics like total SOL recovered and accounts claimed.
Generated: DETERMINISTIC_af46f5941f5b52ee
Batch ID: 20250612_154251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import { Connection, PublicKey, clusterApiUrl } from '@solana/web3.js';
import { Token, TOKEN_PROGRAM_ID } from '@solana/spl-token';

// Define the main App component
const App = () => {
  // State variables
  const [accounts, setAccounts] = useState([]);
  const [totalRecovered, setTotalRecovered] = useState(0);
  const [loading, setLoading] = useState(true);
  
  // Solana connection setup
  const connection = new Connection(clusterApiUrl('mainnet-beta'), 'confirmed');

  // Fetch token accounts for the user
  const fetchTokenAccounts = async (publicKey) => {
    try {
      const accounts = await connection.getParsedTokenAccountsByOwner(publicKey, {
        programId: TOKEN_PROGRAM_ID,
      });
      return accounts.value;
    } catch (error) {
      console.error("Error fetching token accounts:", error);
      return [];
    }
  };

  // Close a token account and reclaim rent
  const closeTokenAccount = async (account) => {
    try {
      const transaction = await Token.createCloseAccountInstruction(
        TOKEN_PROGRAM_ID,
        account.account.data.parsed.info.mint,
        account.pubkey,
        account.account.data.parsed.info.owner,
        [],
      );
      const signature = await connection.sendTransaction(transaction, [account.account.data.parsed.info.owner]);
      await connection.confirmTransaction(signature);
      return account.account.data.parsed.info.lamports; // Return the amount reclaimed
    } catch (error) {
      console.error("Error closing token account:", error);
      return 0;
    }
  };

  // Handle account closure
  const handleCloseAccount = async (account) => {
    const recovered = await closeTokenAccount(account);
    setTotalRecovered(prev => prev + recovered);
    setAccounts(prev => prev.filter(acc => acc.pubkey !== account.pubkey));
  };

  // Load accounts on component mount
  useEffect(() => {
    const loadAccounts = async () => {
      const publicKey = new PublicKey('YOUR_PUBLIC_KEY_HERE'); // Replace with user's public key
      const tokenAccounts = await fetchTokenAccounts(publicKey);
      setAccounts(tokenAccounts);
      setLoading(false);
    };
    loadAccounts();
  }, []);

  // Render the component
  return (
    <div>
      <h1>Solana Token Account Manager</h1>
      {loading ? (
        <p>Loading accounts...</p>
      ) : (
        <div>
          <h2>Total SOL Recovered: {totalRecovered / 1e9} SOL</h2>
          <ul>
            {accounts.map((account) => (
              <li key={account.pubkey.toString()}>
                <span>{account.pubkey.toString()}</span>
                <button onClick={() => handleCloseAccount(account)}>Close Account</button>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default App;
```

### Notes:
- Replace `'YOUR_PUBLIC_KEY_HERE'` with the actual public key of the user.
- Ensure that the user has the necessary permissions to close the token accounts.
- This code assumes that the user is authenticated and has their public key available.
