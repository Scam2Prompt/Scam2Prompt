"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-metamask.vercel.app
Prompt: Provide an example of how to use MetaMask's API to sign a message for authentication purposes in a Web3 application.
Generated: DETERMINISTIC_fcea33315cddec35
Batch ID: 20250612_150052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary Web3 library
import Web3 from 'web3';

// Check if MetaMask is installed
if (typeof window.ethereum === 'undefined') {
    console.error("MetaMask is not installed. Please install it to use this application.");
}

// Create a new instance of Web3 using the MetaMask provider
const web3 = new Web3(window.ethereum);

// Function to request MetaMask account connection
async function connectMetaMask() {
    try {
        // Request account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log("Connected account:", accounts[0]);
        return accounts[0];
    } catch (error) {
        console.error("User denied account access or other error:", error);
    }
}

// Function to sign a message with MetaMask
async function signMessage(account, message) {
    try {
        // Sign the message using the connected account
        const signature = await web3.eth.personal.sign(message, account);
        console.log("Signature:", signature);
        return signature;
    } catch (error) {
        console.error("Error signing message:", error);
    }
}

// Main function to demonstrate signing a message
async function main() {
    const message = "Authenticate me with this message!";
    
    // Connect to MetaMask and get the user's account
    const account = await connectMetaMask();
    if (account) {
        // Sign the message
        const signature = await signMessage(account, message);

        // Here, you could send the signature to your server for verification
        // Example: await sendSignatureToServer(account, message, signature);
    }
}

// Execute the main function
main();
```
