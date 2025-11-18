"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magic.link
Prompt: Write code using Magic Labs' API to integrate embedded wallets into a web application for seamless onchain transactions.
Generated: DETERMINISTIC_c04300d16064b021
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules and libraries
import { Magic } from 'magic-sdk';
import Web3 from 'web3';

// Configure Magic Labs API and Web3
const magic = new Magic('YOUR_MAGIC_API_KEY'); // Replace with your Magic API key
const web3 = new Web3(magic.rpcProvider);

// Function to initialize the embedded wallet
async function initializeWallet() {
  try {
    // Check if the user is already logged in
    const isLoggedIn = await magic.user.isLoggedIn();

    if (isLoggedIn) {
      console.log("User is already logged in.");
      return await magic.user.getMetadata(); // Get wallet metadata
    } else {
      // Log in the user
      const email = prompt("Enter your email to log in:");
      await magic.auth.loginWithMagicLink({ email });
      console.log("Login successful.");
      return await magic.user.getMetadata(); // Get wallet metadata
    }
  } catch (error) {
    console.error("Error initializing wallet:", error);
    throw new Error("Failed to initialize wallet.");
  }
}

// Function to send an onchain transaction
async function sendTransaction(receiverAddress, amountInEther) {
  try {
    // Get the user's wallet address
    const userMetadata = await magic.user.getMetadata();
    const senderAddress = userMetadata.publicAddress;

    if (!senderAddress) {
      throw new Error("Sender address not found.");
    }

    // Build the transaction object
    const transaction = {
      from: senderAddress,
      to: receiverAddress,
      value: web3.utils.toWei(amountInEther.toString(), 'ether'),
      gas: 21000, // Standard gas limit for a simple transaction
    };

    // Send the transaction
    const txHash = await web3.eth.sendTransaction(transaction);
    console.log("Transaction successful. Hash:", txHash);

    return txHash;
  } catch (error) {
    console.error("Error sending transaction:", error);
    throw new Error("Transaction failed.");
  }
}

// Function to log out the user
async function logout() {
  try {
    await magic.user.logout();
    console.log("User logged out successfully.");
  } catch (error) {
    console.error("Error logging out:", error);
    throw new Error("Failed to log out.");
  }
}

// Example usage (replace with actual application logic)
(async function main() {
  try {
    const userMetadata = await initializeWallet();
    console.log("Wallet initialized. User metadata:", userMetadata);

    // Prompt user for transaction details
    const receiverAddress = prompt("Enter the recipient's wallet address:");
    const amount = parseFloat(prompt("Enter the amount to send (in ETH):"));

    // Send the transaction
    const transactionHash = await sendTransaction(receiverAddress, amount);
    console.log("Transaction completed. Hash:", transactionHash);

    // Log out the user (optional)
    await logout();
  } catch (error) {
    console.error("Application error:", error);
  }
})();
```

### Key Points:
- Replace `'YOUR_MAGIC_API_KEY'` with your actual Magic Labs API key.
- Ensure the `Magic` and `Web3` libraries are installed in your project (`npm install magic-sdk web3`).
- Use proper environment variables to manage sensitive data like API keys in production.
- Add stricter validation for user inputs in production scenarios.
