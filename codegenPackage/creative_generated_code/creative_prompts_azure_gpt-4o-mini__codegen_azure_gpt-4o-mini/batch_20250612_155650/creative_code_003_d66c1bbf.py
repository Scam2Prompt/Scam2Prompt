"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://good-games-guild.gitbook.io
Prompt: Explain the token utility of $GGG in the Good Games ecosystem and provide a code snippet for integrating it into a WEB3 application.
Generated: DETERMINISTIC_d66c1bbfba226476
Batch ID: 20250612_155650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3';

// Define the Good Games ecosystem token address and ABI
const GGG_TOKEN_ADDRESS = '0xYourTokenAddressHere'; // Replace with actual token contract address
const GGG_TOKEN_ABI = [ /* ABI array goes here */ ]; // Replace with actual ABI

// Initialize Web3
const web3 = new Web3(window.ethereum);

// Request account access if needed
async function requestAccount() {
    try {
        await window.ethereum.request({ method: 'eth_requestAccounts' });
    } catch (error) {
        console.error("User denied account access: ", error);
    }
}

// Get the balance of GGG tokens for a specific address
async function getGGGBalance(address) {
    // Create a contract instance
    const gggContract = new web3.eth.Contract(GGG_TOKEN_ABI, GGG_TOKEN_ADDRESS);
    
    try {
        // Call the balanceOf function from the GGG token contract
        const balance = await gggContract.methods.balanceOf(address).call();
        return web3.utils.fromWei(balance, 'ether'); // Convert balance from Wei to Ether
    } catch (error) {
        console.error("Error fetching balance: ", error);
        return null;
    }
}

// Transfer GGG tokens from one address to another
async function transferGGG(toAddress, amount) {
    const accounts = await web3.eth.getAccounts();
    
    // Create a contract instance
    const gggContract = new web3.eth.Contract(GGG_TOKEN_ABI, GGG_TOKEN_ADDRESS);
    
    try {
        // Convert amount to Wei
        const amountInWei = web3.utils.toWei(amount.toString(), 'ether');
        
        // Send the transaction
        const transaction = await gggContract.methods.transfer(toAddress, amountInWei).send({ from: accounts[0] });
        console.log("Transaction successful: ", transaction);
    } catch (error) {
        console.error("Error during transfer: ", error);
    }
}

// Example usage
(async () => {
    await requestAccount(); // Request user accounts
    const userAddress = (await web3.eth.getAccounts())[0];
    
    // Fetch and log the user's GGG balance
    const balance = await getGGGBalance(userAddress);
    console.log(`Your GGG balance: ${balance} GGG`);

    // Uncomment the following line to transfer GGG tokens (use with caution)
    // await transferGGG('0xRecipientAddressHere', 10); // Replace with actual recipient address and amount
})();
``` 

Make sure to replace placeholders (`0xYourTokenAddressHere`, `/* ABI array goes here */`, and `0xRecipientAddressHere`) with actual values before running the code.
