"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eng-metamask-cdn.teachable.com
Prompt: What are the best practices for using Metamask in a decentralized application (dApp) to ensure user security?
Generated: DETERMINISTIC_66f2287ddc5e8306
Batch ID: 20250612_155737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Best Practices for Using MetaMask in a dApp to Ensure User Security
 * This code demonstrates how to interact with MetaMask securely in a dApp.
 * It includes best practices such as detecting MetaMask, requesting permissions,
 * and handling errors appropriately.
 */

// Importing ethers.js (or web3.js as an alternative)
import { ethers } from 'ethers';

/**
 * Initialize MetaMask connection and return the provider and signer.
 * @returns {Promise<{provider: ethers.providers.Web3Provider, signer: ethers.Signer}>}
 */
async function initializeMetaMask() {
    try {
        // Check if MetaMask is installed
        if (!window.ethereum) {
            throw new Error('MetaMask is not installed. Please install MetaMask to use this dApp.');
        }

        // Request account access from MetaMask
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Create a provider instance
        const provider = new ethers.providers.Web3Provider(window.ethereum);

        // Get the connected wallet signer (current account)
        const signer = provider.getSigner();

        // Return the provider and signer for further interactions
        return { provider, signer };
    } catch (error) {
        // Log and rethrow the error for handling in the calling function
        console.error('Error initializing MetaMask:', error.message);
        throw error;
    }
}

/**
 * Get the currently connected MetaMask account address.
 * @param {ethers.providers.Web3Provider} provider - The Ethereum provider instance.
 * @returns {Promise<string>} - The connected account address.
 */
async function getConnectedAccount(provider) {
    try {
        // Get the list of connected accounts
        const accounts = await provider.listAccounts();

        // Ensure there is at least one connected account
        if (accounts.length === 0) {
            throw new Error('No accounts connected. Please connect your wallet using MetaMask.');
        }

        // Return the first account (default behavior)
        return accounts[0];
    } catch (error) {
        console.error('Error fetching connected account:', error.message);
        throw error;
    }
}

/**
 * Subscribe to MetaMask events (e.g., account changes, network changes).
 * @param {function} onAccountChange - Callback triggered when accounts change.
 * @param {function} onNetworkChange - Callback triggered when the network changes.
 */
function subscribeToMetaMaskEvents(onAccountChange, onNetworkChange) {
    try {
        // Detect account changes
        window.ethereum.on('accountsChanged', (accounts) => {
            console.log('MetaMask accounts changed:', accounts);
            if (onAccountChange) {
                onAccountChange(accounts);
            }
        });

        // Detect network changes
        window.ethereum.on('chainChanged', (chainId) => {
            console.log('MetaMask chain changed:', chainId);
            if (onNetworkChange) {
                onNetworkChange(chainId);
            }
        });
    } catch (error) {
        console.error('Error subscribing to MetaMask events:', error.message);
    }
}

/**
 * Disconnect MetaMask by resetting subscriptions and application state.
 */
function disconnectMetaMask() {
    try {
        // Clear subscriptions
        window.ethereum.removeAllListeners('accountsChanged');
        window.ethereum.removeAllListeners('chainChanged');
        console.log('MetaMask disconnected and subscriptions cleared.');
    } catch (error) {
        console.error('Error disconnecting MetaMask:', error.message);
    }
}

// Example usage
(async () => {
    try {
        const { provider, signer } = await initializeMetaMask();
        console.log('MetaMask initialized:', { provider, signer });

        const account = await getConnectedAccount(provider);
        console.log('Connected account:', account);

        // Subscribe to MetaMask events
        subscribeToMetaMaskEvents(
            (accounts) => console.log('Account changed:', accounts),
            (chainId) => console.log('Network changed:', chainId)
        );

        // Perform other dApp operations securely

        // Disconnect MetaMask when done
        disconnectMetaMask();
    } catch (error) {
        console.error('Error in dApp initialization:', error.message);
    }
})();
```
