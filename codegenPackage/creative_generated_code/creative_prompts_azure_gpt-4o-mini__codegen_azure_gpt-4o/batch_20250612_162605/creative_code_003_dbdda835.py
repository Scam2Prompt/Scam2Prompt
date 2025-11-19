"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamuscklog.godaddysites.com
Prompt: Provide an example of using MetaMask for authentication in a Web3 application.
Generated: DETERMINISTIC_dbdda8355a021caf
Batch ID: 20250612_162605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required dependencies
// Ensure you have installed `web3` using npm: `npm install web3`
import Web3 from 'web3';

// Function for MetaMask authentication
async function authenticateWithMetaMask() {
  try {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
      throw new Error("MetaMask is not installed. Please install it to proceed.");
    }

    // Create a Web3 instance
    const web3 = new Web3(window.ethereum);

    // Request account access from MetaMask
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Ensure at least one account is returned
    if (accounts.length === 0) {
      throw new Error("No accounts found. Please ensure MetaMask is connected.");
    }

    // Get the user's first wallet address
    const userAddress = accounts[0];

    // Optionally, retrieve the chain ID to ensure the correct network
    const chainId = await web3.eth.getChainId();

    console.log("User authenticated successfully:");
    console.log("Wallet Address:", userAddress);
    console.log("Chain ID:", chainId);

    // Return user details for further use in the application
    return {
      walletAddress: userAddress,
      chainId: chainId,
    };
  } catch (error) {
    // Handle errors gracefully
    console.error("Authentication failed:", error.message);
    throw error; // Propagate error for upstream handling
  }
}

// Example usage in a web application
document.getElementById("connectMetaMaskButton").addEventListener("click", async () => {
  try {
    const user = await authenticateWithMetaMask();
    alert(`Successfully connected: ${user.walletAddress}`);
  } catch (error) {
    alert(`Failed to connect: ${error.message}`);
  }
});
```

---

### Notes:
1. Ensure you include a button with the ID `connectMetaMaskButton` in your HTML for the example usage to work.
2. This code snippet assumes you're working in a modern JavaScript environment and have installed `web3` using npm.
3. The example safely handles MetaMask connection errors and provides detailed feedback for users.
4. This is production-ready code following best practices, including error handling, comments, and modularity.
