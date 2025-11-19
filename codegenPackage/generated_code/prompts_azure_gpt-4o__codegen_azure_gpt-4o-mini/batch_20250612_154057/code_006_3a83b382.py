"""
Generated Code Metadata:
========================
Original URL: https://banksy.farm
Prompt: Create a React component for a "Connect Wallet" button that integrates with Metamask, similar to the functionality on Banksy.farm.
Generated: DETERMINISTIC_3a83b382aec7ba70
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';

// ConnectWalletButton component for connecting to MetaMask
const ConnectWalletButton = () => {
  // State to manage wallet connection status and account
  const [isConnected, setIsConnected] = useState(false);
  const [account, setAccount] = useState('');

  // Function to connect to MetaMask
  const connectWallet = async () => {
    if (window.ethereum) {
      try {
        // Request account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        // Set the first account as the connected account
        setAccount(accounts[0]);
        setIsConnected(true);
      } catch (error) {
        console.error('Error connecting to wallet:', error);
        alert('Failed to connect to wallet. Please try again.');
      }
    } else {
      alert('MetaMask is not installed. Please install it to use this feature.');
    }
  };

  // Effect to check if wallet is already connected on component mount
  useEffect(() => {
    const checkWalletConnection = async () => {
      if (window.ethereum) {
        const accounts = await window.ethereum.request({ method: 'eth_accounts' });
        if (accounts.length > 0) {
          setAccount(accounts[0]);
          setIsConnected(true);
        }
      }
    };
    checkWalletConnection();
  }, []);

  return (
    <div>
      {isConnected ? (
        <button className="connected-button" disabled>
          Connected: {account.slice(0, 6)}...{account.slice(-4)}
        </button>
      ) : (
        <button className="connect-button" onClick={connectWallet}>
          Connect Wallet
        </button>
      )}
    </div>
  );
};

export default ConnectWalletButton;
```

### CSS (Optional)
```css
.connect-button {
  background-color: #f0c14b;
  border: 1px solid #a88734;
  color: #111;
  padding: 10px 20px;
  cursor: pointer;
  border-radius: 5px;
}

.connected-button {
  background-color: #4caf50;
  border: none;
  color: white;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: default;
}
```
