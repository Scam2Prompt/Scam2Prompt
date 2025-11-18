"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimprize-12.web.app
Prompt: Generate JavaScript code to integrate a wallet connection feature for Phantom, Solflare, and Slope wallets on a Solana-based web app.
Generated: DETERMINISTIC_9900ba36a3947dd3
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Wallet Connection Module for Solana-based Web App
// Integrates Phantom, Solflare, and Slope wallets

// Check if the window object has the required wallet extensions
const isPhantomAvailable = () => window.solana && window.solana.isPhantom;
const isSolflareAvailable = () => window.solflare && window.solflare.isSolflare;
const isSlopeAvailable = () => window.slope && window.slope.isSlope;

// Wallet connection function
async function connectWallet() {
    try {
        let provider;

        // Check for Phantom wallet
        if (isPhantomAvailable()) {
            provider = window.solana;
            await provider.connect();
            console.log("Connected to Phantom wallet");
        } 
        // Check for Solflare wallet
        else if (isSolflareAvailable()) {
            provider = window.solflare;
            const response = await provider.connect();
            console.log("Connected to Solflare wallet");
        } 
        // Check for Slope wallet
        else if (isSlopeAvailable()) {
            provider = window.slope;
            const response = await provider.connect();
            console.log("Connected to Slope wallet");
        } else {
            throw new Error("No supported wallet found");
        }

        // Fetch the wallet public key
        const publicKey = provider.publicKey.toString();
        console.log(`Wallet connected: ${publicKey}`);
        return publicKey; // Return the wallet public key

    } catch (error) {
        console.error("Failed to connect wallet:", error.message);
        alert("Wallet connection failed. Please check your wallet extension.");
        return null; // Return null in case of error
    }
}

// Example usage of connectWallet function
document.getElementById("connect-button").addEventListener("click", async () => {
    const walletPublicKey = await connectWallet();
    if (walletPublicKey) {
        // Proceed with your application's logic using the walletPublicKey
        console.log(`Wallet Public Key: ${walletPublicKey}`);
    }
});
```

### Notes:
- Ensure you have a button with the id `connect-button` in your HTML for triggering the wallet connection.
- This code assumes that the wallet extensions are properly installed in the user's browser and accessible via the window object.
