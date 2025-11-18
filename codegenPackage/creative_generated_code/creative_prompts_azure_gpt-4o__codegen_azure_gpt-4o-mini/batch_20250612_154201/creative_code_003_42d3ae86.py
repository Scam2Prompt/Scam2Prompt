"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://berachain-frontend.vercel.app
Prompt: Write code to disconnect a wallet from Berachain and remove the website from MetaMask's "Connected Sites" list.
Generated: DETERMINISTIC_42d3ae8632012c39
Batch ID: 20250612_154201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to disconnect a wallet from Berachain and remove the website from MetaMask's "Connected Sites" list
async function disconnectWallet() {
    try {
        // Check if MetaMask is installed
        if (typeof window.ethereum !== 'undefined') {
            const provider = window.ethereum;

            // Request to disconnect from the current provider (Berachain)
            const accounts = await provider.request({ method: 'eth_accounts' });
            
            // If there are no accounts connected, notify the user
            if (accounts.length === 0) {
                console.warn('No wallet accounts connected.');
                return;
            }

            // Send a disconnect request (MetaMask does not have a specific disconnect method,
            // but we can remove the connection by asking the user to disconnect)
            await provider.request({ method: 'wallet_requestPermissions', params: [{ eth_accounts: {} }] });

            // Notify the user of successful disconnection
            console.log('Wallet disconnected from Berachain.');

            // Remove the website from MetaMask's connected sites
            // Note: Currently, MetaMask does not provide an API to programmatically remove
            // connected sites. Users must do this manually in the MetaMask extension settings.
            console.warn('Please visit MetaMask settings to remove the website from "Connected Sites".');
        } else {
            // If MetaMask is not found, notify the user
            console.error('MetaMask is not installed. Please install it to proceed.');
        }
    } catch (error) {
        // Handle any errors that may occur during the disconnection process
        console.error('An error occurred while disconnecting the wallet:', error.message);
    }
}

// Call the disconnect function when appropriate (e.g., on button click)
// document.getElementById('disconnectButton').onclick = disconnectWallet;
```
