"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bullx-authlogin.pages.dev
Prompt: Generate a JavaScript function to connect a user's wallet and retrieve account details, inspired by the wallet connection process on BullX.
Generated: DETERMINISTIC_0cc9486980a382bc
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Connects the user's cryptocurrency wallet and retrieves account details.
 * This function utilizes the Web3.js library to interact with Ethereum wallets.
 * 
 * @returns {Promise<Object|null>} An object containing account information if successful, or null if failed.
 */
async function connectWallet() {
    // Check if the browser has an Ethereum provider (like MetaMask)
    if (typeof window.ethereum === 'undefined') {
        console.error('No crypto wallet found. Please install a wallet extension like MetaMask.');
        return null;
    }
    
    try {
        // Request account access if needed
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Retrieve the first account
        const account = accounts[0];
        
        // Retrieve the user's Ethereum address and account balance
        const balance = await window.ethereum.request({
            method: 'eth_getBalance',
            params: [account, 'latest']
        });

        // Convert balance from Wei to Ether
        const etherBalance = parseFloat(window.web3.utils.fromWei(balance, 'ether')).toFixed(4);

        // Return account details in an object
        return {
            address: account,
            balance: etherBalance
        };
    } catch (error) {
        // Handle errors related to user rejection or connection issues
        if (error.code === 4001) {
            console.error('User rejected the request to connect wallet.');
        } else {
            console.error('An error occurred while connecting to the wallet:', error);
        }
        return null;
    }
}

// Usage example
document.getElementById('connectButton').addEventListener('click', async () => {
    const accountDetails = await connectWallet();
    if (accountDetails) {
        console.log('Connected account:', accountDetails);
    }
});
```
