"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-audius.com
Prompt: Provide an example of how to implement security features like Wallet Guard using MetaMask.
Generated: DETERMINISTIC_e8aa0edf6dc3bccc
Batch ID: 20250612_163530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, well-documented implementation of a simplified Wallet Guard security feature using MetaMask:

```javascript
// Import dependencies
const ethers = require("ethers");

// Configuration
const provider = new ethers.providers.Web3Provider(window.ethereum);
const METAMASK_REQUIRED_MESSAGE = "MetaMask is required to use this feature.";
const SIGNATURE_WARNING_MESSAGE = "Signing requests should always be reviewed carefully!";
const WALLET_GUARD_MESSAGE = "Are you sure you trust this transaction?";

// Utility function to check MetaMask installation
function checkMetaMaskInstalled() {
  if (typeof window.ethereum === "undefined") {
    alert(METAMASK_REQUIRED_MESSAGE);
    throw new Error(METAMASK_REQUIRED_MESSAGE);
  }
}

// Connect wallet
async function connectWallet() {
  checkMetaMaskInstalled();
  try {
    const accounts = await provider.send("eth_requestAccounts", []);
    return accounts[0]; // Return the connected wallet address
  } catch (error) {
    console.error("Failed to connect wallet:", error.message);
    throw error;
  }
}

// Wallet Guard feature: Confirm transaction approval
async function walletGuardPrompt() {
  return new Promise((resolve) => {
    const userConfirmed = confirm(WALLET_GUARD_MESSAGE);
    resolve(userConfirmed);
  });
}

// Sign a message securely with Wallet Guard
async function signMessageSecurely(message) {
  checkMetaMaskInstalled();
  const walletAddress = await connectWallet();

  try {
    const signer = provider.getSigner();
    
    // Display warning message for user awareness
    alert(SIGNATURE_WARNING_MESSAGE);

    // Wallet Guard prompt
    const isConfirmed = await walletGuardPrompt();
    if (!isConfirmed) {
      throw new Error("User rejected the transaction.");
    }

    // Sign the message
    const signature = await signer.signMessage(message);

    console.log("Message signed successfully:", { message, signature, walletAddress });
    return { message, signature, walletAddress };
  } catch (error) {
    console.error("Failed to sign message securely:", error.message);
    throw error;
  }
}

// Example usage
(async () => {
  try {
    const message = "This is a test message to be signed.";
    const result = await signMessageSecurely(message);
    console.log("Signed message result:", result);
  } catch (error) {
    console.error("Error during signing process:", error.message);
  }
})();
```

### Key Features in the Code:

1. **Error Handling**:
   - Throws errors for critical failures such as MetaMask not being installed or user rejection of transaction.
   - Logs errors for debugging and production monitoring.

2. **Security Prompts**:
   - Alerts the user to read and confirm signing requests.
   - Uses a `confirm` dialog for user approval before signing.

3. **MetaMask Integration**:
   - Connects to MetaMask via the `ethers.js` library.
   - Leverages `signMessage` for secure signing.

Ensure MetaMask is installed and properly set up to test this code.
