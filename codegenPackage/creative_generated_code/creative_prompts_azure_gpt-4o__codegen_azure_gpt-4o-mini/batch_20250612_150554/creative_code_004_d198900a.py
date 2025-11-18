"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.arteratoken.lucaageadesign.com
Prompt: Create a JavaScript function using ethers.js to interact with the Artera Token contract and display the token balance of a connected MetaMask wallet.
Generated: DETERMINISTIC_d198900aa2689eeb
Batch ID: 20250612_150554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the ethers.js library
import { ethers } from 'ethers';

// Define the Artera Token contract address
const ARTERA_TOKEN_ADDRESS = '0xYourArteraTokenAddressHere'; // Replace with the actual contract address

// Define the ABI (Application Binary Interface) for the Artera Token contract
const ARTERA_TOKEN_ABI = [
    // Only include the 'balanceOf' function from the ERC20 standard
    "function balanceOf(address owner) view returns (uint256)"
];

// Function to get the token balance of the connected MetaMask wallet
async function getTokenBalance() {
    try {
        // Check if MetaMask is installed
        if (typeof window.ethereum === 'undefined') {
            throw new Error('MetaMask is not installed. Please install it.');
        }

        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Create an ethers provider using MetaMask
        const provider = new ethers.providers.Web3Provider(window.ethereum);

        // Get the signer (the connected wallet)
        const signer = provider.getSigner();
        
        // Get the connected wallet address
        const address = await signer.getAddress();

        // Create a new instance of the Artera Token contract
        const arteraTokenContract = new ethers.Contract(ARTERA_TOKEN_ADDRESS, ARTERA_TOKEN_ABI, provider);

        // Call the balanceOf function to get the token balance
        const balance = await arteraTokenContract.balanceOf(address);

        // Format the balance to a more readable number (assuming the token has 18 decimals)
        const formattedBalance = ethers.utils.formatUnits(balance, 18);

        // Display the token balance in the console
        console.log(`Token Balance of ${address}: ${formattedBalance} ARTERA`);
    } catch (error) {
        // Handle errors and display them to the user
        console.error('Error fetching token balance:', error.message);
    }
}

// Call the function to display the token balance
getTokenBalance();
```
