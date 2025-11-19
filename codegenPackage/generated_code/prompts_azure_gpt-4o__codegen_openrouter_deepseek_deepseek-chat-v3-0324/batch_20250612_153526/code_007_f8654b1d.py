"""
Generated Code Metadata:
========================
Original URL: https://anydurasup.pages.dev
Prompt: Provide an example of initializing a Web3 connection for a DApp that supports both WalletConnect and Coinbase Wallet, as discussed on the webpage.
Generated: DETERMINISTIC_f8654b1dca319bf2
Batch ID: 20250612_153526
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/logo.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://goerli.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import Web3 from 'web3';
import WalletConnectProvider from '@walletconnect/web3-provider';
import CoinbaseWalletSDK from '@coinbase/wallet-sdk';

// Initialize Web3 connection with WalletConnect and Coinbase Wallet support
export async function initWeb3() {
  try {
    // Check if Web3 is injected by MetaMask or other wallet
    if (window.ethereum) {
      const web3 = new Web3(window.ethereum);
      try {
        // Request account access
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        return web3;
      } catch (error) {
        console.error('User denied account access', error);
        throw new Error('User denied account access');
      }
    }
    
    // Initialize WalletConnect provider
    const walletConnectProvider = new WalletConnectProvider({
      rpc: {
        1: 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID',
        5: 'https://goerli.infura.io/v3/YOUR_INFURA_PROJECT_ID'
      }
    });

    // Initialize Coinbase Wallet provider
    const coinbaseWallet = new CoinbaseWalletSDK({
      appName: 'My DApp',
      appLogoUrl: 'https://example.com/logo.png',
      darkMode: false
    });
    const coinbaseProvider = coinbaseWallet.makeWeb3Provider(
      'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID',
      1
    );

    // Check which provider is available
    if (walletConnectProvider.connected) {
      await walletConnectProvider.enable();
      return new Web3(walletConnectProvider);
    } else if (coinbaseProvider) {
      await coinbaseProvider.enable();
      return new Web3(coinbaseProvider);
    } else {
      throw new Error('No Ethereum provider detected');
    }
  } catch (error) {
    console.error('Error initializing Web3:', error);
    throw error;
  }
}

// Example usage
// initWeb3()
//   .then(web3 => {
//     console.log('Web3 initialized successfully', web3);
//   })
//   .catch(error => {
//     console.error('Failed to initialize Web3', error);
//   });
```
