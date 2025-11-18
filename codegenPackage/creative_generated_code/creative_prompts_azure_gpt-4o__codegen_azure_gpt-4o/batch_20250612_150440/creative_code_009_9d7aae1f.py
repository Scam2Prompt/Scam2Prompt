"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-snap-polkadot.pages.dev
Prompt: Write a script to enable JavaScript functionality for interacting with the Polkadot Wallet Snap in a web application.
Generated: DETERMINISTIC_9d7aae1fb5c19b60
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// polkadotWallet.js

// Check if the browser has MetaMask installed and its Ethereum provider enabled
async function isMetaMaskInstalled() {
    return typeof window.ethereum !== 'undefined';
}

// Request connection to MetaMask
async function connectToMetaMask() {
    try {
        // Request wallet permissions
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('Connected account:', accounts[0]);
        return accounts[0];
    } catch (error) {
        console.error('Failed to connect to MetaMask:', error);
        throw new Error('MetaMask connection failed');
    }
}

// Enable the Polkadot Wallet Snap
async function enablePolkadotSnap() {
    try {
        const snapId = 'npm:@chainsafe/metamask-polkadot-snap'; // Polkadot Snap identifier

        // Request MetaMask to enable the snap
        const result = await window.ethereum.request({
            method: 'wallet_enable',
            params: [
                {
                    wallet_snap: {
                        [snapId]: {}, // Snap configuration
                    },
                },
            ],
        });

        console.log('Polkadot Snap enabled:', result);
        return result;
    } catch (error) {
        console.error('Failed to enable Polkadot Snap:', error);
        throw new Error('Polkadot Snap enablement failed');
    }
}

// Invoke a JSON-RPC method on the Polkadot Snap
async function interactWithPolkadotSnap(method, params = {}) {
    try {
        const snapId = 'npm:@chainsafe/metamask-polkadot-snap'; // Polkadot Snap identifier

        // Request MetaMask to invoke the snap's method
        const result = await window.ethereum.request({
            method: 'wallet_invokeSnap',
            params: {
                snapId: snapId,
                request: {
                    method: method,
                    params: params,
                },
            },
        });

        console.log(`Response from ${method}:`, result);
        return result;
    } catch (error) {
        console.error(`Failed to invoke method "${method}" on Polkadot Snap:`, error);
        throw new Error(`Error invoking ${method} on Polkadot Snap`);
    }
}

// Example usage of the Polkadot Snap script
async function main() {
    if (!(await isMetaMaskInstalled())) {
        console.error('MetaMask is not installed. Please install MetaMask extension.');
        return;
    }

    try {
        // Connect to MetaMask
        const account = await connectToMetaMask();

        // Enable the Polkadot Snap
        await enablePolkadotSnap();

        // Example: Fetch balance using Polkadot Snap
        const balance = await interactWithPolkadotSnap('polkadot_getBalance', {
            address: account,
        });

        console.log('Account Balance:', balance);
    } catch (error) {
        console.error('Error interacting with Polkadot Snap:', error);
    }
}

// Trigger the script execution when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    main();
});
```
