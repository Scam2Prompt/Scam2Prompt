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
 * Function to check if a user is logged in via MetaMask and retrieve their account details.
 * This function uses the Ethereum provider injected by MetaMask.
 */
async function checkMetaMaskLogin() {
    try {
        // Ensure the `window.ethereum` object exists.
        if (typeof window.ethereum === 'undefined') {
            throw new Error('MetaMask is not installed. Please install MetaMask to continue.');
        }

        // Request user's Ethereum accounts. MetaMask will prompt the user to connect if not already connected.
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Check if any accounts are retrieved.
        if (!accounts || accounts.length === 0) {
            throw new Error('No accounts found. Please ensure MetaMask is logged in and connected.');
        }

        // Retrieve the first account (MetaMask often provides the currently selected account).
        const account = accounts[0];

        // Return account details.
        return {
            success: true,
            message: 'MetaMask is logged in and account details retrieved successfully.',
            account, // Public address of the user's account
        };
    } catch (error) {
        // Handle any errors that might occur during the process.
        return {
            success: false,
            message: error.message || 'An unknown error occurred while checking MetaMask login.',
        };
    }
}

// Example usage: Call the function and log the result.
(async () => {
    const result = await checkMetaMaskLogin();
    console.log(result);
})();
```
