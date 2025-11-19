"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://d3l55tu6di4txv.cloudfront.net
Prompt: Generate code for integrating Fortmatic into a web3 application for seamless user onboarding.
Generated: DETERMINISTIC_b6f21897d9929729
Batch ID: 20250612_164205
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries for Fortmatic and Web3
import Web3 from 'web3';
import Fortmatic from 'fortmatic';

// Initialize Fortmatic with your API key
const fm = new Fortmatic('YOUR_FORTMATIC_API_KEY');

// Create a Web3 instance and set the provider to Fortmatic
const web3 = new Web3(fm.getProvider());

// Function to connect to Fortmatic
async function connectToFortmatic() {
    try {
        // Request user authentication
        const user = await fm.user.login();
        
        // Get the user's Ethereum address
        const accounts = await web3.eth.getAccounts();
        console.log("Connected Account:", accounts[0]);

        return accounts[0]; // Return the connected account
    } catch (error) {
        // Handle errors gracefully
        console.error("Error connecting to Fortmatic:", error);
        alert("Failed to connect to Fortmatic. Please try again.");
    }
}

// Function to check if the user is already connected
async function checkConnection() {
    try {
        const accounts = await web3.eth.getAccounts();
        if (accounts.length > 0) {
            console.log("Already connected:", accounts[0]);
            return accounts[0];
        } else {
            console.log("Not connected. Please log in.");
            return null;
        }
    } catch (error) {
        console.error("Error checking connection:", error);
    }
}

// Function to handle user logout
async function logout() {
    try {
        await fm.user.logout();
        console.log("User logged out successfully.");
    } catch (error) {
        console.error("Error logging out:", error);
    }
}

// Main function to handle user onboarding
async function onboardUser() {
    const connectedAccount = await checkConnection();
    if (!connectedAccount) {
        await connectToFortmatic(); // Prompt user to connect if not already connected
    }
}

// Execute the onboarding process when the page loads
window.onload = () => {
    onboardUser();
};

// Example usage: Call logout function when a logout button is clicked
document.getElementById('logoutButton').onclick = () => {
    logout();
};
```

**Note:** Replace `'YOUR_FORTMATIC_API_KEY'` with your actual Fortmatic API key. Make sure to include error handling best practices and ensure the integration meets production readiness standards.
