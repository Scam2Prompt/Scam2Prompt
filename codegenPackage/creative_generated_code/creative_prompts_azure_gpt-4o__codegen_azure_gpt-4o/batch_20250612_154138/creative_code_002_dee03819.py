"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mmamask-us.godaddysites.com
Prompt: Create a React component for a Metamask login button that checks if the Metamask extension is installed and prompts the user to connect their wallet.
Generated: DETERMINISTIC_dee038191661fc41
Batch ID: 20250612_154138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React, { useState } from 'react';

// MetamaskLoginButton Component
const MetamaskLoginButton = () => {
  const [isMetamaskInstalled, setIsMetamaskInstalled] = useState(false);
  const [walletAddress, setWalletAddress] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  // Check if MetaMask is installed
  const checkMetamaskInstallation = () => {
    if (typeof window.ethereum !== 'undefined' && window.ethereum.isMetaMask) {
      setIsMetamaskInstalled(true);
    } else {
      setIsMetamaskInstalled(false);
    }
  };

  // Connect to MetaMask wallet
  const connectWallet = async () => {
    try {
      if (!isMetamaskInstalled) {
        throw new Error('MetaMask is not installed.');
      }

      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      setWalletAddress(accounts[0]);
      setErrorMessage('');
    } catch (error) {
      setErrorMessage(error.message);
    }
  };

  // Effect: Check MetaMask installation on component mount
  React.useEffect(() => {
    checkMetamaskInstallation();
  }, []);

  return (
    <div style={{ textAlign: 'center', margin: '20px' }}>
      {/* Button to Connect Wallet */}
      <button
        onClick={connectWallet}
        disabled={!isMetamaskInstalled}
        style={{
          padding: '10px 20px',
          fontSize: '16px',
          backgroundColor: isMetamaskInstalled ? '#f6851b' : '#ccc',
          color: '#fff',
          border: 'none',
          borderRadius: '5px',
          cursor: isMetamaskInstalled ? 'pointer' : 'not-allowed',
        }}
      >
        {walletAddress ? 'Connected' : 'Connect to MetaMask'}
      </button>

      {/* Display wallet address or error message */}
      <div style={{ marginTop: '10px', fontSize: '14px', color: walletAddress ? 'green' : 'red' }}>
        {walletAddress && <p>Wallet Address: {walletAddress}</p>}
        {errorMessage && <p>Error: {errorMessage}</p>}
      </div>

      {/* Message if MetaMask is not installed */}
      {!isMetamaskInstalled && (
        <p style={{ marginTop: '10px', fontSize: '14px', color: 'red' }}>
          MetaMask is not installed. Please install the extension to use this feature.
        </p>
      )}
    </div>
  );
};

export default MetamaskLoginButton;
```
