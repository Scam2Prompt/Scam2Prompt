"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.sewakamerabandung.id
Prompt: What are the key features of the MetaMask API for integrating cryptocurrency wallets into web applications?
Generated: DETERMINISTIC_192a2db33fbb3bf9
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * MetaMask Integration Example
 * This code demonstrates how to interact with the MetaMask API
 * to connect a user's wallet and fetch the user's account balance.
 */

(async () => {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
        console.error('MetaMask is not installed. Please install it to use this feature.');
        return;
    }

    // Request account access if necessary
    const requestAccountAccess = async () => {
        try {
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            return accounts[0]; // Return the first account
        } catch (error) {
            console.error('Failed to connect to MetaMask:', error);
        }
    };

    // Get the user's account balance
    const getAccountBalance = async (account) => {
        try {
            const balance = await window.ethereum.request({
                method: 'eth_getBalance',
                params: [account, 'latest'],
            });
            // Convert balance from Wei to Ether
            return parseFloat(window.ethereum.utils.fromWei(balance, 'ether')).toFixed(4);
        } catch (error) {
            console.error('Failed to fetch account balance:', error);
        }
    };

    // Main function to execute MetaMask integration
    const main = async () => {
        const account = await requestAccountAccess();
        if (account) {
            console.log('Connected account:', account);
            const balance = await getAccountBalance(account);
            console.log('Account balance:', balance, 'ETH');
        }
    };

    // Execute the main function
    main();
})();
```
