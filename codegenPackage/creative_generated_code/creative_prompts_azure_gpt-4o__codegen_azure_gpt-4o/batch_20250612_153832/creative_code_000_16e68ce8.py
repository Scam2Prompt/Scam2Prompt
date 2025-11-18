"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://public-metamask-com--cdn.bravesites.com
Prompt: Write code to integrate MetaMask login functionality into a decentralized application (dApp) built on Ethereum, ensuring secure authentication using cryptographic signatures.
Generated: DETERMINISTIC_16e68ce8e58017d5
Batch ID: 20250612_153832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from "web3";

// Initialize Web3 instance
let web3;

// Function to check if MetaMask is installed
const isMetaMaskInstalled = () => {
  return typeof window.ethereum !== "undefined" && window.ethereum.isMetaMask;
};

// Function to request account access and authenticate user
const authenticateUser = async () => {
  try {
    // Check if MetaMask is installed
    if (!isMetaMaskInstalled()) {
      throw new Error("MetaMask is not installed. Please install MetaMask to use this dApp.");
    }

    // Initialize Web3 instance with MetaMask provider
    web3 = new Web3(window.ethereum);

    // Request user's Ethereum account access
    const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
    const userAddress = accounts[0]; // Get the first account (default)

    // Generate a random challenge for the user to sign
    const challenge = `Login request for dApp at ${new Date().toISOString()}`;
    
    // Prompt the user to sign the challenge
    const signature = await web3.eth.personal.sign(challenge, userAddress, "");

    // Verify the signature on the backend (this would normally involve backend code)
    // For demonstrative purposes, we'll simulate verification here.
    const recoveredAddress = web3.eth.accounts.recover(challenge, signature);

    if (recoveredAddress.toLowerCase() !== userAddress.toLowerCase()) {
      throw new Error("Signature verification failed. Authentication unsuccessful.");
    }

    // If everything checks out, authentication is successful
    console.log("User authenticated successfully:", userAddress);

  } catch (error) {
    // Handle errors appropriately
    console.error("Error during MetaMask authentication:", error.message);
    alert(error.message);
  }
};

// Example usage: Trigger authentication on button click
document.getElementById("loginButton").addEventListener("click", () => {
  authenticateUser();
});

// Note: Ensure you have a button with id="loginButton" in your HTML file.
// Example:
// <button id="loginButton">Login with MetaMask</button>
```

Make sure to test this code in a browser-based environment that supports Ethereum (e.g., using MetaMask). You may also need to implement backend verification of the cryptographic signature for production-grade security.
