"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connect-metamask-web3.vercel.app
Prompt: Suggest best practices for handling blockchain wallet connections securely in a Next.js application using MetaMask.
Generated: DETERMINISTIC_7dec68f9f7b7b3d2
Batch ID: 20250612_150052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// pages/index.js
import { useState, useEffect } from 'react';

// Best practices: 
// 1. Use environment variables to store sensitive information.
// 2. Validate wallet connection securely.
// 3. Handle errors gracefully.
// 4. Avoid exposing private keys or sensitive data on the frontend.

// React functional component
export default function Home() {
  const [account, setAccount] = useState(null); // State to store the connected wallet address
  const [error, setError] = useState(null); // State to store connection errors
  
  // Function to connect to MetaMask wallet
  const connectWallet = async () => {
    try {
      // Check if MetaMask is installed
      if (!window.ethereum) {
        throw new Error('MetaMask is not installed. Please install it to use this application.');
      }

      // Request wallet connection
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

      // Set connected account
      setAccount(accounts[0]);
      setError(null); // Clear any previous errors
    } catch (err) {
      // Handle errors during wallet connection
      setError(err.message);
      console.error('Error connecting to MetaMask:', err);
    }
  };

  // Function to disconnect wallet (optional, if desired functionality)
  const disconnectWallet = () => {
    setAccount(null); // Clear the connected account
    setError(null); // Clear any errors
  };

  // Effect to fetch account on mount (optional, based on app requirements)
  useEffect(() => {
    const checkConnection = async () => {
      try {
        if (window.ethereum) {
          const accounts = await window.ethereum.request({ method: 'eth_accounts' });
          if (accounts.length > 0) {
            setAccount(accounts[0]);
          }
        }
      } catch (err) {
        console.error('Error checking wallet connection:', err);
      }
    };

    checkConnection();
  }, []);

  return (
    <div>
      <h1>Blockchain Wallet Connection</h1>
      {/* Display connected account or connection UI */}
      {account ? (
        <div>
          <p>Connected Account: {account}</p>
          <button onClick={disconnectWallet}>Disconnect Wallet</button>
        </div>
      ) : (
        <div>
          <button onClick={connectWallet}>Connect Wallet</button>
          {error && <p style={{ color: 'red' }}>Error: {error}</p>}
        </div>
      )}
    </div>
  );
}
```
