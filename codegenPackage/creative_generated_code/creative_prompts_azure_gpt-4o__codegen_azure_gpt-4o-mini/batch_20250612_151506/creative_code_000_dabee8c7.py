"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://d3l55tu6di4txv.cloudfront.net
Prompt: Write code to integrate Fortmatic into a web3 dApp for user authentication without requiring browser extensions or downloads.
Generated: DETERMINISTIC_dabee8c763bda139
Batch ID: 20250612_151506
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
import Fortmatic from 'fortmatic';

// Initialize Fortmatic with your API key
const fortmaticApiKey = 'YOUR_FORTMATIC_API_KEY'; // Replace with your actual Fortmatic API key
const fm = new Fortmatic(fortmaticApiKey);

// Create a Web3 instance with Fortmatic provider
const web3 = new Web3(fm.getProvider());

// Function to connect to Fortmatic and authenticate user
async function connectToFortmatic() {
    try {
        // Request user to log in with Fortmatic
        await fm.user.login();
        
        // Get user account information
        const userAccounts = await web3.eth.getAccounts();
        if (userAccounts.length === 0) {
            throw new Error('No accounts found. User may not be logged in.');
        }
        
        // Display the user's Ethereum account
        console.log('Connected account:', userAccounts[0]);
        
        // You can now interact with the Ethereum network using the authenticated account
        return userAccounts[0]; // Return the connected account
    } catch (error) {
        console.error('Error connecting to Fortmatic:', error);
        alert('Failed to connect. Please try again.');
    }
}

// Call the function to initiate connection
document.getElementById('connectButton').addEventListener('click', connectToFortmatic);

// Example usage of Web3 to get the user's Ethereum balance
async function getUserBalance(account) {
    try {
        const balance = await web3.eth.getBalance(account);
        console.log('User balance (in Ether):', web3.utils.fromWei(balance, 'ether'));
    } catch (error) {
        console.error('Error fetching balance:', error);
    }
}

// Optional: Fetch balance after connecting
document.getElementById('getBalanceButton').addEventListener('click', async () => {
    const account = await connectToFortmatic();
    if (account) {
        await getUserBalance(account);
    }
});
```

### Notes:
- Replace `'YOUR_FORTMATIC_API_KEY'` with your actual Fortmatic API key.
- Include HTML elements with IDs `connectButton` and `getBalanceButton` for the example usage to work correctly.
- Ensure that the Fortmatic library and Web3 are correctly installed in your project.
