"""
Generated Code Metadata:
========================
Original URL: https://frognation.farm
Prompt: Generate a JavaScript code snippet to detect wallet connection status and display a "Loading..." message until the wallet is successfully connected, as seen on frognation.farm.
Generated: DETERMINISTIC_7751f8085d1b74d9
Batch ID: 20250612_145117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checks wallet connection status and displays a loading message until connected.
 * @param {Object} wallet - The wallet object (e.g., from Web3Modal, WalletConnect, etc.)
 * @param {HTMLElement} loadingElement - The DOM element to show loading status
 * @param {HTMLElement} connectedElement - The DOM element to show when connected
 */
async function checkWalletConnection(wallet, loadingElement, connectedElement) {
    try {
        // Show loading state initially
        loadingElement.style.display = 'block';
        connectedElement.style.display = 'none';

        // Check if wallet is already connected
        if (wallet && wallet.isConnected()) {
            await handleConnectedState();
            return;
        }

        // If not connected, attempt to connect
        if (wallet && typeof wallet.connect === 'function') {
            await wallet.connect();
            await handleConnectedState();
            return;
        }

        // If no wallet connection possible
        throw new Error('Wallet connection not available');

    } catch (error) {
        console.error('Wallet connection error:', error);
        loadingElement.textContent = 'Connection failed. Please try again.';
        // Optionally add retry button or other UI elements here
    }

    async function handleConnectedState() {
        // Get account address
        const accounts = await wallet.getAccounts();
        if (!accounts || accounts.length === 0) {
            throw new Error('No accounts found');
        }

        // Update UI
        loadingElement.style.display = 'none';
        connectedElement.style.display = 'block';
        connectedElement.textContent = `Connected: ${shortenAddress(accounts[0])}`;
    }

    function shortenAddress(address, chars = 4) {
        return `${address.substring(0, chars + 2)}...${address.substring(address.length - chars)}`;
    }
}

// Example usage:
// document.addEventListener('DOMContentLoaded', () => {
//     const loadingEl = document.getElementById('loading-status');
//     const connectedEl = document.getElementById('connected-status');
//     checkWalletConnection(window.ethereum, loadingEl, connectedEl);
// });
```
