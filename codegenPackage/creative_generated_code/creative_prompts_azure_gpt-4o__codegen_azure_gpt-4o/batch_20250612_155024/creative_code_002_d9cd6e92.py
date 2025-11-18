"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jirasanf.top
Prompt: Create a function in JavaScript that triggers a MetaMask wallet connection and handles user prompts for acceptance or rejection.
Generated: DETERMINISTIC_d9cd6e922168370a
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Connect to MetaMask wallet
 * This function triggers the MetaMask connection process and handles the user's response.
 *
 * @returns {Promise<string>} A promise resolving to the user's wallet address if connected successfully.
 * @throws {Error} If an error occurs during the connection process or the user rejects the prompt.
 */
async function connectToMetaMask() {
  // Check if MetaMask is installed
  if (typeof window.ethereum === 'undefined') {
    throw new Error('MetaMask is not installed. Please install MetaMask to continue.');
  }

  try {
    // Request account access from MetaMask
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Ensure at least one account is returned
    if (accounts.length === 0) {
      throw new Error('No accounts found. Please ensure your MetaMask wallet has at least one account.');
    }

    // Return the first account (primary wallet address)
    return accounts[0];
  } catch (error) {
    // Handle errors and user rejection
    if (error.code === 4001) {
      throw new Error('User rejected the connection request.');
    }
    throw new Error(`An error occurred while connecting to MetaMask: ${error.message}`);
  }
}

// Example usage:
(async () => {
  try {
    const walletAddress = await connectToMetaMask();
    console.log('Connected wallet address:', walletAddress);
  } catch (error) {
    console.error(error.message);
  }
})();
```
