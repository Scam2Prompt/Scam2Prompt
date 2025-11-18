"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet-connect-v3.devpq.com
Prompt: Provide an example of connecting a dApp to a wallet using WalletConnect V3, referencing the PQ WalletConnect V3 implementation.
Generated: DETERMINISTIC_ea63771d0b752957
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and WalletConnect client
import { WalletConnectClient } from '@walletconnect/client';
import { Web3Provider } from '@walletconnect/web3-provider';

// Define constants for WalletConnect setup
const WALLETCONNECT_PROJECT_ID = '<YOUR_PROJECT_ID>'; // Specify your WalletConnect V3 Project ID
const RELAY_URL = 'wss://relay.walletconnect.com'; // WalletConnect relay server URL

// Initialize WalletConnect client
async function initializeWalletConnect() {
  try {
    // Create a new WalletConnect client instance
    const walletConnectClient = await WalletConnectClient.init({
      relayUrl: RELAY_URL,              // Relay server URL
      projectId: WALLETCONNECT_PROJECT_ID, // WalletConnect Project ID for authentication
    });

    return walletConnectClient;
  } catch (error) {
    console.error('Failed to initialize WalletConnect client:', error);
    throw new Error('WalletConnect initialization error');
  }
}

// Connect to a wallet using WalletConnect
async function connectToWallet(walletConnectClient) {
  try {
    // Define the required blockchain methods and chains
    const chains = ['eip155:1']; // Ethereum mainnet chain ID
    const methods = ['eth_sendTransaction', 'eth_signTransaction', 'personal_sign', 'eth_signTypedData'];

    // Generate a URI and request wallet connection
    const pairing = await walletConnectClient.connect({
      requiredNamespaces: {
        eip155: {
          chains,
          methods,
          events: ['accountsChanged', 'chainChanged'],
        },
      },
    });

    // Display the WalletConnect pairing URI (e.g., for QR Code)
    console.log('WalletConnect pairing URI:', pairing.uri);

    // Wait for wallet connection
    const session = await new Promise((resolve) => {
      walletConnectClient.on('session_update', (updatedSession) => {
        resolve(updatedSession);
      });
    });

    console.log('Wallet connected:', session);
    return session;
  } catch (error) {
    console.error('Failed to connect to wallet:', error);
    throw new Error('Wallet connection error');
  }
}

// Example usage
(async () => {
  try {
    // Initialize WalletConnect client
    const walletConnectClient = await initializeWalletConnect();

    // Connect to wallet
    const session = await connectToWallet(walletConnectClient);

    // Extract wallet information (e.g., accounts, chainId)
    const accounts = session.namespaces.eip155.accounts;
    const chainId = session.namespaces.eip155.chainId;

    console.log('Connected accounts:', accounts);
    console.log('Connected chain ID:', chainId);
  } catch (error) {
    console.error('Error in WalletConnect flow:', error);
  }
})();
```
