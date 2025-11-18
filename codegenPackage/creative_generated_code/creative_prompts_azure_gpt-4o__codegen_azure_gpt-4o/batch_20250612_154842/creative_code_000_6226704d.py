"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom-phi.vercel.app
Prompt: Write code to integrate the Phantom wallet connection feature into a Solana-based web application using the Phantom Connect API.
Generated: DETERMINISTIC_6226704de70058ae
Batch ID: 20250612_154842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required dependencies
import React, { useState, useEffect } from 'react';

// Define the Phantom wallet integration component
const PhantomWalletIntegration = () => {
  // State to track the connection status and wallet public key
  const [walletConnected, setWalletConnected] = useState(false);
  const [publicKey, setPublicKey] = useState(null);

  /**
   * Check if Phantom wallet is installed in the browser
   * @returns {boolean} True if Phantom is installed, otherwise false
   */
  const isPhantomInstalled = () => {
    return window.solana && window.solana.isPhantom;
  };

  /**
   * Connect to the Phantom wallet
   * Sets the public key and updates the connection state
   */
  const connectWallet = async () => {
    try {
      if (!isPhantomInstalled()) {
        alert('Phantom wallet is not installed. Please install it to continue.');
        return;
      }

      // Request connection to the wallet
      const response = await window.solana.connect();
      setWalletConnected(true);
      setPublicKey(response.publicKey.toString());
    } catch (error) {
      console.error('Error connecting to Phantom wallet:', error);
      alert('Failed to connect to the wallet. Please try again.');
    }
  };

  /**
   * Disconnect from the Phantom wallet
   * Resets the connection state and public key
   */
  const disconnectWallet = async () => {
    try {
      await window.solana.disconnect();
      setWalletConnected(false);
      setPublicKey(null);
    } catch (error) {
      console.error('Error disconnecting from Phantom wallet:', error);
      alert('Failed to disconnect from the wallet. Please try again.');
    }
  };

  // Effect to check Phantom wallet installation on component mount
  useEffect(() => {
    if (!isPhantomInstalled()) {
      console.warn('Phantom wallet is not installed in this browser.');
    }
  }, []);

  // Render the wallet connection UI
  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>Phantom Wallet Integration</h1>
      {walletConnected ? (
        <div>
          <p><strong>Connected Wallet Public Key:</strong> {publicKey}</p>
          <button onClick={disconnectWallet} style={{ cursor: 'pointer' }}>
            Disconnect Wallet
          </button>
        </div>
      ) : (
        <div>
          <p>Phantom wallet is {isPhantomInstalled() ? 'installed' : 'not installed'}.</p>
          <button onClick={connectWallet} style={{ cursor: 'pointer' }}>
            Connect Wallet
          </button>
        </div>
      )}
    </div>
  );
};

// Export the component for use in the application
export default PhantomWalletIntegration;
```
