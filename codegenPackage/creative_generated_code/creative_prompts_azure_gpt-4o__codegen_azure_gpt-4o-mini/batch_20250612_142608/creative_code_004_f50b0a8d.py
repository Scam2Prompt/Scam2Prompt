"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wap.xushuishiwu.cn
Prompt: Write code to implement multi-wallet switching functionality using the MetaMask wallet API, as described in the "MetaMask多前钱包" section.
Generated: DETERMINISTIC_f50b0a8d7f3d27d3
Batch ID: 20250612_142608
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary library for Ethereum interaction
import Web3 from 'web3';

// Initialize a global web3 instance
let web3;

// Function to connect to the MetaMask wallet
async function connectWallet() {
    if (typeof window.ethereum !== 'undefined') {
        try {
            // Request account access from the user
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            // Create a new web3 instance with the provider from MetaMask
            web3 = new Web3(window.ethereum);
            console.log("Wallet connected successfully!");
        } catch (error) {
            console.error("User denied account access or connection failed:", error);
        }
    } else {
        console.error("MetaMask is not installed. Please install it to use this app.");
    }
}

// Function to switch wallets (accounts)
async function switchWallet(accountIndex) {
    if (!web3) {
        console.error("Wallet is not connected. Please connect first.");
        return;
    }

    try {
        // Get the list of accounts from MetaMask
        const accounts = await window.ethereum.request({ method: 'eth_accounts' });
        
        // Check if the specified index is valid
        if (accountIndex < 0 || accountIndex >= accounts.length) {
            console.error("Invalid account index. Please select a valid account.");
            return;
        }

        // Set the selected account
        const selectedAccount = accounts[accountIndex];
        console.log("Switched to account:", selectedAccount);
        
        // You can now perform actions with the selected account
        // Example: Fetching the account balance
        const balance = await web3.eth.getBalance(selectedAccount);
        console.log("Account balance:", web3.utils.fromWei(balance, 'ether'), "ETH");

    } catch (error) {
        console.error("Failed to switch wallet:", error);
    }
}

// Event listener for account change
window.ethereum.on('accountsChanged', (accounts) => {
    if (accounts.length === 0) {
        console.warn("Please connect to MetaMask.");
    } else {
        console.log("Account changed:", accounts[0]);
    }
});

// Example usage
(async () => {
    await connectWallet();
    await switchWallet(0); // Switch to the first account
})();
```
