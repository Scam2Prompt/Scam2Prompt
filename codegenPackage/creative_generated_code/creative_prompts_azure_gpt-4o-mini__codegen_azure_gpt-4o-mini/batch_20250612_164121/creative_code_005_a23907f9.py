"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xushuishiwu.cn
Prompt: Create a JavaScript function that connects to the MetaMask wallet and retrieves the user's Ethereum balance.
Generated: DETERMINISTIC_a23907f9f75c6bab
Batch ID: 20250612_164121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Connect to MetaMask wallet and retrieve the user's Ethereum balance.
 * @async
 * @function getEthereumBalance
 * @returns {Promise<string>} The user's Ethereum balance in Ether.
 * @throws {Error} Throws an error if the connection or balance retrieval fails.
 */
async function getEthereumBalance() {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
        throw new Error("MetaMask is not installed. Please install it to use this feature.");
    }

    // Request account access from the user
    await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Get the user's account address
    const accounts = await window.ethereum.request({ method: 'eth_accounts' });
    const account = accounts[0];

    if (!account) {
        throw new Error("No account found. Please connect to MetaMask.");
    }

    try {
        // Retrieve the user's balance in Wei
        const balanceInWei = await window.ethereum.request({
            method: 'eth_getBalance',
            params: [account, 'latest']
        });

        // Convert Wei to Ether (1 Ether = 10^18 Wei)
        const balanceInEther = parseFloat(balanceInWei) / 1e18;

        // Return the balance formatted to 18 decimal points
        return balanceInEther.toFixed(18);
    } catch (error) {
        throw new Error(`Failed to retrieve balance: ${error.message}`);
    }
}

// Example usage
getEthereumBalance()
    .then(balance => console.log(`Your Ethereum balance is: ${balance} ETH`))
    .catch(error => console.error(`Error: ${error.message}`));
```
