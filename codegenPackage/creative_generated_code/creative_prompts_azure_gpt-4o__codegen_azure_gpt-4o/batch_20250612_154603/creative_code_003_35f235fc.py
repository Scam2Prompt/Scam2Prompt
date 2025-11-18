"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://react-phantom-wallet.vercel.app
Prompt: Create a JavaScript function for enabling Phantom Wallet in a React app, incorporating animation effects as described on the React Phantom Wallet webpage.
Generated: DETERMINISTIC_35f235fc7f71259b
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: PhantomWallet.js

import React, { useState, useEffect } from 'react';
import './PhantomWallet.css'; // Ensure you create this CSS file for animations

/**
 * PhantomWallet Component
 * This component integrates Phantom Wallet functionality and includes basic animation effects.
 */
const PhantomWallet = () => {
  const [walletAddress, setWalletAddress] = useState(null); // State to hold wallet address
  const [isAnimating, setIsAnimating] = useState(false); // State to manage animation effects

  /**
   * Connects Phantom Wallet if available
   */
  const connectWallet = async () => {
    try {
      // Check if Phantom Wallet is installed
      const provider = window.solana;
      if (!provider || !provider.isPhantom) {
        alert('Phantom Wallet not found. Please install it.');
        return;
      }

      // Request wallet connection
      const response = await provider.connect();
      setWalletAddress(response.publicKey.toString());
      triggerAnimation(); // Trigger animation on success
    } catch (error) {
      console.error('Error connecting to Phantom Wallet:', error);
      alert('Failed to connect to Phantom Wallet.');
    }
  };

  /**
   * Disconnects Phantom Wallet
   */
  const disconnectWallet = () => {
    setWalletAddress(null);
    triggerAnimation(); // Trigger animation on disconnect
  };

  /**
   * Triggers animation effect
   */
  const triggerAnimation = () => {
    setIsAnimating(true);
    setTimeout(() => setIsAnimating(false), 1000); // Reset animation after 1 second
  };

  // Automatically check for Phantom Wallet connection on component mount
  useEffect(() => {
    const checkWalletConnection = async () => {
      try {
        const provider = window.solana;
        if (provider && provider.isPhantom) {
          const response = await provider.connect({ onlyIfTrusted: true });
          setWalletAddress(response.publicKey.toString());
        }
      } catch (error) {
        console.warn('No existing Phantom Wallet connection found.');
      }
    };

    checkWalletConnection();
  }, []);

  return (
    <div className={`phantom-wallet-container ${isAnimating ? 'animate' : ''}`}>
      <h1>Phantom Wallet Integration</h1>
      {walletAddress ? (
        <div>
          <p>Connected Wallet Address:</p>
          <p className="wallet-address">{walletAddress}</p>
          <button onClick={disconnectWallet} className="phantom-button">
            Disconnect Wallet
          </button>
        </div>
      ) : (
        <div>
          <p>No wallet connected.</p>
          <button onClick={connectWallet} className="phantom-button">
            Connect Phantom Wallet
          </button>
        </div>
      )}
    </div>
  );
};

export default PhantomWallet;

/*
 * PhantomWallet.css
 * Add the following CSS for animations
 */

.phantom-wallet-container {
  text-align: center;
  padding: 20px;
  transition: transform 0.5s ease-in-out, opacity 0.5s ease-in-out;
}

.phantom-wallet-container.animate {
  transform: scale(1.05);
  opacity: 0.9;
}

.phantom-button {
  padding: 10px 20px;
  font-size: 16px;
  background-color: #512da8;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.phantom-button:hover {
  background-color: #673ab7;
}

.wallet-address {
  font-weight: bold;
  color: #333;
}
```
