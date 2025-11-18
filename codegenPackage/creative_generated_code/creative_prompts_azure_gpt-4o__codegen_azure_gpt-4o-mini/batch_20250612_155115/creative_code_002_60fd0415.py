"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aerodrome-finac.xyz
Prompt: Create a function in JavaScript that uses `window.ethereum.request` to fetch the balance of the connected Ethereum account and display it in Ether format, similar to the `checkBalanceButton` functionality.
Generated: DETERMINISTIC_60fd04151f0dbdda
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Fetches the balance of the connected Ethereum account and displays it in Ether format.
 * Assumes that the Ethereum provider is injected in the window (e.g., MetaMask).
 */
async function checkBalance() {
    try {
        // Check if the Ethereum provider is available
        if (typeof window.ethereum !== 'undefined') {
            // Request the user's accounts
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            
            // Ensure the user has at least one account connected
            if (accounts.length === 0) {
                throw new Error("No connected accounts found.");
            }

            const account = accounts[0];

            // Fetch the balance of the account in Wei
            const balanceWei = await window.ethereum.request({
                method: 'eth_getBalance',
                params: [account, 'latest']
            });

            // Convert the balance from Wei to Ether
            const balanceEther = parseFloat(balanceWei) / Math.pow(10, 18);

            // Display the balance in Ether format
            console.log(`Balance of account ${account}: ${balanceEther} ETH`);
        } else {
            throw new Error("Ethereum provider is not available. Please install MetaMask.");
        }
    } catch (error) {
        // Handle errors gracefully
        console.error("Error fetching balance:", error.message);
    }
}

// Example usage: Call checkBalance when a button is clicked
document.getElementById('checkBalanceButton').addEventListener('click', checkBalance);
```
