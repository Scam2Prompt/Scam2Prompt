"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskchromeext.bravesites.com
Prompt: Write a script to enable phishing detection mechanisms when interacting with MetaMask in a browser-based application.
Generated: DETERMINISTIC_878a3c37b3e351cf
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Phishing Detection Script for MetaMask Interaction

// Utility function to check if a URL is from a known phishing source
const isPhishingUrl = (url) => {
    const phishingUrls = [
        'malicious-site.com', // Add known phishing URLs
        'fake-metamask.com'
    ];
    return phishingUrls.some(phishingUrl => url.includes(phishingUrl));
};

// Function to initiate MetaMask connection with phishing detection
const connectToMetaMask = async () => {
    const { ethereum } = window;

    // Check if MetaMask is installed
    if (!ethereum) {
        console.error('MetaMask is not installed. Please install it to use this application.');
        return;
    }

    try {
        // Request account access if needed
        const accounts = await ethereum.request({ method: 'eth_requestAccounts' });

        // Log the connected account
        console.log('Connected account:', accounts[0]);

        // Check the current provider's URL for phishing
        const providerUrl = ethereum._metamask && ethereum._metamask.networkVersion ? ethereum._metamask.networkVersion : '';
        if (isPhishingUrl(providerUrl)) {
            console.warn('Warning: Connected to a potentially phishing site:', providerUrl);
            alert('Warning: You are connected to a site that may be a phishing attempt. Please check the URL.');
            return;
        }

        // Proceed with the application logic
        // Example: Fetch user balance
        const balance = await ethereum.request({
            method: 'eth_getBalance',
            params: [accounts[0], 'latest'],
        });
        
        console.log('User balance:', balance);
        
    } catch (error) {
        // Handle error scenarios
        if (error.code === 4001) {
            // User rejected the request
            console.error('User denied account access.');
        } else {
            console.error('Error connecting to MetaMask:', error);
        }
    }
};

// Add event listener to a button that triggers the MetaMask connection
document.getElementById('connectButton').addEventListener('click', connectToMetaMask);
```

Ensure that the HTML includes a button with the ID `connectButton` for this script to work properly.
