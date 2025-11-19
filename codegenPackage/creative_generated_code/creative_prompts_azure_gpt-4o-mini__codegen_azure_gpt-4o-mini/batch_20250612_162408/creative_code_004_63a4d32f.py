"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonmotivelgen.godaddysites.com
Prompt: How do I handle user sessions after a successful MetaMask login in a blockchain wallet app?
Generated: DETERMINISTIC_63a4d32fcb5ec714
Batch ID: 20250612_162408
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

// Create an instance of Web3
const web3 = new Web3(window.ethereum);

// Session management utility
const sessionManager = {
    // Function to start a user session
    startSession: (userAddress) => {
        // Store the user address in session storage
        sessionStorage.setItem('userAddress', userAddress);
    },

    // Function to end a user session
    endSession: () => {
        sessionStorage.removeItem('userAddress');
    },

    // Function to get the current user session
    getCurrentSession: () => {
        return sessionStorage.getItem('userAddress');
    }
};

// Function to handle user login via MetaMask
async function loginWithMetaMask() {
    try {
        // Request account access if not granted
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Get the user's Ethereum account address
        const accounts = await web3.eth.getAccounts();
        const userAddress = accounts[0];

        // Start the user session
        sessionManager.startSession(userAddress);

        console.log(`Logged in with address: ${userAddress}`);
        return userAddress;
    } catch (error) {
        // Handle errors (e.g., user denied account access)
        console.error('Error logging in with MetaMask:', error.message || error);
        throw new Error('Failed to login with MetaMask');
    }
}

// Function to check if a user is logged in
function isUserLoggedIn() {
    return sessionManager.getCurrentSession() !== null;
}

// Example usage of the login function
document.getElementById('loginButton').addEventListener('click', async () => {
    try {
        const userAddress = await loginWithMetaMask();
        // Proceed with the application logic for a logged-in user
    } catch (error) {
        // Handle any login errors gracefully
        alert('Login failed. Please try again.');
    }
});

// Example usage to log out the user
document.getElementById('logoutButton').addEventListener('click', () => {
    sessionManager.endSession();
    console.log('User logged out');
});
```
