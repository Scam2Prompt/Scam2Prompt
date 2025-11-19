"""
Generated Code Metadata:
========================
Original URL: https://web3-react-meutas5kc-uniswap.vercel.app
Prompt: Write a JavaScript function using Web3-React to check if a wallet is connected and retrieve the currently selected blockchain network (e.g., Optimism Mainnet or Celo Alfajores).
Generated: DETERMINISTIC_89b873d30f0fda8a
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useEffect, useState } from 'react';
import { useWeb3React } from '@web3-react/core';
import { UnsupportedChainIdError } from '@web3-react/core';

const useWalletStatus = () => {
  const { active, account, library, chainId, error } = useWeb3React();
  const [network, setNetwork] = useState(null);
  const [errorMessage, setErrorMessage] = useState(null);

  useEffect(() => {
    // Check if the wallet is connected
    if (active) {
      // Retrieve the current blockchain network
      const getNetworkName = async () => {
        try {
          const networkName = await library.getNetwork();
          setNetwork(networkName.name);
        } catch (err) {
          console.error('Error fetching network:', err);
          setErrorMessage('Failed to retrieve network information.');
        }
      };

      getNetworkName();
    } else {
      setNetwork(null);
    }
  }, [active, library]);

  // Handle unsupported chain errors
  useEffect(() => {
    if (error instanceof UnsupportedChainIdError) {
      setErrorMessage('Unsupported network. Please connect to a supported chain.');
    } else if (error) {
      setErrorMessage('An error occurred while connecting to the wallet.');
    } else {
      setErrorMessage(null);
    }
  }, [error]);

  return { active, account, network, errorMessage };
};

const WalletStatus = () => {
  const { active, account, network, errorMessage } = useWalletStatus();

  return (
    <div>
      {errorMessage && <p style={{ color: 'red' }}>{errorMessage}</p>}
      {active ? (
        <div>
          <p>Wallet connected: {account}</p>
          <p>Current network: {network}</p>
        </div>
      ) : (
        <p>No wallet connected.</p>
      )}
    </div>
  );
};

export default WalletStatus;
```
