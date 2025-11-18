"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-react-meutas5kc-uniswap.vercel.app
Prompt: Generate a React hook using Web3-React to detect wallet disconnection events and prompt users to reconnect their Gnosis Safe wallet.
Generated: DETERMINISTIC_0c676b1ff4bff548
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// useWalletDisconnect.js
import { useEffect, useState } from 'react';
import { useWeb3React } from '@web3-react/core';

/**
 * Custom React hook to detect wallet disconnection events
 * and prompt users to reconnect their Gnosis Safe wallet.
 *
 * @returns {object} reconnectWallet - Function to manually reconnect the wallet
 */
const useWalletDisconnect = () => {
  const { active, deactivate, connector, account, activate } = useWeb3React();
  const [isDisconnected, setIsDisconnected] = useState(false);

  // Function to reconnect wallet (e.g., Gnosis Safe)
  const reconnectWallet = async () => {
    try {
      setIsDisconnected(false); // Reset disconnection state
      if (connector) {
        await activate(connector); // Attempt to reconnect
      }
    } catch (error) {
      console.error('Error reconnecting wallet:', error);
    }
  };

  useEffect(() => {
    // Listener for when the wallet disconnects
    const handleDisconnect = () => {
      console.warn('Wallet disconnected');
      setIsDisconnected(true); // Mark wallet as disconnected
    };

    if (connector && connector.on) {
      connector.on('Web3ReactDeactivate', handleDisconnect); // Subscribe to disconnect events
    }

    // Cleanup listener on component unmount
    return () => {
      if (connector && connector.off) {
        connector.off('Web3ReactDeactivate', handleDisconnect);
      }
    };
  }, [connector]);

  useEffect(() => {
    // Auto-detect if the wallet is disconnected
    if (!active && account === null) {
      setIsDisconnected(true);
    }
  }, [active, account]);

  // Return reconnect function and disconnection state
  return { isDisconnected, reconnectWallet };
};

export default useWalletDisconnect;
```
