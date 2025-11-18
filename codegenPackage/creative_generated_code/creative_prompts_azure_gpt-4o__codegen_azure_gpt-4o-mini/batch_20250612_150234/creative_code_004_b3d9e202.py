"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethpai.com
Prompt: Provide an example of how to use the MetaMask API to allow users to pledge ETH directly from their wallets to a designated smart contract.
Generated: DETERMINISTIC_b3d9e202665f2083
Batch ID: 20250612_150234
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

// Define the smart contract address and ABI (Application Binary Interface)
const contractAddress = '0xYourSmartContractAddress'; // Replace with your smart contract address
const contractABI = [ /* Your smart contract ABI here */ ];

// Initialize Web3 with MetaMask provider
const web3 = new Web3(window.ethereum);

// Function to pledge ETH to the smart contract
async function pledgeETH(amount) {
    try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        
        // Get the user's accounts
        const accounts = await web3.eth.getAccounts();
        const sender = accounts[0]; // Get the first account

        // Convert the amount to wei (1 ETH = 10^18 wei)
        const amountInWei = web3.utils.toWei(amount.toString(), 'ether');

        // Create a contract instance
        const contract = new web3.eth.Contract(contractABI, contractAddress);

        // Send the transaction to the smart contract
        const transaction = await contract.methods.pledge().send({
            from: sender,
            value: amountInWei
        });

        console.log('Transaction successful:', transaction);
    } catch (error) {
        console.error('An error occurred while pledging ETH:', error);
        alert('Transaction failed. Please check the console for more details.');
    }
}

// Example usage: pledge 0.1 ETH
document.getElementById('pledgeButton').addEventListener('click', () => {
    const amount = 0.1; // Desired amount in ETH
    pledgeETH(amount);
});
```

```html
<!-- HTML structure for the pledge button -->
<button id="pledgeButton">Pledge 0.1 ETH</button>
```

```css
/* Optional CSS to style the button */
#pledgeButton {
    padding: 10px 20px;
    font-size: 16px;
    color: white;
    background-color: #007bff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

#pledgeButton:hover {
    background-color: #0056b3;
}
``` 

Make sure you replace `'0xYourSmartContractAddress'` and `/* Your smart contract ABI here */` with the actual smart contract address and ABI you intend to interact with.
