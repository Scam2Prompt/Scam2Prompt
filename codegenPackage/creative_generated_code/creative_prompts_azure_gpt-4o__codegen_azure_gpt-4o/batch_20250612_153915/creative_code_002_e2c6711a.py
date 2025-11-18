"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mymettamasklog.wordpress.com
Prompt: Write JavaScript code that interacts with the MetaMask browser extension API to retrieve wallet details using a seed phrase or private key, as described in the webpage.
Generated: DETERMINISTIC_e2c6711a61fd79cb
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Ensure this code runs in a secure and controlled environment.
// It is important to handle sensitive data such as seed phrases or private keys with utmost caution.
// Never expose sensitive information in client-side code or logs.

// Function to interact with MetaMask and fetch wallet details
async function getWalletDetails() {
  // Ensure MetaMask is installed
  if (typeof window.ethereum === 'undefined') {
    console.error('MetaMask is not installed. Please install it to proceed.');
    return;
  }

  try {
    // Request account access from MetaMask
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

    if (!accounts || accounts.length === 0) {
      throw new Error('No accounts found. Please ensure MetaMask is unlocked.');
    }

    const walletAddress = accounts[0]; // Get the first account (default account)

    // Fetch wallet balance
    const balance = await window.ethereum.request({
      method: 'eth_getBalance',
      params: [walletAddress, 'latest'], // Fetch latest balance
    });

    // Convert balance from Wei to Ether
    const etherBalance = parseFloat(balance) / Math.pow(10, 18);

    // Return wallet details
    const walletDetails = {
      address: walletAddress,
      balance: etherBalance.toFixed(4), // Rounded to 4 decimal places
    };

    console.log('Wallet Details:', walletDetails);
    return walletDetails;
  } catch (error) {
    console.error('Error fetching wallet details:', error.message);
  }
}

// Example usage
getWalletDetails();
```

**Important Note:**  
This code interacts with the MetaMask extension via the browser's `window.ethereum` object. However, there is **no mechanism** to retrieve wallet details directly from a seed phrase or private key using MetaMask's API in a standard, secure environment. Instead, users must import their private key into MetaMask directly (manually) to manage wallets securely.
