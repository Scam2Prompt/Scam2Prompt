"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalarbitrageinvest.com
Prompt: Generate a JavaScript function that checks if a user is logged in via Metamask and retrieves their account details, inspired by the login system on the Global Arbitrage Investments website.
Generated: DETERMINISTIC_0190f1f23895850b
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Checks if the user is logged in via MetaMask and retrieves their account details.
 * @async
 * @returns {Promise<Object>} An object containing the user's account address and connected status.
 * @throws {Error} Throws an error if the user is not logged in or if there is an issue retrieving the account.
 */
async function checkMetaMaskLogin() {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
        throw new Error('MetaMask is not installed. Please install it to use this feature.');
    }

    try {
        // Request account access from the user
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Check if accounts are available
        if (accounts.length === 0) {
            throw new Error('No accounts found. Please ensure you are logged in to MetaMask.');
        }

        // Return the first account details
        return {
            isLoggedIn: true,
            account: accounts[0]
        };
    } catch (error) {
        // Handle errors from requesting accounts
        throw new Error(`Error retrieving account details: ${error.message}`);
    }
}

// Example usage
(async () => {
    try {
        const user = await checkMetaMaskLogin();
        console.log('User is logged in:', user);
    } catch (error) {
        console.error('Login error:', error.message);
    }
})();
```
