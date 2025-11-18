"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://disneyglobalse.web.app
Prompt: Create a web application using JavaScript to allow users to mint Disney-themed NFTs, including a feature to validate waitlist eligibility.
Generated: DETERMINISTIC_67abf16ca4aad28c
Batch ID: 20250612_150858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Disney-themed NFT Minting</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Mint Your Disney-themed NFT</h1>
    <form id="mintForm">
        <label for="walletAddress">Wallet Address:</label>
        <input type="text" id="walletAddress" required>
        <button type="submit">Mint NFT</button>
    </form>
    <div id="message"></div>
    <script src="app.js"></script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    margin: 0;
    padding: 20px;
}

h1 {
    color: #3b5998;
}

#message {
    margin-top: 20px;
    font-weight: bold;
}
```

```javascript
// app.js

// Constants
const WAITLIST = new Set([
    '0x1234567890abcdef1234567890abcdef12345678', // Example address
    '0xabcdef1234567890abcdef1234567890abcdef12'  // Example address
]);

// Function to validate waitlist eligibility
function isEligibleForWaitlist(walletAddress) {
    return WAITLIST.has(walletAddress);
}

// Function to mint NFT
async function mintNFT(walletAddress) {
    try {
        // Placeholder for minting logic (e.g., contract interaction)
        // Replace this with actual minting logic
        console.log(`Minting NFT for ${walletAddress}...`);
        // Simulate minting delay
        await new Promise(resolve => setTimeout(resolve, 1000)); // Simulate async operation
        return true; // Simulate successful minting
    } catch (error) {
        console.error('Minting failed:', error);
        throw new Error('Minting failed, please try again later.');
    }
}

// Event listener for form submission
document.getElementById('mintForm').addEventListener('submit', async (event) => {
    event.preventDefault(); // Prevent default form submission

    const walletAddress = document.getElementById('walletAddress').value.trim();
    const messageElement = document.getElementById('message');

    // Validate wallet address format (basic validation)
    const walletAddressPattern = /^0x[a-fA-F0-9]{40}$/;
    if (!walletAddressPattern.test(walletAddress)) {
        messageElement.textContent = 'Invalid wallet address format.';
        return;
    }

    // Check waitlist eligibility
    if (!isEligibleForWaitlist(walletAddress)) {
        messageElement.textContent = 'You are not eligible for the waitlist.';
        return;
    }

    // Mint the NFT
    try {
        const success = await mintNFT(walletAddress);
        if (success) {
            messageElement.textContent = 'NFT minted successfully!';
        }
    } catch (error) {
        messageElement.textContent = error.message;
    }
});
```
