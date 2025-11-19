"""
Generated Code Metadata:
========================
Original URL: https://web3modal-laboratory-qix0wwvm2-walletconnect1.vercel.app
Prompt: Write code using the Wagmi library to implement "Sign in with Ethereum" (SIWE) functionality, as described in the Web3Modal documentation.
Generated: DETERMINISTIC_317f2084c0d8d513
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import { createClient, getDefaultProvider } from 'wagmi';
import { MetaMaskConnector } from 'wagmi/connectors/metaMask';
import { CoinbaseWalletConnector } from 'wagmi/connectors/coinbaseWallet';
import { getSiweMessage, SiweMessage } from '@siwe-js/siwe';

// Initialize Wagmi client
const client = createClient({
  autoConnect: true,
  provider: getDefaultProvider(),
  connectors: [
    new MetaMaskConnector(),
    new CoinbaseWalletConnector({
      options: {
        appName: 'My App',
      },
    }),
  ],
});

// Function to handle SIWE message
async function handleSiweMessage(
  address: string,
  message: SiweMessage,
  signature: string
) {
  try {
    // Verify the SIWE message
    const isValid = await getSiweMessage().verify({
      address,
      message,
      signature,
    });

    if (!isValid) {
      throw new Error('Invalid SIWE signature');
    }

    // Handle successful verification
    console.log('SIWE verification successful');
    // Add your logic here to authenticate the user
  } catch (error) {
    console.error('Error verifying SIWE signature:', error);
  }
}

// Function to initiate SIWE flow
async function signInWithEthereum() {
  try {
    // Get the user's Ethereum address
    const accounts = await client.getAccounts();
    const address = accounts[0];

    if (!address) {
      throw new Error('User is not connected');
    }

    // Create a SIWE message
    const message = new SiweMessage({
      domain: window.location.host,
      address,
      statement: 'Sign in with Ethereum to the app.',
      uri: window.location.href,
      version: '1',
      chainId: '0x1', // Mainnet
      nonce: Math.random().toString(36).substr(2, 10),
    });

    // Get the user's signature
    const signature = await client.signMessage({
      message: message.prepareMessage(),
    });

    // Handle the SIWE message
    await handleSiweMessage(address, message, signature);
  } catch (error) {
    console.error('Error signing in with Ethereum:', error);
  }
}

// Export the signInWithEthereum function
export default signInWithEthereum;
```
