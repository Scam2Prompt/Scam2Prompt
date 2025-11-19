"""
Generated Code Metadata:
========================
Original URL: https://rplanet-io.vercel.app
Prompt: Create a JavaScript code snippet to integrate a Coinbase Wallet app with a dapp like R-Planet, enabling users to connect with their self-custody wallet and interact with the game's NFT marketplace.
Generated: DETERMINISTIC_e721bd672e973f6a
Batch ID: 20250622_205112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import { CoinbaseWallet } from '@web3-react/coinbase-wallet';
import { initializeConnector } from '@web3-react/core';
import { URLS } from './chains';

// Initialize Coinbase Wallet connector
const [coinbaseWallet, hooks] = initializeConnector(
  (actions) =>
    new CoinbaseWallet({
      actions,
      options: {
        url: URLS[1][0], // Mainnet Ethereum RPC URL
        appName: 'R-Planet',
      },
    })
);

const { useChainId, useAccounts, useIsActivating, useIsActive, useProvider, useENSNames } = hooks;

// Wallet connection component
export const WalletConnector = () => {
  const chainId = useChainId();
  const accounts = useAccounts();
  const isActivating = useIsActivating();
  const isActive = useIsActive();
  const provider = useProvider();
  const ENSNames = useENSNames(provider);

  // Handle connection
  const connect = async () => {
    try {
      await coinbaseWallet.activate();
    } catch (error) {
      console.error('Error connecting to Coinbase Wallet:', error);
    }
  };

  // Handle disconnection
  const disconnect = async () => {
    try {
      if (coinbaseWallet?.deactivate) {
        await coinbaseWallet.deactivate();
      } else {
        await coinbaseWallet.resetState();
      }
    } catch (error) {
      console.error('Error disconnecting from Coinbase Wallet:', error);
    }
  };

  // NFT Marketplace interaction example
  const interactWithMarketplace = async (nftContractAddress, tokenId, action) => {
    if (!isActive || !provider) {
      console.error('Wallet not connected');
      return;
    }

    try {
      // Example: Implement your NFT marketplace interaction logic here
      // This would typically involve contract calls using ethers.js or web3.js
      console.log(`Performing ${action} on NFT ${tokenId} from contract ${nftContractAddress}`);
      
      // Placeholder for actual contract interaction
      // const contract = new ethers.Contract(nftContractAddress, abi, provider.getSigner());
      // const tx = await contract[action](tokenId, { from: accounts[0] });
      // await tx.wait();
      
      console.log(`${action} completed successfully`);
    } catch (error) {
      console.error(`Error during ${action}:`, error);
    }
  };

  return {
    connect,
    disconnect,
    interactWithMarketplace,
    chainId,
    accounts,
    isActivating,
    isActive,
    provider,
    ENSNames
  };
};

// Example usage:
// const wallet = WalletConnector();
// wallet.connect();
// wallet.interactWithMarketplace('0x...', 123, 'buy');
```
