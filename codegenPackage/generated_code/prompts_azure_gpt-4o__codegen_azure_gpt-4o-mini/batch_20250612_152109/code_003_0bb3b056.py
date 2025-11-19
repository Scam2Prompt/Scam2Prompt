"""
Generated Code Metadata:
========================
Original URL: https://sale-humanizedai.web.app
Prompt: Create a React component for a "Connect Wallet" button that interacts with MetaMask, inspired by the wallet connection feature on the HumanizedAi presale site.
Generated: DETERMINISTIC_0bb3b0566f234273
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';

// Define the ConnectWalletButton component
const ConnectWalletButton = () => {
  // State to manage the connected account and loading status
  const [account, setAccount] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Function to connect to MetaMask
  const connectWallet = async () => {
    setLoading(true);
    setError(null);

    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
      setError('MetaMask is not installed. Please install it to use this feature.');
      setLoading(false);
      return;
    }

    try {
      // Request account access
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      // Set the first account as the connected account
      setAccount(accounts[0]);
    } catch (err) {
      // Handle errors during account connection
      setError('Failed to connect to MetaMask. Please try again.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  // Effect to handle account changes
  useEffect(() => {
    const handleAccountsChanged = (accounts) => {
      if (accounts.length > 0) {
        setAccount(accounts[0]);
      } else {
        setAccount(null);
      }
    };

    // Listen for account changes
    window.ethereum.on('accountsChanged', handleAccountsChanged);

    // Cleanup listener on component unmount
    return () => {
      window.ethereum.removeListener('accountsChanged', handleAccountsChanged);
    };
  }, []);

  return (
    <div>
      {error && <div className="error">{error}</div>}
      {account ? (
        <div className="connected">
          Connected: {account}
        </div>
      ) : (
        <button onClick={connectWallet} disabled={loading}>
          {loading ? 'Connecting...' : 'Connect Wallet'}
        </button>
      )}
    </div>
  );
};

export default ConnectWalletButton;
```
