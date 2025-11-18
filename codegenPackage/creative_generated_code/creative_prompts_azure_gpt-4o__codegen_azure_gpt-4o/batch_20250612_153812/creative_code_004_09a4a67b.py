"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welcome-metamask-cdnn.bravesites.com
Prompt: Create a script to display a custom menu for MetaMask wallet interactions, referencing the Siteblocks builder mentioned on the webpage.
Generated: DETERMINISTIC_09a4a67bc6d678b3
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required dependencies
import Web3 from 'web3'; // Web3.js library for interacting with Ethereum blockchain

// Ensure the code only runs once the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
        alert('MetaMask is not installed. Please install it to use the wallet functionalities.');
        return;
    }

    // Initialize Web3 instance using MetaMask's provider
    const web3 = new Web3(window.ethereum);

    // Create a function to display the custom menu
    const createMetaMaskMenu = () => {
        // Create menu container
        const menuContainer = document.createElement('div');
        menuContainer.id = 'metaMaskMenu';
        menuContainer.style.border = '1px solid #ccc';
        menuContainer.style.padding = '20px';
        menuContainer.style.margin = '20px';
        menuContainer.style.borderRadius = '10px';
        menuContainer.style.boxShadow = '0px 4px 6px rgba(0, 0, 0, 0.1)';
        menuContainer.style.backgroundColor = '#f9f9f9';

        // Create menu title
        const menuTitle = document.createElement('h3');
        menuTitle.innerText = 'MetaMask Wallet Menu';
        menuTitle.style.textAlign = 'center';
        menuContainer.appendChild(menuTitle);

        // Connect Wallet Button
        const connectButton = document.createElement('button');
        connectButton.innerText = 'Connect Wallet';
        connectButton.style.margin = '10px';
        connectButton.style.padding = '10px 20px';
        connectButton.style.border = 'none';
        connectButton.style.borderRadius = '5px';
        connectButton.style.cursor = 'pointer';
        connectButton.style.backgroundColor = '#007bff';
        connectButton.style.color = '#fff';

        // Add click event to the connect button
        connectButton.addEventListener('click', async () => {
            try {
                // Connect to MetaMask and request account access
                const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
                alert(`Wallet connected: ${accounts[0]}`);
            } catch (error) {
                alert(`Error connecting to wallet: ${error.message}`);
            }
        });

        menuContainer.appendChild(connectButton);

        // Display Account Button
        const accountButton = document.createElement('button');
        accountButton.innerText = 'Get Account Info';
        accountButton.style.margin = '10px';
        accountButton.style.padding = '10px 20px';
        accountButton.style.border = 'none';
        accountButton.style.borderRadius = '5px';
        accountButton.style.cursor = 'pointer';
        accountButton.style.backgroundColor = '#28a745';
        accountButton.style.color = '#fff';

        // Add click event to the account button
        accountButton.addEventListener('click', async () => {
            try {
                const accounts = await web3.eth.getAccounts();
                if (accounts.length === 0) {
                    alert('No accounts found. Please connect your MetaMask wallet.');
                } else {
                    alert(`Connected Account: ${accounts[0]}`);
                }
            } catch (error) {
                alert(`Error fetching account info: ${error.message}`);
            }
        });

        menuContainer.appendChild(accountButton);

        // Inject menu into the webpage
        document.body.appendChild(menuContainer);
    };

    // Call the function to display the menu
    createMetaMaskMenu();
});
```
