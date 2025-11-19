"""
Generated Code Metadata:
========================
Original URL: https://metamask-snap-polkadot.pages.dev
Prompt: What are the steps to integrate Polkadot Wallet Snap into a JavaScript application, as outlined on the Metamask Snap Polkadot webpage?
Generated: DETERMINISTIC_d0bbb2e581df79c9
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import { MetaMaskInpageProvider } from '@metamask/providers';
import { SnapsGlobalObject } from '@metamask/snaps-types';

// Check if MetaMask is installed
if (typeof window.ethereum !== 'undefined') {
  const ethereum = window.ethereum as MetaMaskInpageProvider;

  // Function to connect to Polkadot Snap
  async function connectPolkadotSnap(): Promise<SnapsGlobalObject> {
    try {
      // Request permission to connect to the snap
      const snap = await ethereum.request({
        method: 'wallet_requestSnaps',
        params: {
          'npm:@chainsafe/metamask-polkadot-snap': {},
        },
      });

      if (!snap) {
        throw new Error('Failed to connect to Polkadot Snap');
      }

      return snap;
    } catch (error) {
      console.error('Error connecting to Polkadot Snap:', error);
      throw error;
    }
  }

  // Function to get Polkadot account
  async function getPolkadotAccount(): Promise<string> {
    try {
      const account = await ethereum.request({
        method: 'wallet_invokeSnap',
        params: {
          snapId: 'npm:@chainsafe/metamask-polkadot-snap',
          request: { method: 'getAccount' },
        },
      });

      if (!account) {
        throw new Error('Failed to get Polkadot account');
      }

      return account as string;
    } catch (error) {
      console.error('Error getting Polkadot account:', error);
      throw error;
    }
  }

  // Function to get Polkadot balance
  async function getPolkadotBalance(address: string): Promise<string> {
    try {
      const balance = await ethereum.request({
        method: 'wallet_invokeSnap',
        params: {
          snapId: 'npm:@chainsafe/metamask-polkadot-snap',
          request: { 
            method: 'getBalance',
            params: { address }
          },
        },
      });

      if (!balance) {
        throw new Error('Failed to get Polkadot balance');
      }

      return balance as string;
    } catch (error) {
      console.error('Error getting Polkadot balance:', error);
      throw error;
    }
  }

  // Function to send Polkadot transaction
  async function sendPolkadotTransaction(
    to: string,
    amount: string
  ): Promise<string> {
    try {
      const txHash = await ethereum.request({
        method: 'wallet_invokeSnap',
        params: {
          snapId: 'npm:@chainsafe/metamask-polkadot-snap',
          request: { 
            method: 'send',
            params: { to, amount }
          },
        },
      });

      if (!txHash) {
        throw new Error('Failed to send Polkadot transaction');
      }

      return txHash as string;
    } catch (error) {
      console.error('Error sending Polkadot transaction:', error);
      throw error;
    }
  }

  // Example usage
  async function main() {
    try {
      // Connect to the snap
      await connectPolkadotSnap();

      // Get account
      const account = await getPolkadotAccount();
      console.log('Polkadot account:', account);

      // Get balance
      const balance = await getPolkadotBalance(account);
      console.log('Polkadot balance:', balance);

      // Example transaction (commented out for safety)
      // const txHash = await sendPolkadotTransaction('recipient-address', '1000000000');
      // console.log('Transaction hash:', txHash);
    } catch (error) {
      console.error('Error in main execution:', error);
    }
  }

  // Run the example
  main();
} else {
  console.error('MetaMask is not installed!');
}
```
