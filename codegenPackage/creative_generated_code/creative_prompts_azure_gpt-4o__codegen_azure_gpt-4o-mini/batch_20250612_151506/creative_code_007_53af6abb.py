"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://d3l55tu6di4txv.cloudfront.net
Prompt: Write code to configure Fortmatic with a specific API key and network for a web3 application.
Generated: DETERMINISTIC_53af6abb305192df
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
import { Fortmatic } from 'fortmatic';
import Web3 from 'web3';

// Configuration for Fortmatic
const API_KEY = 'YOUR_FORTMATIC_API_KEY';  // Replace with your Fortmatic API Key
const NETWORK = 'mainnet';  // Change to desired network (e.g., 'rinkeby', 'mainnet')

// Initialize Fortmatic
const fortmatic = new Fortmatic(API_KEY, { network: NETWORK });

// Create a Web3 instance with Fortmatic provider
const web3 = new Web3(fortmatic.getProvider());

// Function to connect to Fortmatic
async function connectToFortmatic() {
    try {
        // Request user to connect their wallet
        await fortmatic.user.login();
        console.log('User connected to Fortmatic');

        // Retrieve user's account address
        const accounts = await web3.eth.getAccounts();
        console.log('Connected account:', accounts[0]);
        
        // Additional setup can go here (e.g., update UI to show connected account)
        
    } catch (error) {
        console.error('Error connecting to Fortmatic:', error);
        alert('Failed to connect to Fortmatic. Please try again.');
    }
}

// Function to disconnect from Fortmatic
async function disconnectFromFortmatic() {
    try {
        await fortmatic.user.logout();
        console.log('User disconnected from Fortmatic');
        // Additional cleanup can go here (e.g., update UI to show disconnected state)
        
    } catch (error) {
        console.error('Error disconnecting from Fortmatic:', error);
    }
}

// Export the functions for use in the application
export { connectToFortmatic, disconnectFromFortmatic };
```

Make sure to replace `YOUR_FORTMATIC_API_KEY` with your actual Fortmatic API key before running the code. This code is designed to be clean, efficient, and production-ready with proper error handling.
