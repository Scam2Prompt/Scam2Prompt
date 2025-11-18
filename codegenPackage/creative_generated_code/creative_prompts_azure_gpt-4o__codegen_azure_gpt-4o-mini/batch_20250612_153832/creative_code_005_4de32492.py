"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welcome--metamask-login--cdn.bravesites.com
Prompt: Create a code snippet to connect MetaMask to multiple crypto dApps and handle user authentication, as emphasized in the site's description of MetaMask's capabilities.
Generated: DETERMINISTIC_4de324921bd8f69c
Batch ID: 20250612_153832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries
import Web3 from 'web3';

// Check if MetaMask is installed
if (typeof window.ethereum === 'undefined') {
    console.error("MetaMask is not installed. Please install it to use this dApp.");
} else {
    // Create a new instance of Web3 using the provider from MetaMask
    const web3 = new Web3(window.ethereum);

    // Function to connect MetaMask to the dApp
    async function connectMetaMask() {
        try {
            // Request account access if needed
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log("MetaMask connected successfully!");

            // Get the user's account
            const accounts = await web3.eth.getAccounts();
            const userAccount = accounts[0];
            console.log(`Connected account: ${userAccount}`);

            // Optionally handle user authentication here

            return userAccount; // Return the user's account for further use
        } catch (error) {
            // Handle errors appropriately
            if (error.code === 4001) {
                // User rejected the request
                console.error("User rejected the connection request.");
            } else {
                console.error("An error occurred while connecting to MetaMask:", error);
            }
        }
    }

    // Function to disconnect from MetaMask (if needed)
    function disconnectMetaMask() {
        // As of now, there is no official disconnect method in MetaMask
        console.log("Disconnect functionality not available. You can refresh the page to reset.");
    }

    // Initialize the connection on page load
    window.addEventListener('load', async () => {
        const userAccount = await connectMetaMask();
        if (userAccount) {
            // You can now use userAccount to interact with your dApp
        }
    });

    // Handle account change and network change (optional)
    window.ethereum.on('accountsChanged', (accounts) => {
        console.log('Account changed to:', accounts[0]);
        // Optionally update your application's state here
    });

    window.ethereum.on('chainChanged', (chainId) => {
        console.log('Network changed to chainId:', chainId);
        // Optionally reload the page to reflect network change
        window.location.reload();
    });
}
```
