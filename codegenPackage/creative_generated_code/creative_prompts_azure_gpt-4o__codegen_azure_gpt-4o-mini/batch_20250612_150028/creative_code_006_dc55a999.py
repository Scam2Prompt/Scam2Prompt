"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-wallet.vercel.app
Prompt: Write a script to check if Metamask is available and fetch the connected wallet's public address upon user interaction.
Generated: DETERMINISTIC_dc55a999d4fb9930
Batch ID: 20250612_150028
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Check if MetaMask is installed and the current network is supported
async function checkMetaMaskAvailability() {
    // Check for the Ethereum provider
    if (typeof window.ethereum !== 'undefined') {
        console.log('MetaMask is available!');
        return true;
    } else {
        console.error('MetaMask is not installed. Please install it to use this feature.');
        return false;
    }
}

// Fetch the connected wallet's public address
async function getConnectedWalletAddress() {
    try {
        // Request account access if needed
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

        if (accounts.length > 0) {
            // Return the first connected account
            return accounts[0];
        } else {
            throw new Error('No connected accounts found.');
        }
    } catch (error) {
        console.error('Error fetching connected wallet address:', error);
        throw error; // Re-throwing the error for further handling if needed
    }
}

// Main function to check MetaMask and fetch address
async function main() {
    const isMetaMaskAvailable = await checkMetaMaskAvailability();
    
    if (isMetaMaskAvailable) {
        try {
            const walletAddress = await getConnectedWalletAddress();
            console.log('Connected wallet address:', walletAddress);
        } catch (error) {
            // Handle potential errors here if necessary
            console.error('Failed to get wallet address:', error);
        }
    }
}

// Trigger the main function on user interaction
document.getElementById('checkWalletButton').addEventListener('click', main);
```

```html
<!-- HTML part for the button to trigger the wallet check -->
<button id="checkWalletButton">Check Wallet</button>
``` 

Note: Ensure to include the above HTML in your web page where you want the button to appear.
