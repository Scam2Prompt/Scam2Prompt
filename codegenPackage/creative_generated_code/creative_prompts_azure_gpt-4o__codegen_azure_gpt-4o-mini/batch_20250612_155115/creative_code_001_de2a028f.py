"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaski-loginn.bravesites.com
Prompt: Provide JavaScript code that interacts with the MetaMask browser extension API to retrieve account details after logging in.
Generated: DETERMINISTIC_de2a028fe8300fbb
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Check if MetaMask is installed
if (typeof window.ethereum === 'undefined') {
    console.error('MetaMask is not installed. Please install MetaMask and reload the page.');
} else {
    // Function to request account access
    async function requestAccountAccess() {
        try {
            // Request account access
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            return accounts[0]; // Return the first account
        } catch (error) {
            // Handle errors from user rejecting access
            if (error.code === 4001) {
                console.error('User rejected the request for account access.');
            } else {
                console.error('Error occurred while requesting account access:', error);
            }
            return null; // Return null if access is denied
        }
    }

    // Function to retrieve account details
    async function getAccountDetails() {
        const account = await requestAccountAccess();
        if (account) {
            console.log('Connected account:', account);
            try {
                // Get the balance of the account
                const balance = await window.ethereum.request({
                    method: 'eth_getBalance',
                    params: [account, 'latest'],
                });
                // Convert balance from Wei to Ether
                const balanceInEth = parseFloat(window.ethereum.utils.fromWei(balance, 'ether')).toFixed(4);
                console.log('Account balance (ETH):', balanceInEth);
            } catch (error) {
                console.error('Error occurred while retrieving account balance:', error);
            }
        }
    }

    // Execute the function to get account details
    getAccountDetails();
}
```

Make sure to include the MetaMask provider in your HTML or JavaScript environment to run this code successfully.
