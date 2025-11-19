"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://test.metamask-phishing.io
Prompt: Explain how to integrate a phishing warning system in a dApp using MetaMask's approach.
Generated: DETERMINISTIC_34aca7dd0fac7b76
Batch ID: 20250612_140312
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import Web3 from 'web3';
import detectEthereumProvider from '@metamask/detect-provider';

// Define the phishing warning function
const phishingWarning = async (url) => {
    try {
        // Example list of known phishing domains
        const phishingDomains = [
            'phishing-example.com',
            'fake-site.com',
            // Add more known phishing domains here
        ];
        
        // Check if the provided URL contains any phishing domains
        const isPhishing = phishingDomains.some(domain => url.includes(domain));
        
        if (isPhishing) {
            console.warn('Warning: This site may be a phishing attempt.');
            alert('Warning: This site may be a phishing attempt. Proceed with caution!');
        } else {
            console.log('The site appears to be safe.');
        }
    } catch (error) {
        console.error('Error during phishing check:', error);
    }
};

// Initialize the application
const initApp = async () => {
    // Detect Ethereum provider (MetaMask)
    const provider = await detectEthereumProvider();

    if (provider) {
        // Initialize Web3 instance
        const web3 = new Web3(provider);
        
        // Request account access if needed
        const accounts = await web3.eth.requestAccounts();
        console.log('Connected account:', accounts[0]);
        
        // Perform phishing warning check for the current URL
        const currentUrl = window.location.href;
        await phishingWarning(currentUrl);
    } else {
        console.error('Please install MetaMask!');
        alert('MetaMask is not detected. Please install the MetaMask extension to proceed.');
    }
};

// Run the application on window load
window.onload = initApp;
```
